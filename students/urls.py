import tornado.web
from settings import SETTINGS
from views import NavModule

from views import IndexHandler,CardHandler,FamilyHandler,GradeHandler,HealthyHandler,\
SleepHandler,TestHandler,TimeHandler

from ajaxAPI import initWeb,skipWeb,cardWeb,sleepWeb,testWeb,timelineWeb,\
familyWeb,gradeWeb,healthyWeb

from restAPI.v1.restAPI import indexAPI,cardAPI,familyAPI,gradeAPI,healthyAPI,sleepAPI,\
testAPI,timelineAPI

HANDLERS = [
        (r'^/', IndexHandler),
        (r'^/index', IndexHandler),
        (r'^/init', initWeb),
        (r'^/init/skip', skipWeb),
        (r'^/rest/v1/indexAPI', indexAPI),
        
        (r'^/card', CardHandler),
        (r'^/init/card', cardWeb),
        (r'^/rest/v1/cardAPI', cardAPI),
        
        (r'^/family', FamilyHandler),
        (r'^/init/family', familyWeb),
        (r'^/rest/v1/familyAPI', familyAPI),
        
        (r'^/grade', GradeHandler),
        (r'^/init/grade', gradeWeb),
        (r'^/rest/v1/gradeAPI', gradeAPI),
        
        (r'^/healthy', HealthyHandler),
        (r'^/init/healthy', healthyWeb),
        (r'^/rest/v1/healthyAPI', healthyAPI),
        
        (r'^/sleep', SleepHandler),
        (r'^/init/sleep', sleepWeb),
        (r'^/rest/v1/sleepAPI', sleepAPI),
        
        (r'^/test', TestHandler),
        (r'^/init/test', testWeb),
        (r'^/rest/v1/testAPI', testAPI),
        
        (r'^/time', TimeHandler),
        (r'^/init/timeline', timelineWeb),
        (r'^/rest/v1/timelineAPI', timelineAPI),
        ]
        
UI_MODULES={
    'Nav' : NavModule,
}

application = tornado.web.Application(
    handlers = HANDLERS,
    ui_modules=UI_MODULES,
**SETTINGS)
