# Shortest Path Finder Using Dijkstra's Algorithm

## Project Overview

This project implements the Dijkstra's Algorithm to find the shortest path between two positions marked as **X** on a rectangular board. The program processes the board, calculates the path cost, and displays only the fields that belong to the shortest path.

---

## **Project Goal**

The goal of this project is to:

1. Develop a Python implementation of **Dijkstra's Algorithm**.
2. Solve a pathfinding problem on a grid where movement is restricted to horizontal and vertical directions.
3. Respect specific rules, such as zero-cost fields (`J`) and fields marked as start and end positions (`X`).
4. Provide modular, clean, and testable code.

---

## **Rules of the Board**

- **Numbers (0-9):** Represent the cost of entering a cell.
- **Letter `J`:** Represents fields with **zero cost** for entry and exit (special joker fields).
- **Letter `X`:** Represents the **start** and **end** positions for the algorithm.

The program:

- Finds the **least costly path** between two `X` positions.
- Hides all fields that are **not part of the shortest path**.
- Outputs the **total cost** of the path.

---

## Project Structure

The project follows a clean and modular structure:

```
graph/
│
├── main.py                # Entry point of the program
├── graph.py               # Implementation of Dijkstra's Algorithm
├── utils.py               # Utility functions (e.g., board loading)
│
├── plansze/               # Sample board files
│   ├── plansza1.txt
│   ├── plansza2.txt
│   └── plansza3.txt
│
├── tests/                 # Unit tests
│   ├── __init__.py
│   ├── tests_graph.py     # Tests for Dijkstra's algorithm
│   └── tests_utils.py     # Tests for utility functions
│
└── wyniki/                # Folder for program outputs (optional)
```

## How to Run the Project

### 1. Clone the Repository

Use Git to clone the repository:

```bash
git clone https://github.com/kat1478/shortest-path-finder.git
cd <shortest-path-finder>
```

### 2. Run the Program

Execute the program with a sample board file:

```bash
python3 main.py plansze/plansza1.txt
```

### Example Output

```
J11
  X
J
  X
J11
Cost: 3
```

The program:

- Displays only the shortest path.
- Hides all irrelevant cells on the board.
- Outputs the total path cost.

## Sample Boards

Sample board files are located in the `plansze/` directory. Here are a few examples:

### **plansza1.txt**

```
J112J
12X21
J041J
12X11
J111J
```

### **plansza2.txt**

```
J1111
12X21
J044J
22X11
J111J
```

### **plansza3.txt**

```
111X1
11111
J040J
11111
1X111
```

## How to Run Tests

Unit tests are located in the `tests/` directory. Use the `unittest` module to execute the tests:

### Run all tests for the algorithm and utilities:

```bash
python3 tests/tests_graph.py
python3 tests/tests_utils.py
```

### Expected Results:

- Tests should verify the correctness of the shortest path calculation.
- Tests handle edge cases, such as invalid boards or missing X positions.

## Requirements

- **Python 3.6+**
- No additional libraries are required.

## Author

- **Name**: Katarzyna Kadyszewska
- **GitHub Profile**: kat1478

## License

This project is licensed under the **MIT License**. Feel free to use and modify it as needed.

## Future Improvements

- Support for diagonal movement.
- Visualization of the board in a graphical interface.
- More extensive performance testing on larger boards.
