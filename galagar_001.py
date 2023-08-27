import pgzrun

# Screen Setup
WIDTH = 1200
HEIGHT = 1000
TITLE = "GalaGar 2023"

# Render Sprite
ship = Actor ('galaga')
ship.x = WIDTH//2
ship.y = HEIGHT - 100
ship.dead = False
ship.countdown = 1000

# List for Bullet
bullets = []

# List for Enemies
enemies = []
# Make array of enemies
for x in range(8):
    for y in range (5):    
        enemies.append(Actor('bug'))
        enemies [-1].x = 100 + 90 * x
        enemies [-1].y = 150 + 80 * y

# Color pallete
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

score = 0
direction = 1

music.play ("theme")

# Text
def draw_score ():
    screen.draw.text (str(score), (50, 30), fontname="arcade", fontsize=20)
    screen.draw.text ("Galagar 2023", (370, 20), fontname = "arcade", color="orange", align ="center", fontsize = 40)

def on_key_down(key):
    if ship.dead == False:
        if key == keys.SPACE:
            sounds.lazer.play()
            bullets.append (Actor('bullet'))
            bullets[-1].x = ship.x
            bullets[-1].y = ship.y - 55 # sets starting y of bullet
                
def update ():
    global score
    global direction
    
    # keyboard maping
    if ship.dead == False:
        if keyboard.left:
            ship.x -= 5
            if ship.x <= 0:
                ship.x = 0
                
        elif keyboard.right:
            ship.x += 5
            if ship.x >= WIDTH:
                ship.x = WIDTH
        
    for bullet in bullets:
        # remove un needed bullets
        if bullet.y < -20:
            bullets.remove (bullet)
        else:
            bullet.y -= 10
    
    moveDown = False        
    
    if len (enemies) > 0 and (enemies [-1].x > WIDTH-80 or enemies[0].x <80):
        moveDown = True
        direction = direction*-1
    
    for enemy in enemies:
        enemy.x+= 5*direction # Slide rate
        
        if moveDown == True:
            enemy.y += 25  # Drop rate orig:75
        
        if enemy.y > 1000: # Wraps them back to the top
            enemy.y = 100    
        
        # Test for bullet collision
        for bullet in bullets:
            if enemy.colliderect (bullet):
                sounds.explosion.play ()
                score += 150
                bullets.remove (bullet)
                enemies.remove (enemy)
        
        if enemy.colliderect(ship):
            # sounds.explosion.play()
            # enemies.remove (enemy)
            ship.dead = True
    
    # Player regeneration
    if ship.dead:
        ship.countdown -=1
    if ship.countdown == 0:
        ship.dead =False
        ship.countdown = 1000
            
def draw():
    screen.clear()
    screen.fill (BLACK)
        
    for bullet in bullets:
        bullet.draw()
        
    for enemy in enemies:
        enemy.draw()
    
    if ship.dead == False:    
        ship.draw()
    
    draw_score()
    
pgzrun.go ()