# Student Performance Prediction System

## Project Overview

The **Student Performance Prediction System** is a Machine Learning project that predicts whether a student is likely to **Pass or Fail** based on different academic and personal factors.

A **Decision Tree Classifier** is used to train the Machine Learning model and make predictions.

## Dataset

The dataset contains information about students based on the following factors:

- Study Hours
- Attendance
- Previous Score
- Assignments Completed
- Sleep Hours
- Participation
- Internet Access
- Extracurricular Activities

### Target Variable

**Final Result** – Pass or Fail

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Git
- GitHub

## Machine Learning Algorithm

### Decision Tree Classifier

The Decision Tree Classifier is used to learn patterns from the student data and predict the final result of a student.

## Project Workflow

1. Load the student dataset
2. Preprocess the data
3. Convert categorical values into numerical values
4. Separate input features and target variable
5. Split the dataset into training and testing data
6. Train the Decision Tree Classifier
7. Test the model
8. Calculate the model accuracy
9. Enter details of a new student
10. Predict whether the student will Pass or Fail

## How to Run the Project

### Step 1: Clone the Repository

`git clone https://github.com/rishti018/Student-Performance-Prediction.git`

### Step 2: Open the Project Folder

`cd Student-Performance-Prediction`

### Step 3: Install Required Libraries

`python -m pip install pandas scikit-learn`

### Step 4: Run the Program

`python student_performance.py`

## Output

The program displays the model accuracy and allows the user to enter student details such as study hours, attendance, previous score, assignments completed, sleep hours, participation level, internet access, and extracurricular activities.

Based on the entered details, the trained Decision Tree model predicts whether the student is likely to **PASS or FAIL**.

The sample output is available in the **Output** folder of this repository.

## Project Structure

- `Student_Performance_DT.csv` – Student performance dataset
- `student_performance.py` – Main Python program
- `Output` – Sample output
- `README.md` – Project documentation

## Objective

The main objective of this project is to demonstrate how Machine Learning can be used to analyze student-related data and predict academic performance.

## Key Features

- Simple and beginner-friendly Machine Learning implementation
- Uses Decision Tree Classification
- Predicts Pass/Fail results
- Accepts new student details through user input
- Calculates model accuracy

## Author

**Rishti Nagpal**
