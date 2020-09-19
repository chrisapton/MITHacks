from my_app import app
from flask import render_template, request, redirect
import requests

name="Justin Yu"
facts = {"Birthday":"April 10th, 2000", "Favorite Color": "blue", "Favorite Hackathon": "HackMIT"}
posts = [{"title": "This is my 1st post!", "description": "this is my first description!"}]

name="Shirlyn"
facts = {"Birthday":"February 29, 1964", "Favorite Color": "blue", "Favorite Hackathon": "HackMIT"}
posts = [{"title": "This is my 1st post!", "description": "this is my first description!"}]

@app.route("/")
def index():
    return render_template("index.html", name=name, facts=facts, posts=posts)