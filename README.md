# German Flashcards App

A desktop application built with Python and Tkinter designed to assist in learning German vocabulary. The app displays flashcards with dynamic text rendering, tracks words you have mastered, and automatically saves your learning progress locally using Pandas.

---

## Features

* **Timed Flip Mechanism**: Automatically displays the English translation after 3 seconds on a styled card canvas.
* **Persistent Word Tracking**: Automatically removes mastered words from your active study session and exports the updated queue to `data/words_to_learn.csv`.
* **Automatic Progress Fallback**: Loads existing progress from `words_to_learn.csv` if available, or falls back to the master list (`german_words.csv`).
* **Interactive UI**: Custom graphics for card state transitions and lightweight response buttons.

---

## Prerequisites

Ensure you have Python 3.x installed along with the `pandas` library:

```bash
pip install pandas
