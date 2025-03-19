from data_structures.binary_tree import BinaryTree


def search(args):
    bt = BinaryTree()
    print("building the tree...")
    bt.create_from_file(args.file)
    print("tree built...")

    if args.order == "pre-order":
        print("searching the tree...")
