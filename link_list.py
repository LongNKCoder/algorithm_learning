class Node:
    def __init__(self, **kwargs) -> None:
        self.data: int = kwargs.get("data")
        self.p_next: Node = None


class SingleList:
    def __init__(self, **kwargs) -> None:
        self.p_head: Node = kwargs.get("node")

    def print_list(self) -> None:
        if self.p_head is None:
            print("List empty")
            return
        while self.p_head is not None:
            print(self.p_head.data, end=" ")
            self.p_head = self.p_head.p_next

    def length(self) -> int:
        number = 0
        while self.p_head is not None:
            number += 1
            self.p_head = self.p_head.p_next
        return number

    def insert_first(self, data):
        node: Node = Node(data=data)
        if self.p_head is not None:
            node = self.p_head.p_next
        self.p_head = node


if __name__ == "__main__":
    a = SingleList()
    a.insert_first(data=3)
    a.print_list()
