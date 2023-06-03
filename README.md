# Data Analysis Tool Project

The Data Analysis Tool is a Python program that provides basic data analysis features for a given dataset. It allows users to perform various data analysis tasks such as calculating mean and standard deviation, plotting data distributions, counting the number of specific data categories, and more.

## Features

The Data Analysis Tool provides the following features:

- Calculate the mean age: Calculates and displays the mean age of the dataset.
- Calculate the standard deviation of age: Calculates and displays the standard deviation of the age values in the dataset.
- Plot the age distribution: Generates a histogram plot to visualize the age distribution in the dataset.
- Count the number of males and females: Counts and displays the number of males and females in the dataset.
- Calculate the percentage of males and females: Calculates and displays the percentage of males and females in the dataset.
- Add user input: Allows users to add their own data to the dataset, including fields such as name, age, gender, country, income, education level, occupation, marital status, and number of children.
- Save results: Enables users to save the analysis results to a CSV file.
- Plot a boxplot of age by gender: Generates a boxplot to compare the age distribution between different genders.
- Plot a violin plot of age by country: Generates a violin plot to compare the age distribution across different countries.
- Analyze income by education level: Displays a barplot showing the relationship between income and education level.
- Analyze income by occupation: Displays a barplot showing the relationship between income and occupation.
- Analyze income by marital status: Displays a barplot showing the relationship between income and marital status.
- Analyze income by number of children: Displays a barplot showing the relationship between income and the number of children.

## Getting Started

To use the Data Analysis Tool, follow these steps:

1. Install the required dependencies by running the command: `pip install pandas numpy matplotlib seaborn`.
2. Place your dataset in CSV format in the same directory as the program file.
3. Update the code to specify the correct filename of your dataset.
4. Run the program by executing the command: `python data_analysis_tool.py`.

## Requirements

- Python 3.6 or higher
- pandas library
- numpy library
- matplotlib library
- seaborn library

## Example Dataset

The program expects the dataset to be in CSV format with the following columns:
```
id,name,age,gender,country,income,education,occupation,marital_status,children
1,John Doe,25,Male,United States,50000,Bachelor's Degree,Engineer,Single,0
2,Jane Doe,30,Female,United Kingdom,60000,Master's Degree,Manager,Married,2
3,Peter Smith,40,Male,Canada,45000,Bachelor's Degree,Doctor,Married,1
4,Mary Johnson,50,Female,Australia,55000,Associate Degree,Teacher,Single,3
5,Susan Smith,35,Female,United States,70000,Bachelor's Degree,Engineer,Married,2
6,Michael Jones,45,Male,Canada,60000,Master's Degree,Doctor,Single,0
7,Sarah Johnson,55,Female,Australia,80000,Master's Degree,Manager,Married,1
```

Note: The dataset should include appropriate headers in the first row.


## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).
