#numerologisit
def numerologists():
    first = input("Enter your name: ")
    total = 0

    for word in first.split():
        for letter in word:
            total = total + ord(letter.lower()) - ord('a')+1
   
    print("The value of your name is:",total)




numerologists()
