# factorial of 20
fac = 1
for i in range(1,21):
    fac = fac*i
    i = i+1
print("20!=", fac)


# if / else
score = 50
if score < 60:
    print("Your credit is F")
else:
    print("Your credit is A+")
    
    
# do it yourself
import matplotlib.pyplot as plt
a = -2
b = 2
n = 401
dx = (b-a)/(n-1)
x_list = []
y_list = []

for i in range(0,n):
    x = a + i*dx
    y = x**5-5*x**3+4*x
    x_list.append(x)
    y_list.append(y)

plt.plot(x_list, y_list)
plt.show()


# function
def factorial(n):
    mult = 1
    for k in range(1, n+1):
        mult = mult*k
    return mult
print("20!=", factorial(20))    


# class
class class_name: 
    def __init__(self, input):
        something
    def method_1(self, input):
        something
    def method_2(self, input):
        something
 
 
# class1
class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        print("(", self.x,", ",self.y,")")

    def sqrt_magnitude(self):
        return self.x*self.x+self.y*self.y
        
    def inner_product(self, v1):
        return self.x*v1.x+self.y*v1.y

# Test
v1 = Vector2D(1,9)
sqrt_mag_v1 = v1.sqrt_magnitude()
print(sqrt_mag_v1)

v2 = Vector2D(4, 6)
v1_dot_v2 = v1.inner_product(v2)
print(v1_dot_v2)

