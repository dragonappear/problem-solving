# https://www.acmicpc.net/problem/5373
from sys import stdin
input = stdin.readline


def init():
    for s in range(6):
        for i in range(3):
            for j in range(3):
                cube[s][i][j] = color[s]


def rotate_side(side, clock_dir):

    def rotate():
        for _ in range(rot):
            tmp = [['w'] * 3 for _ in range(3)]
            for i in range(3):
                for j in range(3):
                    tmp[j][2-i] = cube[side][i][j]

            for i in range(3):
                for j in range(3):
                    cube[side][i][j] = tmp[i][j]

    rot = 1 if clock_dir else 3

    rotate()  # side 화면 돌리기

    for _ in range(rot):  # side로 둘러싸인 면들 돌리기

        if side == FRONT:
            for i in range(3):
                tmp = cube[UP][2][i]
                cube[UP][2][i] = cube[LEFT][2 - i][2]
                cube[LEFT][2 - i][2] = cube[DOWN][0][2 - i]
                cube[DOWN][0][2 - i] = cube[RIGHT][i][0]
                cube[RIGHT][i][0] = tmp

        elif side == BACK:
            for i in range(3):
                tmp = cube[UP][0][i]
                cube[UP][0][i] = cube[RIGHT][i][2]
                cube[RIGHT][i][2] = cube[DOWN][2][2 - i]
                cube[DOWN][2][2 - i] = cube[LEFT][2 - i][0]
                cube[LEFT][2 - i][0] = tmp

        elif side == LEFT:
            for i in range(3):
                tmp = cube[UP][i][0]
                cube[UP][i][0] = cube[BACK][i][0]
                cube[BACK][i][0] = cube[DOWN][i][0]
                cube[DOWN][i][0] = cube[FRONT][i][0]
                cube[FRONT][i][0] = tmp

        elif side == RIGHT:
            for i in range(3):
                tmp = cube[UP][i][2]
                cube[UP][i][2] = cube[FRONT][i][2]
                cube[FRONT][i][2] = cube[DOWN][i][2]
                cube[DOWN][i][2] = cube[BACK][i][2]
                cube[BACK][i][2] = tmp

        elif side == UP:
            for i in range(3):
                tmp = cube[FRONT][0][i]
                cube[FRONT][0][i] = cube[RIGHT][0][i]
                cube[RIGHT][0][i] = cube[BACK][2][2 - i]
                cube[BACK][2][2 - i] = cube[LEFT][0][i]
                cube[LEFT][0][i] = tmp

        elif side == DOWN:
            for i in range(3):
                tmp = cube[FRONT][2][i]
                cube[FRONT][2][i] = cube[LEFT][2][i]
                cube[LEFT][2][i] = cube[BACK][0][2 - i]
                cube[BACK][0][2 - i] = cube[RIGHT][2][i]
                cube[RIGHT][2][i] = tmp


UP, DOWN, FRONT, BACK, LEFT, RIGHT = 0, 1, 2, 3, 4, 5
cube = [[['w'] * 3 for _ in range(3)] for _ in range(6)]
color = ['w', 'y', 'r', 'o', 'g', 'b']

for _ in range(int(input())):
    init()

    N = int(input().strip())
    for s in input().split():
        if s[0] == 'F':
            rotate_side(FRONT, s[1] == '+')
        elif s[0] == 'B':
            rotate_side(BACK, s[1] == '+')
        elif s[0] == 'U':
            rotate_side(UP, s[1] == '+')
        elif s[0] == 'D':
            rotate_side(DOWN, s[1] == '+')
        elif s[0] == 'L':
            rotate_side(LEFT, s[1] == '+')
        else:
            rotate_side(RIGHT, s[1] == '+')

    for i in range(3):
        for j in range(3):
            print(cube[UP][i][j], end='')
        print()
