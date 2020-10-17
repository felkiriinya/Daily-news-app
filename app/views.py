from flask import render_template
from app import app
from .request import get_sources,get_article
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #Getting Technology related sources

    tech_sources = get_sources('technology')
    business_sources = get_sources('business')
    sports_sources = get_sources('sports')
    
    print(tech_sources)
    title = 'The Daily News'
    return render_template('index.html', title = title, technology = tech_sources, business = business_sources, sports = sports_sources)

@app.route('/source/<id>')
def article(id):
    '''
    view articles function that returns a list of articles on the articles
    '''

    article = get_article(id)
    title = f'Heading {id}'    

    return render_template('article.html',title = title, article = article)