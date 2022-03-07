from flask import Flask, render_template, request, redirect, url_for
from application import app, db
from application.models import restaurants, reviews
from application.forms import Addrestaraunts, Addreviews


@app.route("/")
@app.route("/home")
def home():
    all_reviews = Reviews.query.all()
    all_restaurants = restaurants.query.all()
    

@app.route("/search=<keyword>")
def search(keyword):
    data = db.session.execute(F"SELECT * FROM reviews WHERE desc LIKE '%{keyword}%")



@app.route("/create", methods=["GET", "POST"])
def create():
    form = reviewForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_review = reviews(
                title=form.title.data,
                review=form.review.data,
                rating=form.rating.data,
                restaraunts = restaurants.id
            )
            db.session.add(new_review)
            db.session.commit()
            return  redirect(url_for("home"))
        
   