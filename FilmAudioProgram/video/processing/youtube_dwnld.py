'''
Created on May 21, 2015

@author: Mitali
'''
from __future__ import print_function

from pytube import YouTube


# not necessary, just for demo purposes
from pprint import pprint

yt = YouTube()

# Set the video URL.
yt.url = "https://youtu.be/Ik-RsDGPI5Y"

pprint(yt.videos)

# view the auto generated filename:

print(yt.filename)

# set the filename:
yt.filename = 'pf2'

# You can also filter the criteria by filetype.

pprint(yt.filter('flv'))

print(yt.filter('mp4')[-1])

# you can also get all videos for a given resolution
pprint(yt.filter(resolution='240p'))

video = yt.get('mp4', '240p')

pprint(yt.videos)

video = yt.get('mp4')

video.download()
