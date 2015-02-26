#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:   Travis A. Ebesu
@created:  2015-02-26
@summary:  Multithreaded URL requests
'''
from Queue import Queue
from threading import Thread
from urllib2 import urlopen


def url_request(queue):
    while True:
        # Get URL
        url = queue.get()
        # Open url
        res = urlopen(url)
        # NOTE: if you want this data,
        #       implement another queue
        print res.read()[:50]

        # Signal we finished this task
        queue.task_done()

# Queues are thread safe
queue = Queue()
thread_count = 2
urls = ['http://www.google.com', 'http://www.yahoo.com']

# populate queue with work
for url in urls:
    queue.put(url)

# Start Threads
for i in xrange(thread_count):
    worker = Thread(target=url_request, args=(queue, ))
    worker.setDaemon(True)
    worker.start()


# Wait for queue to finish
queue.join()
