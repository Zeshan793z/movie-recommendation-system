import numpy as np
from flask import Flask, redirect, render_template, request, url_for

from recommendation import recommend_movie

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template('homepage.html')


@app.route("/recommend", methods=['GET', 'POST'])
def recommend():
    if request.method == 'GET':
        return redirect(url_for('homepage'))
    name = request.form['movie_name']
    recommend_movies, images, error = recommend_movie(name)

    new_images = []
    for i in images:
        if type(i) != float:
            new_images.append(i)
        else:
            new_images.append(None)

    return render_template('recommend.html', name=name, movies_count=len(recommend_movies), movies=recommend_movies, images=new_images, error=error)
