import time
import sys

import stomp

conn = stomp.Connection()
conn.connect('admin', 'admin', wait=True)
conn.send('/queue/teste', 'Hello World teste')
time.sleep(2)
conn.disconnect()
