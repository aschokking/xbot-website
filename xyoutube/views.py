from django.shortcuts import render

from apiclient.discovery import build

def get_api():
	key = 'AIzaSyDMg-W4M-P8wGRZrEPM4h67xbIJojGRpj8'
	api = build("youtube", "v3", developerKey=key)
	return api

# Create your views here.
def recent_videos(request):
	api = get_api()

	teamxbot_channel_id = 'UCaWKhXUXqBeQHjnp4HhpOxg'
	results = api.search().list(part="id,snippet", channelId=teamxbot_channel_id).execute()
	