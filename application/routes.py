from flask import Flask, render_template, request, redirect, url_for
from application import app, db
from application.models import Restaurants, Reviews
from application.forms import AddReviews, AddRestaurants


@app.route('/')
@app.route('/home')
def home():
    all_reviews = Reviews.query.all()
    all_restaurants = Restaurants.query.all()
    return render_template('homepage.html', all_reviews = all_reviews, all_restaurants = all_restaurants)
    

@app.route('/createreview', methods=['GET', 'POST'])
def createreview():
    form = AddReviews()
    restaurant = Restaurants.query.all()
    form.restaurants_ID.choices.extend([(restaurants.pk, str(restaurants)) for restaurants in restaurant])
    if request.method == 'POST':
        if not form.validate_on_submit():
            pass
        new_review = Reviews(
            title=form.title.data,
            review=form.review.data,
            rating=form.rating.data,
            restaurants_ID = int(form.restaurants_ID.data))
        db.session.add(new_review)
        db.session.commit()
        return  redirect(url_for('home'))
    return render_template('add.html', form = form, restaurants = restaurant)

@app.route("/addrestaurants", methods=["GET", "POST"])
def addrestaurants():
    form = AddRestaurants()
    if request.method == "POST":
        if form.validate_on_submit():
            new_restaurants = Restaurants(
                name = form.name.data,
                cuisine = form.cuisine.data)
            db.session.add(new_restaurants)
            db.session.commit()
            return  redirect(url_for("home"))
    return render_template('addrestaurants.html', title="Add a Restaurant", form = form)
        

@app.route('/updatereview/<int:pk>', methods=['GET', 'POST'])
def updatereview(pk):
    form = AddReviews()
    review = Reviews.query.filter_by( pk=pk ).first()
    if request.method == 'POST':
        review.review = form.review.data
        review.rating = form.rating.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("updateReviews.html", form = form, title = "update review", review = review)




@app.route('/delete/<int:pk>')
def delete(pk):
    review= Reviews.query.filter_by(pk = pk).first()
    db.session.delete(review)
    db.session.commit()
    return redirect(url_for('home'))


   