# stack implementaion 
class stack_implementation():

# create a constractor 
    def __init__ (self):
        self.stack =[]

#pushing value to the stack
    def push(self,value):
       return self.stack.append(value)

 # The below function is implementation of pop
 
 #  Checking whether the array is empty or not
    def is_empty(self):
       return (len(self.stack) == 0)

# To know the last element
    def top(self):
        if self.is_empty() == True:
            raise ValueError("stack is empty")
        else:
           return  self.stack[-1] # return the last element

# To remove the last element
    def pop(self): 
        top_value = self.top()
        
        removed_value = self.stack.remove(top_value)
        return removed_value

# creating object
list = stack_implementation()

#push elements to the array
list.push(10)
list.push(20)
list.push(50)

# storing the list of array in result varaible
result = list.stack

# storing the list of array that the top is removed
result2 = list.pop()

#printing the list of array
print(result)

#print the list of array that the top is removed
print(result2)


