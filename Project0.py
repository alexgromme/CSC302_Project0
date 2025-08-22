
## NO ADDITIONAL IMPORT STATEMENTS ALLOWED
from testing_21 import test,test_file_content,test_LOM,testNoPrint,test_NoReturn
import sys
import random


#=============================================================================
# q1 - create function quarter() to meet the conditions below
#    - accept one parameter: a string corresponding to the name of a month
#    - determine the quarter of the year within which the month falls
#       --- Example 1: for March -> returns 1
#       --- Example 2: for June -> returns 2
#       --- Example 3: for October -> returns 4
#    - return the quarter # (1, 2, 3, or 4)
#    The quarters are:
#    --- quarter 1: January - March
#    --- quarter 2: April - June
#    --- quarter 3: July - September
#    --- quarter 4: October - December
#
#    - RESTRICTIONS:  None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:  string
#    - return:  integer
#=============================================================================




#==========================================================================
# q2 - create function sumOfSquares() to meet the conditions below
#    - accept one parameter: an integer
#    - calculate the sum of all the squares of integers from 1 up to
#      and including the parameter
#        --- Example 1: 5 -> returns 55, i.e (1+4+9+16+25)
#        --- Example 2: 10 -> returns 385, i.e. (1+4+9+16+25+36+49+64+81+100)
#    - return the sum
#
#    - RESTRICTIONS:  You may NOT use the built-in sum function
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:  integer
#    - return: integer
#==========================================================================




#==========================================================================
# q3 - create function sumEven() to meet the conditions below
#    - accept two integer values, p1 and p2, as parameters
#    - return the sum of all even numbers between p1 and p2 inclusive.
#    - Assume the first parameter is always smaller or equal to the
#       second parameter
#       --- Example 1: 4 and 10 -> returns 28 (4+6+8+10)
#       --- Example 2: 10 and 10 -> returns 10
#       --- Example 3: 11 and 11 -> returns 0
#       --- Example 4: 11 and 13 -> returns 12
#    - return the sum of even numbers
#
#    - RESTRICTIONS: you are NOT allowed to use the built-in sum() function
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#
#    - param:  integer
#              integer
#    - return: integer
#==========================================================================




#==========================================================================
# q4 - create function addValue() to meet the conditions below
#    - accept two parameters: a list of numbers and a number
#    
#    - iterate over the list and add the 2nd parameter value to each
#    - value in the list.
#
#    - you MUST change the values within the list and NOT create a new list
#
#       --- Example: [-5.4379, 7.0643, -41.87, 174.53, -4220] and 33.3 ->
#                     [27.8621, 40.3643, -8.57, 207.83, -4186.7]
#
#    - RESTRICTIONS:  None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:  list (of numbers)
#              float
#    - return: None
#==========================================================================





#==========================================================================
# q5 - create function fullNames() to meet the conditions below
#    - accept two parameters:  a list of first names and a corresponding
#                              list of last names
#    
#    - iterate over the lists and combine the names (in order) to form   
#      full names (with a space between the first and last names);
#      add them to a new list, and return the new list
#       --- Example: first list = ["Sam", "Malachi", "Jim"]
#             second list = ["Poteet", "Strand"]
#
#             returns ["Sam Poteet", "Sam Strand",
#                      "Malachi Poteet", "Malachi Strand",
#                      "Jim Poteet", "Jim Strand"]
#
#    - return the list of full names
#
#    - RESTRICTIONS:  None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - params:  list (of strings)
#               list (of strings)
#    - return:  list (of strings)
#==========================================================================




#=============================================================================
# q6 - create function countLowerCase() to meet the conditions below
#    - accept a string as a parameter
#    
#    - iterate over the string and counts the number of lower case letters
#    - that are in the string
#    - returns the number of lower case letters
#       --- Example 1: 
#           string = "A seCRet YoU DidN'T kNOw."
#           return 9
#       --- Example 2: 
#           string = "sEaRcHiNg for A ConNEcTIOn."
#           return 12
#
#    - RESTRICTIONS:  You may NOT use the following string functions:
#                      upper(), lower(), isupper(), or islower()
#
#    - HINT: Letters can be compared. Any letter between "a" and "z" is a
#            lowercase letter
#
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - params:  string
#    - return:  integer
#=============================================================================




#=============================================================================
# q7 - create function readNLines() to meet the conditions below
#    - accept two parameters:  a file name and a number corresponding
#                              to the number of lines to be read
#    
#    - read the first N lines from the file and concatenate them into a
#      single string;
#    - return the string
#      NOTE:
#           --- the file is automatically generated when this exam file
#                is run and it is placed in the same directory as this
#                exam file
#           --- strip the newline characters from every line before
#               concatenating
#           --- put a space between each line you concatenate
#           --- don't forget to close the file
#           --- you may assume N is less or equal to the number of lines in the textfile
#
#    - RESTRICTIONS:  None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - params:  string
#               integer
#    - return:  string
#=============================================================================

def readNLines(fileName, N):
    """
    Reads N lines from the input file and writes them in one string, with the lines
    separated by a space.

    Args:
        fileName (string): The name/path of the to be read file.
        N (int): number of lines read.

    Returns:
        output (string): The formated string with the corresponding lines (and no space at the end).
    """
    output = ""
    with open(fileName, "r") as file:
        for i in range(N):
            line = file.readline()
            line = line.strip()
            output += line + " "
    return output.strip()


#=============================================================================
# q8 - create function writeEvenNumbers() to meet the conditions below
#    - accept two parameters:  a file name,
#                              and an integer value
#    
#    - open the named file for writing
#    - write to the file all the even numbers between 2 and the
#        integer value, both included.
#        Each number should be on a separate line in the file.
#      --- don't forget to close the file
#    - return the number of lines written to the file
#
#    - RESTRICTIONS:  you may NOT use the built-in function len()
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - params:  string
#               integer
#    - return:  integer
#=============================================================================

def writeEvenNumbers(fileName, value):
    """
    Writes even numbers line by line in the file until the value.

    Args:
        fileName (string): The name/path of the to be edited file.
        value (int): maximum value for the even number.

    Returns:
        count (int): The number of lines and changes the input file.
    """
    count = 0
    with open(fileName, "w") as file:
        for i in range(value+1):
            if (i%2 == 0) and (i >=2) :
                file.write(str(i) + "\n") 
                count += 1
    return count



#==========================================================================
# q9 - create function triangle() to meet the conditions below
#    - accept one parameter: an integer
#    
#    - print a triangle using asterisks, as shown below.
#    - you can assume the parameter is greater than 0.
#
#       --- Example 1:  3 is passed to the function it prints to the console:           
#           *
#           **
#           ***
#       --- Example 2: 4 is passed to the function it prints to the console:          
#           *
#           **
#           ***
#           ****
#
#
#    - RESTRICTIONS:  None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:   integer
#    - return:  None
#==========================================================================
def triangle(size: int) -> None:
    """
    Print a right-angled triangle made of asterisks.

    Args:
        size (int): The height of the triangle (number of rows).

    Returns:
        None: This function only prints the triangle and does not return a value.
    """
    tri = ""
    for i in range(size):          
        for j in range(i + 1):       
            tri += "*"
        tri += "\n"                
    print(tri)

#=============================================================================
# q10 - DEBUG function find
#    - This function currently returns INCORRECT answers
#    - Find and fix the error(s) in the function below
#
#    - the program accepts 2 parameters:
#      --- strList - a list of strings
#      --- c  - a single character
#
#    - it must iterate over the strings in the list strList and
#      count the total number of occurrences of c in the strings
#    - and return the count
#    - you may assume all of the characters, in strList and c, are lowercase
#
#       --- Example 1:
#           strList = ['apple', 'banana', 'cherry']
#           c = 'e'
#           return 2 since there are two occurrences of 'e' in the list
#
#       --- Example 2:
#           strList = ['apple', 'banana', 'cherry', 'asparagus']
#           c = 'a'
#           return 7 since there are seven occurrences of 'a' in the list
#
#    - RESTRICTIONS:  do NOT re-write the function, just find/fix error(s)
#
#    - params:  list (of strings)
#               string (a single character)
#    - return:  integer
#=============================================================================
def find(strList, c):
    '''accept a list of strings, and a character c;
       count the number of occurrences of c in strList;
       return the count'''
    count = 0
    for word in strList:
        for char in word:
            if char == c:
                count += 1
    return count

#The problem was that the parameters strList is instantly overwritten by the function
#Therefore the for-loop iterates over an empty array
#Additionally, the function (if the list weren't overwritten) searched for every element in the list whether or not this element is
#in the list (e.g. if the character would be 'b' and the list [apple, apple, apple] the result would be 3 even if you'd excpet 0)


#==========================================================================
# *************************************************************************
# ******************* DO NOT EDIT CODE BELOW THIS POINT *******************
# *************************************************************************
#==========================================================================
def printErr():
    print(" ",sys.exc_info()[0].__name__,"-line",sys.exc_info()[-1].tb_lineno)
    print(" ",sys.exc_info()[1])
    
#q1==========================================================================   
def test_letterGrade():
    print("\n\t\t**** (10 points) - letterGrade() ****")
    passed = 0
    attempted = 0
    values = [(85,'B'),(40,'F'),(90,'A'),(79,'C'),(60,'D')]
    random.shuffle(values)
    for i in range(5):        
        attempted += 1
        if test(values[i][1], letterGrade, values[i][0]):
            passed += 1
    return passed, attempted

#q1 =========================================================================
def test_quarter():
    print("\n\n\t*******(10 points) - quarter********")
    monthList = [(1,'January'), (1,'February'), (1,'March'), (2,'April'),
                 (2,'May'), (2,'June'), (3,'July'), (3,'August'),
                 (3,'September'), (4,'October'), (4,'November'), (4,'December')]

    passed = 0
    attempted = 0

    for i in range(5):
        attempted += 1
        idx = random.randint(0,11)
        if test(monthList[idx][0], quarter, monthList[idx][1]):
            passed += 1

    return passed, attempted

#q1==========================================================================
def test_positiveIntDiff():
    print("\n\t\t**** (10 points) - positiveIntDiff() ****")
    passed = 0
    attempted = 0
    values = [(-7,12,19),(13,9,4),(-2,-5,3),(-1,1,2), (10,10,0), (-10,10,20)]
    random.shuffle(values)
    for i in range(6):
        attempted += 1
        if test(values[i][2], positiveIntDiff, values[i][0], values[i][1]):
            passed += 1
    return passed, attempted


#q2==========================================================================
def test_sumOfSquares():
    print("\n\t\t**** (10 points) - sumOfSquares() ****")
    passed = 0
    attempted = 0
    values = [(20,2870),(2,5),(5,55),(4,30), (10,385), (0,0)]
    random.shuffle(values)
    for i in range(6):        
        attempted += 1
        if test(values[i][1], sumOfSquares, values[i][0]):          
            passed += 1
    return passed, attempted


#q2 =========================================================================
def test_total():
    print("\n\n*******(10 points) - total ********")

    passed = 0
    attempted = 0

    for i in range(5):
        nums1 = list(range(random.randint(1,5), random.randint(5,10)))
        nums2 = list(range(random.randint(20,22), random.randint(22,25)))
        nums = nums1 + nums2
        attempted += 1
##    if test(106, total, (1,3,4,5,66,7,8,9,3)): passed += 1
        if test(sum(nums), total, tuple(nums)): passed += 1
    nums = ()
    attempted += 1
    if test(0, total, nums): passed += 1
    return passed, attempted

#q2==========================================================================
def test_mult_of_5():
    print("\n\t\t**** (10 points) - mult_of_5() ****")
    passed = 0
    attempted = 0
    values = ((21,[0, 5, 10, 15, 20]),(20,[0, 5, 10, 15]),(25,[0,5,10,15,20]),
              (10,[0,5]),(5,[0]),(0,[]))
    for i in range(6):
        attempted += 1
        if test(values[i][1], mult_of_5, values[i][0]):
            passed += 1
    return passed, attempted

#q2==========================================================================
def test_numCount():
    print("\n\t\t**** (10 points) - numCount() ****")
    passed = 0
    attempted = 0
    nums = [20,2,5,4,54,24,24,25,2,5,10,10,2]
    values = ((nums,2,3),(nums,20,1),(nums,100,0),(nums,24,2),(nums,5,2))
    for i in range(5):
        attempted += 1
        if test(values[i][2], numCount, values[i][0], values[i][1]):            
            passed += 1
    return passed, attempted

#q3==========================================================================
def test_divisibleByTwoInts():
    import string
    print("\n\t\t**** (10 points) - divisibleByTwoInts() ****")
    passed = 0
    attempted = 0
    values = ((3,7,[21, 42, 63, 84]),(50,150,[]),(2,11,[22,44,66,88]),(31,11,[]),(20,4,[20, 40, 60, 80, 100]))
    for i in range(5):
        attempted += 1
        if test(values[i][2], divisibleByTwoInts, values[i][0], values[i][1]):
            passed += 1
    return passed, attempted
           
#q3==========================================================================
def test_sumEven():
    import string
    print("\n\t\t**** (10 points) - sumEven() ****")
    passed = 0
    attempted = 0
    values = [(0,3,2),(4,14,54),(3,15,54),(12,15,26),(12,12,12), (13,13,0)]
    random.shuffle(values)
    for i in range(6):        
        attempted += 1
        if test(values[i][2], sumEven, values[i][0], values[i][1]):            
            passed += 1
    return passed, attempted  


#q3 =========================================================================
def test_numSpaces():
    results = []
    # Note that the strings must also be put inside of single quotes
    # so that the "test" function will print the test case with the
    # double quotes.  But then we need to escape the apostrophes.
    sampleSentences = [
                    ("We have all seen movies", 4),
                    ("with traumatic break ins that filled us with horror. ", 9),
                    ("there is the worst nightmare of many. Fortunately, unlike movies, ", 10),
                    (" It\'s  still pretty terrifying, though, to wake up in ", 11),
                    (" the middle of the  night and realize someone else is in your ", 14),
                    ("house—and one can\'t exactly read a burglar\'s mind or know his or ", 12),
                    ("her intentions. Here\'s a pretty good overview if you ", 9),
                    ("", 0),
                    (" ", 1),
                    ("", 0),
                    (" ", 1)
                    ]

    print("\n\t\t**** (10 points) - numSpaces() ****")
    passed = 0
    attempted = 0

    for i in range(5):
        attempted += 1
        sentence = random.choice(sampleSentences)
        if test(sentence[1], numSpaces, sentence[0]):
            passed += 1
    return passed, attempted




#q4==========================================================================
def test_squareValues():
    print("\n\t\t**** (10 points) - squareValues() ****")
    passed = 0
    attempted = 0

    nums = [i for i in range(100)]
    squares = [i*i for i in range(100)]

    for i in range(5):
        nums1 = []
        nums2 = []
        for j in range(10):
            k = random.randint(0, 99)
            nums1.append(nums[k])
            nums2.append(squares[k])
        attempted += 1
        if test_NoReturn(nums2, squareValues, nums1): passed += 1

    return passed, attempted

#q4 =========================================================================
def test_convertToInts():
    print("\n\t\t**** (10 points) - convertToInts() ****")
    passed = 0
    attempted = 0

    nums = [i for i in range(100)]
    strings = [str(i) for i in range(100)]

    for i in range(5):
        nums1 = []
        nums2 = []
        for j in range(10):
            k = random.randint(0, 99)
            nums1.append(nums[k])
            nums2.append(strings[k])
        attempted += 1
        if test_NoReturn(nums1, convertToInts, nums2): passed += 1

    return passed, attempted

#q4==========================================================================
def test_listAbs():
    print("\n\t\t**** (10 points) - listAbs() ****")
    passed = 0
    attempted = 0

    nums = [(random.random() * 1000 - 500) for i in range(100)]
    pos = []
    for i in nums:
        pos.append(abs(i))

    for i in range(5):
        nums1 = []
        nums2 = []
        for j in range(10):
            k = random.randint(0, 99)
            nums2.append(nums[k])
            nums1.append(pos[k])
        attempted += 1
        
        if test_NoReturn(nums1, listAbs, nums2): passed += 1

    return passed, attempted

#q4==========================================================================
def test_addValue():
    print("\n\t\t**** (10 points) - addValue() ****")
    passed = 0
    attempted = 0

    nums = [(random.random() * 1000 - 500) for i in range(100)]
    pos = []
    for i in nums:
        pos.append(abs(i))

    for i in range(5):
        nums1 = []
        value = random.random() * 1000 - 500
        nums2 = []
        for j in range(10):
            k = random.randint(0, 99)
            nums2.append(nums[k])
            nums1.append(nums[k] + value)
        attempted += 1
        
        if test_NoReturn(nums1, addValue, nums2, value): passed += 1

    return passed, attempted

#q5==========================================================================
def test_createPlates():
    print("\n\t\t**** (10 points) - createPlates() ****")
    passed = 0
    attempted = 0

    Lo3L = [['EHU', 'OPB', 'OXW', 'TEK', 'THU'],
            ['LKW', 'SAJ', 'UMA', 'VBO', 'XED', 'XSH', 'ZIA', 'ZOY'],
            ["RUB", "VOP", "IYE"],
            ["OUH", "KXJ", "GPZ", "PQE"],
            ["UTR", "NJH", "WKT", "MOJ", "TBH"]]
    Lo4D = [[2074, 2246, 3530, 5789, 7356, 8974],
            [5789, 2246, 2074, 8974, 3530, 7356],
            [1681, 4547, 7115],
            [1407, 8225, 1262, 8899, 2336],
            [2565, 9050, 5609]]
    VLo7LD = [['EHU-2074', 'EHU-2246', 'EHU-3530', 'EHU-5789', 'EHU-7356', 'EHU-8974',
              'OPB-2074', 'OPB-2246', 'OPB-3530', 'OPB-5789', 'OPB-7356', 'OPB-8974',
              'OXW-2074', 'OXW-2246', 'OXW-3530', 'OXW-5789', 'OXW-7356', 'OXW-8974',
              'TEK-2074', 'TEK-2246', 'TEK-3530', 'TEK-5789', 'TEK-7356', 'TEK-8974',
              'THU-2074', 'THU-2246', 'THU-3530', 'THU-5789', 'THU-7356', 'THU-8974'],
              ['LKW-5789', 'LKW-2246', 'LKW-2074', 'LKW-8974', 'LKW-3530', 'LKW-7356',
               'SAJ-5789', 'SAJ-2246', 'SAJ-2074', 'SAJ-8974', 'SAJ-3530', 'SAJ-7356',
               'UMA-5789', 'UMA-2246', 'UMA-2074', 'UMA-8974', 'UMA-3530', 'UMA-7356',
               'VBO-5789', 'VBO-2246', 'VBO-2074', 'VBO-8974', 'VBO-3530', 'VBO-7356',
               'XED-5789', 'XED-2246', 'XED-2074', 'XED-8974', 'XED-3530', 'XED-7356',
               'XSH-5789', 'XSH-2246', 'XSH-2074', 'XSH-8974', 'XSH-3530', 'XSH-7356',
               'ZIA-5789', 'ZIA-2246', 'ZIA-2074', 'ZIA-8974', 'ZIA-3530', 'ZIA-7356',
               'ZOY-5789', 'ZOY-2246', 'ZOY-2074', 'ZOY-8974', 'ZOY-3530', 'ZOY-7356'],
              ['RUB-1681', 'RUB-4547', 'RUB-7115',
               'VOP-1681', 'VOP-4547', 'VOP-7115',
               'IYE-1681', 'IYE-4547', 'IYE-7115'],
              ['OUH-1407', 'OUH-8225', 'OUH-1262', 'OUH-8899', 'OUH-2336',
               'KXJ-1407', 'KXJ-8225', 'KXJ-1262', 'KXJ-8899', 'KXJ-2336',
               'GPZ-1407', 'GPZ-8225', 'GPZ-1262', 'GPZ-8899', 'GPZ-2336',
               'PQE-1407', 'PQE-8225', 'PQE-1262', 'PQE-8899', 'PQE-2336'],
              ['UTR-2565', 'UTR-9050', 'UTR-5609',
               'NJH-2565', 'NJH-9050', 'NJH-5609',
               'WKT-2565', 'WKT-9050', 'WKT-5609',
               'MOJ-2565', 'MOJ-9050', 'MOJ-5609',
               'TBH-2565', 'TBH-9050', 'TBH-5609']]

    for i in range(len(Lo3L)):
        attempted += 1
        if test(VLo7LD[i], createPlates, Lo3L[i], Lo4D[i]): passed += 1

    return passed, attempted
        
#q5==========================================================================
def test_commonItem():
    print("\n\t\t**** (10 points) - commonItem() ****")
    passed = 0
    attempted = 0

    lst1 = [2,5,4,7]
    lst2 = [1,2,1,4]  
    attempted += 1
    if test(True, commonItem, lst1, lst2):
        passed += 1

    lst1 = ['a','b','c','a']
    lst2 = ['g','a','c'] 
    attempted += 1
    if test(True, commonItem, lst1, lst2):
        passed += 1
    
    lst1 = ['sara', 'peter', 'alex', 'tom']
    lst2 = ['smith', 'brown', 'jones']    
    attempted += 1
    if test(False, commonItem, lst1, lst2):
        passed += 1

    return passed, attempted

#q5==========================================================================
def test_fullNames():
    print("\n\t\t**** (10 points) - fullNames() ****")
    passed = 0
    attempted = 0

    firstNames = [['William', 'Whitney', 'Urmilla', 'Theresa'],
                  ['Stephanie', 'Stacy', 'Nicolas', 'Morgan', 'Deirdre'],
                  ['Mandy', 'Meredith', 'Amy', 'Hillary'],
                  ['Kristen', 'Mallory', 'Michelle'],
                  ['Julia', 'Courtney', 'Cierra', 'Caitlin', 'Alyssa']]
    lastNames = [['Brown', 'Justice', 'Nuckles', 'Pearce', 'Wilcox'],
                 ['Queen', 'Shepard'],
                 ['Haygood', 'Dominguez', 'Castillo', 'Blanchard'],
                 ['Foster', 'Edwards'],
                 ['Crider', 'Bello', 'Skelton', 'White', 'Wilson']]

    results = [['William Brown','William Justice','William Nuckles','William Pearce','William Wilcox',
                'Whitney Brown','Whitney Justice','Whitney Nuckles','Whitney Pearce','Whitney Wilcox',
                'Urmilla Brown','Urmilla Justice','Urmilla Nuckles','Urmilla Pearce','Urmilla Wilcox',
                'Theresa Brown','Theresa Justice','Theresa Nuckles','Theresa Pearce','Theresa Wilcox'],
               ['Stephanie Queen','Stephanie Shepard',
                'Stacy Queen','Stacy Shepard',
                'Nicolas Queen','Nicolas Shepard',
                'Morgan Queen','Morgan Shepard',
                'Deirdre Queen','Deirdre Shepard',],
               ['Mandy Haygood','Mandy Dominguez','Mandy Castillo','Mandy Blanchard',
                'Meredith Haygood','Meredith Dominguez','Meredith Castillo','Meredith Blanchard',
                'Amy Haygood','Amy Dominguez','Amy Castillo','Amy Blanchard',
                'Hillary Haygood','Hillary Dominguez','Hillary Castillo','Hillary Blanchard'],
               ['Kristen Foster','Kristen Edwards',
                'Mallory Foster','Mallory Edwards',
                'Michelle Foster','Michelle Edwards'],
               ['Julia Crider','Julia Bello','Julia Skelton','Julia White','Julia Wilson',
                'Courtney Crider','Courtney Bello','Courtney Skelton','Courtney White','Courtney Wilson',
                'Cierra Crider','Cierra Bello','Cierra Skelton','Cierra White','Cierra Wilson',
                'Caitlin Crider','Caitlin Bello','Caitlin Skelton','Caitlin White','Caitlin Wilson',
                'Alyssa Crider','Alyssa Bello','Alyssa Skelton','Alyssa White','Alyssa Wilson']]
    for i in range(len(firstNames)):
        attempted += 1
        if test(results[i], fullNames, firstNames[i], lastNames[i]): passed += 1

    return passed, attempted

#q6==========================================================================
def test_createWord():
    results = []
    print("\n\t\t**** (10 points) - createWord() ****")    
    passed = 0
    attempted = 0

    values = [(['case', 'odor', 'orphan', 'local'], 'cool'),
              (['red','are','tuba'], 'rat'),
              (['quarter', 'up', 'issue', 'carrot', 'knit'],'quick'),
              (['highway', 'ocra', 'momentum', 'equator'], 'home'),
              (['giraffe', 'raccoon', 'egret', 'aardvark', 'tiger'], 'great'),
              (['rest', 'early', 'weary', 'am', 'renew', 'dawn'], 'reward'),
              (['many', 'opera', 'november', 'tooth', 'hiccup'], 'month'),
              (['saddle', 'tissue', 'aparatus', 'tank', 'uniform', 'echo'], 'statue'),
              (['sadden', 'tease', 'afterwards', 'title', 'illinios', 'or', 'no'], 'station')]
    random.shuffle(values)

    for i in range(5):
        attempted += 1
        if test(values[i][1], createWord, values[i][0]):            
            passed += 1
    
    return passed, attempted    


#q6==========================================================================
def test_countUpperCase():
    print("\n\t\t**** (10 points) - countUpperCase() ****")
    passed = 0
    attempted = 0

    values = [["WiLL yOu sTilL hAve TO eNlArgE tHe PaRTITion?",18],
              ["ReDDiT uSErs fOUNd The pAREnt’S behAvIOR tO Be TrouBling.",22],
              ["To PUT tHIs TroublE BEHIND them ...", 14],
              ["they rElEasEd two NEW pORTraiTs To marK thEIr tEnth wEddIng aNNiveRsary.", 20],
              ["Her Husband oPTEd fOr A blUE shIrt", 10],
              ["She HAS GOT sUch PoIsE aNd eLeGAncE!", 16],
              ["Only A cERtAIn peRCenTAge HAd to BE sENiorS.", 17],
              ["The REnt WAs sIGNifICAntly cHEapER COmpaREd to wHEre I hAD moVED frOM.", 29],
              ["I sTARTed mEEting SoMe Of mY neIGhbORs.", 15]
             ]
    random.shuffle(values)
    for i in range(5):        
        attempted += 1
        if test(values[i][1], countUpperCase, values[i][0]):            
            passed += 1
    return passed, attempted


#q6==========================================================================
def test_countLowerCase():
    print("\n\t\t**** (10 points) - countUpperCase() ****")
    passed = 0
    attempted = 0

    values = [["WiLL yOu sTilL hAve TO eNlArgE tHe PaRTITion?",19],
              ["ReDDiT uSErs fOUNd The pAREnt’S behAvIOR tO Be TrouBling.",25],
              ["To PUT tHIs TroublE BEHIND them ...", 12],
              ["they rElEasEd two NEW pORTraiTs To marK thEIr tEnth wEddIng aNNiveRsary.", 41],
              ["Her Husband oPTEd fOr A blUE shIrt", 18],
              ["She HAS GOT sUch PoIsE aNd eLeGAncE!", 13],
              ["Only A cERtAIn peRCenTAge HAd to BE sENiorS.", 19],
              ["The REnt WAs sIGNifICAntly cHEapER COmpaREd to wHEre I hAD moVED frOM.", 29],
              ["I sTARTed mEEting SoMe Of mY neIGhbORs.", 17]
             ]
    random.shuffle(values)
    for i in range(5):        
        attempted += 1
        if test(values[i][1], countLowerCase, values[i][0]):            
            passed += 1
    return passed, attempted


#q6==========================================================================
def test_countVowels():
    print("\n\t\t**** (10 points) - countVowels() ****")
    passed = 0
    attempted = 0

    values = [["WiLL yOu sTilL hAve TO eNlArgE tHe PaRTITion?",15],
              ["ReDDiT uSErs fOUNd The pAREnt’S behAvIOR tO Be TrouBling.",18],
              ["To PUT tHIs TroublE BEHIND them ...", 9],
              ["they rElEasEd two NEW pORTraiTs To marK thEIr tEnth wEddIng aNNiveRsary.", 21],
              ["Her Husband oPTEd fOr A blUE shIrt", 10],
              ["She HAS GOT sUch PoIsE aNd eLeGAncE!", 12],
              ["Only A cERtAIn peRCenTAge HAd to BE sENiorS.", 15],
              ["The REnt WAs sIGNifICAntly cHEapER COmpaREd to wHEre I hAD moVED frOM.", 21],
              ["I sTARTed mEEting SoMe Of mY neIGhbORs.", 12]
             ]
    random.shuffle(values)
    for i in range(5):        
        attempted += 1
        if test(values[i][1], countVowels, values[i][0]):            
            passed += 1
    return passed, attempted



#q7==========================================================================
def test_readIt():
    results = []
    print("\n\t\t**** (10 points) - readIt() ****")    
    passed = 0
    attempted = 0
    
    # random float from 1 to 99.9
    list_Size = 10
    lst = random.sample(range(1, 100), list_Size)    
    total = sum(lst)
    output_file = open("sample_input1.txt",'w')
    ms = ""
    ml = []
    for i in range(len(lst)):
        output_file.write(str(lst[i])+"\n")
    output_file.close()
    attempted += 1
    if test(total,readIt,"sample_input1.txt"):            
        passed += 1
        
    list_Size = 5
    lst = random.sample(range(1, 100), list_Size) 
    total = sum(lst)
    output_file = open("sample_input2.txt",'w')
    ms = ""
    ml = []
    for i in range(len(lst)):
        output_file.write(str(lst[i])+"\n")
    output_file.close()     
    attempted += 1
    if test(total,readIt,"sample_input2.txt"):            
        passed += 1

    lst = []
    total = sum(lst)
    random.shuffle(lst)
    output_file = open("sample_input3.txt",'w')
    ms = ""
    ml = []
    for i in range(len(lst)):
        output_file.write(str(lst[i])+"\n")
    output_file.close()     
    attempted += 1
    if test(total,readIt,"sample_input3.txt"):            
        passed += 1

    return passed, attempted


#q7==========================================================================
def test_openAndReturnAverage():
    results = []
    print("\n\t\t**** (10 points) - openAndReturnAverage() ****")    
    passed = 0
    attempted = 0
    
    list_Size = 10
    lst = random.sample(range(1, 100), list_Size) 
    total = sum(lst)/len(lst)
    random.shuffle(lst)
    output_file = open("sample_input1.txt",'w')
    ms = ""
    ml = []
    for i in range(len(lst)):
        output_file.write(str(lst[i])+"\n")
    output_file.close()
    attempted += 1
    if test(total,openAndReturnAverage,"sample_input1.txt"):            
        passed += 1
        
    list_Size = 5
    lst = random.sample(range(1, 100), list_Size)  
    total = sum(lst)/len(lst)
    random.shuffle(lst)
    output_file = open("sample_input2.txt",'w')
    ms = ""
    ml = []
    for i in range(len(lst)):
        output_file.write(str(lst[i])+"\n")
    output_file.close()     
    attempted += 1
    if test(total,openAndReturnAverage,"sample_input2.txt"):            
        passed += 1

    return passed, attempted



##q7 ======================================================================
def test_readNLines():
    print("\n\t\t**** (10 points) - readNLines() ****")
    passed = 0
    attempted = 0

##    attempted += 1
##    if test(None, readNLines, "nofile.txt",10): passed += 1
    
    cars = ["Small Cars", "Mid-Size Cars", "Large Cars", "SUVs", "Trucks",
     "Wagons", "Luxury", "Sports Cars", "Convertibles", "Vans"]
    random.shuffle(cars)
    f = open("testfile.txt", "w")
    for i in cars:
        f.write(i+'\n')
    f.close()
    result = ' '.join(cars[0:4])
    attempted += 1
    if test(result, readNLines, 'testfile.txt',4) or \
         testNoPrint(" " + result, readNLines, 'testfile.txt',4) or \
         testNoPrint(result + " ", readNLines, 'testfile.txt', 4):
        passed += 1
    
    f = open("testfile.txt", "w")
    f.write("apple\napple\nfruit\nfruit\ncarrot\ncarrot\n")
    f.close()
    result = "apple apple"    
    attempted += 1
    if test(result, readNLines, 'testfile.txt',2) or \
         testNoPrint(" " + result, readNLines, 'testfile.txt',2) or \
         testNoPrint(result + " ", readNLines, 'testfile.txt', 2):
        passed += 1   
    
    attempted += 1
    if test("", readNLines, "testfile.txt",0) or \
       testNoPrint(" ", readNLines, "testfile.txt",0):
        passed += 1
    
    return passed, attempted
           
#q8 =========================================================================
def test_writeTwice():
    results = []
    print("\n\t\t**** (10 points) - writeTwice() ****")

    attempted = 0
    passed = 0

    icr = 2
    start = 2
    values = [(['bananas', 'plums', 'watermelon', 'nectarines'],8,9),
              (['oranges','strawberries','melons'],6,7),
              (['grapefruit', 'mandarins', 'apricots', 'peaches', 'rockmelons'],10,11),
              (['grapefruit', 'mandarins'],4,5),
              (['apricots', 'peaches', 'rockmelons'],6,7),
              (['limes'],2,3),
              ([],0,1)]
    random.shuffle(values)
    count = 0
    for n in range(0,3):
        attempted += 1
        filename = "sample_output"+str(n+1)+'.txt'
        returnVal = writeTwice(filename, values[n][0])
        try:
            infile = open(filename, 'r')
        except:
            print("The output file hasn't be created correctly")
        finalList = []
        for i in values[n][0]:
            finalList.append(i)
            finalList.append(i)
        studentList = []
        for i in infile:
            studentList.append(i.strip())
        if studentList == finalList and (returnVal == values[n][1] or returnVal == values[n][2]):
            passed += 1
        infile.close()
    return passed, attempted

#q8 =========================================================================
def test_writeEvenNumbers():
    results = []
    print("\n\t\t**** (10 points) - writeAFileEvenNumbers() ****")

    attempted = 0
    passed = 0

    icr = 2
    start = 2

    list_Size = 3
    lst = random.sample(range(1, 100), list_Size)  
    random.shuffle(lst)


    for n in range(0,list_Size):
        attempted += 1
        filename = "sample_output"+str(n+1)+'.txt'
        returnVal = writeEvenNumbers(filename, lst[n])
        try:
            infile = open(filename, 'r')
        except:
            print("The output file hasn't be created correctly")
        finalList = list(range(2,lst[n]+1,2))
        studentList = []
        for i in infile:
            studentList.append(int(i.strip()))
        
        if studentList == finalList and (returnVal == lst[n]//2 or returnVal == (lst[n]//2)+1):
            passed += 1
        infile.close()

    return passed, attempted




#q8 =========================================================================
def test_writeMinMaxSumCount():
    results = []
    print("\n\t\t**** (10 points) - writeMinMaxSumCount() ****")

    attempted = 0
    passed = 0

    list_Size = 10
    for n in range(0,3):
        lst = random.sample(range(1, 100), list_Size)  
        random.shuffle(lst)
        
        attempted += 1
        filename = "sample_output"+str(n+1)+'.txt'
        returnVal = writeMinMaxSumCount(filename, lst)
        try:
            infile = open(filename, 'r')
        except:
            print("The output file hasn't be created correctly")
        finalList = [min(lst), max(lst), sum(lst), len(lst)]
        studentList = []
        for i in infile:
            studentList.append(int(i.strip()))
        
        if studentList == finalList and returnVal is None:
            passed += 1
        infile.close()
    

    return passed, attempted

#q9=========================================================================
def test_countPairs():
    print("\n\n*******(5 points) - countPairs ********")
    attempted = 0
    passed = 0
    values = [([2,5,8],8,0),
              ([2,3,4,5
                ],7,4),
              ([1,2,4],6,2),
              ([],4,0),
              ([1,5,2,8,0,4],6,4),
              ([1,5,2,11,42,8,0,4],12,4),
              ([1,-5,-3,-4,8,-2,4],4,2)]
    random.shuffle(values)
    for i in range(4):        
        attempted += 1
        if test(values[i][2], countPairs, values[i][0], values[i][1]):            
            passed += 1
    return passed, attempted

#q9 =========================================================================
def test_dupWords():
    print("\n\n*******(5 points) - dupWords ********")
    attempted = 0
    passed = 0
    wt = [[('yes','no','no','hi','bye','hi','hi'), ['hi','no']],
          [('smar', 'smar', 'gorp', 'ibex', 'doup', 'ibex', 'coif', 'smar',
          'coif', 'gorp', 'coif', 'doup'), ['coif', 'doup', 'gorp', 'ibex', 'smar']],
          [('bananas', 'plums', 'watermelon', 'nectarines','plums', 'watermelon'), ['plums', 'watermelon']],
          [("Small Cars", "Mid-Size Cars", "Large Cars", "Mid-Size Cars"), ['Mid-Size Cars']]]

    random.shuffle(wt)
    for i in range(3):    
        attempted += 1
        if test_LOM(wt[i][1], dupWords, wt[i][0]): 
            passed += 1
    return passed, attempted
#q9==========================================================================   
def test_triangle():
    results = []
    print("\n\t\t**** (10 points) - triangle() ****")
    
    passed = 0
    attempted = 0
    row = random.randint(2,9)
    triangle(row)
    row = random.randint(2,9)
    triangle(row)
    return passed, attempted 
        
#q10==========================================================================   

def test_changeValues():
    results = []
    print("\n\t\t**** (5 points) - changeValues() ****")
    passed = 0
    attempted = 0
    values = [([1,2,4,5],[3, 1.0, 12, 2.5]),
              ([2,25,15,3],[6, 12.5, 45, 1.5]),
              ([3,5,3],[9, 2.5, 9]),
              ([3],[9]),
              ([],[])]
    for i in range(len(values)):
        attempted += 1
        # changeValues(values[i][0])
        # print("Testing changeValues({})".format(values[i][0]))
        # if values[i][1]==values[i][0]:
            # passed += 1
        if test_NoReturn(values[i][1], changeValues, values[i][0]):
            passed += 1


    return passed, attempted    

#q10 =========================================================================
def test_numOdds():
    print("\n\n*******(5 points) - numOdds ********")
    attempted = 0
    passed = 0
    attempted += 1
    if test(4, numOdds, [1,3,3,1]): passed += 1
    attempted += 1
    if test(0, numOdds, []): passed += 1
    attempted += 1
    if test(2, numOdds, [-1,-2,-2,-2,-2,-2,-2,1]): passed += 1
    return passed, attempted

#q10 =========================================================================
def test_find():
    print("\n\n*******(5 points) - find ********")
    strList = ['apple', 'banana', 'cherry', 'orange', 'watermelon']
    chars = [['a', 6], ['b', 1], ['c',1], ['e', 5], ['n', 4], ['r', 4]]

    random.shuffle(chars)
    attempted = 0
    passed = 0
    for i in range(3):
        attempted += 1
        if test(chars[i][1], find, strList, chars[i][0]): passed += 1
    return passed, attempted

        
# Main =======================================================================
def main():

    testFunctionList = [test_quarter, test_sumOfSquares, test_sumEven, test_addValue, test_fullNames,
                        test_countLowerCase, test_readNLines, test_writeEvenNumbers, test_triangle, test_find]
        
    functionNames = ['quarter', 'sumOfSquares', 'sumEven', 'addValue', 'fullNames',
                     'countLowerCase', 'readNLines', 'writeEvenNumbers', 'triangle', 'find']

    points = [-1 for i in range(len(testFunctionList))]
    totals = [0 for i in range(len(testFunctionList))]

    for i in range(len(testFunctionList)):
        try:
            points[i], totals[i] = testFunctionList[i]()
                
        except:
            print("**Something is wrong with " + functionNames[i] + "()")
            printErr()
            points[i], totals[i] = -1, 0

    print("\n\n")
    print("Summary of the Test Results")
    print("======================================")

    for i in range(len(testFunctionList)):
        #print(format('q'+str(i+1),'<4'), format(functionNames[i], "27s"), end="")
        print(format('q'+str(i+1),'<4'), format(functionNames[i], "27s"), end="")
        if points[i] >= 0:
            print("%2d out of %2d" % (points[i], totals[i]))            
            if points[i] == totals[i] and points[i] in [0,1]:
                print("{}: Instructor will check the output manually".format(functionNames[i]))
        else:
            print("Not defined or error in function")
#fail =========================================================================
def countFailed(points, totals):
    count = 0
    for i in range(len(points)):
        count += points[i] != totals[i]
    return count
#call =========================================================================
if __name__ == "__main__":
    main()


