"""
CTEC 121
<your name>
<assignment/lab name>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

""" IPO
Input(s): Family member (name)
Process: Outputs the finger family song
Output: prints to terminal screen
"""
def verse(name):
    print(name, "finger,", name, "finger, ")

def chorus():
    print("where are you? Here I am, here I am. How do you do?")

def fingerFamily(name):
    print()
    verse(name)
    chorus()   
    
def main():
    fingerFamily("Daddy")
    fingerFamily("Mommy")
    fingerFamily("Brother")
    fingerFamily("Sister")
    fingerFamily("Baby")

main()