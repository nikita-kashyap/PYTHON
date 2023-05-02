# file = open("ipsum.txt", "rt")
# data = file.read()
# words = data.split()

# print('Number of words in text file :', len(words))



# word = input("enter word, you want to search : ")

# wc=0

# with open('ipsum.txt','r') as file:
#     for line in file:       #to read through ech line
#         words = line.split()    # each word split into list of words
#         for i in words:     # traverse the list
#             if(i==word):
#                 wc=wc+1

# print('Number of repeatation of the word is : ',wc)

a=str(input('enter string:'))
b=a.split()
for i in b:
    print(str(b.count(i))+" "+str(i))