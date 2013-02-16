from celery.task import task
from celery.task.http import HttpDispatchTask

from sys import asd

@task
def add(x, y):
    print "I received %s %s" % (x, y)
    return x + y

@task
def remoteAdd(x, y):
    res = HttpDispatchTask.delay(
        url='http://localhost:8080/service/add/%s/%s' % (x, y),
        method='GET')
    return res.get()

@task
def remoteMultiple(x, y):
    res = HttpDispatchTask.delay(
        url='http://localhost:8080/service/mutiple/%s/%s' % (x, y),
        method='GET')
    return res.get()

@task
def remoteSquare(x, y):
    res = HttpDispatchTask.delay(
        url='http://localhost:8080/service/square/%s' % (x, y),
        method='GET')
    return res.get()

@task
def remoteDiff(x, y):
    res = HttpDispatchTask.delay(
        url='http://localhost:8080/service/diff/%s/%s' % (x, y),
        method='GET')
    return res.get()
