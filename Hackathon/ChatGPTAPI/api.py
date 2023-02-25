from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from chatgpt_wrapper import ChatGPT
import googleapiclient.discovery
import urllib.parse
import re
import json

app = Flask(__name__)
api = Api(app)

def search_youtube(chatgpt_query):

    # Replace with your own API key
    api_key = ''

    # Create a YouTube API client
    youtube = googleapiclient.discovery.build(
        'youtube', 'v3', developerKey=api_key)

    # Define the search query
    query = chatgpt_query

    # Encode the query to URL format
    query = urllib.parse.quote_plus(query)

    # Search for the video
    search_response = youtube.search().list(
        q=query,
        type='video',
        part='id,snippet',
        maxResults=1
    ).execute()

    video_title = search_response['items'][0]['snippet']['title']
    video_id = search_response['items'][0]['id']['videoId']

    result = (video_title, video_id)
    return result

# This is the class that will get a request with a topic, and return ChatGPT's response
class ChatGPTAPI(Resource):
    def post(self):
        chatGPT = ChatGPT()
        responses = {}

        topic = request.args['topic']
        # Format request 
        query = "Create a numbered list of subtopics  (with no other informtion) required to understand " + topic
        # Get the response from ChatGPT
        response = chatGPT.ask(query)
        responses['subtopics'] = response

        searchPrompts = chatGPT.ask("Create YouTube search prompts for each of these subtopics, without using \" \".")

        subtopics_dict = {}

        # Split the input string into lines
        lines = searchPrompts.split('\n')

        # Loop through the lines and extract the subtopic and search term for each one
        for line in lines:
            if line.strip() == "" or line[0].isdigit() == False:
                continue
            videos = []

            try: 
                subtopic, search_term = line.split(":")
            except:
                try:
                    subtopic, search_term = line.split("-")
                except:
                    print("Error: Could not split line into subtopic and search term")
                    continue
            subtopic_num, subtopic_name = subtopic.split(". ")
            search_terms = search_term.split(',')
            for term in search_terms:
                videos.append(search_youtube(term.strip('"')))

            subtopics_dict[subtopic_name] = [videos]

        responses['searchPrompts'] = subtopics_dict

        # Return the response
        return responses
    
api.add_resource(ChatGPTAPI, '/chatgptapi')

if __name__ == '__main__':
    app.run()  # run our Flask app
