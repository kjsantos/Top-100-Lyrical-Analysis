import csv
import pandas as pd

with open ('top100.csv', 'r+', encoding='utf-8') as file:
	top100_df = pd.read_csv(file, header=0)

collected = pd.read_pickle('collected.pkl')

top100_df['song_id'] = collected['song_id'].tolist()
top100_df['lyrics'] = collected['lyrics'].tolist()
top100_df['annotations'] = collected['annotations'].tolist()
top100_df['page_views'] = collected['page_views'].tolist()


top100_df.to_csv('collected_dataset.csv')