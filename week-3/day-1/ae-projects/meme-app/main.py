import webapp2
import jinja2
import os
import random

memeBackgrounds = [
    'https://i.imgflip.com/8p0a.jpg',
    'https://i.kym-cdn.com/entries/icons/mobile/000/023/732/damngina.jpg',
    'https://i.imgflip.com/7m181.jpg',
    'https://i.kym-cdn.com/entries/icons/original/000/027/475/Screen_Shot_2018-10-25_at_11.02.15_AM.png',
    'https://i.kym-cdn.com/entries/icons/original/000/024/062/jerry.jpg',
    'https://www.dailydot.com/wp-content/uploads/2019/03/Unsettled_Tom.jpg',
    'https://i.redd.it/9qivj9l5mdb31.jpg',
    'https://video-images.vice.com/articles/5ae37ca3d7a39f000a7328ad/lede/1524858049454-Screen_Shot_2018-03-28_at_113259_AM.jpeg?crop=0.5625xw%3A1xh%3Bcenter%2Ccenter&resize=650%3A*&output-quality=55',
    'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/mocking-spongebob-1556133078.jpg',
    'https://mondrian.mashable.com/uploads%252Fcard%252Fimage%252F748607%252F73afa0f3-7ef2-4a95-9384-d882abd6b684.png%252F950x534__filters%253Aquality%252880%2529.png?signature=Sg4DErLyhoUELvQhvVxjV60xPsc=&source=https%3A%2F%2Fblueprint-api-production.s3.amazonaws.com',
    'http://thinkingmeme.com/wp-content/uploads/2018/02/Roll-Safe-Think-About-It.jpg',
    'https://media2.giphy.com/media/9JmaNq2uwAab01xKIV/giphy.gif',
    'https://media0.giphy.com/media/l1taVz9esdyGNiUVi/giphy.gif'
]

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        index_template = jinja_env.get_template('templates/index.html')
        self.response.write(index_template.render())

class MemePage(webapp2.RequestHandler):
    def post(self):
        lines = self.request.get('line[]', allow_multiple = True)
        template_ctx = {
            "bg_image": random.choice(memeBackgrounds),
            "lines": lines
        }
        meme_template = jinja_env.get_template('templates/meme.jinja')
        print lines
        self.response.write(meme_template.render(template_ctx))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/meme', MemePage)
], debug=True)
