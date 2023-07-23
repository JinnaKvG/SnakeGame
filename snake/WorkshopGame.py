import os.path
from os.path import join as join_path
from random import randrange

import pyglet

# Find directory of current module.
APPDIR = os.path.dirname(__file__)

window = pyglet.window.Window()
#label = pyglet.text.Label("Hello", x=10, y=20) 

def load_image(name):
    return pyglet.image.load(join_path(APPDIR, "..", name + ".png"))

green_image = load_image("green")
apple_image = load_image("apple")

snake_tiles = {}
for start in ["bottom","end","left","right","top"]:
    for end in ["bottom","end","left","right","top","tongue","dead"]:
            key= start + "-" + end
            image = load_image(join_path("snake-tiles", key))
            snake_tiles[key] = image

TILE_SIZE = 60

def direction (a, b):
    if b == "end":
        return "end"
    x_a, y_a = a
    x_b, y_b = b
    if x_a == x_b + 1:
        return 'left'
    elif x_a == x_b - 1:
        return 'right'
    elif y_a == y_b + 1:
        return 'bottom'
    elif y_a == y_b - 1:
        return 'top'
    else:
        return 'end'

class GameState:
    def draw(self):
        for coords, prev, next in zip(
            self.snake,
            ['end'] + self.snake[:-1],
            self.snake[1:] + ['end']
        ):
            x, y = coords
            before = direction(coords, prev)
            after = direction(coords, next)
            snake_tiles[before + '-' + after].blit(x=x *TILE_SIZE,
                            y=y * TILE_SIZE, 
                            width=TILE_SIZE,
                            height=TILE_SIZE)
            
            
        for x, y in self.food:
            apple_image.blit(x=x *TILE_SIZE,
                            y=y * TILE_SIZE, 
                            width=TILE_SIZE,
                            height=TILE_SIZE)
                            
    def move(self, dt):
        if not self.alive:
            return
            
        head = self.snake[-1]
        x, y = head 
        direction_x, direction_y = self.direction
        new_x = x + direction_x
        new_y = y + direction_y
        new_head = new_x, new_y
       
        if new_head in self.snake:
            self.alive = False
        elif new_x < 0:
            self.alive = False
        elif new_y < 0:
            self.alive = False
        elif new_x >= window.width // TILE_SIZE:
            self.alive = False
        elif new_y >= window.height // TILE_SIZE:
            self.alive = False

        if new_head in self.food:
            #consume the food
            self.food.remove(new_head)
            game.add_food()
        else:
            # Did not eat; remove the tail tile
            del self.snake[0]
            
        self.snake.append(new_head)
 
 
    def add_food(self):
        for i in range (100):
            new_x = randrange (window.width // TILE_SIZE)
            new_y = randrange (window.height // TILE_SIZE)
            new_coords = new_x, new_y
            if not (new_coords in self.snake or new_coords in self.food):
                self.food.append (new_coords)
                return
 
game=GameState()
game.snake = [(1,2),(2,2),(3,2),(3,3),(3,4),(3,5),(4,5)]
game.food = []
game.add_food()
game.add_food()
game.add_food()
# removed: game.move()
game.direction = + 1,0 #to the right
game.direction = 0, +1 #up
game.alive = True

@window.event
def on_key_press(key_code, modifier):
    if key_code == pyglet.window.key.UP:
        game.direction = 0, +1
    elif key_code == pyglet.window.key.DOWN:
        game.direction = 0, -1
    elif key_code == pyglet.window.key.LEFT:
        game.direction = -1, 0
    elif key_code == pyglet.window.key.RIGHT:
        game.direction = +1, 0


@window.event
def on_draw():
    window.clear()
    game.draw()
    
pyglet.clock.schedule_interval(game.move, 1/5)

pyglet.app.run()
