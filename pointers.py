num1=11
num2=num1

print("Before num2 value is updated:")
print("num1=",num1)
print("num2=",num2)


print("\n num1 points to:",id(num1)) #id = address
print("num2 points to:",id(num2))   #both num1 and num2 are at the same location

num2=22
print("\n after num2 value is updated:")
print("num1=",num1)
print("num2=",num2)
print("\n num1 points to",id(num1))
print("\n num2 points to:",id(num2))

#11 is immutable fixed

dict1={
    'value':11
}

dict2=dict1
print("Before value is updated")
print("dict=",dict1)
print("dict2=",dict2)

print("\n dict1 points to",id(dict1))
print("dict2 points to:",id(dict2))

dict2['value']=22
print("\n After value is updated:")
print("dict=",dict1)
print("dict2=",dict2)

print("\n dict1 points to:",id(dict1))
print("dict2 points to:",id(dict2)) #same memory location to locate here
