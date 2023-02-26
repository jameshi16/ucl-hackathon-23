from chatgpt_wrapper import ChatGPT
import googleapiclient.discovery
import sqlapi
import urllib.parse
import re
import json
import config

def search_youtube(chatgpt_query):

    # Replace with your own API key
    api_key = config.youtube_api_key

    # Create a YouTube API client
    youtube = googleapiclient.discovery.build(
        'youtube', 'v3', developerKey=api_key)

    # Define the search query
    query = chatgpt_query

    # Encode the query to URL format
    query = urllib.parse.quote_plus(query)

    # Search for the video
    search_responses = youtube.search().list(
        q=query,
        type='video',
        part='id,snippet',
        maxResults=8
    ).execute()

    results = []

    for video in search_responses['items']:
        video_title = video['snippet']['title']
        video_id = video['id']['videoId']
        result = (video_title, video_id)
        results.append(result)

    return results
    
def CreateSyllabus(topic):
    chatGPT = ChatGPT()
    responses = {}

    query = "Create a numbered list of subtopics (with no other informtion) required to understand " + topic
    response = chatGPT.ask(query)
    chatGPT.page.close()

    topics = response.split('\n')
    for searchPrompt in topics:
        if searchPrompt.strip() == "" or searchPrompt[0].isdigit() == False:
            topics.remove(searchPrompt)

    topics = [topic for topic in topics if topic.strip() != "" and topic[0].isdigit() == True]
    topics = [topic.split('.')[1].strip() for topic in topics]
    responses['subtopics'] = topics
    subtopics_dict = {}
    
    searchPrompts = []
    for i, subtopic in enumerate(topics):
        searchPrompts.append(subtopic + " " + topic)

    for i, searchPrompt in enumerate(searchPrompts):
        videos = []
        videos.append(search_youtube(searchPrompt))
        subtopics_dict[topics[i]] = videos

    responses['searchPrompts'] = subtopics_dict

    # Return the response
    return responses
