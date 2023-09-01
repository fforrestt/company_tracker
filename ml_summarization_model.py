from company_regex import company_regexes
from gdeltdoc import GdeltDoc, Filters, near, repeat
import re 

f = Filters(
    #keyword = "('new chief marketing officer' OR 'hiring')",
    keyword = "hiring",
    start_date = "2023-04-01",
    end_date = "2023-05-10",
    country = ["UK", "US", "AU"],
    #theme = "TAX_FNCACT_BUSINESS_LEADERS",
    #near = near(10, "Disney", "company"),
)

gd = GdeltDoc()

# Search for articles matching the filters
articles = gd.article_search(f)

# Get a timeline of the number of articles matching the filters
# timeline = gd.timeline_search("timelinevol", f)


import pandas as pd
pd.set_option('display.max_rows', 500)

print(articles)

from urllib.request import Request, urlopen
import requests
from boilerpy3 import extractors

extractor = extractors.ArticleExtractor()

# extracted content chunks from GDELT URLs go into this list
juicy_content_list = []


def regex_checker(content):
    matches_found = False
    for pattern in company_regexes.values():
        matches = re.findall(pattern, content)
        if matches:
            matches_found = True
            break
    if matches_found:
        juicy_content_list.append(content)

urls = articles['url'].to_list()
# urls = urls[0:10]

for url in urls:
    try:
        req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
        html = urlopen(req).read()   
        html = str(html.decode('utf-8'))
        content = extractor.get_content(html)
        regex_checker(content) # juicy content is a clean list of str content chunks
    except Exception as e:
        print(f"Caught an exception: {e}")
        continue


print(juicy_content_list)
print(juicy_content_list)


# STEP 1: USE SUMMARIZATION ALGO
# uses transformers lib
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn",truncation=True)
sum_content_list = [] # summarized content goes in here
# sum_content_list: a list of lists where each list contains a dict with "summary text:" as k and summary as v

for content in juicy_content_list:
    summary = summarizer(content) # 152--magic number--won't break QA model
    sum_content_list.append(summary)
#print(sum_content_list) 
print(sum_content_list)
