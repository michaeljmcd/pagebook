import sys
import logging
import requests
from readabilipy import simple_json_from_html_string

def extractUrls(urls):
  result = []

  for url in urls:
    logging.debug('Downloading HTML from ' + url)
    req = requests.get(url)
    article = simple_json_from_html_string(req.text, use_readability=True)
    result.append(article)

  return result

def createEbook(data):
  return None

if __name__ == "__main__":
  res = extractUrls(sys.argv[1:])

  print(res)
