import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        user_locale = self.get_user_locale()
        if user_locale:
            self.write(f'Hello, world! Your language is {user_locale}')
        else:
            self.write(f'Hello, world!')


class LocaleHandler(tornado.web.RequestHandler):
    def get(self, locale):
        self.locale = tornado.locale.get(locale)
        self.render("index.html", product=1, author='Shevchuck G.K.', view=1234)


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/([^/]+)/about-us', LocaleHandler)],
        template_path='templates/',
        debug=True,
        autoreload=True
    )


if __name__ == "__main__":
    tornado.locale.load_translations('locale/')
    app = make_app()

    port = 8888
    app.listen(port)
    print('Server is listening on port {}'.format(port))

    # to start the server on the current thread
    tornado.ioloop.IOLoop.current().start()
