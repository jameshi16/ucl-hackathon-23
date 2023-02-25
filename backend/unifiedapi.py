from flask import Flask, request
from flask_restful import Resource, Api, reqparse

import chatgptapi
import sqlapi

app = Flask(__name__)
api = Api(app)

# This is the class that will get a request with a topic, and return ChatGPT's response
class ChatGPTAPI(Resource):
    def post(self):
        topic = request.args['topic']

        # Get the response from ChatGPT
        response = chatgptapi.CreateSyllabus(topic)

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



api.add_resource(ChatGPTAPI, '/chatgptapi')
api.add_resource(SavedTopicsAPI, '/user/savedtopicsapi')

if __name__ == '__main__':
    app.run()