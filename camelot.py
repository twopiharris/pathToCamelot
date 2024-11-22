"""Marianne Adams
CS120
Path to Camelot"""
import pygame, simpleGE, camelotCharacter
    
class Tile(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
#         self.size = (15, 15)
        self.images = [pygame.image.load("grass.png"),
                       pygame.image.load("path.png"),
                       pygame.image.load("water.png"),
                       pygame.image.load("forest.png")]
        self.setSize(32, 32)
        self.stateName = ["grass", "path", "water", "forest"]
        self.GRASS = 0
        self.PATH = 1
        self.WATER = 2
        self.FOREST = 3
        self.state = self.GRASS
    
    def setState(self, state):
        self.state = state
        self.copyImage(self.images[state])
    
class Rowan(simpleGE.Scene, camelotCharacter.Character):
    def __init__(self, scene):
        super().__init__(scene)
        self.rowan = self.Character("Rowan", 20, 25, 3, 10, 2, 5)
        self.image = pygame.image.load("Rowan.png")
        self.x = 1
        self.y = 2
        self.dx = 2
        self.dy =2
        self.inventory = []
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.dx
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.dx
        if self.isKeyPressed(pygame.K_UP):
            self.y -= self.dy
        if self.isKeyPressed(pygame.K_DOWN):
            self.y += self.dy
        if self.isKeyPressed(pygame.K_a):
            if self.collideswith(potion):
               self.pickUp()
        if self.isKeyPressed(pygame.K_SPACE):
            if self.collideswith(enemy):
                self.fight()
        if self.isKeyPressed(pygame.K_d):
            if potion in inventory:
                self.heal()
    def fight(self):
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setCaption("The Path to Camelot")
        self.tileset = []
        
        self.ROWS = 20
        self.COLS = 40
        
        self.SCREEN_ROWS = 10
        self.SCREEN_COLS = 10
        
        self.offRow = 0
        self.offCol = 0
        
        self.loadMap()
        
        self.sprites = [self.tileset]
        
    def loadMap(self):
        self.map = [
    [1,0,0,0,0,0,0,0,0,0,0,2,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,0,0,0,0,0,0,0,0,0,2,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,0,0,0,0,0,2,1,0,1,0,3,3,3,3,0,0,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,1,1,1,1,1,1,1,0,0,2,1,1,1,0,3,3,3,3,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1],
    [0,0,1,0,0,0,1,1,1,1,1,1,1,0,0,0,3,3,3,3,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1],
    [0,0,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1],
    [0,0,1,0,3,3,3,0,0,0,2,2,1,2,2,2,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1],
    [0,0,1,0,3,3,3,3,3,2,2,0,1,3,3,2,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,2,3],
    [0,0,1,0,3,3,3,3,2,2,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,2,3],
    [0,0,1,0,3,3,3,2,2,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,2,2,2,2,2,3],
    [0,0,1,0,3,3,2,2,0,0,0,0,1,0,3,2,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,2,2,0,0,0,0,3],
    [0,0,1,0,3,2,2,0,0,0,0,0,1,0,3,2,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
    [0,0,1,0,2,2,0,0,0,0,0,0,1,0,3,2,2,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,2,2,0,0,0,0,1,3],
    [0,0,1,2,2,1,1,1,1,1,1,1,1,0,3,3,2,1,2,3,3,3,3,3,1,0,0,0,0,0,2,2,2,0,0,0,0,0,1,3],
    [0,0,1,2,1,1,3,1,0,0,0,0,1,0,3,3,3,1,2,2,3,3,3,3,1,0,0,0,0,2,2,2,2,2,0,0,0,0,1,3],
    [0,1,1,1,1,3,3,1,0,0,0,0,1,0,3,3,3,1,3,2,2,2,2,2,1,0,0,2,2,2,0,0,0,2,2,2,0,0,1,3],
    [1,1,2,3,3,3,3,1,0,0,0,0,1,0,3,3,3,1,3,3,2,2,2,2,1,2,2,2,2,0,0,0,0,0,0,2,2,0,1,2],
    [0,1,1,3,3,3,3,1,0,0,0,0,1,0,3,3,3,1,3,3,2,2,2,2,1,2,2,0,0,0,0,0,0,0,0,0,2,2,1,2],
    [0,2,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,3,3,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,2,1,3],
    [2,2,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3]
]
        for row in range(self.ROWS):
            self.tileset.append([])
            for col in range (self.COLS):
                currentValue = self.map[row][col]
                newTile = Tile(self)
                newTile.setState(currentValue)
                xPos = 16 + (32 * col)
                yPos = 16 + (32 * row)
                newTile.x = xPos
                newTile.y = yPos
                self.tileset[row].append(newTile)
    
#     def showMap(self):
#         for row in range(self.SCREEN_ROWS):
#             for col in range(self.SCREEN_COLS):
#                 currentVal = self.map[row + self.offRow][col + self.offCol]
#                 self.tileset[row][col].setState(currentVal)
                
#     def process(self):
#         if self.isKeyPressed(pygame.K_LEFT):
#             if self.offCol > 0:
#                 self.offCol -= 1
#                 
#         if self.isKeyPressed(pygame.K_RIGHT):
#             if self.offCol < (self.COLS - self.SCREEN_COLS):
#                 self.offCol += 1
#         
#         if self.isKeyPressed(pygame.K_UP):
#             if self.offRow > 0:
#                 self.offRow -= 1
#         
#         if self.isKeyPressed(pygame.K_DOWN):
#             if self.offRow < (self.ROWS - self.SCREEN_ROWS):
#                 self.offRow += 1
#         
#         self.showMap()
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
