#===========================================================================================================================
# Array list
class BrowserHistory:
    def __init__(self, homepage: str):
        self.historyList = [homepage]
        self.currentIdx = 0

    def visit(self, url: str) -> None:
        while self.currentIdx != len(self.historyList) - 1:
            self.historyList.pop()
        self.historyList.append(url)
        self.currentIdx += 1
        return None
    
    def back(self, steps: int) -> str:
        if self.currentIdx - steps < 0:
            self.currentIdx = 0
        else:
            self.currentIdx -= steps
        return self.historyList[self.currentIdx]
    
    def forward(self, steps: int) -> str:
        if self.currentIdx + steps > len(self.historyList) - 1:
            self.currentIdx = len(self.historyList) - 1
        else :
            self.currentIdx += steps
        return self.historyList[self.currentIdx]
    
#===========================================================================================================================
# Linked List
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

#===========================================================================================================================
browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.visit("facebook.com")
browserHistory.visit("youtube.com")
browserHistory.back(1)
browserHistory.back(1)
browserHistory.forward(1)
browserHistory.visit("linkedin.com")
browserHistory.forward(2)
browserHistory.back(2)
browserHistory.back(7)