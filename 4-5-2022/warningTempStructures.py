def main():
    celsius = eval(input("Please enter the temperature in celsius: "))
    fahrenheit = (9/5) * celsius + 32

    if fahrenheit > 90:
        print("It is too hot outisde!")
    elif fahrenheit < 30:
        print("It is too cold outside!")
    else:
        print("The weather is comfortable")
main()
