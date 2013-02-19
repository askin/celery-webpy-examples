import sys
from datetime import datetime
import web
sys.path.append("../celery")
from tasks import celeryAdd
from tasks import celeryDiff
from tasks import celeryMultiple
from tasks import celerySquare
from tasks import celeryAddOndifferentQueue
from tasks import celeryRoluette

from tasks import remoteAdd
from tasks import remoteDiff
from tasks import remoteMultiple
from tasks import remoteSquare

from tasks import Roulette

# web service request with celery
print 'web service request with celery'
result = remoteAdd.delay(5, 2)
while not result.ready():
    pass
print '5 + 2 = %s' % result.get()

# add two numbers on celery
print 'add two numbers on celery'
result = celeryAdd.delay(5, 2)
while not result.ready():
    pass
print '5 + 2 = %s' % result.get()

# add two numbers after 10 seconds
print "Add two number after 10 seconds."
now = datetime.now()
print '%02d:%02d:%02d' % (now.hour, now.minute, now.second)
result = celeryAdd.apply_async((5, 2), countdown=10)
print '5 + 2 = %s' % result.get()
now = datetime.now()
print '%02d:%02d:%02d' % (now.hour, now.minute, now.second)

# add two numbers with another queue
print "add two numbers with another queue"
print "you have to add 'add-queue' consumer to celery"
print "cmd: celery control add_consumer add-queue"
result = celeryAddOndifferentQueue.delay(3, 4)
print "5 + 2 = %s" % result.get()

# test retry operations
print "test retry operations"
try:
    result = celeryRoluette.apply_async((), retry=True)
    print "Result %s" % result.get()
except:
    print "Task fails!!!"

# add tasks to another queue
print "add tasks to another queue"
print "you have to add 'new-queue' consumer"
print "cmd: celery control add_consumer new-queue"
result = celeryAdd.apply_async((5, 2), queue='new-queue')
print "Result %s" % result.get()

# limitless retry example
print "limitless retry example"
r = Roulette()
result = r.apply_async((), retry=True)
print "Result: %s" % result.get()
