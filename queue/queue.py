from typing import Any, Optional


class QNode:
    def __init__(self, value: Any, next: Optional["QNode"] = None):
        self.value = value
        self.next: "QNode" | None = next


class Queue:
    def __len__(
        self,
    ):
        return self._length

    def __init__(self) -> None:
        self._length = 0
        self.head: QNode | None = None
        self.tail: QNode | None = None

    def enqueue(self, item: Any):
        if not self.tail:
            node = QNode(item)
            self.tail = node
            self.head = node
            self._length = 1
            return

        self.tail.next = QNode(item)
        self.tail = self.tail.next
        self._length += 1

    def peek(self):
        if self.head:
            return self.head.value

    def pop(self):
        if not self.head:
            return
        head = self.head
        if self._length == 1:
            self.head = None
            self.tail = None
            self._length = 0
            return head.value

        self.head = self.head.next
        head.next = None
        self._length -= 1
        return head.value
