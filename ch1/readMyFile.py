

print("++++++++++++++++++read by character++++++++++++++++++++++");
f=open("sample.txt");
next=f.read(1)
while next !="":
	print(next)
	next = f.read(1)
print("++++++++++++++++++read by line++++++++++++++++++++++");
f=open("sample.txt");
for line in f.readlines():
	print(line.strip())

