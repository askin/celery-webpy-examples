import sys
import web
sys.path.append("../celery")
from tasks import celeryAdd
from tasks import celeryDiff
from tasks import celeryMultiple
from tasks import celerySquare
from random import randrange


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

class CeleryService:
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
        # if you don't want to result, remove .get()
        return celeryAdd.delay(arg1, arg2).get()

    def diff(self, arg1, arg2):
        # if you don't want to result, remove .get()
        return celeryDiff.delay(arg1, arg2).get()

    def multiple(self, arg1, arg2):
        # if you don't want to result, remove .get()
        return celeryMultiple.delay(arg1, arg2).get()

    def square(self, arg):
        # if you don't want to result, remove .get()
        return celerySquare.delay(arg).get()
        return arg * arg


class index:
    def GET(self):
        return "Hello World"

class Roulette:
    def GET(self, param=None):
        success = '{"status" : "success", "retval" : "Yeap yeah"}'
        failure = '{"status" : "failure", "reason" : "What the fuck!!!"}'
        if randrange(1, 100) % 5 == 0:
            print "Success"
            return success
        else:
            print "Failure"
            return failure


if __name__ == "__main__":
    urls = (
        '/service/([a-z]*)/(\d+)/(\d+)', 'service',
        '/service/([a-z]*)/(\d+)', 'service',
        '/celery-service/([a-z]*)/(\d+)/(\d+)', 'CeleryService',
        '/celery-service/([a-z]*)/(\d+)', 'CeleryService',
        '/roulette(.*)', 'Roulette',
        '/', 'index'
        )
    app = web.application(urls, globals())
    app.run()
