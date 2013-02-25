# -*- coding: utf-8 -*-
import sys
from tasks import celeryAdd


def index():
    return '{"status" : "success", "retval" : "Yeap yeah"}'


def add():
    '''Add two numbers with celery
    '''
    try:
        a = int(request.args[0])
        b = int(request.args[1])
        result = celeryAdd.apply_async((a, b)).get()
        return '{"status" : "success", "retval" : %s}' % result
    except Exception, e:
        return '{"status" : "failure", "reason" : "%s"}' % e
