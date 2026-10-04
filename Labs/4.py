s1="America"
s2="Japan"
l=len(s1)
l2=len(s2)
mi=int(len(s1)/2)
mi2=int(len(s2)/2)

#res=s1[0]+s1[mi]+s1[l-1]+s2[0]+s2[mi2]+s2[l2-1]

res=s1[0]+s2[0]+s1[mi]+s2[mi2]+s1[l-1]+s2[l2-1]
print(res)