marks = [20,30,40,50]

for i in range(0,len(marks)):
    print(marks[i])
#### index = -1 will start from last of the list
print("for last to end")
for i in range(len(marks)-1,-1,-1):
    print(marks[i])

print("while loop")

j = 0;
while j< len(marks):
    print(marks[j])
    j+=1;

marks.append(99)
marks.insert(0,90)
print("after append")
marks.append(99)
marks.insert(0,99)
print(marks)
print("after append")
print(len(marks))


print("##############Break Example #########")
names = ['John', 'Michael', 'Jim', 'Jenny']
for student in names:
    if student=='Jenny':
        break
    print(student);
print("##############continue Example #########")

for i in range(0,len(names)):
    if names[i]=='Jim':
        continue
    print(names[i])

