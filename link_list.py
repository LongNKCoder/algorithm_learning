class Node:
    def __init__(self, **kwargs) -> None:
        self.data: int = kwargs.get("data")
        self.p_next: Node = None


class SingleList:
    def __init__(self) -> None:
        self.p_head: Node = None
        self.p_tail: Node = None

    def print_list(self) -> None:
        p_tmp = self.p_head
        if self.p_head is None:
            print("List empty")
            return
        else:
            while self.p_head is not None:
                print(self.p_head.data, end=" ")
                self.p_head = self.p_head.p_next
            self.p_head = p_tmp
        print()

    def length(self) -> int:
        number = 0
        p_tmp = self.p_head
        while self.p_head is not None:
            number += 1
            self.p_head = self.p_head.p_next
        self.p_head = p_tmp
        return number

    def insert_first(self, data: int):
        node: Node = Node(data=data)
        if self.p_head is None:
            self.p_head = node
            self.p_tail = node
        else:
            node.p_next = self.p_head
            self.p_head = node

    def insert_last(self, data: int):
        node = Node(data=data)
        if self.p_head is None:
            self.p_head = node
            self.p_tail = node
        else:
            self.p_tail.p_next = node
            self.p_tail = node

    def insert_mid(self, pos: int, data: int):
        if pos < 0 or pos > self.length() - 1:
            print("Out of index")
        elif pos == 0:
            self.insert_first(data=data)
        elif pos == self.length() - 1:
            self.insert_last(data=data)
        else:
            count = 0
            node = Node(data=data)
            p_ins = self.p_head
            p_pre = None
            while count != pos:
                count += 1
                p_pre = p_ins
                p_ins = p_ins.p_next
            node.p_next = p_ins
            p_pre.p_next = node
    
    def remove_first(self):
        p_del = self.p_head
        self.p_head = self.p_head.p_next
        p_del.p_next = None
        del p_del
    
    def remove_last(self):
        p_del = self.p_head
        while p_del.p_next != self.p_tail:
            p_del = p_del.p_next
        self.p_tail, p_del = p_del, self.p_tail
        self.p_tail.p_next = None
        del p_del

    
    def remove(self, pos: int):
        if self.p_head is None:
            print("Nothing to delete")
        count = 0
        p_del = self.p_head
        p_pre = None
        while count != pos:
            count += 1
            p_pre = p_del
            p_del = p_del.p_next
        if count == 0:
            self.remove_first()
        elif p_del.p_next is None:
            self.p_tail = p_pre
            self.p_tail.p_next = None
            del p_del
        else:
            p_pre.p_next = p_del.p_next
            p_del.p_next = None
            del p_del

    def get_first(self) -> int:
        return self.p_head.data
    
    def get_last(self) -> int:
        return self.p_tail.data
    
    def get_element(self, pos: int) -> int:
        count = 0
        tmp = self.p_head
        while count != pos:
            count += 1
            tmp = tmp.p_next
        if count == 0:
            return self.get_first()
        elif tmp is None:
            return self.get_last()
        else:
            return tmp.data
    
    def search_node(self, data: int) -> int:
        count = 0
        tmp = self.p_head
        while data != tmp.data:
            if tmp is None:
                print("Can't find")
                return
            count += 1
            tmp = tmp.p_next
        return count

    def sort(self):
        tmp = self.p_head
        while tmp is not None:
            tmp1 = tmp.p_next
            while tmp1 is not None:
                if tmp.data > tmp1.data:
                    tmp.data, tmp1.data = tmp1.data, tmp.data
                tmp1 = tmp1.p_next
            tmp = tmp.p_next
    
    def sum(self):
        tmp = self.p_head


if __name__ == "__main__":
    a = SingleList()
    a.insert_first(data=3)
    a.insert_first(data=4)
    a.insert_last(data=4)
    a.insert_last(data=5)
    a.insert_mid(0, 2)
    a.insert_mid(4, 3)
    a.insert_mid(4, 1)
    a.sort()
    a.print_list()
    # a.remove_first()
    # a.remove(5)
    # a.remove(1)
    # a.remove(2)
    # a.remove_last()
    # a.remove_last()
    # a.print_list()
    # print(a.get_element(0))
    # print(a.get_first())
    # print(a.get_last())
    # print(a.get_element(6))
    # print(a.get_element(5))
    print(a.search_node(4))
