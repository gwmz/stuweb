import argparse

import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

from students.settings import engine,BaseModel
from students.urls import application

define("port", default=8000, help="run on the given port", type=int)
parser=argparse.ArgumentParser(prog='python main.py', usage='%(prog)s [options]', epilog="test args")

def init_db():
    BaseModel.metadata.create_all(engine)

def drop_db():
    BaseModel.metadata.drop_all(engine)

def getArgs():
    parser.add_argument('-run', action='store_true',help='run tornado server')
    parser.add_argument('-sql', action='store_true',help='create table')
    parser.add_argument('-del', action='store_true',help='drop table')
    args=parser.parse_args()
    return vars(args)
    
def doArgs():
    args=getArgs()
    print args
    if (args['run'] ^ args['sql'] ^ args['del']):
        if args['run']:
            http_server = tornado.httpserver.HTTPServer(application)
            http_server.listen(options.port)
            print "Starting development server at http://127.0.0.1:"+str(options.port)
            print "Quit the server with CONTROL-C."
            tornado.ioloop.IOLoop.instance().start()
        elif args['sql']:
            init_db()
        else:
            drop_db()
    else:
        print parser.print_help()

doArgs()
