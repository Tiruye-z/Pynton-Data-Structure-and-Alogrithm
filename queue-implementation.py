# queue implementaion 
class queue_implementation():

# create a constractor 
    def __init__ (self):
        self.stack =[]

#adding value to the stack
    def enqueue(self,value):
       return self.stack.append(value)

 
 #  Checking whether the array is empty or not
    def is_empty(self):
       return (len(self.stack) == 0)

# To know the first element
    def peek(self):
        if self.is_empty() == True:
            raise ValueError("stack is empty")
        else:
           return  self.stack[0] # return the first element

# To remove the first element
    def dequeue(self): 
        first_element = self.peek()
        
        removed_value = self.stack.remove(first_element)
        return first_element

# creating object
list = queue_implementation()

#adding elements to the array
list.enqueue(10)
list.enqueue(20)
list.enqueue(50)

# storing the list of array in "result" varaible
result = list.stack

list.dequeue()

#printing the list of array
print(result)

#print the list of array that the first is removed
# print(result2)

list.enqueue(100)
list.enqueue(200)
list.enqueue(300)
print(list.stack)

print(list.stack[4])





