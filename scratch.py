import requests
from bs4 import BeautifulSoup
URL='https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'

response=requests.get(URL)
print('Status Code',response.status_code)

with open('trending.html','w') as f:
  f.write(response.text)
doc=BeautifulSoup(response.text,'html.parser')


print('Page title:',doc.title.text)
# Find all the video divs

video_divs=doc.find_all('div',class_='ytd-video-renderer')

print(f'Found{len(video_divs)} videos')


# This above command written can't take dynamics pages input because above code took static webpage info ... Node JS
