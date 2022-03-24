def main():
    phrase = input("Please enter in a phrase: ").split()
    print("The amount of words in the phrase is,", end=" ")
    amount = phrase
    print(len(amount))

    a=""
    char=a.join(phrase)
    print("The amount of characters in the phrase is,", len(char))
main()
