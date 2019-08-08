import webapp2
import jinja2
import os
import random
from google.appengine.ext import ndb
from models.city import City
from google.appengine.api import memcache

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class FavPage(webapp2.RequestHandler):
    def get(self):
        cities = City.query(City.name != '').fetch()
        favorites_template = jinja_env.get_template('templates/favorites.jinja')
        self.response.write(favorites_template.render({ "cities": cities }))
    def post(self):
        cities = self.request.get_all('city[]')
        cities = list(dict.fromkeys(cities))
        for city in cities:
            slug = city.replace(' ', '-').lower()
            newCity = City(name = city, slug = slug)
            newCity.put()

        removed_cities = self.request.get_all('removed_city[]')
        removed_cities = list(dict.fromkeys(removed_cities))
        for removed_city in removed_cities:
            saved_cities = City.query(City.name == removed_city).fetch(keys_only=True)
            ndb.delete_multi(saved_cities)
        self.redirect('/')
app = webapp2.WSGIApplication([
    ('/', FavPage)
], debug=True)
