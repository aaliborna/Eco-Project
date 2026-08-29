# 📈 Supply & Demand 1.0

### A Simple Economic Market Simulator

## Why I Built This

While learning Python and Object-Oriented Programming, I wanted to build something that was more than a calculator.

Instead of creating another "guess the number" game or a simple to-do list, I decided to model one of the most fundamental concepts in economics:

> **How prices emerge from the interaction of supply and demand.**

The purpose of this project is not to create a perfect economic model.
Its purpose is to explore how programming can be used to represent real-world systems.

---

# Project Goals

* Practice Python fundamentals.
* Learn Object-Oriented Programming through a real project.
* Separate logic from visualization.
* Model a simple market mathematically.
* Build a foundation that can grow into a larger simulator.

---

# Project Structure

```
project/
│
├── market.py
│   Economic calculations
│
├── visualization.py
│   Graph generation using Matplotlib
│
├── main.py
│   User interaction
│
└── explanation.md
```

The project follows a simple separation of responsibilities:

* **Market** handles economics.
* **Visualization** handles graphics.
* **Main** connects everything together.

---

# Economic Model

Demand:

```
Qd = a - bP
```

Supply:

```
Qs = c + dP
```

The equilibrium price is calculated by solving:

```
Qd = Qs
```

which gives

```
P = (a - c) / (b + d)
```

The equilibrium quantity is then calculated using the demand equation.

---

# Features

✅ Supply Function

✅ Demand Function

✅ Parameter Validation

✅ Valid Economic Domain Detection

✅ Equilibrium Price

✅ Equilibrium Quantity

✅ Market Analysis

✅ Price Analysis

✅ Supply & Demand Visualization

✅ Equilibrium Point Highlighting

---

# Design Philosophy

This project intentionally separates different responsibilities.

The economic model knows nothing about graphs.

The visualization module knows nothing about economic formulas.

The main program only coordinates communication between them.

This makes the code easier to understand, maintain, and expand.

---

# What I Learned

Building this project helped me understand much more than Python syntax.

I learned how to:

* design classes
* organize code into modules
* validate user input
* use dictionaries to structure data
* visualize mathematical models
* debug unexpected behavior
* think about software architecture before writing code

Perhaps the most important lesson was realizing that programming is not just writing code.

Programming is designing systems.

---

# Future Improvements

Some ideas for future versions include:

* Multiple markets
* Taxes and subsidies
* Price ceilings and price floors
* Elasticity analysis
* Consumer and producer surplus
* Dynamic market simulation over time
* Interactive graphical interface
* Data export
* Scenario comparison

---

# Final Note

This project was built as a personal learning journey.

Every feature was implemented step by step, with an emphasis on understanding *why* each component exists rather than simply making the program work.

I hope this project demonstrates not only my interest in computer science, but also my curiosity about using programming to model complex real-world systems.
