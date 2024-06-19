class Node(object) :
    def __init__(self, prev=None, val=0, next=None) :
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = Node(val=homepage)
        self.current = Node(val=homepage)
    def visit(self, url: str) -> None:
        new_node = Node(val=url, prev=self.current)
        self.current.next = new_node
        self.current = self.current.next
    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev != None :
            steps -= 1
            self.current = self.current.prev
        return self.current.val
    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next != None :
            steps -= 1
            self.current = self.current.next 
        return self.current.val
