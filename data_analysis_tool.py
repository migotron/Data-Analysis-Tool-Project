# Author: Miguel Ibarra 【=◈︿◈=】

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
from tqdm import tqdm

# Read the CSV file
df = pd.read_csv('test_dataset.csv')

# Add user input with error handling
def get_user_input():
    total_inputs = 10  # Total number of inputs to enter
    pbar = tqdm(total=total_inputs, desc='User Input', bar_format='{desc}: {percentage:3.0f}%|{bar}| {n}/{total}')
    
    # Find the maximum ID in the DataFrame
    max_id = df['id'].max()
    
    while True:
        try:
            id = max_id + 1  # Generate a unique ID
            name = input('Enter the name: ')
            pbar.update(1)
            age = int(input('Enter the age: '))
            pbar.update(1)
            gender = input('Enter the gender: ')
            pbar.update(1)
            country = input('Enter the country: ')
            pbar.update(1)
            income = int(input('Enter the income: '))
            pbar.update(1)
            education = input('Enter the education level: ')
            pbar.update(1)
            occupation = input('Enter the occupation: ')
            pbar.update(1)
            marital_status = input('Enter the marital status: ')
            pbar.update(1)
            children = int(input('Enter the number of children: '))
            pbar.update(1)
            pbar.close()
            return id, name, age, gender, country, income, education, occupation, marital_status, children
        except ValueError:
            print('Invalid input. Please enter a valid value.')

# Add a progress bar
def show_progress_bar(total=100):
    pbar = tqdm(total=total, maxinterval=100, mininterval=10)
    for _ in range(total):
        pbar.update(1)
    pbar.close()

# Add a user interface
def display_menu():
    print('Welcome to the Data Analysis Tool!')
    print('What would you like to do?')
    print('1. Calculate the mean age')
    print('2. Calculate the standard deviation of age')
    print('3. Count the number of males and females')
    print('4. Calculate the percentage of males and females')
    print('5. Plot the age distribution')
    print('6. Plot a boxplot of age by gender')
    print('7. Plot a violin plot of age by country')
    print('8. Analyze income by education level')
    print('9. Analyze income by occupation')
    print('10. Analyze income by marital status')
    print('11. Analyze income by number of children')
    print('12. Add user input')
    print('13. Save results')
    print('14. Get help')
    print('15. Quit')

def main(df):
    while True:
        display_menu()
        choice = input('Enter your choice: ')

        if choice == '1':
            mean_age = np.mean(df['age'])
            show_progress_bar()
            print('The mean age is:', mean_age)
        elif choice == '2':
            std_age = np.std(df['age'])
            show_progress_bar()
            print('The standard deviation of age is:', std_age)
        elif choice == '3':
            male_count = df[df['gender'] == 'Male'].shape[0]
            female_count = df[df['gender'] == 'Female'].shape[0]
            show_progress_bar()
            print('The number of males is:', male_count)
            print('The number of females is:', female_count)
        elif choice == '4':
            male_percentage = df[df['gender'] == 'Male'].shape[0] / df.shape[0]
            female_percentage = df[df['gender'] == 'Female'].shape[0] / df.shape[0]
            show_progress_bar()
            print('The percentage of males is:', male_percentage * 100, '%')
            print('The percentage of females is:', female_percentage * 100, '%')
        elif choice == '5':
            plt.hist(df['age'], bins=10, edgecolor='black')
            plt.title('Age Distribution')
            plt.xlabel('Age')
            plt.ylabel('Frequency')
            plt.show()
        elif choice == '6':
            sns.boxplot(x='gender', y='age', data=df)
            plt.title('Age Distribution by Gender')
            plt.xlabel('Gender')
            plt.ylabel('Age')
            plt.show()
        elif choice == '7':
            sns.violinplot(x='country', y='age', data=df)
            plt.title('Age Distribution by Country')
            plt.xlabel('Country')
            plt.ylabel('Age')
            plt.show()
        elif choice == '8':
            sns.barplot(x='education', y='income', data=df)
            plt.title('Income by Education Level')
            plt.xlabel('Education Level')
            plt.ylabel('Income')
            plt.xticks(rotation=45)
            plt.show()
        elif choice == '9':
            sns.barplot(x='occupation', y='income', data=df)
            plt.title('Income by Occupation')
            plt.xlabel('Occupation')
            plt.ylabel('Income')
            plt.xticks(rotation=45)
            plt.show()
        elif choice == '10':
            sns.barplot(x='marital_status', y='income', data=df)
            plt.title('Income by Marital Status')
            plt.xlabel('Marital Status')
            plt.ylabel('Income')
            plt.show()
        elif choice == '11':
            sns.barplot(x='children', y='income', data=df)
            plt.title('Income by Number of Children')
            plt.xlabel('Number of Children')
            plt.ylabel('Income')
            plt.show()
        elif choice == '12':
            new_data = get_user_input()
            df.loc[len(df)] = new_data
            show_progress_bar()
            print('User input added successfully!')
        elif choice == '13':
            filename = input('Enter the filename to save the results (e.g., analysis_results.csv): ')
            df.to_csv(filename, index=False)
            show_progress_bar()
            print('Results saved successfully!')
        elif choice == '14':
            print('Help:')
            print('This tool provides basic data analysis features for a given dataset.')
            print('Select an option from the menu to perform various data analysis tasks.')
            print('For more information, please refer to the documentation.')
        elif choice == '15':
            print('Thank you for using the Data Analysis Tool. Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

# Run the program
if __name__ == '__main__':
    main(df)