import tornado.web

class NavModule(tornado.web.UIModule):
    def render(self):
        return self.render_string(
            "nav.html"
        )


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class CardHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('card.html')

class FamilyHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('family.html')

class GradeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('grade.html')
class HealthyHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('healthy.html')
class SleepHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('sleep.html')
class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('test.html')
class TimeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('time.html')
