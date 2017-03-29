# nardify
An app to create Spotify playlists from Nardwuar's interviews

## Introduction
I always watch Nardwuar's [interviews](https://www.youtube.com/channel/UC8h8NJG9gacZ5lAJJvhD0fQ) and wanted to chase up the artists and records that are mentioned. I thought I'd try and automate this by scouring the videos' subtitle files for possible artist names on Spotify and then creating a playlist based on the interview.

## Requirements
Nardify requires the following:

- [youtube-dl](https://rg3.github.io/youtube-dl/)
Which downloads the YouTube video's audio track and accompanying subtitles file in `srt` format (if available), although it's only the subtitle file we're interested in.
- [spotipy](https://github.com/plamere/spotipy)
This is a Python client for the Spotify API which Nardify uses to make searches of possible artists and to generate playlists.

## Usage
You use Nardify by calling
