# Machine learning project to cluster NBA players by how they score the ball on the floor.

## The Goal

The aim of this project is to use machine learning to better understand groups of basketball players based on what types of shots they attempt. Traditionally, players have been classified into 3 main positions: guard, forward, and center. Historically these positions were useful to infer how a player operates within the context of a game. However due to evolution of the game over the past 10 or so years, it has become more difficult to rely on these positions to determine how a player scores the ball on offense. I attempted to use clustering techniques to re-group players based on what types of shots they take, what distance they shoot these shots from, and their proficiency shooting these types of shots. 

## The Data

The National Basketball Association provides publicly available information on all game through their API. For the purpose of this project, I gathered box scores, advanced box scores, and shot specifi cdata from the 2017 season through the present (January 21, 2020). This data set includes data from:

* 3,000+ games
* 700+ players
* 540,000+ shots


I dropped players who do not average at least 5 shot attempts per game. 

## Features

For this project, I wanted to group players based on **bold how** they score on offense. The NBA tags every shot taken in a game with 46 different shot types. However, some of these shots are very similar to one another and using them to differentiate players would create unwanted variance between player groups. For example, there is not much difference between a "layup" and "driving layup". Plays like these are essentially the same thing. Therefore I grouped the NBA's 46 shot types into 8 broader categories which I felt best captured the essence of each offensive action. 
# insert graphic for groups
|Alley-oop|Dunk|Layup|Floater|Hook Shot|Created Jumper|Jump Shot|Rebound Shot|
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |

