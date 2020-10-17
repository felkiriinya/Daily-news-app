from app import app
import urllib.request,json
from .models import source
from .models import articles

Source = source.Source

Articles = articles.Articles


# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config['NEWS_SOURCES_BASE_URL']

#Getting the articles base url
articles_url = app.config['ARTICLES_BASE_URL']


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            sources_results_list =  get_sources_response['sources']
            source_results = process_sources(sources_results_list)

    return source_results    

def process_sources(sources_list):
    '''
    Function that processes the news sources results and turns them into a list of objects
    Args:
            sources_list: A list of dictionaries that contain sources details
    Returns:
            source_results: A list of sources objects
    '''  
    source_results = []
    for source_item in sources_list:
    
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        country = source_item.get('country')
        language = source_item.get('language')

        sources_object = Source(id,name,description,url,category,country,language)

        source_results.append(sources_object)

    return source_results    

def get_article(id):
    '''
    Function that processes the articles and returns a list of articles objects
    '''
    get_article_details_url = articles_url.format(id,api_key)

    with urllib.request.urlopen(get_article_details_url) as url:
       get_article_data = url.read()
       get_articles_response = json.loads(get_article_data)

       articles_results = None

       if get_articles_response['articles']:
           articles_results_list = get_articles_response['articles']
           articles_results = process_articles(articles_results_list) 

    return articles_results       

def process_articles(articles_list):
    articles_object = []
    for article_item in articles_list:
        id = article_item.get('id')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        image = article_item.get('urlToImage')
        date = article_item.get('publishedAt')
         
        if image:
            articles_result = Articles(
                    id, author, title, description, url, image, date)
            articles_object.append(articles_result)

    return articles_object