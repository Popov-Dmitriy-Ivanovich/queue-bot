import queue
def add_to_queue(q,val):
    q.put(val)
    return q
def top_of_queue(q):
    return q.get()
def remove_top(q):
    q.get()
    return q
q = queue.Queue()
q = add_to_queue(q, 2)
q = add_to_queue(q, 0)
q = add_to_queue(q, 1)
while not q.empty():
    print(top_of_queue(q))
print(q.empty())