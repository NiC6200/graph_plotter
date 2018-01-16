import pygame,time


x_min=-100
x_max=100
y_min=-100
y_max=100
height=800
width=800
coordinatex=width/(x_max-x_min)
coordinatey=height/(y_max-y_min)
line_spacingx=5*coordinatex
line_spacingy=5*coordinatey


pygame.init()
board=pygame.display.set_mode((800,800))

#a=[10,5]

white=pygame.Color(255,255,255)
black=pygame.Color(0,0,0)
red=pygame.Color(255,0,0)
blue=pygame.Color(0,0,255)
green=pygame.Color(0,255,0)




board.fill(white)
    #pygame.display.update()
    #time.sleep(1)


def update_variables():

    print(x_min,x_max,' ',line_spacingx,coordinatex,width)


def my_coordinatex(x):
    return x/coordinatex+x_min

def my_coordinatey(y):
    return -y/coordinatey+y_min

def board_coordinatex(x):
    return coordinatex*(x-x_min)

def board_coordinatey(y):
    return height-coordinatey*(y-y_min)

def join_point(surf,col,a,b,t):
    pygame.draw.line(surf,col,a,b,t)
    #pygame.display.update()

def f(func, x):
    y = 0
    for i in range(len(func)):
        y += x ** i * func[i]
    return y


def mark_point(surf, col, a):
    pygame.draw.line(surf, col, (
    int(board_coordinatex(a[0]) + line_spacingx / 4), int(board_coordinatey(a[1]) + line_spacingy / 4)), (
                     int(board_coordinatex(a[0]) - line_spacingx / 4),
                     int(board_coordinatey(a[1]) - line_spacingy / 4)), 3)

    pygame.draw.line(surf, col, (
    int(board_coordinatex(a[0]) + line_spacingx / 4), int(board_coordinatey(a[1]) - line_spacingy / 4)), (
                     int(board_coordinatex(a[0]) - line_spacingx / 4),
                     int(board_coordinatey(a[1]) + line_spacingy / 4)), 3)
    #pygame.display.update()


def draw_graph(surf, col, a, rang):
    if rang == 'full':
        rang = range(0, width)

    yp = int(board_coordinatey(f(a, my_coordinatex(1))))
    for i in rang:
        yo = int(board_coordinatey(f(a, my_coordinatex(i))))
        # print(y)
        if yo < height and yo > 0 and yp > 0 and yp < height:
            # print(i,y)
            join_point(board, col, [i, yo], [i - 1, yp], 3)
            #pygame.display.update()
        yp = yo
    pygame.display.update()

            
def draw_board():
    
    board.fill(white)
    
    for i in range(0,width+1,int(line_spacingx)):
        pygame.draw.line(board,black,(i,height),(i,0))
    
    for i in range(0,height+1,int(line_spacingy)):
        pygame.draw.line(board,black,(width,i),(0,i))
    
    #pygame.draw.line(board,black,(int(board_coordinatex(0)),int(board_coordinatey(y_max))),(int(board_coordinatex(x_max)),int(height/2)),5)
    #pygame.draw.line(board,black,(int(width/2),0),(int(width/2),height),5)
    
    draw_graph(board,black,[0,0],'full')
    pygame.draw.line(board,black,(int(board_coordinatex(0)),int(board_coordinatey(y_max))),(int(board_coordinatex(0)),int(board_coordinatey(y_min))),3)



    
    pygame.display.update()
                     


#time.sleep(2)





draw_board()
mark_point(board,red,[25,-45])
draw_graph(board,blue,[5,2],'full')
draw_graph(board, green, [1,5,1 ], 'full')
draw_graph(board, red, [-100,0,1 ], 'full')
#time.sleep(5)


while True:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            
            if event.key==pygame.K_RIGHT:
                x_min+=int(line_spacingx/4)
                x_max+=int(line_spacingx/4)
                
            if event.key==pygame.K_LEFT:
                x_min-=int(line_spacingx/4)
                x_max-=int(line_spacingx/4)
                
            if event.key==pygame.K_UP:
                y_min+=int(line_spacingy/4)
                y_max+=int(line_spacingy/4)
                
            if event.key==pygame.K_DOWN:
                y_min-=int(line_spacingy/4)
                y_max-=int(line_spacingy/4)
                
            if event.key==pygame.K_a and x_max-x_min-2*int(line_spacingx/4)>0:
                x_max-=int(line_spacingx/4)
                x_min+=int(line_spacingx/4)
                y_max-=int(line_spacingy/4)
                y_min+=int(line_spacingy/4)
                coordinatex=width/(x_max-x_min)
                coordinatey=height/(y_max-y_min)
                line_spacingx=5*coordinatex
                line_spacingy=5*coordinatey
                
            if event.key==pygame.K_s:
                x_max+=int(line_spacingx/4)
                x_min-=int(line_spacingx/4)
                y_max+=int(line_spacingy/4)
                y_min-=int(line_spacingy/4)
                coordinatex=width/(x_max-x_min)
                coordinatey=height/(y_max-y_min)
                line_spacingx=5*coordinatex
                line_spacingy=5*coordinatey
                
            
            elif event.type==pygame.K_q:
                pygame.quit()
                quit()
                
            print(x_min,x_max,' ',line_spacingx,coordinatex,width)
            draw_board()
            mark_point(board,red,[25,-45])
            draw_graph(board,blue,[5,2],'full')
            draw_graph(board, green, [1,5,1 ], 'full')
            draw_graph(board, red, [-100,0,1 ], 'full')
            #pygame.display.update()
            #time.sleep(5)












