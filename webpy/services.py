import web


class service:
    def GET(self, op, arg1, arg2=None):
        template = '{"status" : "success", "retval" : %s}'
        failure = '{"status" : "failure", "reason" : "%s"}'

        try:
            if op == 'add':
                rt = template % self.add(int(arg1), int(arg2))
            elif op == 'diff':
                rt = template % self.diff(int(arg1), int(arg2))
            elif op == 'multiple':
                rt = template % self.multiple(int(arg1), int(arg2))
            elif op == 'square':
                rt = template % self.square(int(arg1))
            else:
                rt = failure % 'unknown op'
        except TypeError, e:
            rt = failure % e

        return rt

    def add(self, arg1, arg2):
        return arg1 + arg2

    def diff(self, arg1, arg2):
        return arg1 - arg2

    def multiple(self, arg1, arg2):
        return arg1 * arg2

    def square(self, arg):
        return arg * arg


class index:
    def GET(self):
        return "Hello World"


if __name__ == "__main__":
    urls = (
        '/service/([a-z]*)/(\d+)/(\d+)', 'service',
        '/service/([a-z]*)/(\d+)', 'service',
        '/', 'index'
        )
    app = web.application(urls, globals())
    app.run()
