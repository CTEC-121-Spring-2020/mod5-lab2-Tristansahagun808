"""
CTEC 121
<Tristan Sahgun>
<Lab 5>
<assignment/lab description
"""

""" IPO
Input(s): age 
Process: Print/output age classification for input age
Output: Print to terminal screen
"""
def main(age):
    try:
        if age < 2:
            return 'I'
        elif age < 13:
            return 'C'
        elif age < 18:
            return 'T'
        elif age <= 130:
            return 'A'
        else:
            return 'U'
    except:
        print("N/A")

def agetest():
    print()
    print(main(-1), "excpect U -1 input")
    print(main(1), "excpect I 1 input")
    print(main(12), "excpect C 12 input")
    print(main(17), "excpect T 17 input")
    print(main(100), "excpect A 100 input")
    print(main(250), "excpect U 250 input")

main(1)
agetest()