# The Dungeon
The princess P has been imprisoned in the bottom-right corner of a dungeon. The dungeon consists of M row, N column(M x N). Knight K initially positioned in the top-left room and must rescue the princess. The knights has the chance to remove one or more obstacles, 
what is the shortest path for the knight to reach and save the princess.

## Input:
* The input of your program is a file containing the floor map of the dungeon.
* The number of obstacles that you will remove. (optional)
* The search algorithm to be used [ BFS, A* ]

Dungeon’s floor map: The floor is a square grid world. Every cell in a grid is either free, or occupied 
by an obstacle. First line of the file containing the (M x N) dungeon map, which are two integers. Every other line in the map contains the coordinates of an obstacle. Numbers in the pair are separated by 
space. The top left room of the floor is (0, 0) and the bottom right room is (m - 1, n - 1).  

*Example of a map file*
```
5 3
1 0
1 1
3 1
3 2
```

## Output: 
The minimum number of steps to walk from the top left room (0, 0) to the bottom right room (m - 1, n - 1)
#### Example 1
```
Input:
Dungeon’s floor map file = 
5 3
1 0
1 1
3 1
3 2
Obstacle to remove = 1
Output:
Steps taken when when 0 obstacle removed = 10. 
(0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (2,1) -> (2,0) -> (3,0) -> (4,0) -> (4,1) -> (4,2) ->
Steps taken when when 1 or less obstacles removed = 6. 
(0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2)
```

### Example 2
```
Input:
Dungeon’s floor map file = 
5 3
0 1
0 2
1 0
1 1
1 2
2 1
Obstacle to remove = 1
Output: 
There is no availble path consider removing more obstacles: when  obstacles removed 0

Steps taken when 1 or less obstacles removed = 6
(0,0) -> (1,0) -> (2,0) -> (3,0) -> (3,1) -> (3,2) -> (4,2) ->
```

# How to run GUI
## Using exe
go to dist\Game.exe double click it or from console starting at the root `Ai-Course`
```
TheDungeons\dist\Game.exe
```
The data files that are available:
```
data/test.txt
data/test2.txt
data/test3.txt
data/test4.txt
data/a.txt 
```
## From source code directly 
starting from the `TheDungeons` folder
```
python -m venv venv
venv\Scripts\activate
pip intsall -r requirements
python Game.py
```

# How to run Console
starting from the `TheDungeons` folder
```
python -m venv venv
venv\Scripts\activate
pip intsall -r requirements
python run.py
```
