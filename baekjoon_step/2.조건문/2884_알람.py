date=input().split(' ')

h=int(date[0])
m=int(date[1])

if m-45<0:
    if h-1<0:
        h=23
        m=60+(m-45)
    else:
        h-=1
        m=60+(m-45)
        
else:
    m-=45
print(h,m,sep=' ')