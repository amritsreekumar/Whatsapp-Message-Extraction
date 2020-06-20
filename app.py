from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import whatsapp_web

class HelloHandler(RequestHandler):
    def get(self):
        print("Request Received")
        messages = whatsapp_web.scrape(None)
        i = 0
        for x in messages:
        	if i%2 == 0:
        		messages[i] = 'Anish -- ' + x
        	else:
        		messages[i] = 'Amrit -- ' + x
        	i = i+1
        print(messages)
        self.write({'chatlog' : messages})

def make_app():
    urls = [("/", HelloHandler)]
    return Application(urls)

if __name__ == '__main__':
    app = make_app()
    app.listen(3000)
    IOLoop.instance().start()