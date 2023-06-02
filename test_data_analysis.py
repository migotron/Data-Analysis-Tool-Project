# Author: Miguel Ibarra 【=◈︿◈=】

import pandas as pd
import numpy as np
import pytest
import os
import data_analysis_tool

def test_calculate_mean_age():
    df = pd.DataFrame({'age': [25, 30, 40, 50, 35, 45, 55]})
    mean_age = np.mean(df['age'])
    assert data_analysis_tool.calculate_mean_age(df) == pytest.approx(mean_age)

def test_count_males_and_females():
    df = pd.DataFrame({'gender': ['Male', 'Female', 'Male', 'Female', 'Female', 'Male', 'Female']})
    male_count = df[df['gender'] == 'Male'].shape[0]
    female_count = df[df['gender'] == 'Female'].shape[0]
    assert data_analysis_tool.count_males_and_females(df) == (male_count, female_count)

def test_calculate_standard_deviation():
    df = pd.DataFrame({'age': [25, 30, 40, 50, 35, 45, 55]})
    std_age = np.std(df['age'])
    assert data_analysis_tool.calculate_standard_deviation(df) == pytest.approx(std_age)

def test_calculate_percentage_of_males_and_females():
    df = pd.DataFrame({'gender': ['Male', 'Female', 'Male', 'Female', 'Female', 'Male', 'Female']})
    male_percentage = df[df['gender'] == 'Male'].shape[0] / df.shape[0]
    female_percentage = df[df['gender'] == 'Female'].shape[0] / df.shape[0]
    assert data_analysis_tool.calculate_percentage_of_males_and_females(df) == (male_percentage, female_percentage)

def test_plot_age_distribution():
    # Create a temporary file for the plot
    temp_file = 'age_distribution.png'
    
    df = pd.DataFrame({'age': [25, 30, 40, 50, 35, 45, 55]})
    data_analysis_tool.plot_age_distribution(df, temp_file)

    # Check if the file was created
    assert os.path.isfile(temp_file)

    # Clean up the temporary file
    os.remove(temp_file)

def test_add_user_input():
    df = pd.DataFrame({'id': [1, 2, 3], 'name': ['John', 'Jane', 'Peter'], 'age': [25, 30, 40],
                       'gender': ['Male', 'Female', 'Male'], 'country': ['USA', 'UK', 'Canada']})

    new_row = (4, 'Mary', 35, 'Female', 'USA')
    expected_df = pd.DataFrame({'id': [1, 2, 3, 4], 'name': ['John', 'Jane', 'Peter', 'Mary'], 'age': [25, 30, 40, 35],
                                'gender': ['Male', 'Female', 'Male', 'Female'], 'country': ['USA', 'UK', 'Canada', 'USA']})

    df = data_analysis_tool.add_user_input(df, new_row)
    pd.testing.assert_frame_equal(df, expected_df)

def test_save_results():
    df = pd.DataFrame({'id': [1, 2, 3], 'name': ['John', 'Jane', 'Peter'], 'age': [25, 30, 40],
                       'gender': ['Male', 'Female', 'Male'], 'country': ['USA', 'UK', 'Canada']})

    file_name = 'results.csv'
    data_analysis_tool.save_results(df, file_name)

    # Check if the file was created
    assert os.path.isfile(file_name)

    # Read the saved file and compare its content with the original DataFrame
    saved_df = pd.read_csv(file_name)
    pd.testing.assert_frame_equal(df, saved_df)

    # Clean up the saved file
    os.remove(file_name)


def test_plot_boxplot_age_by_gender():
    # Create a temporary file for the plot
    temp_file = 'boxplot_age_by_gender.png'

    df = pd.DataFrame({
        'age': [25, 30, 40, 50, 35, 45, 55],
        'gender': ['Male', 'Female', 'Male', 'Female', 'Female', 'Male', 'Female']
    })

    data_analysis_tool.plot_boxplot_age_by_gender(df, temp_file)

    # Check if the file was created
    assert os.path.isfile(temp_file)

    # Clean up the temporary file
    os.remove(temp_file)

def test_plot_violin_plot_age_by_country():
    # Create a temporary file for the plot
    temp_file = 'violin_plot_age_by_country.png'

    df = pd.DataFrame({
        'age': [25, 30, 40, 50, 35, 45, 55],
        'country': ['United States', 'United Kingdom', 'Canada', 'Australia', 'United States', 'Canada', 'Australia']
    })

    data_analysis_tool.plot_violin_plot_age_by_country(df, temp_file)

    # Check if the file was created
    assert os.path.isfile(temp_file)

    # Clean up the temporary file
    os.remove(temp_file)

if __name__ == '__main__':
    pytest.main()