import random

def hangman():
    word_list = ["cat", "dog", "bird"]
    r = random.randint(0, 2)
    word = word_list[r]
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")
    print(board)
    
    while wrong < len(stages) - 1:
        print("\n")
        char = input("1文字予想してね：")
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win! 正解は{}。".format(word))
            win = True
            break
    if not win:
        print("You lose! 正解は{}。".format(word))


hangman()
