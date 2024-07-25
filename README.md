# TODOs
- [] only accept /GET requests from frontend app
- [] update mongodb to only accept requests from api server
    - static outbound ip requires upgraded plan

- [x] deploy api to railway.app
    - https://dev.to/ankur0904/hosting-a-flask-web-server-on-railway-free-1049
- [x] index page displaying all valid endpoints
- [x] only accept /POST requests with the correct static bearer token

## API Endpoints
- `/api/v1/ping`
- `/api/v1/activity/key-presses`
- `/api/v1/activity/left-clicks`
- `/api/v1/activity/right-clicks`
- `/api/v1/activity/mouse-movements`

## Commands
- `python -m venv kazdesu-api-env` recommended way to create venv for python
- `source kazdesu-api-env/Scripts/activate` to activate the venv
- `deactivate` to deactivate
- `pip freeze > requirements.txt` to create a requirements file for a fresh setup
- `pip install -r requirements.txt` to 

## Project Setup (locally)
- create a `.env` file with the following variables
- 
```
ACTIVITY_DB_NAME=
MONGO_URI=
API_STATIC_TOKEN=
```
- create and activate venv
- `pip install -r requirements.txt` inside venv
- `python run.py` to start application
