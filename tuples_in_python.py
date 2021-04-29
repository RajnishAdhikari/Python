#list and tuples are exactly same but in one condition
#in list we can add values but in tuple we cannot
#list is mutable but tuples are immutable
#tuples are always in parenthesis or small bracket()
#note that there is no single value tuple if needed
#then we need to add comma , 
t = (35,56,43.3, True)
print(type(t))
print(t[0])
print(t[0:3])
# using loop and printing one by one
for i in t:
    print(i)