file = open('demo.txt', 'r')
for each in file:
    print (str(each.count(each))+" "+str(each))

file = open("demo.txt", "r")
print (file.read())


#a=str(input('Enter string: '))
#b=a.split()
#for i in b:
#   print(str(b.count(i))+" "+str(i))