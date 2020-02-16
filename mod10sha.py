# Helper functions
def stringToASCII(string):
    newList = []
    for c in string:
        if c.isdigit():
            newList.append(c)
        else:
            string = str(ord(c))
            for n in string:
                newList.append(n)
    return newList

def addBlocks(block1, array):
    array = list(array)
    if len(array) == 0:
        return list(block1)
    block2 = array[:10]
    array = array[10:]
    block1 = createNewBlock(block1, block2)
    return addBlocks(block1, array)

def createNewBlock(block1, block2, newBlock=[], count = 0):
    if count < 10:
        sum = int(block1[count]) + int(block2[count])
        number = sum % 10
        newBlock.append(str(number))
        count += 1
        return createNewBlock(block1, block2, newBlock, count)
    return newBlock


def addTillModOfTen(array, value = -1):
    array = list(array)
    if (len(array) % 10) != 0:
        value += 1
        if value > 9: value = 0
        array.append(str(value))
        return addTillModOfTen(array, value)
    return array

# Hash function
def hash(string):
    string = string.replace(' ', '')
    array = stringToASCII(string)
    array = addTillModOfTen(array)
    firstBlock = array[:10]
    array = array[10:]
    array = addBlocks(firstBlock, array)
    array = ''.join(n for n in array)
    return(array)
