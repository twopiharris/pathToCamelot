# The Path to Camelot

Well met, Traveler! You are Rowan the Swift. Your mission, should you choose to accept it, is to find the magical healing elixir in the city of Camelot. It's imperative that you are quick about it because the princess's life is at stake. Along the way, you will have the opportunity to pick up healing potions to boost your health stats. Various scoundrels and thieves from Avalon will try to thwart you, but you mustn't let them. 

To win, you must get the elixir to the King within a 10 minute time frame with at least 10 HP. Do try not to die, young knight.

## Milestones

### Overall Idea Scheme

1. Scene
2. Characters
3. Objects
4. Walls
5. Labels and buttons
6. Instructions screen
7. Win screen

### Timeline

- 11/19 Basic scene with basic characters
- 11/22 Objects
- 11/25 Walls
- 12/2 Labels and Buttons
- 12/5 Instructions screen
- 12/9 Walls

### Stretch Goals
- Save and load functionality
- Levels

## Psuedocode

Main things I want in the game:

- Method to check if the character is within bounds of current tile
- Method to "pick up" objects
- Check if arrow keys, "a", or <SPACE> pressed
- How do attacks occur?
- Walls (ie, places characters can't walk)
- Win screen
- Varying difficulties with the enemies

### Character Module

Will be in module separate from gameplay. Defines what a "character" is. Can either be defining an enemy or Rowan the Swift.

Attributes:
- Name
- hitPoints 
  - Indicates the health status of the character
  - In terms of coding, it defines how much more damage the character can take
  - HP can go negative
- maxDamage
  - Indicates the maximum damage a character can deal to their opponent
  - maxDamage is greater than 0
  - maxDamage will not be the damage the character does everytime 
- hitChance
  - Indicates how likely the character is to hit the opponent
  - Is a percent
  - Integer between 1-100
- healingFactor
  - Indicates how likely the character is to heal between "hits"
  - Is a percent
  - Integer between 1-100
- maxHealing
  - Maximum amount a character can heal between hits
  - Greater than 0
  - maxHealing will not be the amount the character heals everytime
- armor
  - Does the character have any protection
  - Integer between 0 and 10

#### Initializing

Sets image for characters. Sets position and how the character moves within the game scheme. 

Calls the attributes and assigns them to be public. Defines dx and dy, should move 3 pixels per frame. 

#### Hit Method

Takes self and enemy. Generate a random number between 1-100. If number is less than or equal to hitChance, hit lands. After hit, generate damage using random integer between 1 and maxDamage. Subtract enemy armor from hit damage.

Generate random number between 1-100. If number is less than or equal to healingFactor, character heals. Generate healing using random integer between 1 and maxHealing. Subtract from hit damage. 

Subtract hitDamage from enemy hitPoints. Return enemy hitPoints. 

### Rowan Class

Initializes name and health stats of Rowan. Add image. Uses Character Module.

Initialize inventory. Inventory gets empty list. 

#### Process Method 

If left arrow key pressed, character moves in negative x direction. If right arrow key pressed, character moves in positive x direction. 

If up arrow key pressed, character moves in negative y direction. If down arrow key pressed, character moves in positive y direction.

If space bar is pressed, check if character collideswith an enemy. If so, call fight method. 

If "a" pressed, check if character collideswith an object. If so, call pickUp method. 

If "d" pressed, check if healing potion in inventory. If so, call heal method. 

#### Fight Method

For loop. Each time <SPACE> pressed, character1 hits character2 and character 2 hits character1. Get hitPoints. If hitPoints less than or equal to 0, character dies. Else, check for key press.

#### Pick Up Method

Append object to inventory list. 

#### Heal Method

Remove object from inventory and get healthAdd from object class. Add healthAdd to HP. 

### Enemy Class

Inherits from Character module. Randomize HP, healingFactor, hitChance, armor, and maxDamage. Sets image from list of enemy images.

### Potions Class

Calls simpleGE.sprite. Sets image. Sets position. Position will be random in game scheme. Sets healthAdd. healthAdd will be random integer from 0-5. 

### Elixir Class

Calls simpleGE.sprite. Sets image. Sets position. 

### Tile Class

Will be a tile based map. Plan will be shown in CSV file. Initialize list of images for tiles. Tile size is (32, 32). 

- Grass marked in map as 0
- The path marked as 1
- Water marked as 2
- Forest marked as 3
  
Default state is Grass.

#### Setting the State

Copy the image corresponding with the state. 

### Labels
### Game Class

Defines what the game behavior is. 

#### Initializing

Initialize simpleGE.scene. 

Initialize tileset. Tileset is empty list. Make constant defining rows. There will be 20 rows. Make constant defining the columns. There will be 40 columns. 

Define how many rows of the map will be on screen at once using constant. There will be 5 rows depicted at a time. Make constant defining the columns on a screen at a time. There will be 10 columns shown at a time. Define off row as 0. Define off column as 0. 

Add tileset to list of sprites. 

Call Rowan class. Assume default behavior. Add to list of sprites. 

Create empty list under "enemies". For loop, range 8. Call Enemy class. Assume default behavior. Add to list of enemies. Add to list of sprites. 

Create empty list under "potions". For loop, range 10. Call Potions class. Default behavior. Add to list of potions. Add potions to list of sprites. 

Call Elixir class. Assume default behavior. Add to list of sprites. 

#### Load Map Method

Make state system defining where each tile is in memory. Each tile will be 0, 1, 2, or 3. For each row in range of screen rows constant, append [] to the tileset. For each column, create a new tile and set the state. Set the x position to 16 + (32 * column). Set the y position to 16 + (32 * row). Tile x position gets the x position. Tile y position gets the y position. Append to the tileset row. 

#### Show Map Method

Shows a subset of the map. Subset is the screen rows and screen columns. For each row, and for each column, the current value is the self.map of the row + self.offRow times the column +self.offColum. Use to set the tileset state. 

#### Process Method

Check if left key pressed. Then check if self.offCol is greater than 0. If so, offCol gets subtracted by 1. 

Check if right key is pressed. Then check if self.offCol is less than the difference between the total columns and the screen columns. If so, add 1 to offCol. 

Check if up key is pressed. Then check if self.offRow is greater than 0. If so, subtract 1 from offRow. 

Check if down key is pressed. Then check if self.offRow is less than the difference between total number of rows and the screen rows. If so, add 1 to offRow. 

Call showMap(). 
### Instructions

