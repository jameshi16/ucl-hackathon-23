# UCL CSS Hackathon 2023 - Engineers are Superheros

This project contains the code for the CSS Hackathon 2023 - Engineers are Superheros.
The project was conceived, built, and showcased within a 26 hour limit from 5 February to 6 February.

In the advent of AIs like ChatGPT, a revolution in learning paradigm is bound to take place. This project
takes any topic from a curious learner, generates a syllabus for that, and find videos to furnish the
syllabus.

Upon completing all the videos in each item in the syllabus, they are awarded a community-granted certificate
to prove their worth.

These certificates may mean nothing now, but can become a recognized qualification in the future. With a critical
mass, this technology can be affordable and accessible to anyone who may require an alternative to expensive
tertiary education.

Educators can use the tool to create higher-level courses; one that does not rely on low level understanding,
but high level application. Low level learning can be outsourced to this tool.

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
curl -X POST http://127.0.0.1:5000/user/watchedapi?username=user\&video_id=something
```

CURL command to log a user in:
```
curl -X POST http://127.0.0.1:5000/user/authapi?username=user\&password=password
```

## Frontend

Install the relevant packages and run the server:

```
npm install \
npm run dev
```

If another API (between DaVinci, ChatGPT and Mock) is chosen / backend URL is changed, please change the corresponding values in app.js.
