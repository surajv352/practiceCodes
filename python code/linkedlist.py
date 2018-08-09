class Node:

   def __init__(self,data,nextNode=None):
       self.data = data
       self.nextNode = nextNode

   def getData(self):
       return self.data

   def setData(self,val):
       self.data = val

   def getNextNode(self):
       return self.nextNode

   def setNextNode(self,val):
       self.nextNode = val

class LinkedList:

   def __init__(self,head = None):
       self.head = head
       self.size = 0

   def getSize(self):
       return self.size

   def addNode(self,data):
       newNode = Node(data,self.head)
       self.head = newNode
       self.size+=1
       return True

   def delNode(self,data):
       if self.head is None:
        return
       self.size -= 1
       currentNode = self.head
       previousNode = None
       while currentNode.data != data:
        previousNode = currentNode
        currentNode = currentNode.nextNode
       if previousNode is None:
        self.head = currentNode.nextNode
       else:
        previousNode.nextNode = currentNode.nextNode

   def printNode(self):
       curr = self.head
       while curr:
           print(curr.data)
           curr = curr.getNextNode()

myList = LinkedList()
print("Inserting.....")
myList.addNode(10)
myList.addNode(15)
myList.addNode(25)
print("Printing......")
myList.printNode()
print("-"*10)
myList.delNode(25)
myList.printNode()
print("Size")
print(myList.getSize())