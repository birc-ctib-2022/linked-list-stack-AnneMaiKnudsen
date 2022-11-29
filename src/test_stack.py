"""Testing our stack implementation."""

import pytest
from stack import EmptyStack,Stack

def test_push()->None:
    stack1=Stack()
    stack1.push(1)
    assert stack1.is_empty()==False


def test_top() -> None:
    stack1 = Stack()
    stack1.push(1)
    assert stack1.top()==1


def test_pop() -> None:
    stack1 = Stack()
    stack1.push(1)
    stack1.pop()
    assert stack1.is_empty()==True

def test_exception() -> None:
    stack1 = Stack()
    with pytest.raises(EmptyStack):
        stack1.pop()
        stack1.top()





