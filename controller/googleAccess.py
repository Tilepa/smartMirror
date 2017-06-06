from __future__ import print_function
import datetime
import httplib2
import os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from model.calendarEntry import CalendarEntry
from model.configurations import *

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = "https://www.googleapis.com/auth/calendar.readonly"
CLIENT_SECRET_FILE = "model/client_secret.json"


def get_credentials():
    home_dir = os.path.expanduser("~")
    credential_dir = os.path.join(home_dir, ".credentials")
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, "calendar-python-quickstart.json")

    store = Storage(credential_path)
    credentials = store.get()

    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:
            credentials = tools.run(flow, store)
        print("Storing credentials to " + credential_path)
    return credentials


def get_next_20_calendar_entries():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build("calendar", "v3", http=http)

    now = datetime.datetime.utcnow().isoformat() + "Z"

    eventsResult = service.events().list(
        calendarId="primary",
        timeMin=now,
        maxResults=20,
        singleEvents="true",                # singleEvents must be set to true, otherwise orderBy startTime is not allowed
        orderBy="startTime").execute()
    events = eventsResult.get("items", [])

    calendarEntries = []
    for event in events:
        id = event["id"]
        description = event["summary"]
        startTime = get_date(event["start"].get("dateTime", event["start"].get("date")))
        endTime = get_date(event["end"].get("dateTime", event["end"].get("date")))
        status = event["status"]

        entry = CalendarEntry(id=id, startDate=startTime, endDate=endTime, title=description, status=status)
        calendarEntries.append(entry)

    return calendarEntries


def get_date(date_string):
    additional_time = ""
    try:
        date, additional_time = date_string.split("+")
        date_time = datetime.datetime.strptime(date, "%Y-%m-%dT%X")
    except ValueError:
        date = date_string
        date_time = datetime.datetime.strptime(date, "%Y-%m-%d")

    return date_time
