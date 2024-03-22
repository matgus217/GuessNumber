# GuessNumber

Guess The Number is a python terminal game. Users play against the computer by guessing a number that the computer randomly has chosen. The player can also decide a number and let the computer guess it. 

LINK TO HEROKU

## How to play

 The computer will ask the user to guess a number between 1 and 20, if the user guess a number that is too high the computer will print "Sorry you guessed too high, guess again!". If the user guess a number that is too low, the computer will print "Sorry you guessed too low, guess again!". If the user guess the right number the computer will print "Woho you guessed correct, it was (number)!"

The user can also decide a number and let the computer guess it. The computer will print out "Is (number) too low(L), too high(H), or right(R)?" and the user can choose to press "L" if it is too low, "H" if it is too high or "R" if the number the computer guessed is right. When the computer guesses right the frase "The computer guessed your number, (number)!" will print and the game is over. 

## Features

### Existing features

#### User guessing the number

- The computer will ask the user to enter a name, then greets the user by that name and the game starts

![name](https://github.com/matgus217/GuessNumber/assets/147818054/5a914d13-bc2e-4973-9668-73771b21c553)


- The computer asks the user to guess a number between 1 and 20

![guess](https://github.com/matgus217/GuessNumber/assets/147818054/e83ff616-48f0-4552-9f5c-776f0b81cebd)


- If the user guesses anything else than a number, a message prints that tells the user to only enter numbers.

![numberOnly](https://github.com/matgus217/GuessNumber/assets/147818054/9244868e-d02d-4f08-b796-e65c70b894da)


- The computer print different answers if the user guessed too low, too high or right.

![High or low](https://github.com/matgus217/GuessNumber/assets/147818054/7fd28ace-e65a-4338-9ba1-36754319b583)


- The computer print a message that tells the user that the guess was right.

![correct](https://github.com/matgus217/GuessNumber/assets/147818054/0f40de36-e367-4fec-ae2a-a06f48fb6511)


#### The computer guessing the number

- When the user guessed right, it's the computers turn to guess. A message prints that easily explains for the user how it is going to work.

![computerTurn](https://github.com/matgus217/GuessNumber/assets/147818054/079ebf5a-5ac2-40fe-9a51-84ea691b01c4)


- The computer prints a message asking the user if the number is too low, too high or right. The user press a key (L/H/R).

![computerAsking](https://github.com/matgus217/GuessNumber/assets/147818054/1ba457f5-a988-4a99-9094-8d058002d229)


- When the computer guesses the right number a message prints.

![computerCorrect](https://github.com/matgus217/GuessNumber/assets/147818054/ab67009b-528b-49f8-b7b6-d6e24a7ae1bf)


### Features left to implement
- I would like to set a limit of tries when the user guesses against the computer. It will make the game a bit harder. I did not have the time for that now.

## Data model

As data model i used three functions that stores everything that is needed to run the game such as:
- Print methods that prints out what is happening in the game.
- A user_guess variable that contains the users guesses against the computer.
- A response variable that contains the users answer when the computer is guessing.

## Testing

I have tested the code through a PEP8 linter and confirmed that there are no problems or errors.

![test](https://github.com/matgus217/GuessNumber/assets/147818054/c09843e9-6e6d-4cf6-b40d-eb3fc2f633dc)


### Bugs
There are no bugs.

## Deployment

The project was deployed using Code Institute's moch terminal for Heroku.

Steps I followed for deployment:
- I cloned the repository
- I created a new Heroku app 
- I set the buildpacks to Python and NodeJS
- I linked the Heroku app to the repository
- I clicked on Deploy

## Credits

- I searched the internet for ideas for this project and and I learned alot from [GeeksForGeeks](https://www.geeksforgeeks.org/python-programming-language/)
- I've been watching Code Institute's videos for Python Essentials[CodeInstitute](https://learn.codeinstitute.net/courses/coursev1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/071036790a5642f9a6f004f9888b6a45/?child=first)

