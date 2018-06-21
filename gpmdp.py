import argparse
import datetime
import json
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('-p','--path',help='the path to the .json file containing playback info.')
parser.add_argument('-f','--format',help='how to output the playback information. ex: "{A} - {T}" | A = artist, a = album, T = title, l = elaped, L = length, r = one rating icon, R = two rating icons')
args = parser.parse_args()

likeIcon = ''
likeIconFill =  ''
dislikeIcon = ''
dislikeIconFill = ''
noRatingIcon = ''
if args.path:
    filepath = args.path
else:
    filepath = str(Path.home()) + '/.config/Google Play Music Desktop Player/json_store/playback.json'

with open(filepath) as f:
    data = json.load(f)
    if data['playing']:
        elapsed = str(datetime.timedelta(seconds=int(data['time']['current']))//1000)
        length = str(datetime.timedelta(seconds=int(data['time']['total']))//1000)
        if args.format:
            print(args.format.format(A=data['song']['artist'], \
            a=data['song']['album'],T=data['song']['title'], \
            l=elapsed,L=length,r=(likeIconFill if data['rating']['liked'] == 'true' else dislikeIconFill if data['rating']['disliked'] == 'true' else noRatingIcon), \
            R=((likeIconFill if data['rating']['liked'] == 'true' else likeIcon) + ' ' + dislikeIconFill if data['rating']['disliked'] == 'true' else dislikeIcon)))
        else:
            print(data['song']['artist'],'-',data['song']['title'])
            
            
