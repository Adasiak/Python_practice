# s = "single"
# s[1] = "o"
# print(s)



m = [13,1,5]
n=[1,6,3,5,4]
x = [a+b for a,b in zip(m,n)]

print(x)

def test_(x,y=0,z=2):
    return x+y+z

print(bool(int(9/10)))

y = (lambda x: x*10 +5)(3)

print(y(3))