from tkinter import *

root=Tk()
root.title("converter")
root.geometry("500x100")

#Create labels 
label=Label(root,text="Enter the Infix Equation:").grid(row=0,column=1)
label1=Label(root,text="The Postfix Equation is:").grid(row=1,column=1)

#Entry box is created
e=Entry(root,width=40,borderwidth=4)
e1=Entry(root,width=40,borderwidth=4)

e.grid(row=0,column=2,padx=10,pady=10)
e1.grid(row=1,column=2,padx=10,pady=10)

#Infix to Postfix Calculator
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
        ans = ""  
        prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3} 
        for i in expression: 
            if i.isalpha() or i.isdigit():  
                ans += i         
            
            elif i == "(":   
                c.push(i)
            
            elif i == ')': 
                while self.stack!= 0 and self.stack[-1] != "(":
                    ans+= c.pop()
                self.pop()
     
            else: 
                while self.stack and self.stack[-1]!= '(' and prec[i] <= prec[self.top()]: 
                    ans += self.pop()                                                     
                self.push(i)                                                         
        
        while self.stack: 
            ans += str(self.pop())
        return ans
 

c = Calculator()

#Function for what to do after clicking the button
def click():
    a=c.inf_to_pref(e.get())
    ans=e1.delete(0,END)
    ans=e1.insert(0,a)

def clear():
    e.delete(0,END)
    e1.delete(0,END)

#Button is created 
button=Button(root,text="Enter",command=click)
button.grid(row="0",column="3",padx=10,pady=10)

b2=Button(root,text="Clear",command=clear)
b2.grid(row=1,column=3,padx=10,pady=10)


root.mainloop()
