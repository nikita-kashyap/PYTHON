#on=a,b,c
#off
#on=e,f,g
#off
#alexa
#on:append
#off:pop
on=['a','b','c']
on.append('d')
on.pop()
on.append('e')
on.append('f')
on.append('g')
on.pop()
print(on)
x=[1,2,3]
x.append([4,5])
print(x)
x.extend([6,7])
print(x)
# insert(1,'name'): for insert on a perticular point

x=[1,2,3]
y=x.append(4)
print(y)# none because of change of address
