import json
import traceback
import tornado.web
from students.studentsBak import initBak,cardBak,familyBak,gradeBak,healthyBak,sleepBak,timelineBak,testBak

class indexAPI(tornado.web.RequestHandler):
    def get(self):
        result = {}
        try:
            result = initBak()
            result['state'] = 0
        except:
            result['state'] = -1
        finally:
            self.write(json.dumps(result))

class cardAPI(tornado.web.RequestHandler):
    def get(self):
        quest = self.request.body
        data = json.loads(quest)
        stuID = data
        result = {}
        try:
            result = cardBak(stuID)
            result['state'] = 0
        except:
            result['state'] = -1
            traceback.print_exc()
        finally:
            self.write(json.dumps(result))

class familyAPI(tornado.web.RequestHandler):
    def get(self):
        quest = self.request.body
        data = json.loads(quest)
        stuID = data
        result = {}
        try:
            result = familyBak(stuID)
            result['state'] = 0
        except:
            result['state'] = -1
            traceback.print_exc()
        finally:
            self.write(json.dumps(result))

class gradeAPI(tornado.web.RequestHandler):
    def get(self):
        quest = self.request.body
        data = json.loads(quest)
        stuID = data
        result = {}
        try:
            result = gradeBak(stuID)
            result['state'] = 0
        except:
            result['state'] = -1
            traceback.print_exc()
        finally:
            self.write(json.dumps(result))

class healthyAPI(tornado.web.RequestHandler):
    def get(self):
        quest = self.request.body
        data = json.loads(quest)
        stuID = data
        result = {}
        try:
            result = healthyBak(stuID)
            result['state'] = 0
        except:
            result['state'] = -1
            traceback.print_exc()
        finally:
            self.write(json.dumps(result))

class sleepAPI(tornado.web.RequestHandler):
    def get(self):
        quest = self.request.body
        data = json.loads(quest)
        stuID = data
        result = {}
        try:
            result = sleepBak(stuID)
            result['state'] = 0
        except:
            result['state'] = -1
            traceback.print_exc()
        finally:
            self.write(json.dumps(result))
            
class testAPI(tornado.web.RequestHandler):
    def get(self):
        quest = self.request.body
        data = json.loads(quest)
        stuID = data
        result = {}
        try:
            result = testBak(stuID)
            result['state'] = 0
        except:
            result['state'] = -1
            traceback.print_exc()
        finally:
            self.write(json.dumps(result))   
            
class timelineAPI(tornado.web.RequestHandler):
    def get(self):
        quest = self.request.body
        data = json.loads(quest)
        stuID = data
        result = {}
        try:
            result = timelineBak(stuID)
            result['state'] = 0
        except:
            result['state'] = -1
            traceback.print_exc()
        finally:
            self.write(json.dumps(result))    
