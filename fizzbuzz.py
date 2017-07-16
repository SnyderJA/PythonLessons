
import sys

numentry1 = int(sys.argv[1])
numentry2 = int(sys.argv[2])

while numentry1 <= numentry2:
    if numentry1 % 5 == 0 and numentry2 % 3 == 0:
        print "FizzBuzz"
    elif numentry1 % 3 == 0:
        print "Fizz"
    elif numentry1 % 5 == 0:
        print "Buzz"
    else:
        print numentry1
    numentry1 += 1
