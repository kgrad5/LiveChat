import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os

from datetime import datetime
from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)

class Application(tornado.web.Application):
	chat = {}
	
	def __init__(self):
		handlers = [
				(r"/", IndexHandler),
		]
		settings = dict(
			template_path = os.path.join(os.path.dirname(__file__), "templates"),
			static_path = os.path.join(os.path.dirname(__file__), "static"),
			debug = True,	
		)	
		tornado.web.Application.__init__(self, handlers, **settings)
		
class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('index.html', chatlog = Application.chat)
	def post(self):
		Application.chat[datetime.now().strftime('%x %X')] = self.get_argument('text') 
		self.render('index.html', chatlog = Application.chat)

if __name__ == '__main__':
	# Parse the command line options defined with define() statements, this comes from the
	# tornado.options package
	tornado.options.parse_command_line()
	
	# Boilerplate
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
