import random
from typing import List, Tuple
from player import Player, PlayerStackRun


def olisort_challenge() -> Tuple[bool, str, str]:
    """
    Challenge: sort a list of random integers.

    Steps:
      1. Generate a random list of 10 ints between 0 and 100.
      2. Call Player.olisort to get the player's sorted list.
      3. Compute the expected sorted list using Python's sorted().
      4. Compare and return (passed, expected_str, actual_str).
    """
    # 1) generate input
    data: List[int] = [random.randint(0, 100) for _ in range(10)]

    # 2) get player's result via stub
    # We assume Player.olisort is implemented in player.py
    player = Player((0, 0), 0, 0)  # dummy position and bounds
    player_result: List[int] = player.olisort(data)

    # 3) expected result
    expected: List[int] = sorted(data)

    # 4) compare and return
    passed: bool = player_result == expected
    return passed, str(expected), str(player_result)

class node:
    def __init__ (self, Val):
        self.Val = Val
        self.next = None

    def Next(self):
        return self.next

class Stack:
    def __init__ (self):
        self.head = None
    
    def pop(self):
        if self.head != None:
            temp = self.head
            self.head = self.head.next
            return temp.Val
        else:
            return "There is nothing in the stack." 
    
    def push(self, Value):
        Value = node(Value)

        if self.head == None:
            self.head = Value
        else:
            Value.next = self.head
            self.head = Value
    
    def getLength(self):
        length = 0
        Temp = self.head
        while Temp != None:
            length += 1
            Temp = Temp.next
        return length
    
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def peek(self):
        if self.head == None:
            return None
        else:
            return self.head.Val

def RunThroughAStack():
    Script = ""
    AwnserStack = Stack()
    Awnser = 0
    for x in range(random.randint(1,9)):
        Choice = random.randint(1, 5)
        Num = random.randint(1, 20)
        if Choice >= 1 and Choice <= 4:
            Script += "Push "
            Script += str(Num)
            Script += "\n"
            AwnserStack.push(Num)
        else:
            Script += "Pop\n"
            AwnserStack.pop()
    for n in range(AwnserStack.getLength()):
        temp = AwnserStack.pop()
        Awnser += temp
    Script += "Print"
    Player_Result = PlayerStackRun(Script)
    return Player_Result == Awnser, Awnser, Player_Result
