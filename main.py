from tkinter import *
from tkinter import messagebox
from Word_library import *
from ascii_art import HANGMANPICS
WHITE = "white"
blanks = ""
correct_guesses = ""
inserted_guess = ""
art = HANGMANPICS[0]


def pick_a_word():
    global blanks, correct_answer, correct_guesses, art, hangman_art, entry_box, the_word_label, inserted_guess
    blanks = ""
    correct_guesses = ""
    inserted_guess = ""
    art = HANGMANPICS[0]
    hangman_art.config(text=art)
    entry_box.delete(0, END)
    entry_box.focus_set()
    correct_answer = Word().choose_word()
    for _ in correct_answer:
        blanks += " _"

    the_word_label.config(text=f"The word: {blanks}")


win = Tk()
win.title("Hangman")
win.minsize(200, 400)
win.config(padx=20, pady=20, bg=WHITE)
correct_answer = Word().choose_word()
for i in correct_answer:
    blanks += " _"


def check_answer():
    global correct_answer, entry_box, blanks, correct_guesses, art, inserted_guess
    inserted_guess = entry_box.get().lower()  # Get the input of the user
    entry_box.delete(0, END)
    blanks = ""
    for char in correct_answer:  # check if the chars inserted are in the correct answer and if so it adds it and print it
        if char in inserted_guess or char in correct_guesses:
            blanks += " " + char
            correct_guesses += char

        else:
            blanks += " _"

    the_word_label.config(text=f"The word: {blanks}")  # to print the remaining spaces

    if "_" not in blanks:  # To detect if the whole word has been guessed
        blanks = blanks.replace(" ", "")
        you_win = messagebox.askyesno("Congrats!!!!", "You Won!!!!!\nDo You want to play again")
        if you_win:
            pick_a_word()

        else:
            quit()

    for char in inserted_guess:  # To check if the inserted char not in the correct word and if so it develops the hangman art

        if char not in correct_answer:
            art = HANGMANPICS[HANGMANPICS.index(art) + 1]
            hangman_art.config(text=art)

        # If we reached the final hangman art it will say you lost and say if you want to play again
        if HANGMANPICS.index(art) >= 6:
            you_lost = messagebox.askyesno("Hard Luck", f"You lost!!\nThe word was: {correct_answer}\nDo you want to play again?")
            if you_lost:
                pick_a_word()
                break

            else:
                quit()


# Entry
entry_box = Entry()
entry_box.focus_set()
entry_box.grid(column=1, row=0)

# Labels
entry_box_label = Label(text="Enter your guess:", bg=WHITE)
entry_box_label.grid(column=0, row=0)

hangman_art = Label(text=art, bg=WHITE, pady=20)
hangman_art.grid(column=1, row=3)

the_word_label = Label(text=f"The word: {blanks}", bg=WHITE, font="bold", pady=20)
the_word_label.grid(column=0, row=1, columnspan=2)

# Buttons
confirm_button = Button(text="Confirm", bg=WHITE, activebackground=WHITE, command=check_answer)
confirm_button.grid(column=2, row=0)

win.mainloop()
