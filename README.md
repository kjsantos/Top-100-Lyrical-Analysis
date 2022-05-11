# Top-100-Lyrical-Analysis

## Final Project for INFO-664: Programming for Cultural Heritage at the Pratt Institute School of Information

For my final project in INFO-664, I chose to collect lyric data from the website Genius.com. This repository contains the code that I wrote using Python to collect, clean, and analyze my data. The final deliverable for this project is in the form of a Tableau Dashboard, which you can view [here.](https://public.tableau.com/app/profile/kailen.santos3222/viz/Top100LyricalAnalysis/Dashboard1?publish=yes) 

##Data Collection and Process:

The data collected references the top 100 songs for every year since 2000 as compiled by the website https://chart2000.com. After downloading the chart data, I wrote a Python script to request song data for each top-100 song in order to attach lyrics and other metrics to my data. The code utilizes the [lyricsgenius API client](https://lyricsgenius.readthedocs.io/en/master/) to scrape data from Genius using my develeoper credentials.

After collecting the lyrics of each song, I used a combination of packages in the [Natural Langauge Toolkit (NLTK)](https://www.nltk.org) and the [VADER Sentiment Analysis Tool](https://github.com/cjhutto/vaderSentiment) to highlight key words and assign sentiment scores to each song, which are on a scale of -1.0 to 1.0. 

##Visualization

The Tableau dashboard was created using the final outcome of the collection and cleaning process. The visualization contains 3 main components: A circle graph depicting the number of page views for each song and its sentiment scores, a bubble chart that shows the approximated global revenue share and general sentiment of each song, and a pie chart showing the distribution the sentiments of top-100 songs every year.
