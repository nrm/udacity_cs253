#!/usr/bin/env python
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, Udacity!')

application = webapp.WSGIApplication(
                                     [(r'.*', MainPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()

#print 'Content-Type: text/plain'
#print ''
#print "Hello, Udacyti!"
