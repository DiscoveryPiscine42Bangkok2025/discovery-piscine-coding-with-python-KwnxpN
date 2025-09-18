from checkmate import checkmate

def main():
    # Test Case 1 (from PDF example)
    board1 = """\
R...
.K..
..P.
....\
"""
    print("Test 1:")
    checkmate(board1)
    
    # Test Case 2 (from PDF example)
    board2 = """\
..
.K\
"""
    print("Test 2:")
    checkmate(board2)
    
    # Test Case 3: Queen attack
    board3 = """\
Q...
....
....
...K\
"""
    print("Test 3 (Queen attack):")
    checkmate(board3)
    
    # Test Case 4: Bishop attack
    board4 = """\
B...
....
....
...K\
"""
    print("Test 4 (Bishop attack):")
    checkmate(board4)
    
    # Test Case 5: No attack
    board5 = """\
....
.K..
....
....\
"""
    print("Test 5 (No attack):")
    checkmate(board5)
    
    # Test Case 6: Pawn attack
    board6 = """\
....
.K..
P...
....\
"""
    print("Test 6 (Pawn attack):")
    checkmate(board6)

main()