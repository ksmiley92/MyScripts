# Filename: usefulFunctions.py

# Collection of functions that can be used
# in different programs that need to utilize data collection, sorting, and printing

# Get the values to sort
def askForData(values, size):
    for i in range(size):
        values.append(float(input("Enter a number:")))
    return


# The sort function
def sortData(values, size):
    for x in range(size):
        for ctr in range(size - 1):
            if (value[ctr] > values[ctr + 1]):
                temp = values[ctr];
                values[ctr] = values[ctr + 1];
                values[ctr + 1] = temp;

def printData(values,size):
    for i in range(size):
        print(values[i])