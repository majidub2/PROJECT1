from application import db


class restaraunts(db.Model): #ONE restaurant
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cuisine = db.Column(db.String(100), nullable=False)
    def __str__(self):
        return f"{self.name} is a {self.cuisine} restaurant"
    


class reviews(db.Model): #MANY reviews
    id = db.Column(db.Integer, primary_key=True) 
    title = db.column(db.string(50, nullable=False)
    review = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    restaurants = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    def __str__(self):
        return f"The restaurant scored a {self.rating}, with the following review, titled \n {self.title}: \n {self.review}"