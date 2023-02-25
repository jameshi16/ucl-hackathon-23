from flask import Flask
from flask_restful import Resource, Api, reqparse
from chatgpt_wrapper import ChatGPT

import ast

app = Flask(__name__)
api = Api(app)

chatGPT = ChatGPT()

# This is the class that will get a request with a topic, and return ChatGPT's response
class ChatGPTAPI(Resource):
    def post(self):
        # Get the topic from the request
        parser = reqparse.RequestParser()
        parser.add_argument('topic')
        args = parser.parse_args()
        topic = args['topic']
        # Format request 
        request = "Create a list of subtopics required to understand " + topic
        # Get the response from ChatGPT
        response = chatGPT.get_response(topic)
        # Return the response
        return response
    
api.add_resource(ChatGPTAPI, '/chatgpt')

if __name__ == '__main__':
    app.run()  # run our Flask app
