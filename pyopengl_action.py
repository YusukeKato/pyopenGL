# action game 2017.5.11
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import random

PI = 3.1415926535
flag_jump = True
''' 物理 '''
px = 0.0; py = 0.0    # キャラクタの座標
vx = 0.0; vy = 0.0
ax = 0.0; ay = -0.98
g = 0.98
dt = 0.01
''' 敵 '''
posi = [[-3.0, -0.8, 0.01]]

def ground():
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex3f(-3.0, -1.0, 0.0)
    glVertex3f( 3.0, -1.0, 0.0)
    glEnd()

def charactor():
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    r = 0.2; n = 360
    for i in range(360):
        x = r * math.cos(2.0 * PI * float(i/n))    # 2.0は大切
        y = r * math.sin(2.0 * PI * float(i/n))    # ないと半月
        glVertex3f(x + px, y + py, 0.0)
    glEnd()

def enemy():
    global posi
    glColor3f(1.0, 0.4, 0.5)
    glBegin(GL_LINE_LOOP)
    r = 0.1; n = 360
    for i in range(360):
        x = r * math.cos(2.0 * PI * float(i/n))
        y = r * math.sin(2.0 * PI * float(i/n))
        glVertex3f(x + posi[0][0], y + posi[0][1], 0.0)
    glEnd()

def enemy_controller():
    global posi, px, py
    posi[0][0] += posi[0][2]
    if math.sqrt(pow(posi[0][0]-px, 2) + pow(posi[0][1]-py, 2)) <= 0.3:
        sys.exit()

def judge():
    global px, py, vx, vy, ax, ay, flag_jump
    if px > 2.5:
        px = 2.5
        vx = -vx * 0.6
        ax = -ax
    elif px < -2.5:
        px = -2.5
        vx = -vx * 0.6
        ax = -ax
    if py > 3.0:
        py = 2.8
        vy = 0.0
    elif py < -0.8:
        py = -0.8
        vy = 0.0
        flag_jump = True
    if vx > -0.01 and vx < 0.01:
        vx = 0.0
        ax = 0.0

def butsuri():
    global px, py, vx, vy, ax, ay, g, dt
    px = px + (vx * dt) + (ax * dt * dt) / 2
    vx = vx + (ax * dt)
    py = py + (vy * dt) + (ay * dt * dt) / 2
    vy = vy + (ay * dt)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    butsuri()
    judge()
    ground()
    charactor()
    enemy()
    enemy_controller()
    glFlush()

def resize(w, h):
    glViewport(0, 0, w, h)
    glOrtho(-w / 200.0, w / 200.0, -h / 200.0, h / 200.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glMatrixMode(GL_PROJECTION)

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)

def idle():
    glutPostRedisplay()

def keyboard(key, x, y):
    global vx, vy, ax, flag_jump
    if key == b'a':
        vx = -0.3
        ax = 0.05
    if key == b'd':
        vx = 0.3
        ax = -0.05
    if key == b's' and flag_jump:
        vy = 1.0
        flag_jump = False
    # print(key)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Game Window")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(resize)
    glutKeyboardFunc(keyboard)
    glutIdleFunc(idle)
    glutMainLoop()

main()
