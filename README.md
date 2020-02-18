# crosser
This game is designed as an assignment for Introduction to Software Systems Course.

## How to Play
Clone to repo and make sure pygame is installed on your local machine. Run the game.py file to play the game.

## Game Identity: 
Stylized two-player crosser game where the player completes levels by avoiding obstacles and crossing strips

## Genre:
The game is about two players competing to cross a space filled with pirate ships and spikes. Each player keeps playing turn by turn until they die; the winner is the one who crossed more obstacles in less time.

## Features: 
The score is calculated using the following formula: 

<pre>
Score = Points Accrued - Time taken(in microseconds)/1000<br/>

Points Accrued = +5 for crossing fixed obstacle<br/>
                 +10 for crossing moving obstacle </pre>

Difficulty level is increased for each player if he/she crosses the entire space without any collision by increasing the speed of moving obstacles.

## Interface: 
Controls: Player 1: UP_ARROW, DOWN_ARROW, LEFT_ARROW, RIGHT_ARROW
        Player 2: W, A, S, D

## References: 
Sounds for Level Completion and Collision have been taken from: https://themushroomkingdom.net/media/smb/wav
