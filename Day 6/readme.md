# Day 6

## Exercise
![image](https://user-images.githubusercontent.com/91926955/185399135-0474bb1f-af1d-4a43-b9dd-dfcba828678b.png)
![image](https://user-images.githubusercontent.com/91926955/185399227-d436778d-a909-4b7e-8764-24507e440bca.png)
In this code i am drawing letter I as a challenge.

- https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
![image](https://user-images.githubusercontent.com/91926955/185407211-7487f2fb-10dd-4e72-9e95-ce6e66ca75d5.png)

def turn_around():

turn_left()

turn_left()

def turn_right():

turn_around()

turn_left()
    
def turn_jump():

move()

turn_left()

move()

turn_right()

move()

turn_right()

move()

turn_left()
    
for step in range(6):

turn_jump()


- https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
![image](https://user-images.githubusercontent.com/91926955/185426766-0496f424-7d42-4554-999d-68aa90230c85.png)

def turn_around():

turn_left()

turn_left()

def turn_right():

turn_around()

turn_left()
    
def turn_jump():

move()

turn_left()

move()

turn_right()

move()

turn_right()

move()

turn_left()
    
while at_goal() != True :
    
    turn_jump()

- https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
![image](https://user-images.githubusercontent.com/91926955/185474027-7d40a2d4-0947-4b78-8c14-bba55acafe3d.png)
def turn_around():
    turn_left()
 
    turn_left()
    
def turn_right():

    turn_around()
    
    turn_left()
    
def turn_jump():
        
        turn_left()
        
        move()
        
        turn_right()
        
        move()
        
        turn_right()
        
        move()
        
        turn_left()
   
while at_goal() != True :
    
      if wall_in_front():
             
             turn_jump()
      
      else:
      
              move()






- https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
![image](https://user-images.githubusercontent.com/91926955/185475670-ea6af357-6e01-42f0-8f04-da37a43829f0.png)
def turn_right():

    turn_left()
    
    turn_left()
    
    turn_left()
    
def jump():
      
      turn_left()
      
      while wall_on_right():
           
           move()
      
      turn_right()
      
      move()
      
      turn_right()
      
      while front_is_clear():
           
           move()
      
      turn_left()
  
while at_goal() != True :
      
      if wall_in_front():
               
               jump()
      
      else:
               
               move()


## Escaping the Maze

![escaping the maze](escaping_the_maze.gif)

- https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
![image](https://user-images.githubusercontent.com/91926955/185482417-6d2f9d8c-06f1-4a5b-8b3d-2d6a5d9d2fde.png)

 def turn_right():

    turn_left()
    
    turn_left()
    
    turn_left()
    
while front_is_clear():
       
       move()

turn_left()
    
while  not at_goal() :
       
       if right_is_clear():
            
            turn_right()
            
            move()
       
       elif front_is_clear():
            
            move()
       
       else:
            
            turn_left() 
  


![image](https://user-images.githubusercontent.com/91926955/185399135-0474bb1f-af1d-4a43-b9dd-dfcba828678b.png)
![image](https://user-images.githubusercontent.com/91926955/185399227-d436778d-a909-4b7e-8764-24507e440bca.png)
In this code i am drawing letter I as a challenge.



