from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Restaurants, Reviews
#python3 -m pytest --cov=application
#python3 -m pytest


class TestBase(TestCase):
    def create_app(self): #SETTING UP test configuration
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///test.db',
            SECRET_KEY = 'byemajid',
            DEBUG = True,
            WTF_CSRF_ENABLED = False
        )
        return app

    def setUp(self): #run BEFORE each test (the 'many' side must include the fk)
        db.create_all()
        sample_review = Reviews( title="Sample title", review="Sample review", rating = 3, restaurants_ID = 2 )
        sample_restaurant = Restaurants( name = "Sample name", cuisine = "Sample cuisine")
        db.session.add(sample_review)
        db.session.add(sample_restaurant)
        db.session.commit()
    
    def tearDown(self): #run AFTER each test to "clean up" for the nxt test
        db.session.remove()
        db.drop_all()


class TestHomepage(TestBase):
    def test_homepage_get(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
        self.assertIn(b'Sample title', response.data)


class TestcreateGET(TestBase):
    def test_createreview_get(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
        self.assertIn(b'Sample title', response.data)
 

class TestcreatePOST(TestBase):
    def test_createreview_post(self):
        response = self.client.post(
            url_for('createreview'),
            data = dict(title = 'Sample title 2', review = 'Sample review', rating = 3 ,restaurants_ID = 1),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'Sample title 2', response.data)


class TestaddrestaurantsGET(TestBase):
    def test_addrestaurants_get(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
        self.assertIn(b'Sample name', response.data)


class TestaddrestaurantsPOST(TestBase):
    def test_addrestaurants_post(self):
        response = self.client.post(
            url_for('addrestaurants'),
            data = dict( name = "Sample name 2", cuisine = "Sample cuisine 2"),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'Sample name 2', response.data)

# class TestupdatereviewGET(TestBase):
#     def test_updatereview_get(self):
#         response = self.client.get(url_for('updatereview (pk)'))
#         self.assert200(response)
#         self.assertIn(b'Sample name', response.data)