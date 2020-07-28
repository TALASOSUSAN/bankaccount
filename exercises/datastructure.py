print ("Hello, Dcoder!")
x=range(10)
print(x)

for y in x:
 print(y)
 
#print("-------")
a=range(2,10)
for x in a:
  print(x)
  
 #print("-----") 
x=range(10)
for y in x:
 if y%3==0:
     print(y)
          
x=range(10)
for y in x:
  if y%3!=0:
    print(y)
    
n=range(10)
for x in n:
  if  x%2==0:
    print("{} is divisible by 2".format(x))
  else:
    print("{} is not divisible by 2".format(x))

n=range(0,30)
for x in n:
  if  x%4==0:
    print("{} is divisible by 4".format(x))
  else:
    print("{} is not divisible by 4 or 3".format(x))

  