import json
import traceback
import tornado.web
from studentsBak import initBak,cardBak,familyBak,gradeBak,healthyBak,sleepBak,timelineBak,testBak

class initWeb(tornado.web.RequestHandler):
    def get(self):
        result = {}
        try:
            result = initBak()
            result['state'] = 0
        except:
            result['state'] = -1
        finally:
            self.write(json.dumps(result))
            
class skipWeb(tornado.web.RequestHandler):
    def get(self):
        rData = {}
        try:
            self.set_header('Content-Type', 'application/json; charset=UTF-8')
            rData = FailedStudent.entry()#{}
            rData['state'] = 0
        except:
            rData['state'] = -1
            traceback.print_exc()
        finally:
            self.write(json.dumps(rData))

class cardWeb(tornado.web.RequestHandler):
    def get(self):
        result = {}
        try:
            self.set_header('Content-Type', 'application/json; charset=UTF-8')
            stuID = self.get_argument('stuID',default='', strip=True)
            result = cardBak(stuID)
            result['state'] = 0
        except:
            result['state'] = -1
            traceback.print_exc()
        finally:
            self.write(json.dumps(result))

class familyWeb(tornado.web.RequestHandler):
    def get(self):
        result = {}
        try:
            self.set_header('Content-Type', 'application/json; charset=UTF-8')
            stuID = self.get_argument('stuID',default='', strip=True)
            result = familyBak(stuID)
            result['state'] = 0
        except:
            result['state'] = -1
            traceback.print_exc()
        finally:
            self.write(json.dumps(result))

class gradeWeb(tornado.web.RequestHandler):
    def get(self):
        result = {}
        try:
            self.set_header('Content-Type', 'application/json; charset=UTF-8')
            stuID = self.get_argument('stuID',default='', strip=True)
            result = gradeBak(stuID)
            result['state'] = 0
        except:
            result['state'] = -1
            traceback.print_exc()
        finally:
            self.write(json.dumps(result))

class healthyWeb(tornado.web.RequestHandler):
    def get(self):
        result = {}
        try:
            self.set_header('Content-Type', 'application/json; charset=UTF-8')
            stuID = self.get_argument('stuID',default='', strip=True)
            result = healthyBak(stuID)
            result['state'] = 0
        except:
            result['state'] = -1
            traceback.print_exc()
        finally:
            self.write(json.dumps(result))

class sleepWeb(tornado.web.RequestHandler):
    def get(self):
        result = {}
        try:
            self.set_header('Content-Type', 'application/json; charset=UTF-8')
            stuID = self.get_argument('stuID',default='', strip=True)
            result = sleepBak(stuID)
            result['state'] = 0
        except:
            result['state'] = -1
            traceback.print_exc()
        finally:
            self.write(json.dumps(result))
            
class testWeb(tornado.web.RequestHandler):
    def get(self):
        result = {}
        try:
            self.set_header('Content-Type', 'application/json; charset=UTF-8')
            stuID = self.get_argument('stuID',default='', strip=True)
            result = testBak(stuID)
            result['state'] = 0
        except:
            result['state'] = -1
            traceback.print_exc()
        finally:
            self.write(json.dumps(result))   
            
class timelineWeb(tornado.web.RequestHandler):
    def get(self):
        result = {}
        try:
            self.set_header('Content-Type', 'application/json; charset=UTF-8')
            stuID = self.get_argument('stuID',default='', strip=True)
            result = timelineBak(stuID)
            result['state'] = 0
        except:
            result['state'] = -1
            traceback.print_exc()
        finally:
            self.write(json.dumps(result))         
