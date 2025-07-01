# 🐍 Python Challenge — PyBank & PyPoll

## 🚀 Overview

This project marks a transition from spreadsheet-based analysis to full programming with **Python**. In this challenge, we completed two real-world data analysis tasks using scripting:

- 📊 **PyBank**: Analyze company financial records  
- 🗳️ **PyPoll**: Tally and summarize election results

Both tasks showcase how Python scripting can handle larger datasets more efficiently than Excel, while also teaching foundational data manipulation, file I/O, and reporting techniques.

---

## 📌 Objectives

### 🔹 PyBank

- Calculate the total number of months in the dataset
- Compute the net total of “Profit/Losses”
- Determine monthly changes and average change
- Identify the month with:
  - Greatest increase in profits
  - Greatest decrease in profits
- Export results to a `.txt` file and display in terminal

### 🔹 PyPoll

- Count the total number of votes
- Generate a list of candidates who received votes
- Calculate:
  - Total votes per candidate
  - Vote percentage per candidate
- Identify the winning candidate
- Export results to a `.txt` file and display in terminal

---

## 🧪 Example Output

### ✅ PyBank — Financial Analysis
Financial Analysis

Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)

### ✅ PyPoll — Election Results
Election Results

Total Votes: 369711

Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)

Winner: Diana DeGette

---

## ✅ Requirements Checklist

| Feature                                    | Status |
|--------------------------------------------|--------|
| CSVs read correctly in both scripts        | ✅     |
| Terminal output matches expected format    | ✅     |
| Text files generated with full results     | ✅     |
| Scripts run error-free                     | ✅     |
| Clean and well-commented code              | ✅     |

---

## 🛠️ Technologies Used

- **Python 3**
- Built-in Modules:
  - `csv`
  - `os`

---

## 📦 How to Run

1. Clone this repository.
2. Navigate to either `PyBank` or `PyPoll` folder.
3. Run the script:
   ```bash
   python main.py
4.	Results will print to terminal and be saved to /analysis/results.txt.

---
🧠 Lessons Learned
	•	Python is significantly more efficient than Excel for handling large datasets.
	•	File I/O and string formatting are essential for automating data reporting.
	•	Dictionaries and lists are powerful tools for counting and aggregating structured data.

---
📚 Acknowledgments

This project was developed as part of the [edX Data Analytics Boot Camp]. It demonstrates essential Python skills for early-career data analysts.

---
🧠 Author

Aditi Nankar
Data Analytics Student | Excel to Python Transitioner
