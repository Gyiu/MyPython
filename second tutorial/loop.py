# while expression:
#   statement(s)
count = 0
while(count < 9):
    print "number : ", count
    count = count + 1

num = 1
while(num < 5):
    print "number 2 : ", num
    num = num + 1
else:
    print "special number 2: ", num

# for iterating_var in sequence:
#   statement(s)

for new in "DONY":
    print new


for num in range(10,2000000):
    for i in range(2, num):
        if num%i == 0:
            print "%d is not prime." % (num)
            break;
    else:
        print num, " is prime."