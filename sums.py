from newspaper import Article
import pandas as pd
#result_df = pd.read_excel('articles_final.xlsx')

#Uses newspaper3k to read and summarize articles. 
def sums(url):
    url = url
    article = Article(url)
    article.download()
    article.parse()
    article.text
    article.nlp()
    article.summary
    return article.summary

#Applies newspaper_sums to a dataframe.
def df_summarizer(df):
    summarized_df= pd.DataFrame(columns=['url', 'seendate', 'source country', 'content', 'company', 'failed'])
    for row in df.itertuples():
        try:
            summarized_df.at[row.Index, 'url'] = row.url
            summarized_df.at[row.Index, 'seendate'] = row.seendate
            summarized_df.at[row.Index, 'source country'] = row.sourcecountry
            summarized_df.at[row.Index, 'content'] = sums(row.url)
            summarized_df.at[row.Index, 'company'] = row.company
            summarized_df.at[row.Index, 'failed'] = 0
        except Exception:
            print(row.url + " failed")
            summarized_df.at[row.Index, 'failed'] = 1

    summarized_df.to_excel('summarized_df.xlsx')