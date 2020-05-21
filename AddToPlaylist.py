# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlistItems.insert
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from youtube_api import YouTubeDataAPI
import pandas as pd

playlistID = "PLAYLIST_ID"
api_key = "API_KEY"

yt = YouTubeDataAPI(api_key)
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def authorize():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "CONFIG_FILE_NAME"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    return youtube


def prepareBody(videoID, playlistID):
    body = {
        "snippet": {
            "playlistId": playlistID,
            "resourceId": {
                "playlistId": playlistID,
                "videoId": videoID,
                "kind": "youtube#video"
            },
            "channelId": "UCdwKsR4DCUhOakMHc1o6weg"
        }
    }
    return body


def getVideosByPhrase(query):
    global yt
    searches = yt.search(query, max_results=10000)
    df_search = pd.DataFrame(searches)
    pd.set_option('display.max_rows', df_search.shape[0] + 1)
    return df_search


def checkAlreadyAdded(videoId):
    was_added = False
    with open("already_added.txt", "r") as added:
        for line in added.readlines():
            if videoId in line:
                was_added = True
    return was_added




def main():
    youtube = authorize()
    df_search = getVideosByPhrase("hot16challenge")
    df_search.video_id.drop_duplicates()
    for idx, row in df_search.iterrows():
        video_id = row["video_id"]
        if checkAlreadyAdded(video_id):
            print("Video " + video_id + " was added to playlist")
        else:
            request = youtube.playlistItems().insert(
                part="snippet",
                body=prepareBody(video_id, playlistID)
            )
            response = request.execute()
            print(response)
            with open("already_added.txt", "a") as added:
                added.write(video_id + "\n")


if __name__ == "__main__":
    main()
