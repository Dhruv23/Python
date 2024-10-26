import math
import numpy as np
import scipy as sp
e = np.exp(1)

def nCk(n, k):
    nFact = math.factorial(n)
    kFact = math.factorial(k)
    nMk = n - k
    nMkFact = math.factorial(nMk)
    output = (nFact / (kFact * nMkFact))
    return output

def binomial():
    while True:
        try:
            n = int(input("What is n: "))
            break
        except:
            print("Error, please enter a number\n")
            
    while True:
        try:
            p = float(input("What is p: "))
            break
        except:
            print("Error, please enter a number\n")
    q = 1-p
    Ex = n*p
    Varx = Ex * q
    sd = math.sqrt(Varx)
    print(f"Expected Vaue = {Ex}\nVariance = {Varx}\nStandard Deviation = {sd} \n")
    choice = input("Less than or greater than a value? (L/G/LE/GE/E): ")
    if(choice == "LE"):
        while True:
            try:
                value = int(input("Less than/equal to what value?: "))
                break
            except:
                print("Please enter a value \n")
        i = 0
        total = 0
        while(i <= value):
            total += (nCk(n, i) * (pow(p,i)) *(pow(q, (n-i))))
            i+=1
        print(total)
    elif(choice == "GE"):
        while True:
            try:
                value = int(input("Greater than/equal to what value?: "))
                break
            except:
                print("Please enter a value \n")
        i = value
        total = 0
        while(i <= n):
            total += (nCk(n, i) * (pow(p,i)) *(pow(q, (n-i))))
            i+=1
        print(total)
    elif(choice == "L"):
        while True:
            try:
                value = int(input("Less than what value?: "))
                break
            except:
                print("Please enter a value \n")
        i = 0
        total = 0
        while(i <= value):
            total += (nCk(n, i) * (pow(p,i)) *(pow(q, (n-i))))
            i+=1
        print(total)
    elif(choice == "G"):
        while True:
            try:
                value = int(input("Greater than to what value?: "))
                break
            except:
                print("Please enter a value \n")
        i = value+1
        total = 0
        while(i <= n):
            total += (nCk(n, i) * (pow(p,i)) *(pow(q, (n-i))))
            i+=1
        print(total)
    elif(choice == "E"):
        while True:
            try:
                value = int(input("Equal to what value?: "))
                break
            except:
                print("Please enter a value \n")
        total = (nCk(n, value) * (pow(p,value)) *(pow(q, (n-value))))
        print(total)
    else:
        print("Invalid Input, try again \n")

def poisson():
    while True:
        try:
            r = float(input("What is r: "))
            break
        except:
            print("Please enter a number \n")

    while True:
        try:
            s = float(input("What is s: "))
            break
        except:
            print("Please enter a number \n")
    lambdaP = r*s
    Ex = lambdaP
    Varx = lambdaP
    sd = math.sqrt(Varx)
    print(f"Expected Vaue = {Ex}\nVariance = {Varx}\nStandard Deviation = {sd} \n")
    def OnePoisson(lambdaP, val):
        output = ((pow(e, (0-lambdaP)) * pow(lambdaP, val))/(math.factorial(val)))
        return output
    choice = input("Less than or greater than a value? (L/G/LE/GE/E): ")
    if(choice == "LE"):
        while True:
            try:
                value = int(input("Less than/equal to what value?: "))
                break
            except:
                print("Please enter a number \n")
        i = 0
        total = 0
        while(i<=value):
            total +=OnePoisson(lambdaP, i)
            i+=1
        print(total)
    elif(choice == "GE"):
        while True:
            try:
                value = int(input("Greater than/equal to what value?: "))
                break
            except:
                print("Please enter a number \n")
        value -=1
        i = 0
        total = 0
        while(i<=value):
            total +=OnePoisson(lambdaP, i)
            i+=1
        print(1 - total)
    elif(choice == "L"):
        while True:
            try:
                value = int(input("Less than what value?: "))
                break
            except:
                print("Please enter a number \n")
        i = 0
        total = 0
        while(i<value):
            total +=OnePoisson(lambdaP, i)
            i+=1
        print(total)
    elif(choice == "G"):
        while True:
            try:
                value = int(input("Greater than what value?: "))
                break
            except:
                print("Please enter a number \n")
        i = 0
        total = 0
        while(i<=value):
            total +=OnePoisson(lambdaP, i)
            i+=1
        print(1-total)
    elif(choice == "E"):
        while True:
            try:
                value = int(input("Equal to what value?: "))
                break
            except:
                print("Please enter a number \n")
        i = 0
        le1 = 0
        while(i<=value):
            le1 +=OnePoisson(lambdaP, i)
            i+=1
        i = 0
        le2 = 0
        while(i<=(value-1)):
            le2 +=OnePoisson(lambdaP, i)
            i+=1
        print(le1 - le2)
    else:
        print("Invalid Input \n")
        
def gemometric():
    while True:
        try:
            p = float(input("what is your p value: "))
            break
        except:
            print("Please enter a number")
    
    
    q = 1-p
    Ex = 1/p
    Varx = q/(pow(p,2))
    sd = math.sqrt(Varx)
    print(f"Expected Vaue = {Ex}\nVariance = {Varx}\nStandard Deviation = {sd} \n")

    choice = input("Less than or greater than a value? (L/G/LE/GE/E): ")
    if(choice == "LE"):
        while True:
            try:
                value = int(input("Less than/equal to what value?: "))
                break
            except:
                print("Please enter a number")
        
        total = 1 - pow(q, value)
        print(total)

    elif(choice == "GE"):
        while True:
            try:
                value = int(input("Greater than/equal to what value?: "))
                break
            except:
                print("Please enter a number")
        print(pow(q, (value-1)))

    elif(choice == "L"):
        while True:
            try:
                value = int(input("Less than what value?: "))
                break
            except:
                print("Please enter a number")
        x = pow(q, (value-1))
        print(1-x)
        
    elif(choice == "G"):
        while True:
            try:
                value = int(input("Greater than what value?: "))
                break
            except:
                print("Please enter a number")
        print(pow(q, value))
       
    elif(choice == "E"):
        while True:
            try:
                value = int(input("Equal to what value?: "))
                break
            except:
                print("Please enter a number")
        n = value-1
        print((p*(pow(q, n))))
    else:
        print("Invalid Input \n")


# To add support for continuous functions, add scipy.integrate
# Docs at https://docs.scipy.org/doc/scipy/tutorial/integrate.html 



    


def switch():

    distribution = int(input("What Distribution would you like to use\n1: Binomial\n2: Poisson\n3: Geometric\nPick the number associated with your choice: "))

    if(distribution == 1):
        binomial()
    elif (distribution == 2): 
        poisson()
    elif (distribution ==3):
        gemometric()
    else:
        print("Invalid Choice, exiting \n")

switch()