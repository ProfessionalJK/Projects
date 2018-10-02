f=open("result.txt","rt")
count=len(f.readlines())
f.close()
f=open("result.txt","r")
grade=[]
for val in f.read().split():
    grade.append(int(val))
l=count*2-1
rollno=[]
mark=[]
a=0
while True:
    if a%2==0:
        rollno.append(int(grade[a]))
    else:
        mark.append(int(grade[a]))
    if a >= l:
        break
    a+=1
n=0
nm=len(mark)
print("Roll No.\tMarks")
for n in range(0,nm):
    rn=rollno[n]
    mr=mark[n]
    print(rn,"\t\t",mr)
i=0
r=0
for i in range(0,nm):
    c=mark[i]
    if c >= 32:
        r+=1
    i+=1
print("\nTotal no. of students      Total no.of passed students\n")
print("\t",count,"\t\t\t\t",r)
f.close()
