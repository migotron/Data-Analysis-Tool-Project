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
    while True:
        try:
            id = len(df) + 1  # Auto-incremented ID
            name = input('Enter the name: ')
            age = int(input('Enter the age: '))
            gender = input('Enter the gender: ')
            country = input('Enter the country: ')
            income = int(input('Enter the income: '))
            education = input('Enter the education level: ')
            occupation = input('Enter the occupation: ')
            marital_status = input('Enter the marital status: ')
            children = int(input('Enter the number of children: '))
            return id, name, age, gender, country, income, education, occupation, marital_status, children
        except ValueError:
            print('Invalid input. Please enter a valid value.')

# Add a progress bar
def show_progress_bar(total=100):
    pbar = tqdm(total=total, maxinterval=10)
    for _ in range(total):
        pbar.update(1)
    pbar.close()

# Add a user interface
def display_menu():
    print('Welcome to the Data Analysis Tool!')
    print('What would you like to do?')
    print('1. Calculate the mean age')
    print('2. Calculate the standard deviation of age')
    print('3. Plot the age distribution')
    print('4. Count the number of males and females')
    print('5. Calculate the percentage of males and females')
    print('6. Add user input')
    print('7. Save results')
    print('8. Get help')
    print('9. Plot a boxplot of age by gender')
    print('10. Plot a violin plot of age by country')
    print('11. Analyze income by education level')
    print('12. Analyze income by occupation')
    print('13. Analyze income by marital status')
    print('14. Analyze income by number of children')
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
            plt.hist(df['age'], bins=10)
            plt.title('Age Distribution')
            plt.xlabel('Age')
            plt.ylabel('Count')
            plt.show()
        elif choice == '4':
            male_count = df[df['gender'] == 'Male'].shape[0]
            female_count = df[df['gender'] == 'Female'].shape[0]
            show_progress_bar()
            print('The number of males is:', male_count)
            print('The number of females is:', female_count)
        elif choice == '5':
            male_percentage = df[df['gender'] == 'Male'].shape[0] / df.shape[0]
            female_percentage = df[df['gender'] == 'Female'].shape[0] / df.shape[0]
            show_progress_bar()
            print('The percentage of males is:', round(male_percentage * 100, 2))
            print('The percentage of females is:', round(female_percentage * 100, 2))
        elif choice == '6':
            new_data = get_user_input()
            df.loc[len(df)] = new_data
            show_progress_bar()
            print('User input added successfully!')
        elif choice == '7':
            file_name = input('Enter the file name to save the results: ')
            df.to_csv(file_name, index=False)
            show_progress_bar()
            print('Results saved to', file_name)
        elif choice == '8':
            print('This is a data analysis tool. Choose an option from the menu to perform various analyses on the dataset.')
        elif choice == '9':
            sns.boxplot(x=df['gender'], y=df['age'])
            plt.title('Age Distribution by Gender')
            plt.xlabel('Gender')
            plt.ylabel('Age')
            plt.show()
        elif choice == '10':
            sns.violinplot(x=df['country'], y=df['age'])
            plt.title('Age Distribution by Country')
            plt.xlabel('Country')
            plt.ylabel('Age')
            plt.show()
        elif choice == '11':
            sns.barplot(x=df['education'], y=df['income'])
            plt.title('Income by Education Level')
            plt.xlabel('Education Level')
            plt.ylabel('Income')
            plt.xticks(rotation=45)
            plt.show()
        elif choice == '12':
            sns.barplot(x=df['occupation'], y=df['income'])
            plt.title('Income by Occupation')
            plt.xlabel('Occupation')
            plt.ylabel('Income')
            plt.xticks(rotation=45)
            plt.show()
        elif choice == '13':
            sns.barplot(x=df['marital_status'], y=df['income'])
            plt.title('Income by Marital Status')
            plt.xlabel('Marital Status')
            plt.ylabel('Income')
            plt.xticks(rotation=45)
            plt.show()
        elif choice == '14':
            sns.barplot(x=df['children'], y=df['income'])
            plt.title('Income by Number of Children')
            plt.xlabel('Number of Children')
            plt.ylabel('Income')
            plt.xticks(rotation=0)
            plt.show()
        elif choice == '15':
            print('Thank you for using the Data Analysis Tool. Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

# Run the program
if __name__ == '__main__':
    main(df)