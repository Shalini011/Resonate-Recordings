from routes import rush_fees
from flask import Flask

app = Flask(__name__)


app.add_url_rule('/', view_func=lambda: "Hello World!!")
app.add_url_rule('/rush-fees', view_func=rush_fees.is_rushed_api)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
