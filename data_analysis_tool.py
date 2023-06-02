# Author: Miguel Ibarra 【=◈︿◈=】

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

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
            return id, name, age, gender, country
        except ValueError:
            print('Invalid input. Please enter a valid value.')
        except NameError:
            print('Invalid name. Please enter a valid name.')
        except KeyError:
            print('Invalid gender. Please enter a valid gender.')
        except IndexError:
            print('Invalid country. Please enter a valid country.')

# Add a progress bar
def show_progress_bar():
    print('Processing', end='')
    for _ in range(5):
        print('.', end='', flush=True)
        time.sleep(1)
    print('')

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
    print('9. Quit')

def main(df):
    while True:
        display_menu()
        choice = input('Enter your choice: ')

        if choice == '1':
            mean_age = np.mean(df['age'])
            print('The mean age is:', mean_age)
        elif choice == '2':
            std_age = np.std(df['age'])
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
            print('The number of males is:', male_count)
            print('The number of females is:', female_count)
        elif choice == '5':
            male_percentage = df[df['gender'] == 'Male'].shape[0] / df.shape[0]
            female_percentage = df[df['gender'] == 'Female'].shape[0] / df.shape[0]
            print('The percentage of males is:', male_percentage)
            print('The percentage of females is:', female_percentage)
        elif choice == '6':
            id, name, age, gender, country = get_user_input()
            # Create a new DataFrame row with user input
            new_row = pd.DataFrame([[id, name, age, gender, country]], columns=['id', 'name', 'age', 'gender', 'country'])
            df = pd.concat([df, new_row], ignore_index=True)
            print('User input added successfully.')
        elif choice == '7':
            save_choice = input('Enter the file name to save the results: ')
            df.to_csv(save_choice, index=False)
            print('Results saved successfully.')
        elif choice == '8':
            print('This program provides basic data analysis features.')
            print('You can calculate the mean and standard deviation of age, plot the age distribution,')
            print('count the number of males and females, calculate their percentages, add user input,')
            print('save the results, or quit the program.')
        elif choice == '9':
            print('Thank you for using the Data Analysis Tool. Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

# Run the program
if __name__ == '__main__':
    main(df)