from linkedlist import Node, LinkedList
from stack import Stack

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