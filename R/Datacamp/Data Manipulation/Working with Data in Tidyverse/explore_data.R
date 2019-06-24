# Load dplyr
library(dplyr)

# Filter rows where showstopper is UNKNOWN 
bakeoff %>% 
    filter(showstopper == "UNKNOWN")

# Edit to add list of missing values
bakeoff <- read_csv("bakeoff.csv", skip = 1,
                    na = c("", "NA", "UNKNOWN"))

# Filter rows where showstopper is NA 
bakeoff %>% filter(is.na(showstopper))


bakeoff %>% arrange(us_airdate) %>% glimpse()


# Summarize your data
"
You can combine skim() with other functions in a sequence using the pipe (%>%) operator. For example, you could use other dplyr functions like group_by first, then use skim() by adding a line after the final pipe.
"

# Load skimr
library(skimr)

# Edit to filter, group by, and skim
bakeoff %>% 
  filter(!is.na(us_season)) %>% 
  group_by(us_season)  %>% 
  skim()


# How many variables of each type do we have in the bakeoff data? 
bakeoff %>% skim() %>% summary()


# Distinct and count

# Count rows for each result
bakeoff %>% 
    count(result)

# Count whether or not star baker
bakeoff %>% 
  count(result == 'SB')


# Count episodes

# Find format to parse uk_airdate 
parse_date(bakeoff$uk_airdate, format = "%Y-%m-%d")

# Adapt your code to add a second count() by series again to count the total number of episodes per series.
# Add second count by series
bakeoff %>% 
  count(series, episode) %>%
  count(series)



# Count bakers

# Count the number of rows by series and baker
bakers_by_series <- bakeoff %>% 
  count(series, baker)
  
# Print to view
bakers_by_series
  
# Count again by series; Which series had the most bakers? Which had the least?
bakers_by_series %>% 
  count(series)
  
# Count again by baker; What's the most common baker name?
bakers_by_series %>% count(baker, sort = TRUE)



# Plot
ggplot(bakeoff, aes(episode)) + 
    geom_bar() + 
    facet_wrap(~series)

