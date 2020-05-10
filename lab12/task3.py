import json
import re
import urllib.request

from pytube import YouTube

api_key = "AIzaSyAJv5kq-Eq9IFJI-dVOSf40N73ffcgdzAU"

url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}& key={api_key}"