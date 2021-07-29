import requests

url = 'http://128.199.247.96:3000/api/music'
r = requests.get(url,allow_redirects=True)

print(r.content)
# open('Sunkissed.mp3',('wb')).write(r.content)

