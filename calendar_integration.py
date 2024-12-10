from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import datetime

class CalendarIntegration:
    def __init__(self):
        self.SCOPES = ['https://www.googleapis.com/auth/calendar']
        self.service = self.authenticate()

    def authenticate(self):
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', self.SCOPES)
        creds = flow.run_local_server(port=0)
        return build('calendar', 'v3', credentials=creds)

    def add_event(self, task_name, deadline):
        event = {
            'summary': task_name,
            'start': {
                'dateTime': f"{deadline}T09:00:00",
                'timeZone': 'America/New_York',
            },
            'end': {
                'dateTime': f"{deadline}T10:00:00",
                'timeZone': 'America/New_York',
            },
        }
        event = self.service.events().insert(calendarId='primary', body=event).execute()
        print(f"Event created: {event.get('htmlLink')}")
