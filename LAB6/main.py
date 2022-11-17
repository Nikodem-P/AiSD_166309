from binarytree import *

# tree = BinaryTree(10)
# a = tree.root
# a.add_left_child(9)
# a.add_right_child(2)
# a.left_child.add_left_child(1)
# a.left_child.add_right_child(3)
# a.right_child.add_left_child(4)
# a.right_child.add_right_child(6)
# tree.show()
# assert tree.root.value == 10
#
# assert tree.root.right_child.value == 2
# assert tree.root.right_child.is_leaf() is False
#
# assert tree.root.left_child.left_child.value == 1
# assert tree.root.left_child.left_child.is_leaf() is True

def main():
    tree = BinarySearchTree(8)
    tree.insert_list([3, 1, 6, 4, 7, 10, 14, 13])
    print(tree.contains(6))
    tree.show()
    tree.remove(8)
    tree.show()


if __name__ == '__main__':
    main()