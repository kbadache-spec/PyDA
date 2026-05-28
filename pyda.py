import os
import requests
import wikipedia
from dotenv import load_dotenv

load_dotenv()
def start(question):
  ##api code
  app_id=os.getenv("WOLFRAM_APP_ID")
  try:
    ##set up url for api call
      url=f"http://api.wolframalpha.com/v1/result?appid={app_id}&i={question}"
    
    ##make api call
      response=requests.get(url)
    ##check status and print
      if response.status_code==200:
        return response.text
      else:
        return wikipedia.summary(question, sentences=2)   
  except:
    ##get from wikipedia
        return "an error occured :("
