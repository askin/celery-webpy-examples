from celery.task import task
from celery.task.http import HttpDispatchTask
from random import randrange

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

@task
def celeryAdd(x, y):
    return x + y

@task
def celeryDiff(x, y):
    return x - y

@task
def celeryMultiple(x, y):
    return x * y

@task
def celerySquare(x):
    return x * x

@task(queue='add-queue', name='add_queue')
def celeryAddOndifferentQueue(x, y):
    """Run add operation on different queue named 'add-queue'
    """
    return x + y

@task
def remoteRoluette(count=0):
    """Call roulette service
    """
    try:
        res = HttpDispatchTask.delay(
            url='http://localhost:8080/roulette/',
            method='GET')
        return res.get()
    except Exception, e:
        print "Retry %s" % count
        remoteRoluette.retry((count + 1,),
                             exc=e,
                             countdown=2)

@task
def celeryRoluette(count=0):
    """Call roulette service
    """
    if randrange(1, 100) % 5 == 0:
        print True
        return True
    else:
        print "Retry: %s" % count
        raise celeryRoluette.retry((count + 1,),
                                   exc=Exception("No no no %s" % count),
                                   countdown=2)
