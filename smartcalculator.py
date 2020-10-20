from tkinter import *

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def mod(a,b):
    return a % b

def lcm(a,b):
    L = a if a>b else b
    # the condition of lcm is that it should be lesser or at most equal with the products
    while L <= a*b:
        if L%a == 0 and L%b == 0:
            return L
        L+=1

def hcf(a,b):
    H = a if a<b else b
    while H >= 1:
        if a%H == 0 and b%H == 0:
            return H
        H-=1

# a function that will extract numbers from the text entered by user and move into a dict L
def extract_from_text(text):
    l = []
    # a method .split() will differentiate every entity according to the parameter entered
    for t in text.split(' '):
        # since all every thing couldn't be appended that's why we require try and except method
        try:
            # float(t) will convert evey word and number into float , as words can be changed to
            # float they will move to except , however numbers will get appended into l dict
            l.append(float(t))
        except ValueError:
            pass
    return l
# a function to calculate according to the request from user
def calculate():
    # as the user enters as StringVar() which is stored in textin , so we get everything which user entered
    text = textin.get()
    for word in text.split(' '):
        # need to convert every word of user into uppercase
        if word.upper() in operations.keys():
            try:
                l = extract_from_text(text)
                # now here's the concept we will get all words that are the keys in the dictionary but now
                # we want to execute the value of the key , which obviously is a function , and furthermore
                # we need to apply the fucntion to the two values of list which has number
                r = operations[word.upper()](l[0] , l[1])
                # eg operations['ADD'] is add function which will have parameters as 1st n 2nd element of l
                # after doing this delete the created list
                list.delete(0,END)
                # and now insert the new value into the list
                list.insert(END,r)
            except:
                list.delete(0,END)
                list.insert(END,'something went wrong please enter again')
            finally:
                break
        elif word.upper() not in operations.keys():
            list.delete(0,END)
            list.insert(END,'something went wrong please enter again')

operations = {'ADD':add , 'ADDITION':add , 'SUM':add , 'PLUS':add ,
                'SUB':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
                 'LCM':lcm , 'HCF':hcf , 'PRODUCT':mul , 'MULTIPLICATION':mul,
                 'MULTIPLY':mul , 'DIVISION':div , 'DIV':div ,'DIVIDE':div, 'MOD':mod ,
                  'REMANDER':mod , 'MODULUS':mod}

win = Tk()
win.geometry('500x300')
win.title('Smart Pugger')
win.configure(bg='lightskyblue')

l1 = Label(win , text='Your Smart Calculator is ready',width=20 , padx=3)
l1.place(x=150,y=10)
l2 = Label(win , text='Morning ya Lordship' , padx=3)
l2.place(x=180,y=40)
l3 = Label(win , text='How can i help you' , padx=3)
l3.place(x=176,y=130)

textin = StringVar()
e1 = Entry(win , width=30 , textvariable = textin)
e1.place(x=100,y=160)

b1 = Button(win , text='Just this' ,command=calculate)
b1.place(x=210,y=200)

list = Listbox(win,width=20,height=3)
list.place(x=150,y=230)

win.mainloop()
