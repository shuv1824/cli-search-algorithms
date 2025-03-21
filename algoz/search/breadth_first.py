from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def search(args):
    bt = BinaryTree()
    print("building the tree...")
    bt.create_from_file(args.file)
    print("tree built...")

    if args.order == "level-order":
        print("searching the tree...")
        target = args.word

        if bt.root.data == target:
            print("Word found!")
            return

        queue = Queue()
        queue.enqueue(bt.root)

        while queue.get_len():
            node = queue.dequeue()

            if node.left:
                if node.left.data == target:
                    print("Word found!")
                    return
                else:
                    queue.enqueue(node.left)

            if node.right:
                if node.right.data == target:
                    print("word found!")
                    return
                else:
                    queue.enqueue(node.right)

        print("Word not found :(")
        return

    print("breadth-first-search can only be used with --order 'level-order'")
