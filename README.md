# Rock, Paper, Scissors Game

A simple Python implementation of the classic Rock, Paper, Scissors game. Play against the computer and see who wins!

## Features
- User-friendly interface with clear prompts
- Case-insensitive input handling (e.g., "rock", "ROCK", or "RoCk" all work)
- Input validation to ensure valid choices
- Descriptive win/loss messages (e.g., "Paper covers Rock")
- Random computer opponent choices

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
2. **Ensure Python is Installed**:
   - This game requires Python 3.x. Check your Python version:
     ```bash
     python --version
     ```
   - If Python is not installed, download it from [python.org](https://www.python.org/downloads/).

3. **No Additional Dependencies**:
   - The game uses only the standard `random` library, which comes with Python.

## Usage
1. **Run the Game**:
   ```bash
   python rock_paper_scissors.py
   ```
2. **Play**:
   - Enter your choice (`Rock`, `Paper`, or `Scissors`) when prompted.
   - The computer will randomly select its choice and display the result.
   - Invalid inputs will prompt you to choose a valid option.

   Example:
   ```
   Let's play Rock, Paper, Scissors!
   Enter your choice (Rock, Paper, Scissors): Rock
   My decision is Paper
   I win! Paper covers Rock.
   ```

## Code Structure
- `rock_paper_scissors.py`: The main
