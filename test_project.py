from tkinter import Tk
from tkinter import Button
from project import reset_quiz
from project import get_words
import project
import csv
import pandas as pd
from project import delete_row 

def test_get_words():
    # Create a temporary CSV file with known data
    word = "cat"
    meaning = "animal"
    
    with open("dictionary.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["word", "meaning"])
        writer.writerow({"word": word, "meaning": meaning})

    # Call the get_words function and get the results
    meaning_list, word_list, dictionary = project.get_words()  # Replace 'your_module' with the actual module name

    # Define the expected results
    expected_meaning_list = ["animal"]
    expected_word_list = ["cat"]
    expected_dict = [{"meaning": "animal","word": "cat"}]

    # Check if the results match the expected values using pytest assertions
    assert meaning_list == expected_meaning_list
    assert word_list == expected_word_list
    assert dictionary == expected_dict

# Test for reset_quiz
def test_reset_quiz():
    root = Tk()
    button = Button(root, text="Start Quiz")
    button.pack()
    
    reset_quiz()
    
    assert len(root.winfo_children()) == 1

def test_delete_row():
    # Create a sample CSV file with data for testing
    data = {'word': ['apple', 'banana', 'cherry'], 'meaning': ['fruit', 'fruit', 'fruit']}
    df = pd.DataFrame(data)
    df.to_csv('sample_dictionary.csv', index=False)

    # Initially, the sample CSV should have 3 rows
    initial_data = pd.read_csv('sample_dictionary.csv')
    assert len(initial_data) == 3

    k = (1, "sample_dictionary.csv")
    # Delete the second row (index 1)
    delete_row(k)

    # Reload the data after deletion
    updated_data = pd.read_csv('sample_dictionary.csv')

    # Check if the row was removed
    assert len(updated_data) == 2
    assert updated_data.iloc[0]['word'] == 'apple'
    assert updated_data.iloc[1]['word'] == 'cherry'

    # Teardown: Remove the sample CSV file
    import os
    os.remove('sample_dictionary.csv')