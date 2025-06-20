```
# 🪓 Word Guesser CLI Game

🎮 A fun terminal-based Hangman game written in Python!  
Guess the secret word one letter at a time while avoiding the hangman drawing. With multiple difficulties, colored feedback, and replay options — it’s the OG game with a Gen Z glow-up.

---

## 🧠 How It Works

- The game picks a random 5-letter word.
- You choose your **difficulty**:
  - Easy: 8 attempts
  - Medium: 6 attempts (default)
  - Hard: 4 attempts
- Guess letters one at a time.
- You lose an attempt on every wrong guess.
- The hangman stick figure updates with each wrong attempt.
- You win by guessing the full word before the drawing completes.

---

## 🎯 Features

✅ 150+ Word Bank  
✅ Difficulty Levels (Easy, Medium, Hard)  
✅ Hangman Stick Figure Drawing  
✅ Color-coded terminal output  
✅ Replay without restarting  
✅ Used letter tracker  
✅ Input validation and feedback

---

## 🛠️ Setup

1. **Clone the repo**:
```

git clone [https://github.com/yourusername/hangman-cli.git](https://github.com/bhutamanav11/word_guesser.git)
cd word_guesser

```

2. **Run the game**:
```

python hangman.py

```

✅ No extra libraries needed – pure Python!

---

## 🧩 File Structure

```

hangman-cli/
├── word_guesser.py     # Main game logic
├── README.md      # You're reading it ;)

```

---

## 📸 Sneak Peek

```

🎯 Welcome to Hangman!
Current Word: \_ \_ \_ \_ \_
Guess a letter: e
✅ Great Guess!
📜 Letters used: e

```
 _______
|/      |
|      (_)
|      \|/
|       |
|      / \
|
|___
```

```

---

## 🚀 Future Upgrades (PRs Welcome!)

- Word hints or categories
- Full word guessing (Wordle-style)
- Scoreboard / win streak tracker
- Web version using Flask or React

---

## 🧑‍💻 Author

Made with 💻 by [Manav Bhuta](https://github.com/bhutamanav11)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
```
