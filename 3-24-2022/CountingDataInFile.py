def wc():
    fname= input('Enter the file name: ')
    infile = open(fname, 'r')
    data = infile.read()

    print('The number of characters:', len(data))
    print('The number of words:', len(data.split()))
    print('The number of lines is:', len(data.split("\n")))

wc()
        
