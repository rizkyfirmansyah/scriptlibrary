# View the first 6 rows of data
head(weather)

# View the last 6 rows of data
tail(weather)

# View a condensed summary of the data
str(weather)


'''
The first thing to do when you get your hands on a new dataset is to understand its structure. There are several ways to go about this in R, each of which may reveal different issues with your data that require attention.

In this course, we are only concerned with data that can be expressed in table format (i.e. two dimensions, rows and columns). As you may recall from earlier courses, tables in R often have the type data.frame. You can check the class of any object in R with the class() function.

Once you know that you are dealing with tabular data, you may also want to get a quick feel for the contents of your data. Before printing the entire dataset to the console, it\'s probably worth knowing how many rows and columns there are. The dim() command tells you this.

'''

# Check the class of bmi
class(bmi)

# Check the dimensions of bmi
dim(bmi)

# View the column names of bmi
names(bmi)


'''
str() and glimpse() give you a preview of your data, which may reveal issues with the way columns are labelled, how variables are encoded, etc.

You can use the summary() command to get a better feel for how your data are distributed, which may reveal unusual or extreme values, unexpected missing data, etc. For numeric variables, this means looking at means, quartiles (including the median), and extreme values. For character or factor variables, you may be curious about the number of times each value appears in the data (i.e. counts), which summary() also reveals.
'''

# Check the structure of bmi
str(bmi)

# Load dplyr
library(dplyr)

# Check the structure of bmi, the dplyr way
glimpse(bmi)

# View a summary of bmi
summary(bmi)


