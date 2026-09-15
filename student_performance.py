import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
data = pd.read_csv("Student_Performance_DT.csv")
print("Student Performance Prediction System")
print("--------------------------------------")
print("\nDataset:")
print(data.head())
data["Internet_Access"] = data["Internet_Access"].map({
    "Yes": 1,
    "No": 0
})
data["Extracurricular"] = data["Extracurricular"].map({
    "Yes": 1,
    "No": 0
})
data["Final_Result"] = data["Final_Result"].map({
    "Pass": 1,
    "Fail": 0
})
X = data.drop("Final_Result", axis=1)
y = data["Final_Result"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy:", round(accuracy * 100, 2), "%")
print("\nEnter Student Details")
print("--------------------")
study_hours = float(input("Study Hours: "))
attendance = float(input("Attendance (%): "))
previous_score = float(input("Previous Score: "))
assignments = int(input("Assignments Completed: "))
sleep_hours = float(input("Sleep Hours: "))
participation = int(input("Participation Level: "))
internet = input("Internet Access (Yes/No): ")
internet = 1 if internet.lower() == "yes" else 0
extracurricular = input("Extracurricular Activities (Yes/No): ")
extracurricular = 1 if extracurricular.lower() == "yes" else 0
new_student = [[
    study_hours,
    attendance,
    previous_score,
    assignments,
    sleep_hours,
    participation,
    internet,
    extracurricular
]]
prediction = model.predict(new_student)
if prediction[0] == 1:
    print("\nFinal Prediction: PASS")
else:
    print("\nFinal Prediction: FAIL")