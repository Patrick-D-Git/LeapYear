# A program to determine if a year is a leap year

year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")

# """ a year is a leap year if it is divisible by 4, except for years that are divisible by 100, unless they are
# also divisible by 400. This formula ensures that the Gregorian calendar remains aligned with Earth's orbit around
# the Sun as accurately as possible. """

# example: 2024 is a leap year
