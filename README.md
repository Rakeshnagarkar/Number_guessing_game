
# Number Guessing Game

This is a simple number guessing game where the player tries to guess a randomly chosen number between 1 to 100 within a limited number of attempts.


## How to Play

The game will look something like this:
```bash
   " 


'  .-./   ,--.,--. ,---.  ,---.  ,---.     ,-'  '-.|  ,---.  ,---.     ,--,--, ,--.,--.,--,--,--. 
|  | .---.|  ||  || .-. :(  .-' (  .-'     '-.  .-'|  .-.  || .-. :    |      \|  ||  ||        | 
'  '--'  |'  ''  '\   --..-'  `).-'  `)      |  |  |  | |  |\   --.    |  ||  |'  ''  '|  |  |  | 
 `------'  `----'  `----'`----' `----'       `--'  `--' `--' `----'    `--''--' `----' `--`--`--'  
Welcome To The Number Guessing Game!
I'm Thinking Of Number Between 1 to 100
pssst the correct answer is 5
Choose difficulty type 'hard or 'easy': 
```


1.Clone the repository or download the number-guessing-game.py file.

2.Install the art library by running the following command:


```bash
  pip install art
```
3.Run the game using the following command:

```bash
  python number-guessing-game.py
```

4.The game will welcome you and prompt you to choose a difficulty level: "easy" or "hard".

5.If you choose "hard", you will have 5 attempts to guess the number. If you choose "easy", you will have 10 attempts.

6.You will then be prompted to make a guess. Enter your guess as an integer.

7.The game will tell you if your guess is too high or too low.

8.Keep guessing until you either correctly guess the number or run out of attempts.

9.If you correctly guess the number, you win the game! If you run out of attempts, you lose.

10.You will then be prompted to play again. If you choose "yes", the game will start again with a new randomly chosen number. If you choose "no", the game will end.

Have fun playing!

## Design

The number guessing game code is designed around a single function, 'play_game()', which encapsulates the entire game. The game starts with a welcome message and a logo created using the 'art' library. A random number is chosen from a range of possible numbers using the 'random.choice()' function, and the game's difficulty is set based on user input. The game's main loop is a 'while' loop that checks the user's guess against the chosen number and adjusts the number of chances remaining accordingly. The game ends when the user correctly guesses the number or runs out of chances. The code is well-structured and easy to read, with the use of functions, loops, and conditional statements making it clear what the code is doing at each step. The game's difficulty level and number of chances are customizable, making it easy to adjust the game's difficulty.

## Libraries/Tools

I imported ‘random’ to implement shuffling of numbers. Python is my language of choice because I'm extremely comfortable in the environment and it is highly readable
