import turtle
import random
import json
import pygame
from data import game_data
import graphics

#boxes[0][i] gives X-axis of GRID,boxes[1][i] gives Y-axis of GRID,boxes[2][i] gives WHAT APLHABET IS STORED OVER IT
#games[0][i] givess gotian x y axis in form of tupples,#games[1][i] givess gotian location of alphabet stored,#games[2][i] givess gotian alpabet stored in it, 
pygame.mixer.init()

# pygame.mixer.music.load('theme.mp3')

# pygame.mixer.music.play(-1)

x = -740
y = 320
i = 0
boxes = []
list1 = []
list2 = []
list3 = []

gotians_x_y_axis=[]
alphabet_location=[]
alphabets=[]
got_x=330
got_y=320
english = ""
new1=0
new2=0
game=[]
index_of_box_giving_alphabet=0
l1=game_data["alphabet_score"]
turn=0
score=0
score1=0
countdown=99
z=0
old_alphabets_location=[]
indices=[]
go=0
data=[[],[]]


colors = ["grey", "chartreuse4", "teal", "DarkOrchid4", "darkgoldenrod4", "chocolate", "MidnightBlue", "peachpuff4"]
scrabble = turtle.Screen()
scrabble.title("Python Scrabble Game")
scrabble.bgcolor("maroon")
turn_no=0

maze_turtle = turtle.Turtle()
my_turtle2 = turtle.Turtle()
points = turtle.Turtle()
points.hideturtle()
my_turtle3 = turtle.Turtle()
points.color("maroon")
maze_turtle.speed(100000)
my_turtle2.speed(100000)
my_turtle3.speed(100000)
maze_turtle.hideturtle()
my_turtle2.hideturtle()
my_turtle3.hideturtle()
maze_turtle.color("black")
my_turtle2.color("Black")
my_turtle3.color("white")


#to store 225 gotians of grid
for _ in range(225):
    if x > -180:
        x = -740
    list1.append(x)
    list3.append("")
    x += 40

for _ in range(225):
    if i == 15:
        i = 0
        y -= 40
    list2.append(y)
    i += 1

boxes.append(list1)
boxes.append(list2)
boxes.append(list3)

#drawing 225 gotains grid
for i in range(225):
    col = random.choice(colors)
    graphics.draw_rectangle(maze_turtle, boxes[0][i], boxes[1][i], 40, 40, col)



#gotian list is here to store the x and y axis of the gotains, alphabet stores the location at which my alphabet will be and alphaets is used to store thee alpabet at that spot
#the varaible english would later be used to store the alphabet that is clicked on at gotian
#game is another main list which will append other lists in it

#here i will define gotian values 17 here cane be 16 works totally fine if i add more users then add 8 to it and change i==8 and i==16 and also change b
def gotians_value():
      global got_y,got_x
      a=got_x
      b=got_y-50
      chk=0
      for i in range(17):   
                         if(i==8):
                              a=330
                              b-=150  
                         else:
                              no=random.randint(1,75)
                              alphabets.append(game_data["gotian"][no])
                              gotians_x_y_axis.append((a,b))
                              alphabet_location.append((a+15,b-25))
                              a+=40                       

#draw users name the user no and his score will be passed to it                                
def draw_user(i,score,name):
     global go
     if(i==0):
            x=330
            y=320
     elif(i==1):
            x=330
            y=170
    
     my_turtle2.penup()
     my_turtle2.goto(x,y)
     my_turtle2.pendown()
     graphics.draw_rectangle(points,x+215,y+25,40,40,"maroon")
     my_turtle2.write(f"UserName:{name}   Score = {score} ", font=("modern love", 14, "bold"))
     if(go==0):
                graphics.draw_goat(my_turtle2,game,0,8)
                go+=1
     elif(go==1):
                graphics.draw_goat(my_turtle2,game,8,16) 
                go+=1     

 #draws the gotians after recieving the coordinates              
def draw_goat(a,b):
          
          for i in range(a,b):
                    if(game[2][i]!=""):
                        col=random.choice(colors)
                        graphics.draw_rectangle(maze_turtle,game[0][i][0],game[0][i][1],40,40,col)
                        my_turtle2.penup()
                        my_turtle2.goto(game[1][i][0],game[1][i][1])
                        my_turtle2.pendown()
                        my_turtle2.write(game[2][i],font=("modern love", 15, "bold"))
                    
gotians_value()
game.append(gotians_x_y_axis)
game.append(alphabet_location)
game.append(alphabets)

#takes input
def users_input():
     return turtle.textinput("Input", "Enter your name:")

# currently drawing 2 users
name=users_input() 
draw_user(0,0,name)
name1=users_input() 
draw_user(1,0,name1) 

#submit BUTTON
graphics.draw_rectangle(maze_turtle,250,-270,120,30,"SkyBlue4")
my_turtle2.penup()
my_turtle2.goto(270,-295)
my_turtle2.pendown()
my_turtle2.write("Submit",font=("modern love", 15, "bold")) 

#search aka most important function
def search(x):
    word_list = game_data["words"]  
    global score, score1,l1,turn,countdown,turn_no
    words = ""
    words1 = ""
    words2 = ""
    words3 = ""

   # (horizontal)
    for i in range(x, 0, -1):
        if boxes[0][i] != -740 and boxes[2][i] != "":
            words += boxes[2][i]
        else:
            break

    #  up (vertical)
    for i in range(x, 0, -15):  # Fixed step to search vertically
        if boxes[1][i] != 320 and boxes[2][i] != "":
            words1 += boxes[2][i]
        else:
            break

    # right (horizontal)
    for i in range(x, 225):  # Increase to cover full grid horizontally
        if boxes[0][i] != -180 and boxes[2][i] != "":
            words2 += boxes[2][i]
        else:
            break

    # Collect letters going down (vertical)
    for i in range(x, 225, 15):  # Correct step to search vertically
        if boxes[1][i] != -240 and boxes[2][i] != "":
            words3 += boxes[2][i]
        else:
            break
    
    
    if (words in word_list or words[::-1] in word_list or
        words1 in word_list or words1[::-1] in word_list or
        words2 in word_list or words2[::-1] in word_list or
        words3 in word_list or words3[::-1] in word_list):
        #this appends the word to datat to append in json
        data[0].append(words)

        for i in range(len(words)):
         chk=words[i]
         old_alphabets_location.clear()
         #calcutaes the socre of the user and data[1] appends the score to make it present in JSON file
         for key in l1:
          if(key["alphabet"]==chk):
               if(turn==0):
                    score+=key["score"]
                    data[1].append(score)
               elif(turn==1):
                    score1+=key["score"]  
                    data[1].append(score1)
        
        indices.clear() #indices of the grid on ehcih alphabet was stored
        #json file work
        with open("player_data.json", "w") as file:
              json.dump(data, file, indent=4)

        #checks wohse turn it was again draws the score undo 1 fill the empty gotian list and turn would change no turn    
        if(turn==0):
         draw_user(0,score,name)
         undo1(0)
         turn=1
        elif(turn==1):
         draw_user(1,score1,name1)
         undo1(1)    
         turn=0   

            

    else:
        #calls udno simple to return
        undo()
        if(turn==0):
             turn=1
        elif(turn==1):
             turn=0
       
    countdown=99
    #timer()   
    #check if the turns are 10 or not
    check(turn_no)

#the check function to end game
def check(a):
     print(a,"reached")
     if(a==4):
          maze_turtle.clear()   #clears all grid gotians words etc
          my_turtle2.clear()
          my_turtle3.clear()
          graphics.draw_rectangle(my_turtle2,-400,250,750,450,"black")
          my_turtle2.penup()
          my_turtle2.goto(0,0)
          my_turtle2.pendown()
          my_turtle3.write(f"THE GAME HAS ENDED. WELL PLAYED\n\n",align="center", font=("modern love", 20, "bold"))
          if(score>score1):
               my_turtle3.write(f"{name} HAS WON THE GAME",align="center", font=("modern love", 20, "bold"))
          else:
                 my_turtle3.write(f"{name1}HAS WON THE GAME",align="center", font=("modern love", 20, "bold"))
          with open('example.txt', 'w') as file:
            file.write(f'User 1: {name} Score: {score}\n')
            file.write(f'User 2: {name1} Score: {score1}\n')  #file handling


def undo1(id):
       #undo 1 takes id to check whose turn it was and then check what would be inital and final no for the loop to check in gotian
       if(id==0):
             a=0
             b=8
       else:
             a=8
             b=16 

       print("old aliphabet locations",old_alphabets_location)
       for i in range(15):
          print(boxes[2][i])
       #now check which ever is empty than re drwas over it over it which ever is empty   
       for i in range(a,b):
                    if(game[2][i]==""):
                        no=random.randint(1,75)
                        game[2][i]=game_data["gotian"][no]
                        col=random.choice(colors)
                        graphics.draw_rectangle(maze_turtle,game[0][i][0],game[0][i][1],40,40,col)
                        my_turtle2.penup()
                        my_turtle2.goto(game[1][i][0],game[1][i][1])
                        my_turtle2.pendown()
                        my_turtle2.write(game[2][i],font=("modern love", 15, "bold"))


#returns values back to gotians                 
def undo():
     
     print("old aliphabet locations",old_alphabets_location)
     for i in range(15):
          print(i,".",boxes[2][i],end="")

     for i in range(16):
          if(game[2][i]==""):
                    game[2][i]=old_alphabets_location.pop()
                    col=random.choice(colors)
                    graphics.draw_rectangle(maze_turtle,game[0][i][0],game[0][i][1],40,40,col)
                    my_turtle2.penup()
                    my_turtle2.goto(game[1][i][0],game[1][i][1])
                    my_turtle2.pendown()
                    my_turtle2.write(game[2][i],font=("modern love", 15, "bold"))
     for i in range(len(indices)):
           boxes[2][indices[i]]=""  #again makes the box of grid empty
           col=random.choice(colors)
           graphics.draw_rectangle(maze_turtle,boxes[0][indices[i]],boxes[1][indices[i]],40,40,col) 
     old_alphabets_location.clear()
     indices.clear()
     print(game[2])   

def timer():
      global countdown, turn
      my_turtle3.penup()
      my_turtle3.goto(280,-340)
      my_turtle3.pendown
      my_turtle3.clear()
      if countdown >= 0:
        my_turtle3.write(f"Time: {countdown}", font=("Arial", 18, "bold"))
        countdown -= 1
        scrabble.ontimer(timer, 1000)
      else:
           my_turtle3.clear()
           if(turn==0):
                turn=1
           elif(turn==1):
                turn=0
           countdown=10
           undo()
           timer()            

def users_alphbet():
     return turtle.textinput("Input", "Enter Alphabet:")

def get_mouse_click_coor(x, y):
   global help
   global english,turn,turn_no
   global new1,old_alphabets_location
   global new2,index_of_box_giving_alphabet,lasty

   #checks for the submit button
   if((x>=250 and x<=370)and(y<=-270 and y>=-310)):
           search(index_of_box_giving_alphabet)
           turn_no+=1
           

   if(turn==0):
         a=0
         b=8
   elif(turn==1):
         a=8
         b=16             
   for i in range(a,b):
        
     if (game[1][i][0] - 20 <= x <= game[1][i][0] + 20) and (game[1][i][1] - 20 <= y <=game[1][i][1] + 20):
           english=game[2][i]
           if(english=="-"):#if user selects dash
                charcter = users_alphbet()
                game[2][i]=charcter
                english=game[2][i]

           old_alphabets_location.append(game[2][i])
           game[2][i]=""
           help=1
           game[2][i]=""
           new1=game[1][i][0]-15
           new2=game[1][i][1]+25
           

     elif (help==1):
            for z in range (225): 
                  if((x>=boxes[0][z]and x<=boxes[0][z]+40)and(y<=boxes[1][z] and y>=boxes[1][z]-40)) :
                        if(boxes[2][z]==""):
                              x=boxes[0][z]
                              y=boxes[1][z]
                              col=random.choice(colors)
                              graphics.draw_rectangle(maze_turtle,x,y,40,40,col)
                              graphics.draw_rectangle(maze_turtle,new1,new2,40,40,"maroon")
                              boxes[2][z]=english

                              my_turtle2.penup()
                              my_turtle2.goto(boxes[0][z]+15,boxes[1][z]-25)
                              my_turtle2.pendown()
                              my_turtle2.write(english,font=("modern love", 15, "bold")) 
                              help=0  
                              index_of_box_giving_alphabet=z
                              indices.append(z) #appends the indices so can draw over specidic indices of grid

#timer()
scrabble.onscreenclick(get_mouse_click_coor) 
turtle.done()                             