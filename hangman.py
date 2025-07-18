from tkinter import *
from tkinter import messagebox
import random


def get_random_word():
    with open('words.txt', 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file if line.strip()]
    return random.choice(words)

no_of_tries = 5
word = get_random_word()
user_word = ['_' for _ in word]
used_letters = []
polish_letters = 'aąbcćdeęfghijklłmnńoóprsśtuvwxyzźż'
game_over = False

def new_game():
    global  no_of_tries, word, user_word, used_letters, game_over
    no_of_tries = 5
    word = get_random_word()
    user_word = ['_' for _ in word]
    used_letters = []
    game_over = False

    word_label.config(text=' '.join(user_word))
    used_label.config(text='Użyte litery: ')
    result_label.config(text='')
    letter_entry.delete(0, END)
    guess_button.config(state='normal')

def ask_new_game():
    answer = messagebox.askyesno('Koniec gry', 'Czy chcesz zagrać ponownie?')
    if answer:
        new_game()
    else:
        root.destroy()

def guess_letter():
    global no_of_tries, game_over
    if game_over:
        return

    letter = letter_entry.get().lower()
    letter_entry.delete(0, END)


    if letter not in polish_letters or len(letter) != 1:
        result_label.config(text='Niepoprawna litera')
        return

    if letter in used_letters:
        result_label.config(text='Już podałeś tą literę')
        return

    used_letters.append(letter)
    used_label.config(text='Użyte litery: ' + ', '.join(used_letters))

    if letter in word:
        for index, char in enumerate(word):
            if char == letter:
                user_word[index] = letter
        result_label.config(text="Dobra litera!")
    else:
        no_of_tries -= 1
        result_label.config(text=f'Zła litera!  Pozostało prób: {no_of_tries}')

    word_label.config(text=' '.join(user_word))

    if ''.join(user_word) == word:
        result_label.config(text='Brawo! To jest to słowo!')
        guess_button.config(state='disabled')
        game_over = True
        ask_new_game()
    elif no_of_tries == 0:
        result_label.config(text=f'Koniec gry! Słowo to: {word}')
        guess_button.config(state='disabled')
        game_over = True
        ask_new_game()


root = Tk()
root.title('Wisielec')
root.geometry('400x300')
root.bind('<Return>', lambda event: guess_letter())

word_label = Label(root, text=' '.join(user_word), font=('Helvetica', 24))
word_label.pack(pady=20)

letter_entry = Entry(root, font=('Helvetica', 16), width=5, justify='center')
letter_entry.pack()

guess_button = Button(root, text="Zgadnij", command=guess_letter)
guess_button.pack(pady=10)

result_label = Label(root, text='', font=('Helvetica', 12))
result_label.pack(pady=10)

used_label = Label(root, text='Użyte litery: ', font=('Helvetica', 12))
used_label.pack(pady=10)


root.mainloop()