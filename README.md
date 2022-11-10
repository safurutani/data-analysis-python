# data-analysis-python
5 freecodecamp projects for data analysis certification

----------------------------------------
MEAN, VAR, STD

Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.

If a list containing less than 9 elements is passed into the function, it should raise a ValueError exception with the message: "List must contain nine numbers." The values in the returned dictionary should be lists and not Numpy arrays.


-----------------------------------------
DEMOGRAPHIC DATA

In this challenge you must analyze demographic data from a csv file using Pandas. You are given a dataset of demographic data that was extracted from the 1994 Census database.

You must use Pandas to answer the following questions:

How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)

What is the average age of men?

What is the percentage of people who have a Bachelor's degree?

What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?

What percentage of people without advanced education make more than 50K?

What is the minimum number of hours a person works per week?

What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?

What country has the highest percentage of people that earn >50K and what is that percentage?

Identify the most popular occupation for those who earn >50K in India.


------------------------------------------------------------
MEDICAL DATA VISUALIZER

In this project, you will visualize and make calculations from medical examination data using matplotlib, seaborn, and pandas. The dataset values were collected during medical examinations.

The rows in the dataset represent patients and the columns represent information like body measurements, results from various blood tests, and lifestyle choices. You will use the dataset to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.

Create a chart similar to examples/Figure_1.png, where we show the counts of good and bad outcomes for the cholesterol, gluc, alco, active, and smoke variables for patients with cardio=1 and cardio=0 in different panels.

Use the data to complete the following tasks in medical_data_visualizer.py:

Add an overweight column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.

Normalize the data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, make the value 0. If the value is more than 1, make the value 1.

Convert the data into long format and create a chart that shows the value counts of the categorical features using seaborn's catplot(). The dataset should be split by 'Cardio' so there is one chart for each cardio value. The chart should look like examples/Figure_1.png.

Clean the data. Filter out the following patient segments that represent incorrect data:

-diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))

-height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))

-height is more than the 97.5th percentile

-weight is less than the 2.5th percentile

-weight is more than the 97.5th percentile

Create a correlation matrix using the dataset. Plot the correlation matrix using seaborn's heatmap(). Mask the upper triangle. The chart should look like examples/Figure_2.png.


---------------------------------------------------------------------
TIME SERIES VISUALIZER

For this project you will visualize time series data using a line chart, bar chart, and box plots. You will use Pandas, Matplotlib, and Seaborn to visualize a dataset containing the number of page views each day on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03. The data visualizations will help you understand the patterns in visits and identify yearly and monthly growth.


----------------------------------------------------------------------
SEA LEVEL PREDICTOR

You will analyze a dataset of the global average sea level change since 1880. You will use the data to predict the sea level change through year 2050.

The scatter plot of original data will contain a line of best fit for the given data and project the trend up to 2050. A second line of best fit will also be included to show the increased upward trend starting from 2000 and projecting to 2050 as well.
