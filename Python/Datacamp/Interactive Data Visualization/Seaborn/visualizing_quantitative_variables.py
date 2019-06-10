# Change to use relplot() instead of scatterplot()
sns.relplot(x="absences", y="G3", 
                data=student_data,
                kind='scatter',
                col="study_time",
                row="study_time")

# Show plot
plt.show()


# Adjust further to add subplots based on family support
sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter", 
            col="schoolsup",
            col_order=["yes", "no"],
            row='famsup',
            row_order=['yes', 'no'])

# Show plot
plt.show()

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot of horsepower vs. mpg
	sns.relplot(x="horsepower", y="mpg", 
	            data=mpg, kind="scatter", 
	            size="cylinders",
	            hue='cylinders')

# Show plot
plt.show()

# Create a scatter plot of acceleration vs. mpg
sns.relplot(x="acceleration", y="mpg", 
            data=mpg, kind="scatter", 
            style="origin",
            hue='origin')


## Line plots

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot
sns.relplot(x='model_year', y='mpg',
            data=mpg,
            kind='line')


# Show plot
plt.show()

## Visualizing standard deviation with line plots

# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line",
            ci='sd')

# Show plot
plt.show()

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Add markers and make each line have the same style
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None, style="origin", 
            hue="origin",
            markers=True,
            dashes=False)

# Show plot
plt.show()