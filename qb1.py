e=[]
c=50
h=30
d=list(map(int,input().split()))
for i in d:
	q=((2*c*i)/h)**0.5
	e.append(q)
print(e)
