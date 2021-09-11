from collections import deque

queue = deque()

queue.append(5)
print(queue)
queue.append(4)
print(queue)
queue.append(3)
print(queue)
queue.append(2)
print(queue)
queue.append(1)
print(queue)

queue.pop() # stack : FILO 
print(queue)

queue.popleft() # queue : FIFOs
print(queue)
print(list(queue)) # deque의 list 변환