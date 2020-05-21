#YouTube Playlist Adder

##Description

I've created that script in purpose of create my playlist with all videos connected with one of the most awesome challenge known mainly in Poland.

This challenge name is #hot16challenge2 and it's started by Polish rapper named Solar. It was organized for charity purpose to rise funds for Polish medical care during the COVID-19 epidemic.

More information about that challenge:

Hot16challenge is an initiative for rappers and singers. Idea of the action is to record one verse including 16 bars, publish it and then nominate four more artists who have 72 hours to reply. Main goal of Hot16challenge is to activate as many artists as possible and to mobilize firstly hip-hop industry, then hopefully whole music industry to help fight COVID-19 by music.
Hot16challenge participants and their fans as well can donate to link or any charity campaign in fight with coronavirus. Official Site: <a href="hot16challenge.network">hot16challenge.network</a>


##Installation

I was running the script using Python 3.7 and I don't know if it will work on lower versions.

To run a script you need to firstly install packages from requirments.txt 

<i>pip install -r requirments.txt</i>

##Configuration

For configuration purpose you need configure OAuth credentials and ApiKey for connecting to YouTubeData API - <a href="https://developers.google.com/youtube/v3/quickstart/python">More info</a>

After you will have your authorization data replace variables:

- api_key = "API_KEY"
- client_secrets_file = "CONFIG_FILE_NAME"
- playlistID = "PLAYLIST_ID" - for example in this link https://www.youtube.com/playlist?list=PLoA2YWj0Z65ZEC3n6J_aAsKn0TeuMb0LB is PLoA2YWj0Z65ZEC3n6J_aAsKn0TeuMb0LB

````