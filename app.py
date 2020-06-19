from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import whatsapp_web

class HelloHandler(RequestHandler):
    def get(self):
        print("Request Received")
        messages = whatsapp_web.scrape(None)
        Dict = {}
        Dict2 = {}
        i = 0
        for x in messages:
        	if i%2 == 0:
        		Dict['Anish'] = x
        		Dict2[i] = Dict
        	else:
        		Dict['Amrit'] = x
        		Dict2[i] = Dict
        	Dict = {}
        	i = i+1
        print(Dict2)
        self.write({'chatlog' : Dict2})

def make_app():
    urls = [("/", HelloHandler)]
    return Application(urls)

if __name__ == '__main__':
    app = make_app()
    app.listen(3000)
    IOLoop.instance().start()