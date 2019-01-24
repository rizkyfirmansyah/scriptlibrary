'''
Tidyr function
gather()
spread()
separate()
unite()
'''

'''
The most important function in tidyr is gather(). It should be used when you have columns that are not variables and you want to collapse them into key-value pairs.

The easiest way to visualize the effect of gather() is that it makes wide datasets long. As you saw in the video, running the following command on wide_df will make it long:

gather(wide_df, my_key, my_val, -col)

'''

'''
\'data.frame\':	199 obs. of  30 variables:
 $ Country: chr  "Afghanistan" "Albania" "Algeria" "Andorra" ...
 $ Y1980  : num  21.5 25.2 22.3 25.7 20.9 ...
 $ Y1981  : num  21.5 25.2 22.3 25.7 20.9 ...
 $ Y1982  : num  21.5 25.3 22.4 25.7 20.9 ...
 $ Y1983  : num  21.4 25.3 22.5 25.8 20.9 ...
 $ Y1984  : num  21.4 25.3 22.6 25.8 20.9 ...
'''

# Apply gather() to bmi and save the result as bmi_long
bmi_long <- gather(bmi, year, bmi_val, -Country)

# View the first 20 rows of the result
head(bmi_long, n = 20)


'''
The opposite of gather() is spread(), which takes key-values pairs and spreads them across multiple columns. This is useful when values in a column should actually be column names (i.e. variables). It can also make data more compact and easier to read.

The easiest way to visualize the effect of spread() is that it makes long datasets wide. As you saw in the video, running the following command will make long_df wide:

spread(long_df, my_key, my_val)

'''

# Apply spread() to bmi_long
bmi_wide <- spread(bmi_long, year, bmi_val)

# View the head of bmi_wide
head(bmi_wide)

'''
The separate() function allows you to separate one column into multiple columns. Unless you tell it otherwise, it will attempt to separate on any character that is not a letter or number. You can also specify a specific separator using the sep argument
'''


# Apply separate() to bmi_cc
bmi_cc_clean <- separate(bmi_cc, col = Country_ISO, into = c("Country", "ISO"), sep = "/")

# Print the head of the result
head(bmi_cc_clean)


'''
The unit() function allows you to take multiple columns and pastes them together. By default, the contents of the columns will be separated by underscores in the new column, but this behavior can be altered via the sep argument.
'''

# Apply unite() to bmi_cc_clean
bmi_cc <- unite(bmi_cc_clean, Country_ISO, Country, ISO, sep = "-")

# View the head of the result
head(bmi_cc)

# View the head of census
head(census)

# Gather the month columns
census2 <- gather(census, month, amount, -YEAR)

# Arrange rows by YEAR using dplyr's arrange
census2_arr <- arrange(census2, YEAR)

# View first 20 rows of census2
head(census2_arr, n = 20)


# View first 50 rows of census_long
head(census_long, 50)

# Spread the type column
census_long2 <- spread(census_long, type, amount)

# View first 20 rows of census_long2
head(census_long2, 20)

# View the head of census_long3
head(census_long3)

# Separate the yr_month column into two
census_long4 <- separate(census_long3, yr_month, c("year", "month"))

# View the first 6 rows of the result
head(census_long4)

