from my_app import app
from flask import render_template, request, redirect
import requests

name="Enlighten Me"
facts = {"Birthday":"February 29, 1964", "Favorite Color": "blue", "Favorite Hackathon": "HackMIT"}
posts = [{"title": "Topic:", "description": "enter controversial topic"}]

@app.route("/")
def index():
    return render_template("index.html", name=name, facts=facts, posts=posts)

@app.route("/change_name")
def change_name():
    global name
    new_name = request.args.get('name')
    name = new_name
    return redirect("/")

@app.route("/post", methods=["POST"])
def post():
    global posts
    if request.method == "POST":
        print(request)
        post_info = request.get_json()
        posts.append({"title": post_info["title"], "description": post_info["description"]})
    return redirect("/")

