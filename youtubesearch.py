import googleapiclient.discovery
import urllib.parse


def search_youtube(chatgpt_query):

    # Replace with your own API key
    api_key = 'your api key'

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


# Create a tuple of (video_title, video_id) and return it

# # Extract the video URL from the search result
# video_url = 'https://www.youtube.com/watch?v=' + \
#     search_response['items'][0]['id']['videoId']

# return (video_url)


def promtToList(promt):
    i = promt.index(':')
    promt = promt[i+1:]
    return (promt.split(","))


def search_multi(querry_lst):
    querry = querry_lst
    responses = []
    for q in querry:
        responses.append(search_youtube(q))
    return responses


def promtListToUrls(ListofPromts):
    querries = [[]]
    for (index, promt) in enumerate(ListofPromts):
        querries.append([])
        promts = promtToList(promt)  # split promt into list of querries
        querries[index].append(search_multi(promts))  # get urls for each promt
    return querries


def main():
    promts = ["Algebra: Solving linear equations, Functions explained, Introduction to sequences and series",
              "Calculus: Introduction to differentiation, Integration by substitution, Limits explained"]
    urls = promtListToUrls(promts)
    print(urls)


if __name__ == "__main__":
    main()
