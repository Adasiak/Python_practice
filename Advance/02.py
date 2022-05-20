#strings and bytes are not directly interchangeable
#strings contain unicode, bytes are raw 8-bit values
def main():
    #define some starting values
    b=bytes([0x41, 0x42, 0x43, 0x44])
    print (b)
    s="This isastring"
    print(s)
    #TODO: Try combining them.
    print(b,s)
    #TODO: Bytes and strings need to be properly encoded and decoded
    s2=b.decode('utf-8')
    print(s2+s)
    #before you can work on them together
    b2 =  s.encode('utf-8')
    print(b+b2)
    #TODO: encode the string as UTF-32
    b3 = s.encode('utf-32')
    print(b3)
    

if __name__ == "__main__":
    main()