#  ⚽ Breakout Game

This project is a classic **Breakout** game built using HTML5 Canvas and JavaScript. The objective is to break all the bricks using a ball without losing all your lives.

## 🎲 How to Play

- Move the paddle left or right to bounce the ball and break the bricks.
- Clear all the bricks to win the game.
- The game ends when you lose all your lives.

### 🎮 Controls
- **Left Arrow Key**: Move paddle left
- **Right Arrow Key**: Move paddle right
- **Mouse Movement**: Move the paddle based on mouse position.

## 🚀 Features

- **Bricks and Collision Detection**: The game features multiple rows and columns of bricks. When the ball collides with a brick, the brick disappears and the score increases.
- **Score and Lives**: The score is displayed on the canvas. You start with 3 lives, and each time the ball passes the paddle, you lose a life.
- **Win Condition**: Break all bricks to win the game. If the ball misses the paddle three times, the game is over.

## 📁 Files

- **`index.html`**: The HTML structure for the game.
- **`breakout.js`**: Contains the game logic and rendering using the canvas API.
- **`breakout.css`**: Provides the styling for the canvas and the layout.
- **`breakout_bg.png`**: Background image for the game canvas.

## 🖥️ Installation

To run the Breakout Game locally, follow these steps:

1. **Clone the repository**:
   Open your terminal and run the following command to clone the project to your local machine: 


```bash 
git clone https://github.com/your-username breakout-game.git
```

2. Navigate to the project directory: After cloning, change into the project's directory:
```bash
cd breakout-game
```

3. Open the game: Simply open the index.html file in your web browser to start playing:

- For Windows, double-click on the index.html file.
- For macOS or Linux, you can open the file using this command:
```bash
open index.html       # For macOS
xdg-open index.html   # For Linux
```

## 📌 License

This project is open-source and available under the MIT License.
