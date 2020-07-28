

s1={1,2,3,4,5}
s2={"a","b","c","d","d"}
s3={3,4,5,6,7}

s1.add(6)
print(s1)

s2.update(["e","f","g"])
print(s2)

print("a" in s2)
print("z" in s2)

s1.remove(6)
print(s1)


s1.discard(7)
print(s1)


x=s1.difference(s3)
print(x)

y=s3.difference(s1)
print(y)
    
s4=s1.union(s3)
print(s4)

s5=s1.intersection(s3)
print(s5)