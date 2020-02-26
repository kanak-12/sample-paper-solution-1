string=input()
substring=input()
c=0
for i in range(0,len(string)):
	if substring==string[i:i+len(substring)]:
		c=c+1
print(c)
