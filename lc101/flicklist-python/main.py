import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):
        movielist = ["Shawn of the Dead", "Ferris Bueller's Day Off", "Interstellar", "Batman Begins", "Logan"]
        return random.choice(movielist)

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        self.response.write(content)

        movie2 = self.getRandomMovie()
        if movie != movie2:
        # build the response string
            content = "<h1>Tomorrow's Movie</h1>"
            content += "<p>" + movie2 + "</p>"
            self.response.write(content)
        else:
            movie2 = self.getRandomMovie()
            content = "<h1>Tomorrow's Movie</h1>"
            content += "<p>" + movie2 + "</p>"
            self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
