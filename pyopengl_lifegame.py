from OpenGL.GL import *
from OpenGL.GLUT import *
import sys
import random

WIDTH = 600
HEIGTH = 600
cs = 10
COL = int(WIDTH / cs)
ROW = int(HEIGTH / cs)

field = [[0 for i in range(ROW+2)] for j in range(COL+2)]

timeCount = 0
size = 0.015
DEAD = 0; ALIVE = 1

def dead_or_alive():
    for i in range(1,COL):
        for j in range(1,ROW):
            count = 0
            for m in range(-1, 2):
                for n in range(-1, 2):
                    if field[j+m][i+n] == ALIVE:
                        count += 1
            if field[j][i] == ALIVE:
                if count < 2 or count > 3:
                    field[j][i] = DEAD
            elif field[j][i] == DEAD:
                if count == 3:
                    field[j][i] = ALIVE

def field_create():
    glPointSize(8.0)
    glBegin(GL_POINTS)
    x = size; y = size
    for j in range(COL):
        y += size
        x = size
        for i in range(ROW):
            if field[j][i] == 0:
                glColor3f(0.0, 0.0, 0.0)
                glVertex3f(x, y, 0.0)
            else:
                glColor3f(0.6, 1.0, 0.4)
                glVertex3f(x, y, 0.0)
            x += size
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    # 生死判定
    dead_or_alive()
    # 配置
    put()
    # フィールド作成
    field_create()
    glFlush()

def init():
    glClearColor(1.0, 0.4, 0.4, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0)
    # ランダム配置
    '''
    for k in range(400):
        ranx = random.randint(2,60)
        rany = random.randint(2,60)
        field[ranx][rany] = 1
    '''

def put():
    global timeCount
    timeCount += 1
    if timeCount > 10:
        k = random.randint(3,57)
        # Rペントミノ
        field[55][k] = 0; field[55][k+1] = 1; field[55][k+2] = 1
        field[56][k] = 1; field[56][k+1] = 1; field[56][k+2] = 0
        field[57][k] = 0; field[57][k+1] = 1; field[57][k+2] = 0
        timeCount = 0

def idle():
    glutPostRedisplay()

def keyboard(key, x, y):
    if int(key) == 1:
        ranx = random.randint(2,58)
        rany = random.randint(2,58)
        field[ranx][rany] = 1
    else:
        print("key")

def main():
    glutInit(sys.argv)    #GLUT,OpenGL環境の初期化
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGTH)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"GAME")    #ビットとして渡す必要がある(asciiコード)
    init()
    glutDisplayFunc(display)
    glutIdleFunc(idle)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

try:
    main()
except:
    print("error")
