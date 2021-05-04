'''for 1 value we use one key
duplicate value is allowed in dict 
but duplicate key is not allowed'''
d ={1:"ram",2:"hari"}
print(d)
for i in d:
    print(i)


#calling key for the respective value
print(d[2])

#adding and removing elements in dict
di={}
di["a"] = 'ram'
di["b"] = 'hari'
di["c"] = 'shyam'
print(di)
di.pop("a")
print(di)