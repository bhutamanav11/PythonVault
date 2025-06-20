import random
import time

word_bank = [
    'apple', 'beach', 'brain', 'brick', 'candy', 'chair', 'clean', 'cloud', 'crate', 'dance',
    'diary', 'drink', 'earth', 'email', 'fancy', 'field', 'flame', 'flash', 'floor', 'focus',
    'frame', 'fresh', 'ghost', 'glass', 'gloom', 'grass', 'great', 'green', 'grief', 'happy',
    'heart', 'honey', 'horse', 'house', 'human', 'jelly', 'jolly', 'juice', 'knife', 'knock',
    'laugh', 'light', 'lucky', 'magic', 'mango', 'metal', 'money', 'month', 'mouse', 'music',
    'night', 'ocean', 'olive', 'orbit', 'paint', 'paper', 'party', 'peach', 'phone', 'photo',
    'piano', 'plant', 'plate', 'power', 'pride', 'quiet', 'rainy', 'reach', 'ready', 'river',
    'robot', 'rocky', 'roomy', 'round', 'scarf', 'scope', 'sharp', 'sheep', 'shirt', 'shock',
    'short', 'shout', 'skate', 'smile', 'smoke', 'snack', 'solar', 'solid', 'sound', 'spice',
    'spicy', 'spine', 'spoke', 'sport', 'spout', 'spray', 'stack', 'stage', 'stare', 'steak',
    'steam', 'stone', 'store', 'storm', 'story', 'strap', 'straw', 'style', 'sugar', 'sunny',
    'sweet', 'sweat', 'swing', 'sword', 'table', 'taste', 'teach', 'teeth', 'thing', 'threw',
    'throw', 'tight', 'tiger', 'timer', 'toast', 'today', 'token', 'tooth', 'topic', 'torch',
    'total', 'touch', 'tower', 'trace', 'track', 'trail', 'train', 'treat', 'trend', 'tribe',
    'truck', 'trick', 'trophy', 'tulip', 'tutor', 'unity', 'urban', 'vapor', 'video', 'voice',
    'vowel', 'waste', 'watch', 'water', 'weird', 'whale', 'wheat', 'wheel', 'white', 'whole',
    'windy', 'witch', 'witty', 'world', 'worry', 'wrist', 'write'
]

hangman_stages = [
    """
     _______
    |/      |
    |
    |
    |
    |
    |
    |___
    """,
    """
     _______
    |/      |
    |      (_)
    |
    |
    |
    |
    |___
    """,
    """
     _______
    |/      |
    |      (_)
    |       |
    |       |
    |
    |
    |___
    """,
    """
     _______
    |/      |
    |      (_)
    |      \\|
    |       |
    |
    |
    |___
    """,
    """
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |
    |
    |___
    """,
    """
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      /
    |
    |___
    """,
    """
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      / \\
    |
    |___
    """
]

while True:
    print("\n=======================")
    print("🎯 Welcome to Hangman!")
    print("=======================")

    word = random.choice(word_bank)
    guessed_word = ['_'] * len(word)
    guessed_letters = set()

    difficulty = input("\nChoose difficulty (easy/medium/hard): ").lower()
    if difficulty == "easy":
        max_attempts = 8
    elif difficulty == "hard":
        max_attempts = 4
    else:
        max_attempts = 6  # default medium

    attempts = max_attempts

    while attempts > 0:
        print('\nCurrent Word: ' + ' '.join(guessed_word))
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Invalid input! Please enter one letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You've already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
            print("\033[92m✅ Great Guess!\033[0m")
        else:
            attempts -= 1
            print("\033[91m❌ Wrong Guess!\033[0m")
            print(f"Attempts left: {attempts}")
            print("Drawing Hangman...")
            time.sleep(0.5)
            stage_index = min(6, max_attempts - attempts)
            print(hangman_stages[stage_index])

        print("📜 Letters used:", ' '.join(sorted(guessed_letters)))

        if '_' not in guessed_word:
            print("\n🎉 YOU WIN!")
            print("🎊👏 Great job! The word was:", word)
            break

    if '_' in guessed_word:
        print("\n💀 GAME OVER!")
        print("☠️ The word was:", word)

    play_again = input("\n🔁 Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("👋 Thanks for playing! See ya!")
        break
