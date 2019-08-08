from google.appengine.ext import ndb

class City(ndb.Model):
    name = ndb.StringProperty()
    slug = ndb.StringProperty()
