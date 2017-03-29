from itertools import groupby
import spotipy
import sys
from itertools import combinations

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
