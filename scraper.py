from selenium import webdriver
from selenium.webdriver.chrome.options import Options
URL='https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'




def get_driver():
  chrome_options=Options()
  chrome_options.add_argument('--no-    sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
      driver=webdriver.Chrome(options=chrome_options)

  return driver


if__name__=="__main__":
  print('Creating driver')
  driver.get(URL)
  print('Page title:',driver.title)






