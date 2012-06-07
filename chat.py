import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('index.html', chatlog = [])
	def post(self):
		self.render('index.html', chatlog = self.get_argument('text'))

if __name__ == '__main__':
	# Parse the command line options defined with define() statements, this comes from the
	# tornado.options package
	tornado.options.parse_command_line()
	app = tornado.web.Application(
	
	# Define the routes and their associated handlers. Routes are regexp.
		handlers = [
			(r"/", IndexHandler),
		],
		template_path = os.path.join(os.path.dirname(__file__), "templates"),
		static_path = os.path.join(os.path.dirname(__file__), "static"),
		debug = True
	)
	
	# Boilerplate
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
