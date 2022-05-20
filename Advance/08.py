#Demonstrate the use of variable argument lists

#TODO: defineafunction that takes variable arguments

from re import A


def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result

def main():
    #TODO: pass different arguments    
    print(addition())
    
    #TODO: pass an existing list

if __name__ == "__main__":
    main()