from itertools import groupby
import spotipy
import sys
from itertools import combinations
import subprocess

youtube_id = '6s5vlQdQp4s'

program_to_call = 'youtube-dl'
arg1 = r"-o data/{0}\"/%(id)s.%(ext)s\"".format(youtube_id)
arg2 = '-x'
arg3 = '--sub-lang'
arg4 = 'en'
arg5 = '--write-sub'
arg6 = '--sub-format'
arg7 = 'vtt'
arg8 = '--convert-subtitles'
arg9 = 'srt'
arg10 = '--write-auto-sub'
arg11 = '--continue'
arg12 = '--write-info-json'
arg13 = '--write-description'
arg14 = '--write-annotations'
arg15 = '--min-filesize'
arg16 = '50k'
arg17 = '--ignore-errors'
arg18 = '--write-all-thumbnails'
arg19 = '--no-call-home'
arg20 = '--audio-format'
arg21 = 'mp3'
arg22 = youtube_id

subprocess.call([program_to_call, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21, arg22])





file_name = r'data/r-XuaFIfP2E/r-XuaFIfP2E.en.srt'

with open(file_name) as f:
    res = [list(g) for b, g in groupby(f, lambda x: bool(x.strip())) if b]

text_raw = [i[2:] for i in res]

spotify = spotipy.Spotify()

count = 0
for line in sorted(text_raw):
    count += 1
    print("testing line {0} of {1}".format(count, len(text_raw)))
    try:
        lst = line[0].split()
        for start, end in combinations(range(len(lst)), 2):
            name_list = lst[start:end+1]
            try_name = ' '.join(name_list)
            results = spotify.search(q='artist:' + try_name, type='artist')
            items = results['artists']['items']
            if len(items) > 0:
                # import ipdb; ipdb.set_trace()
                # print(try_name)
                artist = items[0]
                if try_name.lower() == artist['name'].lower():
                    print(artist['name'], artist['images'][0]['url'])
    except IndexError:
        pass
