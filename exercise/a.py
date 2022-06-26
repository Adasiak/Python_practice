import os

from math import factorial
def clearConsole():
    command ="clear"
    os.system(command)

def fun1(n):
    for i in range(1,n+1):
        # for j in range(1,i+1):
        count = str(i)+str(" ") 
        print(count * i)
        # print("\n")

def fun2(n):
    for x in range(n):
        for y in range(n-x+1):
            print( end="   " )

        for y in range(x+1):
            temm = factorial(y) * factorial(x-y)
            temp = factorial(x)//temm 
            print(str("  ")+str(temp) , end="   " )
        print()

def abbccc(num):
    number = 65
    for i in range(0,num):
        for j in range(0,i+1):
            char = chr(number)
            print(char, end=" ")
        number += 1
        print("\r")

def abcd(num):
    number = 65
    for i in range(0,num):
        for j in range(0,i+1):
            char = chr(number+j)
            print(char, end=" ")
        print("\r")

def abcdef(num):
    number = 65
    for i in range(0,num):
        for j in range(0,i+1):
            char = chr(number)
            print(char, end=" ")
            number += 1
        print("\r")

def updatedic():
    d1 = {"k1":10, "k2":20, "k3":30}
    list_of_keys = []
    for i in d1.keys():
        list_of_keys.append(i)
    print(list_of_keys)
    for i in d1.keys():
        d1[i] += 10
    print(d1) 

def rand(n):
    import random
    n = random.randint(0,n)
    while True:
        try:
            l = int(input("Enter your number: "))
        except:
            print("Please enter a valid number")
        if l == n:
            break
        else:
            print("Try again \n")

def arraray(*args, **kwargs):
    print(args)
    print(kwargs)

def shalowcopy():
    first = [1,2,3,4,5,6,7,8,9]
    second = first
    second.append(10)
    print(first)
    print(second)

def som():
    first = [1,2,3,4,5,6,7]
    print(first[-1:-4:-1])

def asci():
    value = input("Enter value")
    print("The asci value of '" + value + "is", ord(value))

def suffff():
    from random import shuffle
    values =  ["Mama",'City','State','Country']
    shuffle(values)
    print(values)

def floor():
    print(5//2)
    print(-7//2)
    print(7.0//2)
    print(-8.0//2)

def check_pass(arr):
    arr.append(4)

def somm():
    arr = [1,2,3]
    print(arr)
    check_pass(arr)
    print(arr)
    print("Hello Python"[::-1])

def qq():
    listll = [1,2,3,4,5,6,7,8]
    mmm = listll*2
    print(listll*2)
    print(mmm)

def armstrong(n):
    sum = 0
    temp = n 
    while temp>0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if n == sum :
        print(n,"is the strongest ")
    else:
        print(n,"is not  the strongest ")

def perfect_number(n):
    sum = 0
    for i in range(1, n):
        if n % i==0:
            sum += i
    print(sum)
    if n == sum:
        print(n," is perfect number ")
    else:
        print(n," is not perfect number ")

def strong_number(n):
    sum = 0
    temp = n 
    while n:
        i = 1
        fact = 1
        rem =  n % 10
        while i <= rem :
            fact *=i
            i+=1
        sum += fact
        n=n//10
    if sum == temp:
        print("Is strong number ")
    else:
        print(" is Not strong number ")

def seclar(n):
    import random
    list_of_numbers = []
    for i in range(n):
        list_of_numbers.append(random.randint(0,100))
    
    list_of_numbers.sort()
    print(list_of_numbers)
    print("secend largest number is",list_of_numbers[-2])

def swap(n):
    import random
    list_of_numbers = []
    for i in range(n):
        list_of_numbers.append(random.randint(0,100))
    
    list_of_numbers.sort()
    temp1 = list_of_numbers[0]
    temp2 = list_of_numbers[-1]
    list_of_numbers[0] = temp2
    list_of_numbers[-1] = temp1
    print(list_of_numbers)

def volves():
    inputstring = "bsxiuqbxkjnxjkNJKBXHJABCXHABCJKcjkancjkanbJKN"
    lis_of_Valves = ["A","a","e","E","O","o",'I','i','U','u']

    list_of_comon = []
    for i in inputstring:
        if i in lis_of_Valves:
            list_of_comon.append(i)
    print(list_of_comon)

def break_a_list(n):
    import random
    list_of_numbers = []
    for i in range(n):
        list_of_numbers.append(random.randint(0,100))

    count_of_braek = 7
    out = [list_of_numbers[i:i+count_of_braek] for i in range(0,len(list_of_numbers),count_of_braek)]
    print(out)

def main():
    clearConsole()
    try:
        n = int(input("enter your numbert to patern: "))
    except:
        print("Please enter a valid number")
    fun1(n)
    fun2(n)
    abbccc(n)
    abcd(n)
    abcdef(n)
    updatedic()
    rand(n)
    arraray(1,"Hello",name="Python")
    shalowcopy()
    som()
    asci()
    suffff()
    floor()
    somm()
    qq() 
    armstrong(n)
    perfect_number(n)
    strong_number(n)
    seclar(n)
    swap(n)
    volves()
    break_a_list(n)

if __name__ == "__main__":
    main()
