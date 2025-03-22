from data_structures.binary_tree import BinaryTree


def binary_search(target, root):
    pass


def search(args):
    bst = BinaryTree()

    print("building tree...")
    bst.create_bst_from_file(args.file)
    print("tree built...")

    print("searching tree...")
    target = args.word

    if binary_search(target, bst.root):
        print("word found!")
        return
    else:
        print("word not found :(")
