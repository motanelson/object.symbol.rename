def adds(n1:float,n2:float,down:float,up:float):
    n=n1+n2
    return min(up,max(n,down))


b=0
c=False
for a in range(-8,18):
    b=adds(a,10,0,10)
    print(str(b))