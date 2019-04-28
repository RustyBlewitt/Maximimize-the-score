from funcs import priority_q
import time
from math import floor

objs = [priority_q() for i in range(16)]

for e, o in enumerate(objs):
    for j in range(e + 1, 1, -1):
        o.enqueue(j)

    print("Array of this tree: " + str(o.nodes))
    o.show_heap()
    print("\n")

    time.sleep(1)

for j in range(14):
        a = o.dequeue()
        print("Dequeued %d\n" %a)
        o.show_heap()
        print("\n")
        time.sleep(1)
