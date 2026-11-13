# -student-dropout-analysis-weka
Student Dropout Analysis Using WEKA and Data Mining

Project Overview

This project focuses on analyzing student data using Data Mining techniques and WEKA. It explores student academic performance and behavioral patterns through data preprocessing, data transformation, Data Cube analysis and association rule mining.

Dataset Description

* Total Records: 300 students
* Total Attributes: 16
* Dataset: Student Dropout Behavior Dataset
* File Formats: CSV and ARFF

Technologies Used

* WEKA
* Python
* Pandas
* Data Mining
* Association Rule Mining
* CSV and ARFF

Project Modules

1. Data Preprocessing

Prepared and transformed the student dataset into binary format for data mining operations.

2. Data Cube Analysis

Implemented Data Cube analysis using Python to examine student information based on:

* Gender
* Age Group
* Final Marks
* Student Count
* Average Final Marks

3. WEKA Analysis

Used WEKA Explorer to load, preprocess and analyze student datasets in ARFF format.

4. Association Rule Mining

Explored association rule mining using Apriori and FP-Growth algorithms to identify patterns and relationships in student data.

Project Structure

student-dropout-analysis-weka/
│
├── create_binary_data.py
├── data_cube.py
├── student_dropout_behavior_dataset.csv
├── student_dropout_behavior_dataset.csv.arff
├── student_binary_data.csv
├── student_binary_data.csv.arff
├── student_data_cube.csv
├── student_data_cube.csv.arff
├── README.md
└── .gitignore

How to Run

Python Implementation

1. Install Python.
2. Install Pandas:

pip install pandas

3. Generate binary dataset:

python3 create_binary_data.py

4. Run Data Cube analysis:

python3 data_cube.py

WEKA Implementation

1. Open WEKA.
2. Select Explorer.
3. Click Open File.
4. Load the required ARFF dataset.
5. Explore the data using the available data mining algorithms.

Key Learning Outcomes

* Data preprocessing and transformation.
* Working with CSV and ARFF datasets.
* Data Cube implementation.
* Data analysis using WEKA.
* Association rule mining using Apriori and FP-Growth.

Author

Shirisha TS
Computer Science and Engineering (Data Science)
