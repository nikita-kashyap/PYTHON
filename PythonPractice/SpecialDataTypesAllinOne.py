
code={
    'a':[1,2,3,4,5],#len
    'b':(6,7,8,9,10),#sec ele
    'c':[[1,2,3,4,5],[6,7,8,9,10]],#flatened
    'd':'',                    #lower of j
    'e':{'f':{'g','h','i'}}, #access ghi
    'j':'HAPPY NEW YEAR', #lower 
    'k':('l','m','n','o'),# reverse
    'p':['HAPPY','NEW','YEAR'],# comaplete as one string
    'q':{} # key value and index value(enum)
}

alen=len(code['a'])
print('length of a: ',alen)

secEle=tuple(code.values())[1]
print('second element of b: ',secEle)

flatened=[f for i in code['c'] for f in i]
print('flatened value of c is:  ',flatened)

lowerOfJinD=(code['d']+code['j'].lower())
print('Lower value of j in d:   ',lowerOfJinD)

accessGHI=(code['e']['f'])
print('print g,h,i of e:    ',accessGHI)

reverseOf_k=list(code.values())[6]
list_=list(reverseOf_k)
list_.reverse()
print('reversed value of k: ',list_)

singleString=(code['p'][0]+code['p'][1]+code['p'][2])
print('converted in single String:  ',singleString)

enum_=(enumerate(flatened))
res=list(enum_)
print('the enumeration is:  ',res)

# a=[[1,2],[2,3],[5,6]]
# b=[[1,3],[2,6],[8,10],[15,16]]#OUTPUT=[1,6],[8,10][15,16]