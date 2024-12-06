# Cannon Shooter Game

## Description

Cannon Shooter is an action-packed arcade game built using Python and Pygame, where you control a cannon to shoot down falling enemies and avoid getting hit. The game features a level system, power-ups, and shield mechanics to enhance gameplay. You can choose from multiple player models and track your progress with a score, level, and lives system.

## Features

- **Multiple Player Models**: Choose from various cannon models.
- **Random Backgrounds**: Enjoy a dynamic game experience with random background images.
- **Enemies and Bullets**: Shoot bullets at falling enemies (spheres).
- **Power-ups**: Collect power-ups that activate a shield to protect you.
- **Score and Level System**: Track your progress with a score and level system. The game gets more challenging as you advance to higher levels.
- **Pause Functionality**: Pause and resume the game at any time by pressing 'P'.
- **Game Over**: The game ends when you lose all your lives.

## Installation

### Prerequisites

- **Python 3.x**: Make sure you have Python 3.x installed on your machine. You can download it from the official [Python website](https://www.python.org/downloads/).
- **Pygame**: This game uses Pygame for graphics and sound. Install it by running the following command:

```bash
pip install pygame
```

### Cloning the Repository

1. Open your terminal or command prompt.
2. If you don't have the repository yet, you can clone it by running the following command (replace the URL with your repository URL if needed):

```bash
git clone https://github.com/Manuella-R/cannon-shooter-game.git
```

3. Navigate to the directory where the game is cloned:

```bash
cd cannon-shooter-game
```

### Setting Up the Game

1. **Assets**: The game requires several assets (such as images and sounds). Make sure to have the following folder structure in your game directory:

    ```
    cannon-shooter-game/
    ├── player/
    ├── enemies/
    ├── damage/
    ├── background/
    ├── shot.wav
    ├── grenade.wav
    ├── cannon_shooter_game.py
    └── README.md
    ```

    - The **player/** folder should contain images of different cannon models.
    - The **enemies/** folder should contain images of enemy spheres.
    - The **damage/** folder should contain images for the explosion effects when enemies are destroyed.
    - The **background/** folder should contain images for random backgrounds.


2. **Set up images and sounds**: If you don’t have the assets already, you can create or download suitable images and sounds. Place them in their respective folders.

### Running the Game

Once everything is set up, you can run the game using Python.

1. In your terminal, navigate to the directory where the game files are located.
2. Run the game with the following command:

```bash
python cannon_shooter_game.py
```

This will launch the game window where you can start playing.

Alternatively, under the Code section in the repository, download the zipped folder containing the project files and run it on preferred IDE

## Game Controls

- **Arrow Keys**: Move the cannon left and right.
- **Spacebar**: Fire bullets.
- **'P' Key**: Pause and resume the game.
- **'S' Key**: Start the game from the intro screen.
- **'E' Key**: Exit the game from the intro screen.

## Code Explanation

### Main Components:

1. **Intro Screen**:
    - Displays the game title and options to start or exit the game.
    - Press 'S' to start and 'E' to exit.

2. **Model Selection**:
    - Choose your player cannon model before starting the game.
    - You can select a model by pressing the corresponding number key (1-5).

3. **Gameplay**:
    - **Cannon Movement**: Use the left and right arrow keys to move the cannon horizontally across the screen.
    - **Bullet Firing**: Press the spacebar to shoot bullets from the cannon.
    - **Enemy Spheres**: Spheres fall from the top of the screen, and your goal is to shoot them for points.
    - **Power-ups**: Occasionally, power-ups will appear, and you can collect them to activate a shield that protects you from one enemy hit.
    - **Levels and Difficulty**: The game gets more difficult as you progress through levels. As your score increases, the level will automatically increase, and the enemies will fall faster.

4. **HUD (Heads-Up Display)**:
    - The game displays the current **lives**, **score**, **level**, and a message indicating if the **shield is active** on the top of the screen.
  
5. **Pause/Resume**:
    - Press 'P' to pause the game. When the game is paused, it displays a "PAUSED" message. Press 'P' again to resume.

6. **Game Over**:
    - The game ends when you lose all your lives. A "GAME OVER" message will be displayed, and the game will wait for a few seconds before closing.

### Level and Score System:

- **Score**: Every time you destroy an enemy sphere, you earn 10 points.
- **Level Progression**: The game increases in difficulty as you progress through the levels. The number of spheres increases and their speed increases as well.
- **Level Up**: The level increases when your score reaches 100 times the current level. For example, at level 1, you need 100 points to reach level 2, and at level 2, you need 200 points to reach level 3, and so on.


## Screenshot and Gameplay
**Here is a screenshot of the game**:
![Screenshot 2024-12-06 042915](https://github.com/user-attachments/assets/77b683d0-721f-489b-8420-6eb237283f2d)


## Power-ups and Shield:

- **Power-ups**: Occasionally, a power-up will appear on the screen. If the cannon collides with the power-up, it activates a shield.
- **Shield**: The shield protects you from one enemy hit for 5 seconds. When the shield is active, a "SHIELD ACTIVE" text will appear on the screen.


## Tips for Contributing

- If you'd like to contribute to the game (e.g., adding new features, fixing bugs), feel free to fork the repository and create a pull request.
- Ensure that any changes are well-tested and documented.


