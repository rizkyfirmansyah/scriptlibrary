'''
haven is an extremely easy-to-use package to import data from three software packages: SAS, STATA and SPSS. Depending on the software, you use different functions:

SAS: read_sas()
STATA: read_dta() (or read_stata(), which are identical)
SPSS: read_sav() or read_por(), depending on the file type.

'''

# Load the haven package
library(haven)

# Import sales.sas7bdat: sales
sales <- read_sas("sales.sas7bdat")

# Display the structure of sales
str(sales)

# haven is already loaded

# Import the data from the URL: sugar
sugar <- read_dta("http://assets.datacamp.com/production/course_1478/datasets/trade.dta")

# Structure of sugar
str(sugar)

# Convert values in Date column to dates
sugar$Date <- as.Date(as_factor(sugar$Date))

# Structure of sugar again
str(sugar)


### Import SPSS

'''
Depending on the SPSS data file you\'re working with, you\'ll need either read_sav() - for .sav files - or read_por() - for .por files.

'''

# haven is already loaded

# Import person.sav: traits
traits <- read_sav("person.sav")

# Summarize traits
summary(traits)

# Print out a subset
subset(traits, Extroversion > 40 & Agreeableness > 40)


### Import with foreign package

# Load the foreign package
library(foreign)

# Import florida.dta and name the resulting data frame florida
florida <- read.dta("florida.dta")

# Check tail() of florida
tail(florida)

'''
The arguments you will use most often are convert.dates, convert.factors, missing.type and convert.underscore. Their meaning is pretty straightforward, as Filip explained in the video

'''

# foreign is already loaded

# Specify the file path using file.path(): path
path <- file.path("worldbank", "edequality.dta")

# Create and print structure of edu_equal_1
edu_equal_1 <- read.dta(path)
str(edu_equal_1)

# Create and print structure of edu_equal_2
edu_equal_2 <- read.dta(path, convert.factors = FALSE)
str(edu_equal_2)

# Create and print structure of edu_equal_3
edu_equal_3 <- read.dta(path, convert.underscore = TRUE)
str(edu_equal_3)

### Import SPSS with foreign

'''
read.spss() to read SPSS data files. To get a data frame, make sure to set to.data.frame = TRUE inside read.spss().

'''

# foreign is already loaded

# Import international.sav as a data frame: demo
demo <- read.spss("international.sav", to.data.frame = TRUE)

# Create boxplot of gdp variable of demo
boxplot(demo$gdp)

'''
If you\'re familiar with statistics, you\'ll have heard about Pearson\'s Correlation. It is a measurement to evaluate the linear dependency between two variables, say X and Y. It can range from -1 to 1; if it\'s close to 1 it means that there is a strong positive association between the variables. If X is high, also Y tends to be high. If it\'s close to -1, there is a strong negative association: If X is high, Y tends to be low. When the Pearson correlation between two variables is 0, these variables are possibly independent: there is no association between X and Y.
'''


'''
In this exercise you will experiment with another argument, use.value.labels. It specifies whether variables with value labels should be converted into R factors with levels that are named accordingly. The argument is TRUE by default which means that so called labelled variables inside SPSS are converted to factors inside R.
'''

# foreign is already loaded

# Import international.sav as demo_1
demo_1 <- read.spss("international.sav", to.data.frame = TRUE)

# Print out the head of demo_1
head(demo_1)

# Import international.sav as demo_2
demo_2 <- read.spss("international.sav", to.data.frame = TRUE, use.value.labels = FALSE)

# Print out the head of demo_2
head(demo_2)

