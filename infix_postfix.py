class Calculator:
    def __init__(self):
        self.stack = []

    def isempty(self):
        return len(self.stack) == 0

    def top(self):
        return self.stack[-1] 

    def pop(self):
        if self.isempty():
            return -1
        return self.stack.pop()

    def push(self, expression):
        self.stack.append(expression)

    def inf_to_pref(self, expression):
        ans = ""  #Creates an empty string to enter operands to it as it enters
        prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3} #Sets the precedence order of the operators
        for i in expression: 
            if i.isalpha() or i.isdigit():  #If the incomming element is an alphabet or a number it enters into the empty string
                ans += i         
            
            elif i == "(":   #If the incomming element is "(" it pushes it into the stack without checking the preference 
                c.push(i)
            
            elif i == ')':  #If the incomming element is ")" it pops out all the operators until "(" is found
                while self.stack!= 0 and self.stack[-1] != "(":
                    ans+= c.pop()
                self.pop()
     
            else: 
                while self.stack and self.stack[-1]!= '(' and prec[i] <= prec[self.top()]: #Checks the precedence order of the incomming 
                    ans += self.pop()                                                      # with the top operator in the stack
                self.push(i)                                                         
        
        while self.stack: #Pops all the operator till the stack is empty
            ans += str(self.pop())
        return ans
 

c = Calculator()
a=c.inf_to_pref(input("Enter the Infix Expression: "))
print("The Postfix Expression is",a)
