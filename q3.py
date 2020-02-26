l=list(map(int,input().split()))
e=[]
for i in l:
	f=1
	while i!=0:
		f=f*i
		i=i-1
	e.append(f)
print(e)



