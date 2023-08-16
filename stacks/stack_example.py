#!/usr/bin/env python

from stack import Stack

stack = Stack()

stack.push("thing")
print("Last val on stack: " + stack.peek())
print("Stack size: " + str(stack.size()))

stack.push("blah")
print("Last val on stack: " + stack.peek())
print("Stack size: " + str(stack.size()))

stack.pop()
print("Last val on stack: " + stack.peek())
print("Stack size: " + str(stack.size()))
