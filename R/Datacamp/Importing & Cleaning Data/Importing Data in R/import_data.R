### Importing data

# With stringsAsFactors, you can tell R whether it should convert strings in the flat file to factors.

pools <- read.csv("swimming_pools.csv", stringsAsFactors = FALSE)

# Check the structure of pools
str(pools)

hotdogs <- read.delim("hotdogs.txt", header = FALSE)

# read.delim - header defaults to TRUE; while sep = "\t" by default
# read.table - header defaults to FALSE; while sep = " " by default

path <- file.path("data", "hotdogs.txt")

# Import the hotdogs.txt file: hotdogs
hotdogs <- read.table(path,
                      sep = "\t",
                      col.names = c("type", "calories", "sodium"))

#
# Finish the read.delim() call
hotdogs <- read.delim("hotdogs.txt", header = FALSE, col.names = c("type", "calories", "sodium"))

# Select the hot dog with the least calories: lily
lily <- hotdogs[which.min(hotdogs$calories), ]

# Select the observation with the most sodium: tom
tom <- hotdogs[which.max(hotdogs$sodium), ]

# Print lily and tom
print(lily)
print(tom)

##
hotdogs2 <- read.delim("hotdogs.txt", header = FALSE,
                       col.names = c("type", "calories", "sodium"),
                       colClasses = c("factor", "NULL", "numeric")


## library readr
'''
library(readr)
read_delim()
read_csv()
read_tsv()
'''
potatoes <- read_csv("potatoes.csv")

# read_delim
'''
col_types = 'cdil_'
c = character
d = double
i = integer
l = logical
_ = skip
'''
properties <- c("area", "temp", "size", "storage", "method",
                "texture", "flavor", "moistness")

# Import potatoes.txt using read_delim(): potatoes
potatoes <- read_delim("potatoes.txt", delim = "\t", col_names = properties)

##
fac <- col_factor(levels = c("Beef", "Meat", "Poultry"))
int <- col_integer()

# Edit the col_types argument to import the data correctly: hotdogs_factor
hotdogs_factor <- read_tsv("hotdogs.txt",
                           col_names = c("type", "calories", "sodium"),
                           col_types = list(fac, int, int))

# required data.table package
# fread(file, select = "", drop = "")
potatoes <- fread("potatoes.csv", select = c(6, 8))

# Plot texture (x) and moistness (y) of potatoes
plot(potatoes$texture, potatoes$moistness)

## readxl
'''
require(readxl)

excel_sheets()
read_excel()
'''

pop_1 <- read_excel("urbanpop.xlsx", sheet = 1)
pop_2 <- read_excel("urbanpop.xlsx", sheet = 2)
pop_3 <- read_excel("urbanpop.xlsx", sheet = 3)

# Put pop_1, pop_2 and pop_3 in a list: pop_list
pop_list <- list(pop_1, pop_2, pop_3)

# Display the structure of pop_list
str(pop_list)

# Read all Excel sheets with lapply(): pop_list
pop_list <- lapply(excel_sheets("urbanpop.xlsx"),
                    read_excel,
                    path = "urbanpop.xlsx")

# Display the structure of pop_list
str(pop_list)

#
cols <- c("country", paste0("year_", 1960:1966))
pop_b <- read_excel("urbanpop_nonames.xlsx", sheet = 1, col_names = cols)

head(pop_b, n = 2)

# gdata
'''
Using perl to read xls data source and converted into csv format while R will read csv with the read.csv() function that is loaded by default, through the utils package
read.xls()

'''
library(gdata)

columns <- c("country", paste0("year_", 1967:1974))

# Finish the read.xls call
urban_pop <- read.xls("urbanpop.xls", sheet = 2,
                      skip = 50, header = FALSE, stringsAsFactors = FALSE,
                      col.names = columns)
