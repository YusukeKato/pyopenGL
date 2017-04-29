from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import random

vertex = [
  [ 0.0, 0.0, 0.0 ],
  [ 1.0, 0.0, 0.0 ],
  [ 1.0, 1.0, 0.0 ],
  [ 0.0, 1.0, 0.0 ],
  [ 0.0, 0.0, 1.0 ],
  [ 1.0, 0.0, 1.0 ],
  [ 1.0, 1.0, 1.0 ],
  [ 0.0, 1.0, 1.0 ]
]

edge = [
  [ 0, 1 ],
  [ 1, 2 ],
  [ 2, 3 ],
  [ 3, 0 ],
  [ 4, 5 ],
  [ 5, 6 ],
  [ 6, 7 ],
  [ 7, 4 ],
  [ 0, 4 ],
  [ 1, 5 ],
  [ 2, 6 ],
  [ 3, 7 ]
]

face = [
  [ 0, 1, 2, 3 ],
  [ 1, 5, 6, 2 ],
  [ 5, 4, 7, 6 ],
  [ 4, 0, 3, 7 ],
  [ 4, 5, 1, 0 ],
  [ 3, 2, 6, 7 ]
]

normal = [
  [ 0.0, 0.0,-1.0 ],
  [ 1.0, 0.0, 0.0 ],
  [ 0.0, 0.0, 1.0 ],
  [-1.0, 0.0, 0.0 ],
  [ 0.0,-1.0, 0.0 ],
  [ 0.0, 1.0, 0.0 ]
]

light0pos = [ 0.0, 30.0, 50.0, 1.0 ]
light1pos = [ 50.0, 30.0, 0.0, 1.0 ]

green = [ 0.0, 1.0, 0.0, 1.0 ]
blue = [ 0.6, 0.8, 1.0, 1.0 ]

WIDTH = 600; HEIGTH = 600
ARIVE = 1; DEAD = 0
MAX = 20
timeCount = 0
field = [[[0 for i in range(MAX)] for j in range(MAX)] for k in range(MAX)]

def put():
    global timeCount
    timeCount += 1
    if timeCount > 10:
        x = random.randint(1, MAX-2)
        y = random.randint(1, MAX-2)
        z = random.randint(1, MAX-2)
        # Rペントミノ
        field[x-1][y-1][z] = 0; field[x-1][y][z] = 1; field[x-1][y+1][z] = 1
        field[x+0][y-1][z] = 1; field[x+0][y][z] = 1; field[x+0][y+1][z] = 0
        field[x+1][y-1][z] = 0; field[x+1][y][z] = 1; field[x+1][y+1][z] = 0
        timeCount = 0

def cube(x, y, z, flag):
    c1 = random.uniform(0.2, 1.0)
    c2 = random.uniform(0.2, 1.0)
    c3 = random.uniform(0.2, 1.0)
    #glColor3d(c1, c2, c3)
    #glColor3d(0.5, 0.8, 0.8)
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, [c1,c2,c3,1.0])
    vertex2 = []
    for j in range(8):
        a = [(vertex[j][0])+x, (vertex[j][1])+y, (vertex[j][2])+z]
        vertex2.append(a)
    if flag == 1:
        glBegin(GL_LINES);
        for i in range(12):
            glVertex3dv(vertex2[edge[i][0]])
            glVertex3dv(vertex2[edge[i][1]])
        glEnd()
    elif flag == 2:
        glBegin(GL_QUADS);
        for j in range(6):
            glNormal3dv(normal[j])
            for i in range(4):
                glVertex3dv(vertex2[face[j][i]])
        glEnd()

def field_create():
    for x in range(MAX):
        for y in range(MAX):
            for z in range(MAX):
                if field[x][y][z] == ARIVE:
                    cube(float(x), float(y), float(z), 2)

def dead_or_arive():
    for x in range(1, MAX-1):
        for y in range(1, MAX-1):
            for z in range(1, MAX-1):
                count = 0
                for i in range(-1,2):
                    for j in range(-1,2):
                        if field[y+i][x+j][z] == ARIVE:
                            count += 1
                if field[y][x][z] == ARIVE:
                    if count < 2 or count > 3:
                        field[y][x][z] = DEAD
                elif field[y][x][z] == DEAD:
                    if count == 3:
                        field[y][x][z] = ARIVE

def display():
    global vertex
    global edge
    glLightfv(GL_LIGHT0, GL_POSITION, light0pos)
    glLightfv(GL_LIGHT1, GL_POSITION, light1pos)
    # 配置
    put()
    # 生死判定
    dead_or_arive()
    # フィールド生成
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    field_create()
    glPopMatrix()
    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glLoadIdentity()
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)
    glCullFace(GL_FRONT)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, green)
    glLightfv(GL_LIGHT1, GL_SPECULAR, green)
    # 初期位置
    '''
    for i in range(200):
        p1 = random.randint(0, MAX-1)
        p2 = random.randint(0, MAX-1)
        p3 = random.randint(0, MAX-1)
        field[p1][p2][p3] = ARIVE
    '''

def idle():
    glutPostRedisplay()

def resize(w, h):
  glViewport(0, 0, w, h)
  glLoadIdentity()
  gluPerspective(30.0, w / h, 1.0, 100.0)
  gluLookAt(30.0, 40.0, 50.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)  #カメラ位置

def main():
    glutInit(sys.argv)    #GLUT,OpenGL環境の初期化
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(WIDTH, HEIGTH)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"GAME")    #ビットとして渡す必要がある(asciiコード)
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(resize)
    glutIdleFunc(idle)
    glutMainLoop()

main()
