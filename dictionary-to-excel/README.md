
---

### 📄 `README.md`

````markdown
# 📝 Dictionary to Excel Converter (User Input Based)

This Python program allows users to interactively create a dictionary by entering custom keys and multiple values for each key, and then exports the data to an Excel file. The program saves the Excel file **in the same directory as the Python script**.

---

## 🚀 Features

- Accepts custom key names (like `"roll number"`, `"name"`, etc.).
- Allows user to define how many values to enter per key.
- Keeps asking for more keys until the user says `"no"`.
- Automatically pads shorter columns with blank values.
- Saves the final data into an Excel file (`output.xlsx`) in the **same folder as the script**.

---

## 📦 Requirements

Make sure you have Python installed along with the following packages:

- `pandas`
- `openpyxl` (for writing `.xlsx` files)

### Install Dependencies

You can install the required libraries using pip:

```bash
pip install pandas openpyxl
````

---

## 📁 File Structure

```
project/
│
├── your_script.py         # ← Your main Python script
├── output.xlsx            # ← Excel file generated (after running)
└── README.md              # ← This file
```

> ✅ The Excel file will be saved in the **same folder** as `your_script.py`.

---


## 🧑‍💻 How to Run

1. Open a terminal or command prompt.
2. Navigate to the folder where `your_script.py` is located.
3. Run the script using Python:

```bash
python your_script.py
```

4. Follow the prompts to:

   * Enter key names (e.g., `"roll number"`, `"name"`).
   * Specify how many values to enter for each.
   * Enter each value one by one.
   * Decide whether to add more keys.

5. When finished, an Excel file named `output.xlsx` will be created in the same folder.

---

## 📊 Example Output (Excel File)

| roll number | name  |
| ----------- | ----- |
| 101         | Alice |
| 102         | Bob   |
| 103         |       |

---

## 📌 Notes

* The program automatically pads shorter columns with empty strings to ensure all columns are the same length.
* If you want to change the file name or path, you can modify the `save_to_excel()` function in the script.

---

## 📃 License

This project is for educational and personal use. No license required.

---

```

---

Let me know if you want the `README.md` to include screenshots, command-line examples, or if you'd like to generate it as a downloadable file.
```

