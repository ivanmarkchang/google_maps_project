import datetime
import json
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials


response = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?'
	'units=imperial'
	'&origins=ENTER-COORDINATES-HERE'
	'&destinations=ENTER-COORDINATES-HERE'
	'&departure_time=now'
	'&traffic_model=best_guess'
	'&key=<ENTER_GOOGLE_DEVELOPER_API_KEY_HERE>')


data = json.loads(response.text)

duration_seconds = data['rows'][0]['elements'][0]['duration_in_traffic']['value']
duration_minutes = round(duration_seconds/60,2)

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('ENTER_ABSOLUTE_PATH_HERE EG. /USERS/ME/CLIENT_SECRET.JSON', scope)
client = gspread.authorize(creds)
wks = client.open('Commute history').sheet1

now = datetime.datetime.now()
wks.append_row([now.strftime('%A'), now.strftime('%H'':''%M'), duration_minutes])
