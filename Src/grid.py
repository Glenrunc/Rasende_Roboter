from plate import *

HEIGHT = 800
WIDTH = 800 

class Grid(object):

    def __init__(self):
        self.grid = np.array([[Case() for _ in range(16)] for _ in range(16)])
        self.count_move = 0

    def reset_move(self):
        self.count_move = 0 

    def wall_around(self):
        for i in range(16):
            self.grid[0, i].wall[0] = True
            self.grid[i,0].wall[3] = True
            self.grid[-1, i].wall[2] = True
            self.grid[i, -1].wall[1] = True

    def center_goal(self):
        self.grid[7,7].wall[3] = True
        self.grid[7,7].wall[0] = True
        self.grid[7,8].wall[0] = True
        self.grid[7,8].wall[1] = True
        self.grid[8,7].wall[3] = True
        self.grid[8,7].wall[2] = True
        self.grid[8,8].wall[1] = True
        self.grid[8,8].wall[2] = True

    #Add status to the Case --> add player 
    def add_status(self, color, i, j):
        player = Player(color)
        self.grid[i,j].status = player

    def clean_status(self,i,j):
        player = Player(Color.EMPTY)
        self.grid[i,j].status = player
    
    def clean_color_grid(self):
        for i in range(16):
            for j in range(16):
                self.grid[i, j].clean()     

    def win_display(self,screen):
            font = pygame.font.Font(None,100)
            text = font.render("YOU HAVE WON",True,(0,0,0))
            pos = (125,375)
            screen.fill((rd.randint(0,255),rd.randint(0,255),rd.randint(0,255)))
            screen.blit(text,pos)
            pygame.display.update()
         
    def win(self,screen):
        timeout = t.time()
        if self.grid[self.goal_coordinate[0],self.goal_coordinate[1]].status.color == self.color_goal :
            while t.time() - timeout < 2:
                self.win_display(screen)
            screen.fill((255,255,255))
            self.update_super_goal()
            self.initial_position = self.position_robot
            self.count_move = 0
    
    #reset the round
    def reset(self,i,j):
        if (i == -1 and j==16):
            self.count_move = 0
            self.clean_color_grid()
            for robot in self.position_robot:
                self.clean_status(self.position_robot.get(robot)[0],self.position_robot.get(robot)[1])
            for robot in self.initial_position:
                self.add_status(robot,self.initial_position.get(robot)[0],self.initial_position.get(robot)[1])
            self.actualize_robot_position()
    
    def print_way(self,i,j):

        self.possible_move()
        for couple in self.possible_move_per_robot[self.grid[i,j].status.color]:
            for direction,coordinate in couple.items():
                k = i
                l = j
                if direction == 'RIGHT':
                    while l < coordinate[1]:
                        self.grid[i,l+1].update_color(COLOR_MAP.get(self.grid[i,j].status.color))
                        l=l+1
                if direction == 'LEFT':
                    while l > coordinate[1]:
                        self.grid[i,l-1].update_color(COLOR_MAP.get(self.grid[i,j].status.color))
                        l=l-1
                if direction == 'UP':
                    while k > coordinate[0]:
                        self.grid[k-1,j].update_color(COLOR_MAP.get(self.grid[i,j].status.color))
                        k=k-1
                if direction == 'DOWN':
                    while k < coordinate[0]:
                        self.grid[k+1,j].update_color(COLOR_MAP.get(self.grid[i,j].status.color))
                        k=k+1


    def move(self,i,j):
        # self.possible_move()
        if 0 <= i < 16 and 0 <= j < 16:
            #IF the player wants to clean a way 
            if (self.grid[i,j].color == (255,255,255)) and (self.grid[i,j].status.color == Color.EMPTY):
                self.clean_color_grid()
            #When The player click on a robot , usefull to indicate the possible way  
            if (self.grid[i,j].status.color != Color.EMPTY):
                self.clean_color_grid()
                self.possible_move()
                self.print_way(i,j)
            #MOVE 
            if(self.grid[i,j].color != (255,255,255)):

                self.possible_move()

                if i < self.position_robot[INVERTED_COLOR_MAP[self.grid[i, j].color]][0]:
                    new_pos = self.get_move(INVERTED_COLOR_MAP[self.grid[i, j].color],'UP')
                    self.add_status(INVERTED_COLOR_MAP[self.grid[i, j].color],new_pos[0],j)
                    self.clean_status(self.position_robot[INVERTED_COLOR_MAP[self.grid[i, j].color]][0],self.position_robot[INVERTED_COLOR_MAP[self.grid[i, j].color]][1])
                    self.clean_color_grid()
                    self.possible_move()
                    self.count_move = self.count_move + 1

            if(self.grid[i,j].color != (255,255,255)):

                self.possible_move()  

                if i > self.position_robot[INVERTED_COLOR_MAP[self.grid[i, j].color]][0]:
                    new_pos = self.get_move(INVERTED_COLOR_MAP[self.grid[i, j].color],'DOWN')
                    self.add_status(INVERTED_COLOR_MAP[self.grid[i, j].color],new_pos[0],j)
                    self.clean_status(self.position_robot[INVERTED_COLOR_MAP[self.grid[i, j].color]][0],self.position_robot[INVERTED_COLOR_MAP[self.grid[i, j].color]][1])
                    self.clean_color_grid()
                    self.possible_move()
                    self.count_move = self.count_move + 1


            if(self.grid[i,j].color != (255,255,255)):
                
                self.possible_move()  

                if j > self.position_robot[INVERTED_COLOR_MAP[self.grid[i, j].color]][1]:
                    new_pos = self.get_move(INVERTED_COLOR_MAP[self.grid[i, j].color],'RIGHT')
                    self.add_status(INVERTED_COLOR_MAP[self.grid[i, j].color],i,new_pos[1])
                    self.clean_status(self.position_robot[INVERTED_COLOR_MAP[self.grid[i, j].color]][0],self.position_robot[INVERTED_COLOR_MAP[self.grid[i, j].color]][1])
                    self.clean_color_grid()
                    self.possible_move()
                    self.count_move = self.count_move + 1


            if(self.grid[i,j].color != (255,255,255)):
                
                self.possible_move()  

                if j < self.position_robot[INVERTED_COLOR_MAP[self.grid[i, j].color]][1]:
                    new_pos = self.get_move(INVERTED_COLOR_MAP[self.grid[i, j].color],'LEFT')
                    self.add_status(INVERTED_COLOR_MAP[self.grid[i, j].color],i,new_pos[1])
                    self.clean_status(self.position_robot[INVERTED_COLOR_MAP[self.grid[i, j].color]][0],self.position_robot[INVERTED_COLOR_MAP[self.grid[i, j].color]][1])
                    self.clean_color_grid()
                    self.possible_move()
                    self.count_move = self.count_move + 1
       

        # print(self.possible_move_per_robot)

    #Get the move with the color and the direction      
    def get_move(self, color, direction):
        self.possible_move()
        color_data = self.possible_move_per_robot.get(color)
        for data in color_data:
            for dir in data:
                if dir == direction:
                    return data[dir]
        return None
    
    #Get the possible move for each robot
    def possible_move(self):

        self.actualize_robot_position()
        self.possible_move_per_robot = {} #{<Color.BLUE: 3>: [{'RIGHT': (2, 5)}, {'LEFT': (2, 0)}, {'UP': (1, 1)}, {'DOWN': (5, 1)}], <Color.RED: 4>: [{'RIGHT': (0, 3)}, {'LEFT': (0, 0)}, {'DOWN': (1, 1)}], <Color.GREEN: 2>: [{'RIGHT': (5, 15)}, {'LEFT': (5, 7)}, {'UP': (0, 12)}, {'DOWN': (6, 12)}], <Color.YELLOW: 1>: [{'RIGHT': (4, 14)}, {'LEFT': (4, 3)}, {'UP': (0, 7)}, {'DOWN': (5, 7)}]}
        color_robot = [Color.BLUE,Color.RED,Color.GREEN,Color.YELLOW]

        for robot in color_robot:
            i = self.position_robot[robot][0]
            j = self.position_robot[robot][1]
            self.possible_move_per_robot[robot] = []
            k = i
            l = j
            while l < 15 :
                if ((self.grid[k,l].wall[1] == False) and (self.grid[k,l+1].wall[3] == False) and (self.grid[k,l+1].status.color == Color.EMPTY)): 
                    l = l+1   
                else:
                    break
            if(l!=j):    
                self.possible_move_per_robot[robot].append({"RIGHT":(k,l)})
            # To the left
            k = i
            l = j    
            while l > 0 :
                if ((self.grid[k,l].wall[3] == False) and (self.grid[k,l-1].wall[1] == False) and (self.grid[k,l-1].status.color == Color.EMPTY)): 
                    l = l-1   
                else:
                    break
            if(l!=j):
                self.possible_move_per_robot[robot].append({"LEFT":(k,l)})              
            # To the up 
            k = i
            l = j 
            while k > 0 :
                if ((self.grid[k,l].wall[0] == False) and (self.grid[k-1,l].wall[2] == False) and (self.grid[k-1,l].status.color == Color.EMPTY)): 
                    k = k-1   
                else:
                    break
            if(k != i):
                self.possible_move_per_robot[robot].append({"UP":(k,l)})            
            #To the down 
            k = i
            l = j 
            while k < 15 :
                if ((self.grid[k,l].wall[2] == False) and (self.grid[k+1,l].wall[0] == False) and (self.grid[k+1,l].status.color == Color.EMPTY)): 
                    k = k+1   
                else:
                    break
            if(k != i):
                self.possible_move_per_robot[robot].append({"DOWN":(k,l)})        


      
   
    
    def initHeur(self,robot_position):
        self.add_status(Color.RED, 7, 7)
        self.add_status(Color.BLUE, 7, 8)
        self.add_status(Color.GREEN, 8, 8)
        self.actualize_robot_position()
        
        robot=Color.YELLOW
        cible = self.goal_coordinate
    #on met l'emplacement de la cible à 0
        self.grid[cible[0],cible[1]].heuristique=0
        
    #emplacement de départ
        p_fictif=[cible[0],cible[1]]
        self.grid[p_fictif[0],p_fictif[1]].heuristique=0
        a_traiter=[]
        a_traiter.append(p_fictif)
        
        while(a_traiter!=[]):
            p_fictif=a_traiter[0]
            value=self.grid[p_fictif[0],p_fictif[1]].heuristique +1
            self.add_status(robot, p_fictif[0], p_fictif[1]) #on met le robot sur la case
            self.actualize_robot_position()
            self.possible_move()
            coor=self.get_move(robot,'UP')
            if coor is not None :
                if (self.grid[coor[0],coor[1]].heuristique == -1 ):
                    up=p_fictif[0]-1
                    while (up >= coor[0]):
                        temp=[up,p_fictif[1]]
                        a_traiter.append(temp)
                        self.grid[temp[0],temp[1]].heuristique=value
                        up=up-1
            coor=self.get_move(robot,'DOWN')
            if coor is not None :
                if (self.grid[coor[0],coor[1]].heuristique == -1):
                    down=p_fictif[0]+1
                    while (down <= coor[0]):
                     
                        temp=[down,p_fictif[1]]
                        a_traiter.append(temp)
                        self.grid[temp[0],temp[1]].heuristique=value
                        down=down+1
            coor=self.get_move(robot,'LEFT')
            if coor is not None :
                if (self.grid[coor[0],coor[1]].heuristique == -1):
                    left=p_fictif[1]-1
                    while (left >= coor[1]):
                       
                        temp=[p_fictif[0],left]
                        a_traiter.append(temp)
                        self.grid[temp[0],temp[1]].heuristique=value
                        left=left-1
            coor=self.get_move(robot,'RIGHT')
            if coor is not None :
                if (self.grid[coor[0],coor[1]].heuristique == -1):
                    right=p_fictif[1]+1
                  
                    while (right <= coor[1]):
                      
                        temp=[p_fictif[0],right]
                        a_traiter.append(temp)
                        self.grid[temp[0],temp[1]].heuristique=value
                        right=right+1
            self.clean_status(p_fictif[0], p_fictif[1])
                

            a_traiter.pop(0)
        self.clean_status(7,7)
        self.clean_status(7,8)
        self.clean_status(8,8)
        for color in robot_position:  
            self.add_status(color,robot_position[color][0],robot_position[color][1])
        self.actualize_robot_position()

    
    
    
    def printHeur(self):
        print("Here is the heuristic table usefull for BFS and A*")
        tab = np.zeros((16,16))
        for i,ligne in enumerate(self.grid):
            for j,element in enumerate(ligne):
                tab[i][j]=element.heuristique
        print(tab)

    def getHeur(self,position):
        return self.grid[position[0],position[1]].heuristique
        
            
           


      #Get the possible move for a goal
    def possible_move_goal(self, goal_position):
        
        possible_move= []


        
        i = goal_position[0]
        j = goal_position[1]
        k = i
        l = j
        while l < 15 :
            if ((self.grid[k,l].wall[1] == False)): 
                l = l+1   
            else:
                break
        if(l!=j):    
            possible_move.append((k,l))
        # To the left
        k = i
        l = j    
        while l > 0 :
            if ((self.grid[k,l].wall[3] == False) & (self.grid[k,l-1].wall[1] == False)): 
                l = l-1   
            else:
                break
        if(l!=j):
            possible_move.append((k,l))            
        # To the up 
        k = i
        l = j 
        while k > 0 :
            if ((self.grid[k,l].wall[0] == False) & (self.grid[k-1,l].wall[2] == False)): 
                k = k-1   
            else:
                break
        if(k != i):
            possible_move.append((k,l))            
        #To the down 
        k = i
        l = j 
        while k < 15 :
            if ((self.grid[k,l].wall[2] == False) & (self.grid[k+1,l].wall[0] == False)): 
                k = k+1   
            else:
                break
        if(k != i):
            possible_move.append((k,l))   

        return possible_move


    #After a move, the robot position needs to be update                        
    def actualize_robot_position(self):
        self.position_robot = {}

        for i in range(16):
            for j in range(16):
                if(self.grid[i,j].status.color != Color.EMPTY):
                    color = self.grid[i, j].status.color
                    position = (i, j)
                    self.position_robot[color] = position


    #Create the grid with random position of the plate
    def create_grid(self):
        # _plate1.rotate()
        # _plate2.rotate()
        # _plate3.rotate()
        # _plate4.rotate()

        self.grid[:8,:8] = _plate1.l_grid
        self.grid[:8,8:] = _plate2.l_grid
        self.grid[8:,:8] = _plate3.l_grid
        self.grid[8:,8:] = _plate4.l_grid


    #Design the final grid with wall around etc...
    def grid_final(self):
        self.create_grid()
        self.wall_around()
        self.center_goal()
        #ROBOT INITIALIZED
        self.add_status(Color.RED, 0, 1)
        self.add_status(Color.BLUE, 2, 1)
        self.add_status(Color.YELLOW, 4, 7)
        self.add_status(Color.GREEN, 5, 12)
        self.actualize_robot_position()
        self.initial_position = self.position_robot
        self.update_super_goal()

    #Random choice of the mission to be completed
    def update_super_goal(self):

        goal = mission_tab[rd.randint(0,len(mission_tab)-1)]
        self.goal_coordinate = (goal[0],goal[1])
        self.color_goal = goal[2]
        self.mission_goal = goal[3]
        self.asset_goal = ASSET_MAP.get((self.color_goal, self.mission_goal),"empty")
    
    #Use to display the board
    def display(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (5, 10, 50, 30))
        #Screen count move 
        police = pygame.font.Font(None, 36)

        text = police.render(str(self.count_move), True, (0,0,0))
        screen.blit(text, (5,10))
        screen.blit(pygame.image.load("../Asset/reset_button.png"),(760,5))
        for i in range(16):
            for j in range(16):

                x = j * 45 + 40
                y = i * 45 + 40
                
                # x = i * ((WIDTH - WIDTH//16*2) // 16) + WIDTH//16
                # y = j((HEIGHT - HEIGHT//16*2) // 16) + HEIGHT//16
                
                # if self.grid[i, j].color != (255,255,255):
                # pygame.draw.rect(screen, self.grid[i, j].color, (x, y, 45,45)) TO be WORKED
                

                if self.grid[i, j].wall[0]:
                    pygame.draw.line(screen, (0, 0, 0), (x, y), (x + 45, y), 5)
                else:
                    if not (i in [7, 8] and j in [7, 8]):
                        pygame.draw.line(screen, (0, 0, 0), (x, y), (x + 45, y), 1)
                if self.grid[i, j].wall[1]:
                    pygame.draw.line(screen, (0, 0, 0), (x + 45, y), (x + 45, y + 45), 5)
                else:
                    if not (i in [7, 8] and j in [7, 8]):
                        pygame.draw.line(screen, (0, 0, 0), (x + 45, y), (x + 45, y + 45), 1)
                if self.grid[i, j].wall[2]:
                    pygame.draw.line(screen, (0, 0, 0), (x, y + 45), (x + 45, y + 45), 5)
                else:
                    if not (i in [7, 8] and j in [7, 8]):
                        pygame.draw.line(screen, (0, 0, 0), (x, y + 45), (x + 45, y + 45), 1)
                if self.grid[i, j].wall[3]:
                    pygame.draw.line(screen, (0, 0, 0), (x, y), (x, y + 45), 5)
                else:
                    if not (i in [7, 8] and j in [7, 8]):
                        pygame.draw.line(screen, (0, 0, 0), (x, y), (x, y + 45), 1)
                
                
               
                screen.blit(pygame.image.load(self.grid[i][j].status.asset), (x+7, y+7))

                if self.grid[i, j].status.color == Color.EMPTY:
                    pygame.draw.circle(screen, self.grid[i, j].color, (x + 22, y + 22), 5)
            # CENTER GOAL
            original_image = pygame.image.load(self.asset_goal)
            scaled_image = pygame.transform.scale(original_image, (original_image.get_width() * 2.25, original_image.get_height() * 2.25))
            screen.blit(scaled_image, (45*7+45, 45*7+45))

            #MISSION
            for mission in mission_tab:
                if(self.grid[mission[0],mission[1]].status.color == Color.EMPTY):
                    screen.blit(pygame.image.load(ASSET_MAP.get((mission[2],mission[3]),"empty")),(mission[1]*45+45,mission[0]*45+45))
            
 # Creation of the fourth plates, just for testing reason, will be replaced by real random generation      
_plate1 = Plate()
# _plate1.wall_generation(0)
#Double protection
_plate1.l_grid[0][3].wall[1] = True
_plate1.l_grid[2][5].wall[1] = True
_plate1.l_grid[2][5].wall[2] = True
_plate1.l_grid[4][0].wall[2] = True
_plate1.l_grid[4][2].wall[1] = True
_plate1.l_grid[4][2].wall[0] = True
_plate1.l_grid[5][1].wall[2] = True
_plate1.l_grid[5][7].wall[2] = True
_plate1.l_grid[5][7].wall[3] = True
_plate1.l_grid[6][1].wall[3] = True
_plate1.l_grid[6][1].wall[0] = True
_plate2 = Plate()
# _plate2.wall_generation(1)
_plate2.l_grid[0][1].wall[1] = True
_plate2.l_grid[1][5].wall[1] = True
_plate2.l_grid[1][5].wall[1] = True
_plate2.l_grid[1][5].wall[1] = True
_plate2.l_grid[3][1].wall[3] = True
_plate2.l_grid[3][1].wall[0] = True
_plate2.l_grid[4][6].wall[0] = True
_plate2.l_grid[4][6].wall[1] = True
_plate2.l_grid[6][4].wall[2] = True
_plate2.l_grid[6][4].wall[3] = True

_plate3 = Plate()
# _plate3.wall_generation(2)
_plate3.l_grid[1][4].wall[2] = True
_plate3.l_grid[1][4].wall[3] = True
_plate3.l_grid[2][0].wall[2] = True
_plate3.l_grid[2][6].wall[3] = True
_plate3.l_grid[2][6].wall[0] = True
_plate3.l_grid[4][7].wall[0] = True
_plate3.l_grid[4][7].wall[1] = True
_plate3.l_grid[5][1].wall[0] = True
_plate3.l_grid[5][1].wall[1] = True
_plate3.l_grid[6][3].wall[1] = True
_plate3.l_grid[6][3].wall[2] = True
_plate3.l_grid[7][4].wall[1] = True

_plate4 = Plate()
# _plate4.wall_generation(3)
_plate4.l_grid[1][5].wall[2] = True
_plate4.l_grid[1][5].wall[3] = True
_plate4.l_grid[3][1].wall[1] = True
_plate4.l_grid[3][1].wall[2] = True
_plate4.l_grid[4][7].wall[0] = True
_plate4.l_grid[5][6].wall[0] = True
_plate4.l_grid[5][6].wall[1] = True
_plate4.l_grid[6][2].wall[0] = True
_plate4.l_grid[6][2].wall[3] = True
_plate4.l_grid[7][4].wall[3] = True
