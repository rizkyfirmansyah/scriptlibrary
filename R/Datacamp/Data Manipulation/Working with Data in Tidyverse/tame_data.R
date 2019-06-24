# Cast a character to a number

"
Use parse_number() to practice, then
Use col_number() to cast.
But sometimes you'll need to start with casting, then diagnose parsing problems using a new readr function called problems().
"

# Try to cast technical as a number
desserts <- read_csv("desserts.csv",
                      col_types = cols(
                        technical = col_number())
                     )

# View parsing problems
problems(desserts)

# Edit code to fix the parsing error 
desserts <- read_csv("desserts.csv",
                      col_types = cols(
                        technical = col_number()),
                        na = c("", "NA", "N/A") 
                     )

# View parsing problems
problems(desserts)



# Cast a character to a date

# Find format to parse uk_airdate 
parse_date("17 August 2010", format = "%d %B %Y")

# Edit to cast uk_airdate
desserts <- read_csv("desserts.csv", 
                     na = c("", "NA", "N/A"),
                     col_types = cols(
                       technical = col_number(),
                       uk_airdate = col_date(format = "%d %B %Y")
                     ))

# Print by descending uk_airdate
desserts %>% arrange(desc(uk_airdate))
## Notice that us_airdate didn't need to be cast - this is because the date format %Y-%m-%d is unambiguous, so it is automatically parsed as a date by readr.



# Cast a variable as a factor

"
Factors are categorical variables, where the possible values are a fixed and known set. For example, take a simple factor like bake below:

bake <- c('pie', 'cake', 'neither') 
parse_factor(bake, levels = NULL) 
[1] pie  cake neither
Levels: pie cake neither
Remember to use ?parse_factor to read more about the levels argument. And remember that for every parse_* function, there is a col_* function for casting.
"


# Cast result a factor
desserts <- read_csv("desserts.csv", 
                     na = c("", "NA", "N/A"),
                     col_types = cols(
                       technical = col_number(),
                       uk_airdate = col_date(format = "%d %B %Y"),
                       result = col_factor(levels = NULL)
                     ))
                    
# Glimpse to view
glimpse(desserts)



# Recode a character variable

# Count rows grouping by nut variable
desserts %>% 
    count(nut, sort = TRUE)


# Count rows grouping by nut variable
desserts %>% 
    count(nut, sort = TRUE)
    
# Recode filberts as hazelnuts
desserts_2 <- desserts %>% 
  mutate(nut = recode(nut, "filbert" = "hazelnut"))

# Count rows again 
desserts_2 %>% 
    count(nut, sort = TRUE)


# Count rows grouping by nut variable
desserts %>% 
    count(nut, sort = TRUE)
    
# Edit code to recode "no nut" as missing
desserts_2 <- desserts %>% 
  mutate(nut = recode(nut, "filbert" = "hazelnut", 
                           "no nut" = NA_character_))

# Count rows again 
desserts_2 %>% 
    count(nut, sort = TRUE)

##  NA is a logical constant, so it is always helpful to remember the NA constants like NA_character_ and NA_integer_ when working with strings or numbers. Always know your variable types!



# Recode a numeric variable

# Create dummy variable: 1 if won, 0 if not
desserts <- desserts %>% 
  mutate(tech_win = recode(technical, `1` = 1,
                           .default = 0))


# You may have noticed that tech_win is a numeric variable (a dbl). Adapt your code to use recode_factor() instead of recode to convert it to a factor.
# Edit to recode tech_win as factor
desserts <- desserts %>% 
  mutate(tech_win = recode_factor(technical, `1` = 1,
                           .default = 0))

# Count to compare values                      
desserts %>% 
  count(technical == 1, tech_win)



# Recode factor to plot

# Recode channel as factor: bbc (1) or not (0)
ratings <- ratings %>% 
  mutate(bbc = recode_factor(channel, 
                             "Channel 4" = 0,
                             .default = 1))
                            
# Select to look at variables to plot next
ratings %>% 
  select(series, channel, bbc, viewer_growth)
  
# Make a filled bar chart
ggplot(ratings, aes(x = series, y = viewer_growth, fill = bbc)) +
  geom_col()



# Select and reorder variables
"

The select() helpers allow you to select variables based on their names.

In this exercise, you'll work with the ratings data to practice combining helpers, and you'll use a new helper function called everything() which can be useful when reordering columns. Use ?everything to read more.
"

# Move channel to first column
ratings %>% 
  select(channel, everything())

# Drop 7- and 28-day episode ratings
ratings %>% 
  select(-ends_with("day"))

# Move channel to front and drop 7-/28-day episode ratings
ratings %>% 
  select(channel, everything(), -ends_with("day"))
## everything() is a great little helper! If it had been placed at the end, it would have added back in all the columns that end with "day". Placing it before deselecting columns, though, is a real time-saver



# Reformat variables

# Glimpse to see variable names
glimpse(messy_ratings)

# Load janitor
library(janitor)

# Reformat to lower camelcase
ratings <- messy_ratings %>%
  clean_names(., "lower_camel")
    
# Glimpse new tibble
glimpse(ratings)


# Reformat to snake case
ratings <- messy_ratings %>%  
  clean_names("snake")



# Rename and subset variables

# Select 7-day viewer data by series
viewers_7day <- ratings %>%
    select(series, ends_with("7day"))

# Glimpse
glimpse(viewers_7day)

# Adapt your code to rename each 7-day viewers variable to viewers_7day_<episode>, where <episode> takes on all the possible episode values.

# Adapt code to also rename 7-day viewer data
viewers_7day <- ratings %>% 
    select(series, viewers_7day_ = ends_with("7day"))

# Glimpse
glimpse(viewers_7day)



# Rename and reorder variables
# Adapt code to drop 28-day columns; keep 7-day in front
viewers_7day <- ratings %>% 
    select(viewers_7day_ = ends_with("7day"),
        everything(),
        -ends_with("28day"))

# Glimpse
glimpse(viewers_7day)


# Adapt code to keep original order
viewers_7day <- ratings %>% 
    select(everything(), viewers_7day_ = ends_with("7day"), 
           -ends_with("28day"))

# Glimpse
glimpse(viewers_7day)

