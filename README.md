# INext-task

## Instructions for execution

### Initial setup on Google Developer Console
1. Create a new project
2. Enable Gmail API by navigating to Library
3. Add OAuth consent screen (Add URI as "http:localhost:8080/")
4. Create Credentials and Download the json file as "credentials.json"


### Generate token.json file
1. Make sure your "credentials.json" file is in the same working directory as your project
2. Run quickstart.py file => python quickstart.py
3. Signup with your account and hit allow
4. You will have "token.json" file created in your folder for future logins


### Run Flask app
export FLASK_APP=app
export FLASK_ENV=development
flask run
