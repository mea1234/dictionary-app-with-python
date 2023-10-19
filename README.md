# Quiz and Flashcard App with Tkinter

## Vidoe Demo
https://youtu.be/uow9XApMT7A?si=cvvCkGGzPxKn1G9F 

## Description

This project is a Python application designed to facilitate the process of learning new words and assessing vocabulary knowledge. Developed as the final project for CS50's Introduction to Programming in Python, this user-friendly app is intended to help English learners improve their language skills. The application is built using the Tkinter library for creating the graphical user interface.

### Features

#### 1. Word Addition
- Users can add new words to their dictionary along with their meanings. Two methods are provided:
  - Manual Entry: Input the word and meaning manually.
  - Meaning Lookup: Utilize the built-in meaning lookup feature that fetches synonyms and definitions from the NLTK WordNet database.

#### 2. Flashcard Mode
- In this mode, users can:
  - View words and their corresponding meanings.
  - Practice pronunciation with the built-in text-to-speech feature.
  - Easily delete words from their dictionary as they master them.

#### 3. Quiz Mode
- The application offers a quiz mode to test users' knowledge of word meanings. Users can answer questions about word meanings and keep track of their scores.

#### 4. User-Friendly Interface
- The user interface is intuitively designed, ensuring ease of navigation. Users can switch between quiz and flashcard modes with the click of a button.

#### 5. Data Persistence
- Word and meaning data are saved in a CSV file, allowing users to revisit and continue their learning journey.

### File Structure

- "project.py": The main script that launches the application.
- "dictionary.csv": The CSV file used to store user-added words and their meanings. I choose this file because it's easy to use for me, as long as i work dict type 
data, csv file and it's method give me the oportuniry to save data precesialy, and retrieve them easily for later use. 
- "README.md": This file, containing the project documentation.
- "test_project.py" contains test functiond for several functions from project.py 
- "test_dictionary" is used in proces of testing functions in "test_project.py"
- "requirements" file encompass all third part libraries which was used in my project


### requirement

- Tkinter: For creating the graphical user interface.
- csv: For handling CSV files.
- random: For generating random choices in the quiz mode.
- pyttsx3: For implementing text-to-speech functionality.
- ttkbootstrap: Used for styling the GUI.
- pandas: For data manipulation and handling the CSV file.
- nltk: Utilized to retrieve word meanings using the WordNet database.


### Design Choices

- The application follows a clean and straightforward design to ensure a user-friendly experience.
- I used ttkbootstrap, adopting the "superhero" theme for a modern and minimalist aesthetic. This theme provide a pleasing dark environment that helps focus the user's attention on the words without overwhelming their visual experience.
- A CSV file is used for data storage, providing easy data persistence and allowing users to review their progress.
- To enhance the learning experience, I've incorporated pyttsx3. This feature enables users to practice word pronunciation seamlessly within the app, making the learning process more convenient.

