def tempC_Fahrenheit():

    temp = int(input("Enter temperature in Celcius: "))

    fahrenheit = temp * (1.8) + 32

    print("Temperature in Fahrenheit is: " + str(fahrenheit))

tempC_Fahrenheit()


def tempF_Celcius():

    temp = int(input("\nEnter temperature in Fahrenheit: "))

    celcius = (temp - 32) / 1.8

    print("Temperature in Celcius is: " + str(celcius))

tempF_Celcius()
