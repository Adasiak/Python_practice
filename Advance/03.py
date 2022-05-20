#demonstrate template string functions
def main():
    #Usual string formatting with format()
    str1= "You' re watching {0} by {1}".format("Advanced Python", "JoeMarini")
    
    print(str1)

    #TODO: createatemplate with placeholders
    templ =  Template("You' re watching {0} by {1}".format("Advanced Python")
    #TODO: use the substitute method with keyword arguments

    #TODO: use the substitute method withadictionary


if __name__ == "__main__":
  main()