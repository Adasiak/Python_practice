import string


def palindrome(string_to_check = "kajak"):
    try:
        str2 = string_to_check[::-1]
        if str2 == string_to_check:
            print("String is palindrome")
        else:
            print("String is not palindrome")
    except:
        print("Error")

# palindrome()


def palindrome2(string_to_check = "kajak"):
    try:
        list_tmp = range(len(string_to_check)) 
        list_temp2 = []
        
        for i in range(len(string_to_check)):

            if string_to_check[i] == string_to_check[len(string_to_check) - 1 -i]:
                continue
            else:
                print("String is not palindrome")
                return "String is not palindrome"
        print("String is palindrome")
    except:
        print("Error")

stringgg = "1234321"
palindrome2(stringgg)