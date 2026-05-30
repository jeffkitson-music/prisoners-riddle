# 🕵️‍♂️ The 100 Prisoners Riddle Simulator
Building the Prisoner's Riddle in Python. This project is based Veritasium's YouTube Video. 

<center>

[![Watch the video](https://img.youtube.com/vi/iSNsgj1OCLA/hqdefault.jpg)](https://www.youtube.com/embed/iSNsgj1OCLA)

</center>

## :books: About
This project simulates the famous [100 Prisoner's Problem](https://en.wikipedia.org/wiki/100_prisoners_problem) as proposed by Anna Gál and Peter Bro Miltersen. Using a looping strategy, the group's survival goes from virutally zero to about 31%. 

---

## 🧠 The Problem Setup
* **100 prisoners** are numbered 1 to 100.
* **100 boxes** are placed in a room, each containing a random number from 1 to 100 inside.
* Each prisoner goes into the room one by one and can open up to **50 boxes** to find their own number. They cannot communicate afterward.
* If **every single prisoner** finds their own number, they all go free. If even **one** fails, they are all executed.

### The Strategy
1. **Random Guessing:** If every prisoner picks 50 random boxes, they only have a 50% chance of finding their number. The mathematical odds of the whole group suriviving are virtually zero. It's $(\frac{1}{2})^{100}$. That's ~0.0000000000000000000000000000008%! Yikes!
2. **The Loop Strategy:** A prisoner opens the box labeled with their own number. They look at the card inside, and then open the box with *that* number. They repeat this loop until they find their number or run out of tries. Mathematically, that gives them a nearly 32% chance. While the odds still aren't with them, one in three is way better than the alternative!


## 🛠️ How to Run It

1. Clone the repository:
   ```bash
   git clone https://github.com/jeffkitson-music/prisoners-riddle.git
2. Run it in Python
   ```python
   python prisoners_riddle.py --games <number of simulations>

