import pgzrun

# Screen Setup
WIDTH = 1200
HEIGHT = 1000
TITLE = "GalaGar 2023"

# Color pallete
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

direction = 1

enemies = []
for x in range(8):
    for y in range (5):    
        enemies.append(Actor('bug'))
        enemies [-1].x = 100 + 90 * x
        enemies [-1].y = 150 + 80 * y

def update ():
    global direction

    moveDown = False 

    if len (enemies) > 0 and (enemies [-1].x > WIDTH-80 or enemies[0].x <80):
        moveDown = True
        direction = direction*-1
    
    for enemy in enemies:
        enemy.x+= 5*direction # Slide rate
        if moveDown == True:
            enemy.y += 75       # Drop Rate if drop rate goes higher
                                # then we lose a row of aliens. orig:80
        if enemy.y >= 999:
            enemy.y = 100
        
    
def draw ():
    
    screen.clear()
    screen.fill (BLACK)
    
    for enemy in enemies:
        enemy.draw()


pgzrun.go ()