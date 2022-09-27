1. File Explainations:
    1. The .png files are the images that are displayed while the game is playing
    2. The .mp3 files are the sounds that are played while the game is playing
    3. probability.txt: The main probability file that shows the probability of making a
    fieldgoal and updates after each kick.
    4. Project.py: The main game file

2. Project overview:
    My project is based on the Madden football game's field goal kicking. It tests timing of pressing
    the space bar in the desired spot on both the vertical distance meter and the horizontal direction
    meter. The best distance and direction is in the center (Green) and progressivly gets worse the
    farther you get from center with the worst being in the red. The game has a 1 player and 2 player
    option as well as a darkmode and sound options. The largest challenges I faced included getting the 
    meters bars to move, getting the game to register a make and a miss, and the overall flow of the 
    game through functions.

3. Commands:
    The game is easy to run by simply running the file. To progress throught the game, click the desired
    buttons. When on the kicking phases, press the space bar to set the meters and progress to the next
    kick.

4. Needed programs:
    The only needed programs are pygame

5. Inputs:
    The inputs that are necessary are the space bar and mouse clicks

6. Output files:
    The probability.txt updates after each kick and is the only output file

7. Sources:
    https://www.pygame.org/docs/tut/ChimpLineByLine.html: I used this source to help with the basics of
    pygame, it also helped with getting the characters to move.

    https://opensource.com/article/17/12/game-python-add-a-player I used this source to help creating
    classes in my game. I also progressed through the articles in the series to learn how to make a game.
    I used and motified some of example codes to make my game run.
