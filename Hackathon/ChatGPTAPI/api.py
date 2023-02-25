from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from chatgpt_wrapper import ChatGPT
import re
import json

app = Flask(__name__)
api = Api(app)

# This is the class that will get a request with a topic, and return ChatGPT's response
class ChatGPTAPI(Resource):
    def post(self):
        chatGPT = ChatGPT()
        responses = {}

        topic = request.args['topic']
        # Format request 
        query = "Create a list of subtopics required to understand " + topic
        # Get the response from ChatGPT
        response = chatGPT.ask(query)
        responses['subtopics'] = response

        searchPrompts = chatGPT.ask("Create a YouTube search prompt for each of these subtopics, with each prompt not inside quotes.")
        responses['searchPrompts'] = searchPrompts

        # Return the response
        return responses
    
api.add_resource(ChatGPTAPI, '/chatgptapi')

if __name__ == '__main__':
    app.run()  # run our Flask app
