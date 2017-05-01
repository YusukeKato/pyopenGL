from OpenGL.GL import *
from OpenGL.GLUT import *
import sys

def display():
    x = 0.2; y = 0.2
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(100.0)
    glBegin(GL_POINTS)
    for j in range(-1, 2):
        x += 0.2
        y = 0.2
        for i in range(-1, 2):
            y += 0.2
            if j == 1 or (j == 0 and i == 0) or (j == -1 and (i == 0 or i == 1)):
                glColor3f(0.4, 0.8, 0.8)
            else:
                glColor3f(1.0, 1.0, 1.0)
            glVertex3f(x, y, 0.0)
    glEnd()
    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"lifegame_man")
    init()
    glutDisplayFunc(display)
    glutMainLoop()

try:
    main()
except:
    print("error")
