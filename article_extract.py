from newspaper import Article
import csv

def getLinks():
    links = []
    f = open('links.txt', 'r')
    for link in f.readlines():
        links.append(link.strip())
    f.close()
    return links

def saveToCsv(articles):
    header = ['Title','News','Summary','Keywords']
    with open('articles.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(articles)
    
def getArticleDetails(article):
    details = {}
    details['Title'] = article.title
    details['News'] = article.text
    details['Summary'] = article.summary
    details['Keywords'] = article.keywords
    return details

def fetchArticle(links):
    articles = []
    for link in links:
        article = Article(link)
        article.download()
        article.parse()
        article.nlp()
        article_details = getArticleDetails(article)
        articles.append(article_details)
    return articles
    
if __name__ == "__main__":
    print("Reading links...")
    links = getLinks()
    print("Getting articles...")
    articles = fetchArticle(links)
    print("Saving to csv...")
    saveToCsv(articles)