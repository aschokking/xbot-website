from django.shortcuts import render
import pdb

from apiclient.discovery import build

def get_api():
	key = 'AIzaSyDMg-W4M-P8wGRZrEPM4h67xbIJojGRpj8'
	api = build("youtube", "v3", developerKey=key)
	return api

def get_videos():
	api = get_api()

	teamxbot_channel_id = 'UCaWKhXUXqBeQHjnp4HhpOxg'
	return api.search().list(part="id", type='video', channelId=teamxbot_channel_id).execute()


# Create your views here.
def recent_videos(request):
	results = get_videos()
	pdb.set_trace()
	embed_url_base = "http://www.youtube.com/embed/"

	videos = []
	for item in results['items']:
		videos.append({'embed_url': (embed_url_base + item['id']['videoId']) })

	return render(request, 'xyoutube/videos.html', { 'videos': videos })