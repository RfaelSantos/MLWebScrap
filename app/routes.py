from flask import Flask, render_template, request
from mercado_livre_scraper import MercadoLivreScraper

app = Flask(__name__)
mercado_livre_scraper = MercadoLivreScraper()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    query = request.args.get('query')

    mercado_livre_scraper.connect()

    names, prices, links = mercado_livre_scraper.search_product(query)

    if names and prices:
        df = mercado_livre_scraper.create_dataframe(names, prices, links)
        divs = []
        for _, row in df.iterrows():
            divs.append(render_template('result_div.html', name=row['Name'], price=row['Price'], link=row['Link']))
        mercado_livre_scraper.driver.quit()
        return render_template('search_results.html', divs=divs)

    return "No results found!"
