class Config:
    '''
    General configuration parent class
    '''
    # https://newsapi.org/v2/sources?apiKey=f1ffdc1e372b4ca09f0a7c5abe5a0194
    # https://newsapi.org/v2/top-headlines?country=us&apiKey=f1ffdc1e372b4ca09f0a7c5abe5a0194
    # https://newsapi.org/v2/everything?q=bitcoin&apiKey=f1ffdc1e372b4ca09f0a7c5abe5a0194

    NEWS_SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'


class ProdConfig(Config):
    '''articles_result = Articles(
                id, author, title, description, url, image, date)
        articles_object.append(articles_result)

    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True