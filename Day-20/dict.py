''''
d={'sugar':40,'salt':20,'cookingoil':80,'chilli':60}
r=dict(map(lambda i: (i[0],i[1]+i[1]*0.18),d.items()))
r1=dict(map(lambda i: (i[0],i[1]-i[1]*0.5),d.items()))
print(r)
print(r1)
'''

d={'sugar':40,'salt':20,'cookingoil':80,'chilli':60}
r=dict(filter(lambda i:i[1]>50,d.items()))
r1=dict(filter(lambda i:i[1]<50,d.items()))
print(r,r1)

