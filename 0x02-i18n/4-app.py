#!/usr/bin/env python3
"""Basic Flask App"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration Class for Flask"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


#@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel.init_app(app, locale_selector=get_locale)

@app.route('/')
def get_index() -> str:
    """Home/index route"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
