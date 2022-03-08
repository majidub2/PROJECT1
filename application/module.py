from application import db


class Restaurants(db.Model): #ONE restaurant
    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cuisine = db.Column(db.String(100), nullable=False)
    restaurant_reviews = db.relationship('reviews', backref = restaurants)
    def __str__(self):
        return f"{self.name} is a {self.cuisine} restaurant"
    


class Reviews(db.Model): #MANY reviews
    pk = db.Column(db.Integer, primary_key=True) 
    title = db.column(db.String(50, nullable=False)
    review = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    restaurants_ID = db.Column(db.Integer, db.ForeignKey('restaurants.pk'))
    def __str__(self):
        return f"The restaurant scored a {self.rating}, with the following review, titled \n {self.title}: \n {self.review}"