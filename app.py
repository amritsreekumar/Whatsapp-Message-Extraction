from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import whatsapp_web
import json
import time
from datetime import datetime

class HelloHandler(RequestHandler):
    def get(self):
        print("Request Received")
        initialtime = datetime.now()
        messages = whatsapp_web.scrape(None)
        i = 0
        for x in messages:
        	if i%2 == 0:
        		messages[i] = 'Peter -- ' + x
        	else:
        		messages[i] = 'Timothy -- ' + x
        	i = i+1
        #print(messages)
        self.write(json.dumps({'chatlog' : messages}))
        print("Request Completed")
        finaltime = datetime.now()
        print(finaltime-initialtime)

def make_app():
    urls = [("/", HelloHandler)]
    return Application(urls)

if __name__ == '__main__':
    app = make_app()
    app.listen(3000)
    IOLoop.instance().start()