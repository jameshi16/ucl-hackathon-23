from flask import Flask
from flask_restful import Resource, Api, reqparse
from chatgpt_wrapper import ChatGPT

app = Flask(__name__)
api = Api(app)

# This is the class that will get a request with a topic, and return ChatGPT's response
class ChatGPTAPI(Resource):
    def get(self):
        chatGPT = ChatGPT()
        responses = []
        # Get the topic from the request
        parser = reqparse.RequestParser()
        parser.add_argument('topic')
        args = parser.parse_args()
        topic = args['topic']
        # Format request 
        request = "Create a list of subtopics required to understand " + topic
        # Get the response from ChatGPT
        response = chatGPT.ask("hello")
        responses.append(response)

        # Return the response
        return response
    
api.add_resource(ChatGPTAPI, '/chatgptapi')

if __name__ == '__main__':
    app.run()  # run our Flask app
