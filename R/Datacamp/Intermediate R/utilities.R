# Extract the name column from titanic
pass_names <- titanic$Name

# Create the logical vector is_man
is_man <- grepl(", Mr\\.", pass_names)

# Count the number of men
sum(is_man)

# Count number of men based on gender
sum(titanic$Sex == "male")


"""
In the previous exercise, it appeared that the title Mr. may not cover all men on board. Instead of manually going through all titles that appear in the Name column of titanic, we can write a clever gsub() command that extracts the title part.

The pattern we'll need is the following:

"^.*, (.*?)\\..*$"
With ^ and $ we signify the start and end of the string. Next, we have two .* parts in there: wildcards for the last name and first names. With , (.*?)\\. we use a similar pattern as before, but the parentheses allow us to re-use whatever is matched inside the parentheses in our replacement.

"""

# Extract the name column from titanic
pass_names <- titanic$Name

# Create titles
titles <- gsub("^.*, (.*?)\\..*$", "\\1", pass_names)

# Call unique() on titles
unique(titles)

[1] "Mr"           "Mrs"          "Miss"         "Master"       "Don"         
 [6] "Rev"          "Dr"           "Mme"          "Ms"           "Major"       
[11] "Lady"         "Sir"          "Mlle"         "Col"          "Capt"        
[16] "the Countess" "Jonkheer"

"""
To figure out which passenger has which title, we can create a matrix. In this matrix, each passenger is a row, and each column represents a title. If a certain matrix element is TRUE, this means that the passenger has the title. This also means that every row can only contain one TRUE, the rest being FALSE, because titles are mutually exclusive. That is, nobody is titled both Mr. and Major, for instance. To end up with this matrix, we could use the following for loop:

res <- matrix(nrow = length(pass_names),
              ncol = length(titles))

for (i in seq_along(titles)) {
  res[, i] <- grepl(titles[i], pass_names)
}

There's a way more concise way to do this, however. Remember the vapply() function from the third chapter? You can use it to call grepl() over all titles in the titles vector, with pass_names as an additional argument. If you do this properly, you'll end up with the exact same matrix described above. Simply taking the sum of this matrix should give us the total number of hits for each title, and thus the total count of males inferred from their respective titles.
"""

# Create variables for passenger names and titles
pass_names <- titanic$Name
titles <- paste(",", c("Mr\\.", "Master", "Don", "Rev", "Dr\\.", "Major", "Sir", "Col", "Capt", "Jonkheer"))

# Finish the vapply() command
hits <- vapply(titles,
               FUN = grepl,
               FUN.VALUE = logical(length(pass_names)),
               pass_names)

# Calculate the sum() of hits
sum(hits)

# Count number of men based on gender
sum(titanic$Sex == "male")


# Finish the convert_name() function
convert_name <- function(name) {
  # women: take name from inside parentheses
  if (grepl("\\(.*?\\)", name)) {
    gsub("^.*?\\((.*?)\\)$", "\\1", name)
  # men: take name before comma and after title
  } else {
    # Finish the gsub() function
    gsub("^(.*?),\\s[a-zA-Z\\.]*?\\s(.*?)$", "\\2 \\1", name)
  }
}

# Call convert_name on name
clean_pass_names <- vapply(pass_names, FUN = convert_name,
                           FUN.VALUE = character(1), USE.NAMES = FALSE)

# Print out clean_pass_names
clean_pass_names

"""
Suppose we want to change men's names to a modern format, without a title, and change the women's names to only include their own name, like this:

> clean_pass_names[1:2]
[1] "Owen Harris Braund"
[2] "Florence Briggs Thayer"
To make this conversion, we've started a function convert_name() that converts the name depending on the case (male or female). The first gsub() function uses \\1 as the replacement argument. This is a reference to the matched characters that are captured inside the parentheses of the pattern. To see how it works, try the following example in the console:

gsub("(a|b|c)", "_\\1_", "all cool brother")

"""

# Have a look at head() of dob1 and dob2
head(dob1)
head(dob2)

# Convert dob1 to dob1d, convert dob2 to dob2d
dob1d <- as.Date(dob1)
dob2d <- as.Date(dob2, format = "%B %d, %Y")

# Combine dob1d and dob2d into single vector: birth_dates
birth_dates <- c(dob1d, dob2d)

# titanic, dob1 and dob2 are preloaded
dob1d <- as.Date(dob1)
dob2d <- as.Date(dob2, format = "%B %d, %Y")
birth_dates <- c(dob1d, dob2d)
disaster_date <- as.Date("1912-04-15")

# Add birth_dates to titanic (column Birth)
titanic$Birth <- birth_dates

# Create subset: survivors
survivors <- subset(titanic, Survived == 1)

# Calculate average age of survivors
mean(disaster_date - survivors$Birth, na.rm = TRUE)

