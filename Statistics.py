def evenorodd(number):
    myevenorodd = number %2
    if myevenorodd == 0:
        return "even"
    else:
        return "odd"

def round(number):
    myround = number % 1
    if myround >= .5:
        print("The value of myround is: ",myround)
        return 1-myround
    else:
        return -1*(myround)

def mean(number):
    mynumber = number.split()
    mynumber = map(int,mynumber)
    icount = 0
    sum = 0
    for i in mynumber:
        icount = icount + 1
        sum = sum + i
    return sum/icount

def median(number):
    icount = 0
    mynumber = number.split()
    mynumber = map(int,mynumber)
    mynumber = sorted(mynumber)
    for i in mynumber:
        icount = icount + 1
    myvalue = icount/2
    myvalue = myvalue + round(myvalue)
    myvalue = int(myvalue)
    eoro = evenorodd(icount)
    print("sorted myinput: ",mynumber)
#    print("mynumber[myvalue]: ",mynumber[myvalue])
#    print("mynumber[myvalue-1]: ",mynumber[myvalue-1])
    if eoro=="even":
        return (mynumber[myvalue] + mynumber[myvalue-1])/2
    if eoro=="odd":
        return mynumber[myvalue-1]



#myinput = input("Enter your number, separated by a space\n: ")
myinput = '10 2 1 0 5 33 9 100 31'
print("myinput: ",myinput)
mymean = mean(myinput)
print ("Mean: ", mymean)
mymedian = median(myinput)
print ("Median: ", mymedian)
