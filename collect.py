import lyricsgenius
import requests
import json
import csv
import pandas as pd
from requests.exceptions import HTTPError, Timeout

client_id = 'vIrAcKuJdypnblUjhwO2qDFsGWDxUuoJe0k-vNDfjFJfM3CMjQIDS-uNp_gosPzx'
client_secret = 'PmRObzAHupNdEk4xJA7ofaEgw1mx6zqc2unq2J1nB-zQS8s6JAVjRRKwce-wThF_jNFul6vG8kUH8VaC0MXMwA'
token = '1DUqwEz-0e6Rp7q2eB8cEJuBifEpvm2PhivONDWyZcZoAqPE9sN-jby8GFGs-NPF'


top100_df = pd.read_csv('top100.csv', header=0)

song_list = top100_df['song'].tolist()
artist_list = top100_df['artist'].tolist()
song_id = []
page_views = []
lyrics = []
annotations = []




for i in range(len(song_list)):

	try:
		genius = lyricsgenius.Genius(token)
		song = genius.search_song(f"{song_list[i]}", f"{artist_list[i]}")
		try:
			song_id.append(song.id)
			lyrics.append(song.lyrics)
		except:
			song_id.append(None)
			lyrics.append(None)
		try:
			annotations.append(song.annotation_count)
		except AttributeError:
			annotations.append(None)
		try:
			page_views.append(song.stats.pageviews)
		except AttributeError:
			page_views.append(None)


	except HTTPError as e:
	    print(e.errno)    # status code
	    print(e.args[0])  # status code
	    print(e.args[1])  # error message
	    song_id.append(None)
	    lyrics.append(None)
	    annotations.append(None)
	    page_views.append(None)
	except Timeout:
		song_id.append(None)
		lyrics.append(None)
		annotations.append(None)
		page_views.append(None)
		pass

df_songinfo = pd.DataFrame(data={"song_id": song_id, "lyrics": lyrics, "annotations": annotations, "page_views": page_views})

df_songinfo.to_pickle("collected.pkl")

top100_df['song_id'] = song_id
top100_df['lyrics'] = lyrics
top100_df['annotations'] = annotations
top100_df['page_views'] = page_views

top100df.to_csv('final_dataset.csv')




