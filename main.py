from gdelt_search import gdelt_search
from company_regexes import company_regexes
from sums import df_summarizer, sums

def main():
    gdelt_articles = gdelt_search(company_regexes, '2023-05-17', '2023-05-18')
    df_summarizer(gdelt_articles)
    
if __name__ == '__main__':
    main()