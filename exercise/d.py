import os 
def clearConsole():
    command = 'clear'
    os.system(command)

def fun1():   
    s1 = {1,2,3,7,4,5,6}
    s2={5,6,7,8,9}
    print(s1.intersection(s2))
    print()

def palindrome(n): 
    temp = n
    rev = 0 

    while n>0: 
        digit = n%10
        rev = rev * 10 + digit
        n = n//10
    if temp == rev: 
        print("this is a palindrome")
    else:
        print("this is not a palindrome")
    print()

def patern1(n): 
    for i in range(1,n+1):
        number_to_print = str(i)+" "
        print(number_to_print * i) 
    print()

def patern_hash(n): 
    for i in range(1,n+1):
        number_to_print = "#"+" "
        print(number_to_print * i) 
    print()
    
def patern2(n): 
    outpot_str = ""
    for i in range(n):
        outpot_str = outpot_str + str(i)+" "
        print(outpot_str ) 
    print()

def patern_pascal(n): 
    from math import factorial
    
    for i in range(n):
        for j in range(n-i+1):
            print(end="   ")
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end="    ")
        print()
    print()
 
def patern_abb(n):
    number = 65
    for i in range(n):
        number_to_print = chr(number+i-1)+" "
        print(number_to_print * i) 
    print()

def patern_abcd(n):
    number = 65
    for i in range(0,n):
        for j in range(0,i+1):
            number_to_print = chr(number)
            print(number_to_print, end=" ") 
            number += 1
        print("\r")
    print()

def dicchange():
    d1 = {"k1": 10,"k2":20 ,"k3":30,"k4":40}
    for i in d1.keys():
        d1[i] = d1[i]+1
    print(d1.values())
    print()

def print_rrandom(n):
    import random
    print(random.randint(0,n))
    print()

def main():
    clearConsole()
    fun1()
    while True:
        try:
            n = int(input("enter n: "))
            break
        except:
            print("its not a number")
    # palindrome(n)
    patern1(n)
    patern_hash(n)
    patern2(n)
    patern_pascal(n)
    patern_abb(n)
    patern_abcd(n)
    dicchange()
    print_rrandom(n)

if __name__ == '__main__':
    main()
