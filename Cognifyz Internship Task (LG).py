#!/usr/bin/env python
# coding: utf-8

# In[301]:


#Task 1
#Importing the neccesary libraries

import pandas as pd 
import numpy as np
import sklearn as sk
import matplotlib.pyplot as plt
import seaborn as sns


# In[302]:


#Loading the dataset
df = pd.read_csv ('internship data.csv')


# In[303]:


df.shape 


# In[304]:


df.head ()


# In[305]:


df.tail()


# In[306]:


df.describe()


# In[307]:


df.isnull().sum()


# In[308]:


# Gathering Information about the data
df.info()


# In[309]:


# Check for duplicates along rows
duplicates = df[df.duplicated(subset=df.columns)]

# Print the duplicates
print("Duplicate rows:")
print(duplicates)


# In[310]:


# Task 2

# Extracting Gender Information
gender_data = df['gender']


# In[311]:


# Frequency distribution of 'Gender'
gender_counts = df['gender'].value_counts()
gender_percentage = (gender_counts / len(df)) * 100


# In[312]:


gender_distribution = pd.DataFrame({'Counts': gender_counts, 'Percentage': gender_percentage})


# In[313]:


gender_distribution = pd.DataFrame({'Counts': gender_counts, 'Percentage': gender_percentage})


# In[314]:


# Create a bar plot
plt.figure(figsize=(12, 6))
plt.title("Gender Distribution")
plt.bar(gender_counts.index, gender_counts.values, color = ['Skyblue','Green'])
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()


# In[315]:


# Task 3

# Extracting age Information
age_data = df['age']


# In[316]:


age_counts = df['age'].value_counts()
age_income = (age_counts / len(df)) * 100


# In[317]:


age_distribution = pd.DataFrame({'Counts': age_counts, 'income': age_income})


# In[318]:


print("\nAge Distribution:")
print(age_distribution)


# In[ ]:





# In[319]:


# calculating using statistical analysis of Age
mean_age = df['age'].mean()

median_age = df['age'].median()

std_dev_age = df['age'].std()

print(f"Mean Age: {mean_age}")
print(f"Median Age: {median_age}")
print(f"standard deviation of Age: {std_dev_age}")


# In[ ]:





# In[320]:


# Task 4

#Analyse investment Avenues

data = {
    'Avenue': ['Mutual fund', 'Equity', 'Fixed Deposits', 'Public Providence fund']
}

# Count the occurences of each avenue
avenue_counts = df['Avenue'].value_counts()

# Display the Counts
print(avenue_counts)

# Determine the  avenue with the highest frequency
most_frequency_avenue = avenue_counts.idxmax()
max_count = avenue_counts.max()

print(f"The avenue with the highest frequency is: {most_frequency_avenue}")
print(f"it appears {max_count} times in the dataset.")


# In[321]:


# Freqeuncy Analysis of investment avenue

plt.figure(figsize=(8, 5))
avenue_counts.plot(kind='bar', color='skyblue')
plt.title('Distribution of Investment Avenues')
plt.xlabel('Investment Avenue')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


# In[ ]:





# In[322]:


# Task 5

# Explore Reasons Column
data = {
    'Purpose': [
        'wealth creation','Savings for future', 'Returns',
    ]
}

# Count the occurences of each avenue
Purpose_counts = df['Purpose'].value_counts()

# Display the Counts
print(Purpose_counts)

# Determine the purpose with the highest frequency
most_frequency_Purpose = Purpose_counts.idxmax()
max_count = Purpose_counts.max()

print(f"The purpose with the highest frequency is: {most_frequency_Purpose}")
print(f"it appears {max_count} times in the dataset.")



# In[323]:


# Summarize Purpose Reasons

plt.figure(figsize=(8, 5))
Purpose_counts.plot(kind='bar', color='orange')
plt.title('Purpose of investment choices')
plt.xlabel('Investment Choices')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


# In[324]:


# Task 6

# Examine the column containing information about participants Objectives

# Analyzing Objective

data = {
    'Objective': [
        'Capital Appreciation', 'Growth', 'Income', 
        
    ]
}

# inspect the first few entries

print("First few entries of the 'Objective' column:")
print(df['Objective'].head())

# identify unique Objectives

unique_Objective = df['Objective'].unique()
print("\nUnique Objective:")
print(unique_Objective)

# Frequency Analysis

objective_counts = df['Objective'].value_counts()
print("\nFrequency of Each Objective:")
print(objective_counts)


# In[325]:


# List and describe objectives

Objective_counts = df['Objective'].value_counts()

# Plotting the bar chart

plt.figure(figsize=(8, 5))
Objective_counts.plot(kind='bar', color='Green')
plt.title('Purpose of Savings Objective')
plt.xlabel('Savings Objective')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


# In[326]:


# Task 7

# inspect the column
print("First few entries of the 'information_sources' column:")
print(df['Source'].head())

# identify unique sources of common information
unique_sources = df['Source'].unique()
print("\nUnique Sources of Information:")
print(unique_sources)

# perform frequency analysis on the sources
source_counts = df['Source'].value_counts()
print("\nFrequency of Each Source of Investment Information:")
print(source_counts)

# Visualize the Common information sources

plt.figure(figsize=(10, 6))
source_counts.plot(kind='bar', color='skyblue')
plt.title('Sources of Investment Information')
plt.xlabel('Source')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


# In[327]:


# Step 1: Perform frequency analysis on the sources of investment information
source_counts = df['Source'].value_counts()

# Step 2: Identify the most common sources (Top N, if desired)
most_common_sources = source_counts.head(5)  # Change the number to top N sources if needed

# Step 3: Summarize the findings
print("Most Common Sources of Investment Information:")
print(most_common_sources)

# Step 4: (Optional) Visualize the top sources with a bar chart

plt.figure(figsize=(10, 6))
most_common_sources.plot(kind='bar', color='lightgreen')
plt.title('Top Sources of Investment Information')
plt.xlabel('Source')
plt.ylabel('Count')
plt.xticks(rotation=45)


# In[328]:


# Task 8

# Inspect the first few entries

print("First few entries of the 'Duration' column:")
print(df['Duration'].head())


# In[329]:


# Summary statistics

duration_summary = df['Duration'].describe()
print("\nSummary Statistics for 'Duration':")
print(duration_summary)


# In[330]:


# Frequency distribution

duration_counts = df['Duration'].value_counts()
print("\nFrequency of Each Duration:")
print(duration_counts)


# In[331]:


# Plot the distribution

plt.figure(figsize=(10, 6))
df['Duration'].hist(bins=20, color='blue', edgecolor='black')
plt.title('Distribution of Durations')
plt.xlabel('Duration (in years or relevant unit)')
plt.ylabel('Frequency')
plt.show()


# In[ ]:





# In[ ]:





# In[332]:


# Example data
data = {
    'Investment Duration': [
        '1-3 years', 'More than 5 years', '3-5 years', 'Less than 1 year',
        'Less than 1 year', '1-3 years', '3-5 years', '3-5 years',
        '1-3 years', '3-5 years', '3-5 years', '1-3 years',
        # Add more entries as needed
    ]
}

df = pd.DataFrame(data)

# Mapping investment durations to numeric values
duration_mapping = {
    'Less than 1 year': 0.5,
    '1-3 years': 2,
    '3-5 years': 4,
    'More than 5 years': 6  # or another value like 7, depending on your assumption
}

# Apply the mapping to convert text to numeric values
df['Numeric Duration'] = df['Investment Duration'].map(duration_mapping)

# Now calculate the average duration
average_duration = df['Numeric Duration'].mean()

# Display the result
print(f"The average investment duration is: {average_duration:.2f} years")


# In[ ]:





# In[ ]:





# In[333]:


# Task 9

# Create a summary list of expectations

expectations_summary = [
    {
        "Expectation Range": "20%-30%",
        "Description": "This range indicates moderate expectations, where participants anticipate a steady and reasonable return on their investment. This is the most common expectation, suggesting that many participants are seeking balanced growth."
    },
    {
        "Expectation Range": "30%-40%",
        "Description": "Participants with this expectation are aiming for higher returns. This group likely includes those who are willing to take on more risk for the possibility of greater rewards."
    },
    {
        "Expectation Range": "10%-20%",
        "Description": "This expectation range reflects a more conservative outlook, where participants expect lower returns. These participants may prioritize security and stability over high returns."
    }
]

# Display the expectations summary

for expectation in expectations_summary:
    print(f"Expectation Range: {expectation['Expectation Range']}")
    print(f"Description: {expectation['Description']}\n")


# In[ ]:





# In[ ]:





# In[334]:


# Task 10

# Calculate the correlation analysis
correlation_analysis = selected_columns.corr()

print(correlation_analysis)


# In[335]:


# Scatter plot between Age and Investment Duration

sns.scatterplot(x='age', y='Duration', data=selected_columns)
plt.title('Scatter plot: Age vs Duration')
plt.xlabel('age')
plt.ylabel('Duration')
plt.show()


# In[ ]:




