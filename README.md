# Scrabble Game

This project is a Python-based implementation of the popular Scrabble game. The game utilizes the `turtle` module for graphical rendering, the `pygame` module for sound, and JSON files for data handling.

## Features

1. **Dynamic Grid:**
   - A 15x15 grid of colored tiles is dynamically generated.
   - Each tile can hold a letter or remain empty.

2. **Player Interaction:**
   - Allows two players to input their names and take turns.
   - Players can place letters from their available "gotians" (pieces).

3. **Word Validation:**
   - Words are validated against a predefined dictionary (`game_data["words"]`).
   - Words can be checked horizontally, vertically, and in reverse.

4. **Scoring System:**
   - Each letter has a specific score, as defined in the game data.
   - Scores are displayed and updated in real-time for both players.

5. **Timer and Turns:**
   - A countdown timer is implemented to limit the time per turn.
   - Turns alternate between players after each valid or invalid move.

6. **Graphics:**
   - Custom visuals for the grid, tiles, and players' scores.
   - Dynamic drawing of pieces and letters on the grid.

7. **Game End:**
   - The game ends after a fixed number of turns (e.g., 10 turns).
   - Displays the winner and saves the final scores to a text file.

## Modules and Files

### Dependencies
- `turtle`: For graphical UI.
- `pygame`: For sound effects.
- `random`: For randomizing piece colors and letters.
- `json`: For reading and writing game data.

### External Files
- **`game_data.py`**: Contains predefined words and letter scores.
- **`graphics.py`**: Contains helper functions for drawing rectangles, text, and other graphical elements.
- **`player_data.json`**: Stores player progress and scores.
- **`example.txt`**: Outputs final scores after the game ends.

## How It Works

1. **Grid Initialization:**
   - The grid is drawn using the `turtle` module, with 225 tiles arranged in a 15x15 matrix.

2. **Player Setup:**
   - Players enter their names.
   - "Gotians" (pieces) are randomly assigned to each player.

3. **Gameplay:**
   - Players click on their pieces to pick a letter and place it on the grid.
   - Words are validated once the "Submit" button is clicked.
   - Scores are calculated based on the placed letters.

4. **Endgame:**
   - After 10 turns, the game declares the player with the highest score as the winner.
   - Results are saved to `example.txt`.

## Key Functions

### Initialization
- `gotians_value()`: Initializes pieces for players.
- `draw_user(i, score, name)`: Draws the player's name and score on the screen.
- `users_input()`: Captures user input for player names and letters.

### Gameplay Mechanics
- `search(x)`: Validates words on the grid in all directions.
- `undo1(id)` / `undo()`: Handles undo functionality for players' moves.
- `get_mouse_click_coor(x, y)`: Detects player clicks and updates the grid.

### Endgame
- `check(a)`: Determines the end of the game and declares the winner.
- `timer()`: Manages the countdown for each turn.

## How to Run
1. Install the required Python modules:
   ```bash
   pip install pygame
   ```

2. Ensure the following files are in the same directory:
   - `game_data.py`
   - `graphics.py`
   - `player_data.json`

3. Run the main Python script:
   ```bash
   python main.py
   ```

## Files Generated
- **`player_data.json`**: Stores the game progress, including scores and words formed.
- **`example.txt`**: Outputs the final scores of the players after the game ends.

## Future Enhancements
- **AI Player:** Add a single-player mode with AI.
- **Advanced Scoring:** Include multipliers for special tiles (e.g., double/triple word scores).
- **Dynamic Dictionary:** Allow players to use custom dictionaries.
- **Network Play:** Enable multiplayer gameplay over the internet.

---

Enjoy the game and challenge your vocabulary skills!

