#gdelt mega search, dates must be in YYYYMMDD format, no slashes
from gdeltdoc import GdeltDoc, Filters, near, repeat
import re
import pandas as pd
from time import sleep

#Function that iterates through a dictionary of companies and searches for articles about potential new hires in executive positions. 
#Currently only set to search once, however, uncomment as many blocks as you like in order to broaden the search. 
#The function will return a dataframe of all articles found, and will save it to an excel file contianing the URLS, titles, and dates of the articles.

def gdelt_search(dictionary, start_date, end_date):
    dfs = []
    for key, value in dictionary.items():
        f = Filters(
            keyword = "{} new chief marketing officer".format(key),
            start_date = start_date,
            end_date = end_date,
            country = ["UK", "US", "AU"]
            #theme = "TAX_FNCACT_BUSINESS_LEADERS",
            #near = near(10, "Disney", "company"),
        )
        
        sleep(2)
        print('searching {}'.format(key))
        gd = GdeltDoc()
        articles = gd.article_search(f)
        articles['company'] = key
        dfs.append(articles)
        '''
        f2 = Filters(
            keyword = "{} chief marketing officer".format(key),
            start_date = start_date,
            end_date = end_date,
            country = ["UK", "US", "AU"]
            #theme = "TAX_FNCACT_BUSINESS_LEADERS",
            #near = near(10, "Disney", "company"),
        )
        sleep(2)
        gd = GdeltDoc()
        articles2 = gd.article_search(f2)
        articles2['company'] = key
        dfs.append(articles2)
        f3 = Filters(
            keyword = "{} new CEO".format(key),
            start_date = start_date,
            end_date = end_date,
            country = ["UK", "US", "AU"]
            #theme = "TAX_FNCACT_BUSINESS_LEADERS",
            #near = near(10, "Disney", "company"),
        )

        gd = GdeltDoc()
        articles3 = gd.article_search(f3)
        articles3['company'] = key
        dfs.append(articles3)
        f4 = Filters(
            keyword = "{} new CMO".format(key),
            start_date = start_date,
            end_date = end_date,
            country = ["UK", "US", "AU"]
            #theme = "TAX_FNCACT_BUSINESS_LEADERS",
            #near = near(10, "Disney", "company"),
        )
        sleep(2)

        gd = GdeltDoc()
        articles4 = gd.article_search(f4)
        articles4['company'] = key
        dfs.append(articles4)
        f5 = Filters(
            keyword = "{} new chief executive officer".format(key),
            start_date = start_date,
            end_date = end_date,
            country = ["UK", "US", "AU"]
            #theme = "TAX_FNCACT_BUSINESS_LEADERS",
            #near = near(10, "Disney", "company"),
        )
        sleep(2)

        gd = GdeltDoc()
        articles5 = gd.article_search(f5)
        articles5['company'] = key
        dfs.append(articles5)
        f6 = Filters(
            keyword = "{} new chief marketing officer".format(key),
            start_date = start_date,
            end_date = end_date,
            country = ["UK", "US", "AU"]
            #theme = "TAX_FNCACT_BUSINESS_LEADERS",
            #near = near(10, "Disney", "company"),
        )
        sleep(2)

        gd = GdeltDoc()
        articles6 = gd.article_search(f6)
        articles6['company'] = key
        dfs.append(articles6)
        '''
    try:  
        gdelt_articles = pd.concat(dfs)
        gdelt_articles = gdelt_articles.drop_duplicates(subset = 'title')
        gdelt_articles.to_excel('gdelt_articles.xlsx')
        return gdelt_articles
    except ValueError:
        print("{} no articles found".format(key))