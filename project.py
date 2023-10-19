from tkinter import *
import csv
import random
import pyttsx3
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import pandas as pd
from tkinter import ttk
from nltk.corpus import wordnet
import nltk
nltk.download('wordnet')

root=tb.Window(themename="superhero")


def main():
    global word_input, meaning_input
    root.title("Quiz App")
    root.geometry("650x550")
    reset_quiz()

    root.mainloop()

def reset_quiz():
    for widget in root.winfo_children():
        widget.destroy()

    label = tb.Label(root, text="Dictionary", font=("Helvetica", 20, "bold"), bootstyle="default")
    label.pack(pady=50)

    label_w = tb.Label(root, text="Word", font=("Helvetica", 15), bootstyle="default")
    label_w.pack()
    word_input = Entry(root, width=50, borderwidth=4)
    word_input.pack()
    meaning_list = []
    meaning_cb = ttk.Combobox(root, values = meaning_list, width = 80)

    meaning_button_clicked = False
    def show_meaning():
        nonlocal meaning_cb
        nonlocal meaning_list
        nonlocal meaning_button_clicked
        meaning_button_clicked = True
        if meaning_cb:
            meaning_cb.pack_forget()
        if meaning_list:
            meaning_list.clear()
            meaning_cb.pack_forget()
        word_in = word_input.get()
        syns = wordnet.synsets(word_in)
        first_mean = syns[0].lemmas()[0].name()
        second_mean = syns[1].lemmas()[0].name()
        def_mean = (syns[0].definition())
        print(first_mean, second_mean, def_mean)
        meaning_list.extend([first_mean, second_mean, def_mean])
        print(meaning_list)
        meaning_cb.config(value = meaning_list)
        meaning_input.destroy()
        meaning_list.clear()
        # meaning_cb = ttk.Combobox(root, values = meaning_list, width = 50)
        meaning_cb.pack(pady=(1,10), before=add_word_button)
        

    my_style = tb.Style() 
    my_style.configure("primary.TButton", font=("Helvetica", 15))
    my_style.configure("disabled.TButton", font=("Helvetica", 15))
    my_style.configure("secondary.TButton", font=("Helvetica", 15))

    button_meaning = tb.Button(root, text="Meaning", bootstyle="secondary", style="secondary.TButton", command=show_meaning)
    button_meaning.pack()

    meaning_input = Entry(root, width=80, borderwidth=4)
    meaning_input.pack(pady=(1,10))

    button_start_quiz = tb.Button(root, text="Start Quiz", bootstyle="primary", style="disabled.TButton", state="disabled", command=quiz)
    button_flashc = tb.Button(root, text="Flashcards", bootstyle="primary", style="disabled.TButton", state="disabled", command=flashcard)
    row_listk, _, _ = get_words()
    word_numbk = len(row_listk)
    if word_numbk >= 1:
        button_flashc.config(style="primary.TButton", state="normal")
    if word_numbk >= 4:
        button_start_quiz.config(style="primary.TButton", state="normal")

    def fill_dictionary():
        word = word_input.get()
        if meaning_button_clicked == True:
            meaning = meaning_cb.get()
        else:
            meaning = meaning_input.get()
        with open("dictionary.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["word", "meaning"])
            writer.writerow({"word": word, "meaning": meaning})
            
        row_list, _, _ = get_words()
        word_numb = len(row_list)
        if word_numb >= 1:
            button_flashc.config(style="primary.TButton", state="normal")
        if word_numb >= 4:
            button_start_quiz.config(style="primary.TButton", state="normal")
        


    add_word_button = tb.Button(root, text="Add word", bootstyle="primary", style="primary.TButton", command=fill_dictionary)
    add_word_button.pack(pady=10)

    button_start_quiz.pack(side="left", pady=10, padx=90)
    
    button_flashc.pack(side="right", pady=10, padx=90)

def get_words():
    dict = []
    meaning_list = []
    word_list = []
    with open("dictionary.csv", newline="") as file:
        reader = csv.DictReader(file, fieldnames=["word", "meaning"])
        for row in reader:
            dict.append(row)
            meaning_list.append(row["meaning"])
            word_list.append(row["word"])

        return (meaning_list, word_list, dict)

def delete_row(x):
    ind, dictio = x
    data = pd.read_csv(dictio)
    data = data.drop(data.index[ind])

    data.to_csv(dictio, index=False)


def quiz():
    # Clear the previous widgets
    for widget in root.winfo_children():
        widget.destroy()

    meaning_list, word_list, dict = get_words()
 

    current_question = 0
    score = 0

    def check_answer(user_answer):
        nonlocal score
        if user_answer == meaning_list[current_question]:
            score += 1
        next_question()

    def next_question():
        nonlocal current_question
        current_question += 1
        if current_question < len(word_list):
            display_question(current_question)
        else:
            display_result()

    def display_question(index):
        # Clear the previous widgets
        for widget in root.winfo_children():
            widget.destroy()

        word = word_list[index]
        filtered_list = meaning_list[:index] + meaning_list[index+1:]
        random_meanings = random.sample(filtered_list, 3)
        random_meanings.append(dict[index]["meaning"])
        random.shuffle(random_meanings)

        question_label = tb.Label(root, text=f"Q{index + 1}: What is the meaning of '{word}'?", font=("Helvetica", 16, "bold"), bootstyle="default")
        question_label.pack(pady=(50,30))

        my_style = tb.Style()
        my_style.configure("danger.Outline.TButton", font=("Helvetica", 10))

        for i, meaning in enumerate(random_meanings):
            button = Button(root, text=f"{i + 1}) {meaning}", width = 40, wraplength = 400, font = ("Helvetica", 14), command=lambda m=meaning: check_answer(m))
            button.pack(pady=15)

    def display_result():
        for widget in root.winfo_children():
            widget.destroy()
        result_label = tb.Label(root, text=f"You scored {score} out of {len(word_list)}", font=("Helvetica", 20, "bold"), bootstyle="default")
        result_label.pack(pady=50)

        style = tb.Style()
        style.configure("my.TButton", font=("Helvetica", 15))

        button_stover = tb.Button(root, text="Start Over", bootstyle="primary", style="my.TButton", command = quiz)
        button_stover.pack(pady=30)
        button_addw = tb.Button(root, text = "Add word", bootstyle="primary", style="my.TButton", command = reset_quiz)
        button_addw.pack()

    display_question(current_question)

def flashcard():
    for widget in root.winfo_children():
        widget.destroy()
    
    meaning_list, word_list, dict = get_words()
    index = 0

    def speak_w():
        engine = pyttsx3.init()
        engine.say(f"{word_list[index]}")
        engine.runAndWait()

    def speak_m():
        engine = pyttsx3.init()
        engine.say(f"{meaning_list[index]}")
        engine.runAndWait()

    word_label = tb.Label(root, text=f"{word_list[index]}", font =("Helvetica", 30))
    word_label.pack(pady=(40,5))

    my_style = tb.Style()
    my_style.configure("secondary.TButton", font=("Helvetica", 15))

    speak_button_w = tb.Button(root, text="sound",  bootstyle="primary", style="secondary.TButton", command=speak_w)
    speak_button_w.pack()
    mean_label = tb.Label(root, text="", font =("Helvetica", 15))
    mean_label.pack(pady=(40,5))
    speak_button_m = tb.Button(root, text="sound", bootstyle="primary", style="secondary.TButton", command=speak_m)
    speak_button_m.pack()
    speak_button_m.pack_forget()

    my_style.configure("primary.TButton", font=("Helvetica", 15))  

    def next():
        nonlocal index
        index += 1
    

        if index == len(word_list):
            for widget in root.winfo_children():
                widget.destroy()
            reset = tb.Button(root, text = "Add word", bootstyle="primary", style="primary.TButton", command = reset_quiz)
            reset.pack(pady=50)

        speak_button_m.pack_forget()
        word_label.config(text=f"{word_list[index]}")
        mean_label.config(text="")

                          
    def show_meaning():

        def insert_line_breaks(input_string, max_line_length):
            lines = []
            while input_string:
                lines.append(input_string[:max_line_length])
                input_string = input_string[max_line_length:]
            return '\n'.join(lines)
        meaning_txt = meaning_list[index]
        print(meaning_txt)
        txt_meaning = insert_line_breaks(meaning_txt, 40)
        print(txt_meaning)

        mean_label.config(text=txt_meaning)

        speak_button_m.pack(before=mean_button)

    mean_button = tb.Button(root, text="Meaning", bootstyle="primary", style="primary.TButton", width=15, command=show_meaning)
    mean_button.pack(pady=20)
    next_button = tb.Button(root, text="Next", bootstyle="primary", style="primary.TButton", width=15, command=next)
    next_button.pack(pady=20)

    ind = (index, "dictionary.csv")
    delet_button = tb.Button(root, text="Delete", bootstyle="primary", style="primary.TButton", width=15, command=lambda x  = ind  : delete_row(x))
    delet_button.pack(pady=20)
   

if __name__=="__main__":
    main()