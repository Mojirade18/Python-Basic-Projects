### **Student Average Score Calculator**

#### **Purpose:**
This program calculates the weighted average score for multiple students based on their performance in four categories: Quiz, Homework, Recitation, and Test. The weight for each category is predefined. The program is designed to be flexible, allowing easy addition of new students, categories, or changes to category weights.

---

### **1. Data Structures:**

#### **1.1 Student Data:**
The program stores the scores for each student in dictionaries. Each key in the dictionary represents a category (e.g., "Quiz", "Homework", etc.), and the associated value is a list of scores for that category.

Example:
```python
mark = {
    "Quiz" : [70,66.2,80.5],
    "Homework": [90,88,72.6],
    "Recitation": [40.5,65.6],
    "Test": [85.4,63.4]
}
```

#### **1.2 Weights for Categories:**
The weight of each category (Quiz, Homework, Recitation, Test) is defined in a dictionary:
```python
weights = {
    "Quiz": 0.2,
    "Homework": 0.1,
    "Recitation": 0.3,
    "Test": 0.4
}
```

---

### **2. Functions:**

#### **2.1 `avg(scores)`**

**Description:**  
This function calculates the average score for a given list of scores.

**Parameters:**
- `scores` (list of floats): The list containing the scores for a category (e.g., Quiz, Homework).

**Returns:**
- A float representing the average of the scores.

**Example:**
```python
avg([70, 80, 90])  # Returns: 80.0
```

**Note:** If the list is empty, the function returns `0`.

---

#### **2.2 `stud_average(student_data, category_weights)`**

**Description:**  
This function calculates the weighted average score for a student, based on their scores in different categories and the corresponding weights.

**Parameters:**
- `student_data` (dict): A dictionary containing the student's scores for each category. The dictionary structure matches the one used in the program (e.g., `{"Quiz": [70,66.2,80.5], "Homework": [90,88,72.6], ...}`).
- `category_weights` (dict): A dictionary containing the weight of each category (e.g., `{"Quiz": 0.2, "Homework": 0.1, "Recitation": 0.3, "Test": 0.4}`).

**Returns:**
- A float representing the student's weighted average score, rounded to two decimal places.

**Example:**
```python
student_data = {
    "Quiz" : [70, 66.2, 80.5],
    "Homework": [90, 88, 72.6],
    "Recitation": [40.5, 65.6],
    "Test": [85.4, 63.4]
}

category_weights = {
    "Quiz": 0.2,
    "Homework": 0.1,
    "Recitation": 0.3,
    "Test": 0.4
}

stud_average(student_data, category_weights)  # Returns: 71.42
```

---

#### **2.3 `main()`**

**Description:**  
This is the main function that organizes the program. It initializes the student data and category weights, then calls `stud_average()` for each student to compute their weighted average score.

**Parameters:**  
None.

**Returns:**  
None (It prints the results for each student).

**Example Output:**
```text
The average score for Mark is: 71.42 %
The average score for Bill is: 62.85 %
The average score for Jane is: 88.61 %
```

---

### **3. Execution Flow:**

1. **Data Initialization:**
   - Student data is stored in dictionaries (`mark`, `bill`, `jane`), where each student's category scores are kept.
   - The weights for each category (Quiz, Homework, Recitation, Test) are stored in a separate dictionary (`weights`).

2. **Main Function Execution:**
   - The `main()` function iterates over a dictionary of students (`students`), where each student's name is the key, and their corresponding data is the value.
   - For each student, the program calculates their weighted average score using `stud_average()`.
   - It then prints the weighted average score for each student.

---

### **4. Example Use Case:**

- **Input:**
    The program uses predefined data for three students (Mark, Bill, Jane). Each student has scores in the categories of Quiz, Homework, Recitation, and Test.

- **Output:**
    The program will calculate and print the average score for each student based on the predefined weights:
    
    ```text
    The average score for Mark is: 71.42 %
    The average score for Bill is: 62.85 %
    The average score for Jane is: 88.61 %
    ```

---

### **5. Flexibility:**

- **Adding New Students:**
  To add a new student, you can add their data to the `students` dictionary. The program will handle the rest of the calculations automatically.
  
  Example:
  ```python
  new_student = {
      "Quiz" : [78, 80, 82],
      "Homework": [85, 90, 92],
      "Recitation": [65, 70],
      "Test": [88, 90]
  }
  students["New Student"] = new_student
  ```

- **Changing Weights:**
  You can modify the `weights` dictionary to change the contribution of each category to the final score. For example, if you want Recitation to contribute 25% instead of 30%, update the dictionary:
  ```python
  weights["Recitation"] = 0.25
  ```

---

### **6. Potential Enhancements:**

- **Dynamic Input:** Instead of hardcoding student data, allow users to input scores and categories dynamically through the command line or a graphical interface.
- **Error Handling:** Add more robust error handling to catch issues like empty score lists, invalid data types, or mismatched category lists.
- **Export Results:** Extend the program to export the results (e.g., to a CSV or JSON file) for record-keeping or analysis.

---

This documentation provides an overview of the program’s purpose, structure, functions, and how to extend or modify it for future needs.
