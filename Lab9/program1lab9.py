def squareEach(nums):
    for i in range(len(nums)):
        nums[i]= nums[i]**2

def sumList(nums):
    total = 0

    for i in range(len(nums)):
        total = total+nums[i]
    return total

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = eval(strList[i])

def test():
    infile = open("numbers.txt", 'r')
    data = infile.readlines()
    toNumbers(data)
    squareEach(data)
    print("The sum of the numbers in the file is:",sumList(data))
test()
