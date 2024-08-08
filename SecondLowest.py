if __name__ == '__main__':
   students = [ ]
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])
marklist = []
name=[]

for i  in students:
    marklist.append(i[1])
filterfirstmin = list(filter(lambda x: (x!=min(marklist)),marklist))
secondminlist = min(filterfirstmin)
for i  in students:
    if i[1]==secondminlist:
        name.append(i[0])

for i in  sorted(name):
    print(i)
