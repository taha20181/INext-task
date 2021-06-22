# Flask import
from flask import Flask

# imports for google Gmail API
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

global creds

# Flask app instance
app = Flask(__name__)


SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
creds = None

# root api
@app.get('/')
def index():
    return "<h1 style='text-align:center;'>Welcome to GMAIL API</h1>"


# function to verify the user and create token.json file
def verify():
    global creds
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=8080)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    results = service.users().messages().list(
        userId='me', labelIds=['INBOX']).execute()
    messages = results.get('messages', [])

    return service, messages


# api to fetch the most recent mail(s) from Gmail A/c
@app.get('/getRecentMail')
def getRecentMail():
    service, messages = verify()

    # increase message count to fetch n latest emails
    message_count = 1
    for message in messages[:message_count]:
        msg = service.users().messages().get(
            userId='me', id=message['id']).execute()
        print(msg)
        email = (msg['snippet'])
        print(f'{email}\n')

    return f'Your recent mail => {email}'


if __name__ == "__main__":
    app.run(debug=True)
