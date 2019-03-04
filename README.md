# Connect4
Play connect 4 against some depth first search oriented AI! Be warned, there's twist: every 10 turns a random piece is removed from the board.

## Report

Three trials were carried out for each AI. Blue always represents the AI the statistics correspond to. Red always represents the control group, which is a 'Defense AI' that blocks three in a rows.

### Intelligent Agent Pattern

|     Items    	|                                    Implementation                                    	|
|:------------:	|:------------------------------------------------------------------------------------	|
|  Environment 	| Connect4 board                                                                       	|
|     Agent    	| <ul> <li>Random</li> <li> Defense </li><li> Defense Agro </li><li> Mobile Defense Agro </li><li> DFS </li></ul>|
|     Sensors    	| <ul> <li>Variations of three in a row</li> <li> Mobile moves </li><li> Depth (for dfs) </li><li> Four in a rows </li></ul>|
|  Percepts 	| Placeable columns on the board                                                                       	|
|  Actuators 	| An individual columns total score                                                                       	|
|  Actions 	| Add or remove a piece from the board                                                                       	|

### AI Types
- **Defense** - Blocks three in a rows, otherwise uses random moves.
- **Defense Agro** - Blocks three in a rows and forces a win if it has a three in a row, otherwise uses random moves.
- **Mobile Defense Agro** - Blocks three in a rows and forces a win if it has a three in a row, otherwise places pieces in the most mobile locations i.e. locations that open up the most options for future moves.
- **DFS** - Generates moves to a specified ply depth using DFS. Each column is evaluated by minimaxing each ply with values generated from the mobile, defensive, and aggressive methods described in the above agents. 

### [Statistics](https://docs.google.com/spreadsheets/d/1WFtJvH4xyIPUyRgYX3VY5aSd5MTep_LCcQxXsL9Izck/edit?usp=sharing)
[![Statistics](stats3.PNG)](https://docs.google.com/spreadsheets/d/1WFtJvH4xyIPUyRgYX3VY5aSd5MTep_LCcQxXsL9Izck/edit?usp=sharing)

### Sample GUI Output

#### Version 1:

![asdfasdf](sampleOutput.PNG)


#### Version 2:


![TGUI](gui.PNG)


#### Notes
* The "Start AI Battle!" button only works when two AIs are matched against eachother.
* If you are a player, all you need to do to start playing is click a column on the board.
* Individual AIvAI games can be stepped through by clicking on the board instead of pressing the "Start AI Battle!" button.
* Blue goes first. Red goes second.

### Sample CLI Output

#### Mobile Defense Agro Output:

![CLI](sampleOutputCMD.PNG)


#### DFS Output:


![CLI](cliOutput2.PNG)

#### Notes
* ```CheckThreeInARow``` corresponds to the AI deciding to play defensively and block the player from winning.
  * The type of win the AI is blocking is specified directly above the ```CheckThreeInARow``` print out.
  * Example of blocking a vertical three in a row in column 5:
  ``` 
    vertical
    CheckThreeInARow: 5
  ```
* ```AGGRO``` corresponds to the AI making an aggresive move to advance its win condition
  * Example of the AI completing a four in a row in column 1:
  ```
    AGGRO: 1
  ```
* ```MOBILE``` corresponds to the AI placing a piece in a location with as many adjacent slots open as possible.
  * Example of the AI placing a mobile piece in column 3:
  ```
    MOBILE: 3
  ```
* ``` Column actuator->action evaluations ``` corresponds to the score of each column after the DFS agent has finished evaluating moves to the specified ply.
 * Example of a finished DFS evaluation (the maximum is chosen):
 ``` 
 Column actuator->action evaluations:  [4.333333333333329, 6.333333333333329, 6.333333333333329, 6.190476190476186, 76.19047619047628, 0, 4.333333333333329]
 DFS chose column: 4
 ```
  
### Bugs
  * Don't play as ```player``` for red team, its clunky.
  * The code is disgusting :)
  * Probably a lot more :D
