import pytest
from linkedlists import LinkedList, Node


def test_new_list():
    llist = LinkedList()
    assert (llist.head is None)


def test_new_node():
    _node = Node("a")
    assert (_node is not None)
    assert (_node.data == "a")


def test_add():
    llist = LinkedList()

    _node = Node("a")
    llist.add_first(_node)
    assert (llist.head == _node)
