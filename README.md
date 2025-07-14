# ⚫ Go-Game ⚪

In this project, the goal is to develop a program that allows two players to play the game of Go. The program will define a set of abstract data types to represent and manipulate the board and the stones placed by each player.

[Go](<https://en.wikipedia.org/wiki/Go_(game)>) is an abstract strategy board game for two players, originating in China over 2,500 years ago. Players take turns placing stones with the goal of surrounding more territory than their opponent.

## 🪨 Goban

The board of Go, also called **Goban** is a rectangular board typically composed of 19×19 lines that form a grid of intersections. Smaller boards of 13×13 or 9×9 are also common in beginner or fast-paced games.

### ➤ Intersection

Each intersection is uniquely identified by a capital letter from **A to S** (columns) and a number from **1 to 19** (rows). Two intersections are **adjacent** if they are directly connected horizontally or vertically (not diagonally) without any intersections in between.

All intersections are read left to right, bottom to top and they can be empty or occupied by stones placed by either player, white ⚪ or black ⚫.

### ➤ Chains

Two intersections are connected if it is possible to trace a path between them by moving only through adjacent intersections of the same type:

- all occupied by black stones,

- all occupied by white stones, or

- all empty.

A chain of stones is a group of one or more connected intersections occupied by stones of the same color.

### ➤ Liberties

The **liberties** of a stone are all the empty intersections that are adjacent to it. If the stone is part of a chain, its liberties include all the empty intersections adjacent to any stone in that chain.

### ➤ Territory

A **territory** is a maximal group of one or more connected empty intersections that are all connected to each other and not connected to any other empty intersections outside the group.

### ➤ Border

The **border** of a territory is the set of all intersections occupied by stones that are adjacent to the territory.

A territory is said to belong to a player if its border is occupied only by stones of that player's color.

## 🕹️ Game Rules

For this project, we will consider the following rules of the game Go:

1. **Start**: At the beginning of the game, the board is empty. The player with black stones plays first. Players alternate turns thereafter.

2. **Turn**: On their turn, a player can either pass or play. A player's move consists of the following steps (performed in order):

   - **Place**: Place a stone of their color on an empty intersection. Stones cannot be moved to another intersection after being played.
   - **Capture**: Remove any opponent's stones from the board that have no liberties.

3. **Illegal Moves**: The following restrictions must be considered when placing stones:

   - **Suicide**: A move is illegal if one or more stones of the player's color are left without liberties after the move is resolved.
   - **Repetition (ko)**: A move is illegal if it creates a board state that has occurred previously in the game after all steps of the move are completed.

4. **End and Scoring**: The game ends when both players pass consecutively. In the final board state, a player's score is the sum of the total number of intersections that:

   - belong to that player's territory.
   - are occupied by a stone of that player's color.

5. **Winner**: The player with the highest score is the winner. If both players have the same score, the white player wins.

---

## ⚙️ How to Run

### ✅ 1. Check Python Installation

Make sure you have **Python 3** installed. To verify, open your terminal or command prompt and run:

```bash
python3 --version
```

If Python is installed, this will show the version number. If not, you can download it [here](https://www.python.org/downloads/).

### ✅ 2. Start a Game

To start a game, add the following code to the end of the `FP2324P2.py` file:

```python
go(9, (), ())
```

This will start a 9x9 game with no initial stones. You can adjust the board size and initial stones as needed.

### ✅ 3. Run the Program

Once Python is installed and you have added the game initialization code, you can run the Go game using the following command:

```bash
python3 FP2324P2.py
```

### ✅ 3. Run the Tests (Optional)

This repository includes two test files: `test_private.py` and `test_public.py`.

➤ Install **pytest** (if needed):

```bash
pip install pytest
```

➤ Run the tests:

```bash
pytest test_private.py
pytest test_public.py
```

### ⚠️ Note on Private Tests

Some private tests in `test_private.py` have been commented out because they rely on external files that are not available in this repository.

## 📄 Project Description

You can find the full project description [here](https://github.com/maddie0120/go-game/blob/main/FP2324P2.pdf).
