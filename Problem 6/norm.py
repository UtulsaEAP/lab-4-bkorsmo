"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Brady Korsmo
Lab Time: Thursday @2
"""

def norm():
    # Write your code here
    integers = float(input())
    numbers = []
    place = integers
    x=0

    while (integers >0 ):
        value = float(input())
        integers = integers-1
        numbers.append(value)

    print(numbers)
    maxvalue = max(numbers)
    while (place >0):
        number = numbers[x]
        number = number/maxvalue
        place += -1
        print((f'{number:.2f}'))
        x = x+1


if __name__ == "__main__":
    norm()