from application import db


class Restaurants(db.Model): #ONE restaurant
    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    cuisine = db.Column(db.String(15), nullable=False)
    restaurant_reviews = db.relationship('Reviews', backref = 'restaurants') #benefit of this is that you can query further to return what you want by using methods like filter/filter_by, order_by
    def __str__(self):
        return f"{self.name} is a {self.cuisine} restaurant"
#    


class Reviews(db.Model): #MANY reviews
    pk = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(50), nullable=False)
    review = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    restaurants_ID = db.Column(db.Integer, db.ForeignKey('restaurants.pk'))