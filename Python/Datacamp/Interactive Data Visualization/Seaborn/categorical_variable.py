# Count plots

# Create column subplots based on "Age Category", which separates respondents into those that are younger than 21 vs. 21 and older.
sns.catplot(y="Internet usage", data=survey_data,
            kind="count",
            col='Age Category')

# Show plot
plt.show()


# Bar plots with percentages

# Create a bar plot of interest in math, separated by gender
sns.catplot(x='Gender', y='Interested in Math',
            data=survey_data,
            kind='bar')


# Show plot
# When the y-variable is True/False, bar plots will show the percentage of responses reporting True. This plot shows us that males report a much higher interest in math compared to females.
plt.show()

## Customizing bar plots

# Turn off the confidence intervals
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",
            order=["<2 hours", 
                   "2 to 5 hours", 
                   "5 to 10 hours", 
                   ">10 hours"],
           ci=None)

# Show plot
plt.show()


# Create and interpret a box plot

# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours", 
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
sns.catplot(x='study_time', y='G3', data=student_data,
            kind='box', order=study_time_order)


# Show plot
plt.show()

## Omitting outliers

# Create a box plot with subgroups (colored based on location) and omit the outliers
sns.catplot(x='internet', y='G3', data=student_data,
            kind='box', hue='location',
            sym='')


# Show plot
plt.show()


# Adjusting the whiskers

# Set the whiskers to 0.5 * IQR
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=0.5)

# Show plot
plt.show()

# Extend the whiskers to the 5th and 95th percentile
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[5, 95])

# Show plot
plt.show()


## Point plots
## the median is more robust to outliers, rather than mean. Suppose you have a lot of outliers in your dataset, median is a better statistic to use

# Add caps to the confidence interval
sns.catplot(x="famrel", y="absences",
			data=student_data,
            kind="point",
            capsize=0.2,
            join=False) # Remove the lines joining the points        
# Show plot
plt.show()

# Create a point plot with subgroups
sns.catplot(x='romantic', y='absences',
            data=student_data,
            kind='point',
            hue='school',
            ci=None) # Turn off the confidence intervals for this plot

# Show plot
plt.show()


# Import median function from numpy
from numpy import median

# Plot the median number of absences instead of the mean
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None,
            estimator=median) ## Since there may be outliers of students with many absences, import the median function from numpy and display the median number of absences instead of the average.
# Show plot
plt.show()

