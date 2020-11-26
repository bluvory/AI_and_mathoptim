print(1+3)
print(5/2)
print(9%5)
print(5**2)


print(type(600))       # int
print(type(3.14))      # float
print(type("Hello"))   # string


x = 10
print(x)
x = 100  # int
print(x)
y = 3.14  # float
print(x*y)
print(type(x*y))  # float


# indexing : starting at 0
a = [1,2,3,4,5]
print(a[0])
print(a[0:3])
print(a[:3])
print(a[:-2])
print(a[2:])
print(a[:-1])

print(len(a))
a[2] = 5  # 3 -> 5
print(a)


# { 'dictionary' : value }
city = {'Seoul' : 0, 'Busan' : 1}
print(city['Seoul'])
print(city['Busan'])
city['Bucheon'] = 2
print(city)


# for loop
for k in [1,2,3,4,5]:
    print("Hello Everyone!")


# Without for loop
print("Hello Everyone!")
print("Hello Everyone!")
print("Hello Everyone!")
print("Hello Everyone!")
print("Hello Everyone!")


# the range function
for k in range(1,6):
    print(k, "squared is", k*k)

for x in range(5, 0, -1):
    print(x)
  

# summaion
sum = 0
for i in range(1, 21):
    sum = sum + (i*i)
print("sum of first 20 squares is", sum)


# while loop
sum = 0
k = 1
while k < 21:
    sum = sum + k*k
    k = k+1
print(sum)


# factorial of 20 ?
res = 1
k = 1
while k < 21:
    res = res*k
    k = k + 1
print(res)



