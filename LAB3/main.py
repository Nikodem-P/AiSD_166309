from linkedlist import Node, LinkedList
from stack import Stack
from queue import Queue

stos = Stack()
print(f'Dlugosc: {len(stos)}')
stos.push(11)
print(f'Stos: {stos}')
print(f'Dlugosc: {len(stos)}')
print(f'Pop: {stos.pop()}')
print(f'Dlugosc: {len(stos)}')

stos.push(12)
print(f'Pop: {stos.pop()}')

stos.push(13)
stos.push(14)
print(f'Stos: {stos}')
print(f'Dlugosc: {len(stos)}')
print(f'Pop: {stos.pop()}')
print(f'Pop: {stos.pop()}')

print("================================")

bufor = Queue()
print(len(bufor))
bufor.enqueue(11)
print(len(bufor))
print(bufor.peek())
print(bufor.dequeue())
print(len(bufor))

print("")
bufor.enqueue(12)
print(bufor)
print(bufor.dequeue())
print(bufor)

print("")
bufor.enqueue(13)
bufor.enqueue(14)
print(bufor)
print(bufor.peek())
print(len(bufor))
print(bufor.dequeue())
print(bufor.dequeue())
print(len(bufor))