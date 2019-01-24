## Removing duplicate info

my_df[, -3] # Omit third column

# Define vector of duplicate cols (don't change)
duplicates <- c(4, 6, 11, 13, 15, 17, 18, 20, 22, 
                24, 25, 28, 32, 34, 36, 38, 40, 
                44, 46, 48, 51, 54, 65, 158)

# Remove duplicates from food: food2
food2 <- food[, -duplicates]


# Define useless vector (don't change)
useless <- c(1, 2, 3, 32:41)

# Remove useless columns from food2: food3
food3 <- food2[, -useless]


## Finding columns

'''
All of the columns with nutrition info contain the character string "100g" as part of their name, which makes it easy to identify them.

stringr and food3 are pre-loaded in your workspace.
'''

# Create vector of column indices: nutrition
nutrition <- str_detect(names(food3), "100g")

# View a summary of nutrition columns
summary(food3[, nutrition])


## Replacing missing values

'''
In this exercise, you\'ll replace all NA values with zeroes in the sugars_100g column and make histograms to visualize the result. Then, you will exclude the observations which have no sugar to see how the distribution changes.

'''

# Find indices of sugar NA values: missing
missing <- is.na(food3$sugars_100g)

# Replace NA values with 0
food3$sugars_100g[missing] <- 0

# Create first histogram
hist(food3$sugars_100g, breaks = 100)

# Create food4
food4 <- food3[food3$sugars_100g > 0, ]

# Create second histogram
hist(food4$sugars_100g, breaks = 100)


## Dealing with messy data

'''
Your dataset has information about packaging, but there\'s a bit of a problem: it\'s stored in several different languages (Spanish, French, and English). This takes messy data to a whole new level! There is no R package to selectively translate, but what if you could just work with the messy data directly?

You\'re in luck! The root word for plastic is same in English (plastic), French (plastique), and Spanish (plastico). To get a general idea of how many of these foods are packaged in plastic, you can look through the packaging column for the string "plasti".

stringr is pre-loaded in your workspace.
'''


# Find entries containing "plasti": plastic
plastic <- str_detect(food3$packaging, "plasti")

# Print the sum of plastic
sum(plastic)

