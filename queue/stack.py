from typing import Any


class SNode:
    def __init__(self, value: Any, next: "SNode" | None = None) -> None:
        self.value = value
        self.next: "SNode" | None = next


class Stack:
    def __init__(self) -> None:
        self.length = 0
        self.head: SNode | None = None

    def __len__(self):
        return self.length

    def peek(self):
        if self.head:
            return self.head.value

    def push(self, item):
        if not self.head:
            self.length = 1
            self.head = SNode(item)
            return
        self.length += 1
        self.head = SNode(item, self.head)

    def pop(self):
        if not self.head:
            return
        head = self.head
        self.length -= 1
        self.head = self.head.next
        head.next = None
        return head.value
