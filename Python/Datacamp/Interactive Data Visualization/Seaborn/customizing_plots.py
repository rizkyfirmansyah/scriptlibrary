# Changing style and palette

# Set the style to "whitegrid"
sns.set_style('whitegrid')
sns.set_palette('Purples') # Set the color palette to "Purples"
sns.set_palette("RdBu") # Change the color palette to "RdBu"


# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", 
                  "Often", "Always"]

sns.catplot(x="Parents Advice", 
            data=survey_data, 
            kind="count", 
            order=category_order)

# Show plot
plt.show()

# Changing the scale

# Set the context to "paper"
sns.set_context('paper')
# Change the context to "notebook"
sns.set_context("notebook") # increase the size
sns.set_context("talk") # increase more than notebook
sns.set_context("poster") # largest scale available

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")

# Show plot
plt.show()

# Set the style to "darkgrid"
sns.set_style('darkgrid')

# Set a custom color palette
sns.set_palette(['#39A7D0', '#36ADA4'])

# Create the box plot of age distribution by gender
sns.catplot(x="Gender", y="Age", 
            data=survey_data, kind="box")

# Show plot
plt.show()

## FacetGrids > catplot() and relplot() vs. AxesSubplots scatterplot() boxplot()

# Adding a title to a FacetGrid object

# Create scatter plot
g = sns.relplot(x="weight", 
                y="horsepower", 
                data=mpg,
                kind="scatter")

# Add a title "Car Weight vs. Horsepower"
g.fig.suptitle('Car Weight vs. Horsepower') # FacetGrids

# Show plot
plt.show()


## Adding a title and axis labels
# Create line plot
g = sns.lineplot(x="model_year", y="mpg_mean", 
                 data=mpg_mean,
                 hue="origin")

# Add a title "Average MPG Over Time"
g.set_title('Average MPG Over Time') # AxesSubplots

# Add x-axis and y-axis labels
g.set(xlabel='Car Model Year',
    ylabel='Average MPG')

# Show plot
plt.show()

## Rotating X-ticks label
# Create point plot
sns.catplot(x="origin", 
            y="acceleration", 
            data=mpg, 
            kind="point", 
            join=False, 
            capsize=0.1)

# Rotate x-tick labels
plt.xticks(rotation=90)

# Show plot
plt.show()

# Box plot with subgroups

# Set palette to "Blues"
sns.set_palette('Blues')

# Adjust to add subgroups based on "Interested in Pets"
g = sns.catplot(x="Gender",
                y="Age", data=survey_data, 
                kind="box", hue='Interested in Pets')

# Set title to "Age of Those Interested in Pets vs. Not"
g.fig.suptitle('Age of Those Interested in Pets vs. Not')

# Show plot
plt.show()


# Set the figure style to "dark"
sns.set_style('dark')

# Adjust to add subplots per gender
# Adjust the bar plot code to add subplots based on "Gender", arranged in columns.
g = sns.catplot(x="Village - town", y="Likes Techno", 
                data=survey_data, kind="bar",
                col='Gender')

# Add title and axis labels
g.fig.suptitle("Percentage of Young People Who Like Techno", y=1.02)
g.set(xlabel="Location of Residence", 
       ylabel="% Who Like Techno")

# Show plot
plt.show()


###
