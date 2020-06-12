def sudoku2(grid):
    # check each row
    for row in grid:
        number_set_1 = []
        for element in row:
            if element != '.':
                if element in number_set_1:
                    print("row %s has a doublicat %s" % (row, element))
                    return False
                else:
                    number_set_1.append(element)
        
    # check each column
    for column_index in range(0, 9):
        number_set_2 = []

        for row_index in range(0, 9):
            element = grid[row_index][column_index]
            if element != '.':
                if element in number_set_2:
                    return False
                else:
                    number_set_2.append(element)
    
    # check each square 
    for square_hor in range(0, 3):

        for square_ver in range(0, 3):
            number_set_3 = []
            

            for x in range(0, 3):
                row_index = x + square_hor * 3
                for y in range(0, 3):
                    column_index = y + square_ver * 3
                    element = grid[row_index][column_index]

                    if element != '.':
                        if element in number_set_3:
                            return False
                        else:
                            number_set_3.append(element)

    return True


grid=[['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]


# print(sudoku2(grid))


crypt = ["TEN", 
 "TWO", 
 "ONE"]

solution = [["O","1"], 
 ["T","0"], 
 ["W","9"], 
 ["E","5"], 
 ["N","4"]]


def isCryptSolution(crypt, solution):
    solution_dict = {}
    for x in solution:
        solution_dict[x[0]] = x[1]

    
    uncryptedList = []
    for word in crypt:
        word_num = ''
        for letter in word:
            word_num += solution_dict[letter]

        if word_num[0] == '0' and len(word_num) > 1:
            return False
        else:
            uncryptedList.append(int(word_num))
    
    if uncryptedList[0] + uncryptedList[1] == uncryptedList[2]:
        return True
    else:
        return False

        
    
    





# print(isCryptSolution(crypt, solution))

# Definition for singly-linked list:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def removeKFromList(l, k):
    fakeHead = ListNode(None)
    fakeHead.next = l
    current = fakeHead
    while current:
        while current.next and current.next.value == k:
            current.next = current.next.next
        current = current.next
    return fakeHead.next



list_x = [3, 1, 2, 3, 4, 5, 3] 
k = 3
l = ListNode(list_x)

# print(removeKFromList(l, k))


class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def lenght(self):
        cur = self.head
        total = 0
        while cur.next != None:
            
    