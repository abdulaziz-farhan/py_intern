
def solve(n):
    board = [-1] * n

    def place(r):
        if r == n:
            return True

        for c in range(n):
            if all(c != board[i] and abs(c-board[i]) != r-i
                   for i in range(r)):
                board[r] = c
                if place(r + 1):
                    return True
        return False

    if place(0):
        for c in board:
            print("." * c + "Q" + "." * (n-c-1))
    else:
        print("No solution")

n = int(input("Enter N: "))
if n > 0:
    solve(n)
else:
    print("Enter a positive number")
