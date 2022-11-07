from tree import *

f = TreeNode('F', [])
b = TreeNode('B', [])
g = TreeNode('G', [])
a = TreeNode('A', [])
d = TreeNode('D', [])
c = TreeNode('C', [])
e = TreeNode('E', [])
i = TreeNode('I', [])
h = TreeNode('H', [])

i.add(h)
g.add(i)
f.add(g)
d.add(c)
d.add(e)
b.add(a)
b.add(d)
f.add(b)

tree = Tree(f)
tree.show()
