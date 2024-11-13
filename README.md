# The Path to Camelot

Well met, Traveler! You are Rowan the Swift. Your mission, should you choose to accept it, is to find the magical healing elixir in the city of Camelot. It's imperative that you are quick about it because the King's daughter's life is at stake. Along the way, you will have the opportunity to pick up coins and healing potions to boost your health stats. Various scoundrels and thieves from Avalon will try to thwart you, but you mustn't let them. 

To win, you must get the elixir to the King within a 10 minute time frame with at least 10 HP. Do try not to die, young knight.

## Milestones

1. Scene
2. Characters
3. Objects
4. Walls
5. Labels and buttons
6. Instructions screen
7. Win screen

## Timeline

- 11/19 Basic scene with basic characters
- 11/22 Objects
- 11/25 Walls
- 12/2 Labels and Buttons
- 12/5 Instructions screen
- 12/9 Walls

__Stretch Goals:__

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

### Character Class

Defines what a "character" is. Can either be defining an enemy or Rowan the Swift.

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

#### Initializing

Sets image for characters. Sets position and how the character moves within the game scheme. 

Calls the attributes and assigns them to be public. Defines dx and dy, should move 3 pixels per frame. 

#### Process Method

If left arrow key pressed, character moves in negative x direction. If right arrow key pressed, character moves in positive x direction. 

If up arrow key pressed, character moves in negative y direction. If down arrow key pressed, character moves in positive y direction.

If space bar is pressed, check if character collideswith an enemy. If so, call fight method. 

If "a" pressed, check if character collideswith an object. If so, call pickUp method. 


#### Fight Method

#### Pick Up Method

### Objects Class
### Scene Class
### Labels
### Game Class
### Instructions
