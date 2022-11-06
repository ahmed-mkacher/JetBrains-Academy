import random
import art
import words

print(art.logo)
user_choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:').lower()

wins = 0
losses = 0
attempts = 8
k = 0
word_list = ["python", "java", "swift", "javascript"]
word_list.append(words.word_list)


def main():
    global user_choice
    global wins
    global losses
    global attempts
    global k
    hidden = ""
    input_history = []
    computer_choice = random.randint(0, len(word_list)-1)
    word = word_list[computer_choice]
    word_length = len(word)
    word_as_list = list(word)
    for i in range(word_length):
        hidden += "-"
    hidden_as_list = list(hidden)
    while attempts > 0:
        print(f"\n{hidden}")
        letter = input("Input a letter ")
        if len(letter) != 1:
            print("Please, input a single letter.")
        elif not letter.isalpha() or letter.isupper():
            print("Please, enter a lowercase letter from the English alphabet.")
        elif letter in input_history:
            print("You've already guessed this letter.")
            attempts -= 1
        elif letter in word_as_list:
            for j in range(word_length):
                if letter == word_as_list[j]:
                    hidden_as_list[j] = letter
            hidden = "".join(hidden_as_list)
        elif letter not in word_as_list:
            attempts -= 1
            print(art.stages[len(art.stages) - k - 1])
            print(f"That letter doesn't appear in the word.")
            k += 1
        input_history.append(letter)
        if hidden == word:
            wins += 1
            print(f"You guessed the word {word}!\nYou survived!")
            break
        if attempts == 0:
            losses += 1
            print("You lost!")
    user_choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:').lower()


while True:
    if user_choice == "play":
        main()
    if user_choice == "results":
        print(f"You won: {wins} times\nYou lost: {losses} times")
        user_choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:').lower()
    elif user_choice == "exit":
        quit()
