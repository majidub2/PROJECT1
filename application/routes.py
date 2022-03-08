from flask import Flask, render_template, request, redirect, url_for
from application import app, db
from application.models import restaurants, reviews
from application.forms import Addrestaraunts, Addreviews


@app.route('/')
@app.route('/home')
def home():
    all_reviews = Reviews.query.all()
    all_restaurants = restaurants.query.all()
    return render_template('homepage.html', all_reviews = all_reviews, all_restaurants = all_restaurants)
    

@app.route('/search=<keyword>')
def search(keyword):
    data = db.session.execute(F'SELECT * FROM reviews WHERE desc LIKE '%{keyword}%')
    data = list(data)
    num_results = len(data)
    return render_template('search.html', res = [str(res) for res in data], n = num_results)

@app.route('/createreview', methods=['GET', 'POST'])
def createreview():
    form = Addreviews()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_review = reviews(
                title=form.title.data,
                review=form.review.data,
                rating=form.rating.data)
                # restaraunts = form.restaurants_ID.data)
            db.session.add(new_review)
            db.session.commit()
            return  redirect(url_for('home'))
    return render_template('add.html', form = form)
        

@app.route('/updatereview/<int:pk>', methods=['GET', 'POST'])
def updatereview(pk):
    form = Addreviews()
    review = reviews.query.filter_by(pk=pk).first()
    if request.method == 'POST':
        reviews.review = form.review.data
        review.rating = form.rating.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("update.html", form = form, title = "updated review", review = review)


@app.route('/delete/<int:pk>')
def delete(pk):
    review= reviews.query.filter_by(pk = pk).first()
    db.session.delete(review)
    db.session.commit()
    return redirect(url_for('home'))


   