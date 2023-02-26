# UCL CSS Hackathon 2023 - Engineers are Superheros

This project contains the code for the CSS Hackathon 2023 - Engineers are Superheros.
The project was conceived, built, and showcased within a 26 hour limit from 5 February to 6 February.

The collaborators are:
- @jameshi16
- @Gen1Code
- @JKoenigUCL
- @JKoenigUCL
- @olliestone

## Backend

A virtual environment should be setup, and the relevant packages should be installed from requirements.txt:

```
virtualenv .pyvenv \
source .pyvenv/bin/activate \
pip install -r requirements.txt
```

Instructions from https://github.com/mmabrouk/chatgpt-wrapper#installation should be followed to set up ChatGPT for
programmatic access.

A file, `config.py` should be created with the following parameters:
```python
openai_api_key=
youtube_api_key=
```

The `openai_api_key` parameter can be omitted if the ChatGPT implementation is used.

### Magic Incantations

CURL command to generate things based on topics:
```
curl -X POST http://127.0.0.1:5000/mockapi?username=user\&topic=test
```

CURL command to obtain saved topics:
```
curl -X POST http://127.0.0.1:5000/user/savedtopicsapi?username=user
```

CURL command to mark a video as watched:
```
curl -X POST http://127.0.0.1:5000/user/savedtopicsapi?username=user\&video_id
```

CURL command to log a user in:
```
curl -X POST http://127.0.0.1:5000/user/savedtopicsapi?username=user\&password=password
```

## Frontend

Install the relevant packages and run the server:

```
npm install \
npm run dev
```
