# Data-Analysis-Tool-Project

The Data Analysis Tool is a Python program that provides basic data analysis features for a given dataset. It allows users to perform various data analysis tasks such as calculating mean and standard deviation, plotting data distributions, counting the number of specific data categories, and more.

## Features

- Calculate the mean age: The program calculates and displays the mean age of the dataset.
- Calculate the standard deviation of age: The program calculates and displays the standard deviation of the age values in the dataset.
- Plot the age distribution: The program generates a histogram plot to visualize the age distribution in the dataset.
- Count the number of males and females: The program counts and displays the number of males and females in the dataset.
- Calculate the percentage of males and females: The program calculates and displays the percentage of males and females in the dataset.
- Add user input: The program allows users to add their own data to the dataset, including fields such as name, age, gender, and country.
- Save results: The program enables users to save the analysis results to a CSV file.
- Get help: The program provides information and guidance on how to use its features.
- Quit: The program allows users to exit the tool.

## Getting Started

1. Install the required dependencies by running the command: `pip install pandas numpy matplotlib`.
2. Place your dataset in CSV format in the same directory as the program file.
3. Update the code to specify the correct filename of your dataset.
4. Run the program by executing the command: `python data_analysis_tool.py`.

## Requirements

- Python 3.6 or higher
- pandas library
- numpy library
- matplotlib library

## Example Dataset

The program expects the dataset to be in CSV format with the following columns:

```
id,name,age,gender,country
1,John Doe,25,Male,United States
2,Jane Doe,30,Female,United Kingdom
3,Peter Smith,40,Male,Canada
4,Mary Johnson,50,Female,Australia
5,Susan Smith,35,Female,United States
6,Michael Jones,45,Male,Canada
7,Sarah Johnson,55,Female,Australia
8,David Brown,28,Male,United States
9,Emily Davis,32,Female,United Kingdom
10,Robert Wilson,43,Male,Canada
11,Lisa Taylor,48,Female,Australia
12,Mark Anderson,38,Male,United States
13,Amy Thompson,27,Female,United States
14,James White,33,Male,Canada
15,Michelle Martin,42,Female,Australia
```


## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).
