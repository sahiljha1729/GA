# Evolving String — Genetic Algorithm Simulator

A interactive visualizer for a Genetic Algorithm written in Python and Flask. The app takes a target string input and attempts to "evolve" a 
population of randomly generated characters until they match the target phrase, simulating natural selection in real time.

---

##  What I Built & Implemented

* **Core GA Engine:** Written from scratch in Python (`app.py`), using object-oriented `DNA` classes to manage gene structures, crossover logic, and mutation logic.
* **Non-Linear Fitness Scaling:** Implemented exponential fitness scaling ($\text{fitness}^2$) when generating the mating pool. This gives stronger
* candidates a significantly higher probability of passing down genes while maintaining enough genetic diversity to prevent early stagnation.
* **Custom Dynamic UI:** Designed a responsive, side-by-side dark layout with CSS Grid/Flexbox so parameters can be tweaked on the left while
* generation-by-generation output logs (best string, fitness %, and average fitness) update in a scrollable table on the right.
* **Full-Stack Web Server:** Wrapped the raw algorithm inside a lightweight Flask backend to handle form submissions, state management, and real-time generation rendering.

---

##  Algorithm Breakdown

1. **Population Initialization:** Generates a initial array of $N$ random strings matching the length of the target string using character sets (letters + spaces).
2. **Fitness Scoring:** Evaluates each candidate by counting exact character matches against the target phrase:
   Fitness = matching characters/total length
3. **Selection Pool:** Uses fitness squaring to populate a mating pool, heavily favoring top performers for reproduction.
4. **Crossover:** Performs single-point crossover between two parents chosen from the pool to create offspring.
5. **Mutation:** Iterates through child genes and replaces characters with random ones based on the user-defined mutation rate to explore new search space and avoid local optima.

---

##  Project Structure

GA/
├── static/
│   └── styles.css       # Custom dark theme & table layout
├── templates/
│   └── index.html       # Control panel & output dashboard
├── app.py               # Genetic Algorithm logic & Flask server
├── requirements.txt     # Dependencies for local setup & deployment
└── README.md
