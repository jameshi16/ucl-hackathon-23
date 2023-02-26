from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

import chatgptapi
import davinciapi
import mockapi
import sqlapi

app = Flask(__name__)
CORS(app)
api = Api(app)

class ChatGPTAPI(Resource):
    def post(self):
        username = request.args['username']
        topic = request.args['topic']

        # Get the response from ChatGPT
        response = chatgptapi.CreateSyllabus(topic)

        # Add the topic to the database
        sqlapi.addTopic(topic,response['subtopics'],response['searchPrompts'])

        # Add the topic to the user's saved topics
        sqlapi.UserToTopic(username,topic)

        # Return the response
        return response
    
class DavinciAPI(Resource):
    def post(self):
        username = request.args['username']
        topic = request.args['topic']

        # Get the response from Davinci
        response = davinciapi.CreateSyllabus(topic)

        # Add the topic to the database
        sqlapi.addTopic(topic,response['subtopics'],response['searchPrompts'])

        # Add the topic to the user's saved topics
        sqlapi.UserToTopic(username,topic)

        # Return the response
        return response

class MockAPI(Resource):
    def post(self):
        username = request.args['username']
        topic = request.args['topic']

        # Get the response from Mock
        response = mockapi.CreateSyllabus(topic)

        # Add the topic to the database
        sqlapi.addTopic(topic,response['subtopics'],response['searchPrompts'])

        # Add the topic to the user's saved topics
        sqlapi.UserToTopic(username,topic)

        # Return the response
        return response

class SavedTopicsAPI(Resource):
    def post(self):
        # Get the username from the request
        username = request.args['username']

        # Get the topics from the database
        topics = sqlapi.TopicBreakdownFromUser(username)

        # Return the topics
        return topics
    
class WatchedAPI(Resource):
    def post(self):
        # Get the username and video id from the request
        username = request.args['username']
        video_id = request.args['video_id']

        # Add the video to the watched table
        sqlapi.watched(username,video_id)

        # Return a success message
        return {'message': 'success'}
    
class AuthAPI(Resource):
    def post(self):
        # Get the username and password from the request
        username = request.args['username']
        password = request.args['password']

        # Check if the username and password are correct
        if sqlapi.authenticate(username,password):
            return {'message': 'success'}
        else:
            return {'message': 'failure'}



api.add_resource(ChatGPTAPI, '/chatgptapi')
api.add_resource(DavinciAPI, '/davinciapi')
api.add_resource(MockAPI, '/mockapi')
api.add_resource(SavedTopicsAPI, '/user/savedtopicsapi')
api.add_resource(WatchedAPI, '/user/watchedapi')
api.add_resource(AuthAPI, '/user/authapi')

if __name__ == '__main__':
    app.run()
