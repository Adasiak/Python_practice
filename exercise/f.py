import os
def clearConsole():
    command = 'clear'
    os.system(command)

def findNext(string_of_number):
    number =  list(map(int, string_of_number))
    length_of_string = len(string_of_number)

    for i in range(length_of_string-1 ,0,-1):
        if number[i] > number[i-1]:
            break

    if i ==1 and number[i] <= number[i-1]:
        print("Next numbern not posible")
        return
    
    x = number[i-1]
    smallest = i
    for j in range(i+1,length_of_string):
        if number[j] > x and number[j] < number[smallest]:
            smallest = j
    
    number[smallest],number[i-1] = number[i-1],number[smallest]

    x = 0

    for j in range(i):
        x = x * 10 + number[j]

    number = sorted(number[i:])

    for j in range(length_of_string-i):
        x = x * 10 + number[j]

    print("Next number is : ",x)

def main():
    clearConsole()
    n = str(input('Enter value: '))
    findNext(n)

if __name__ == '__main__':
    main()