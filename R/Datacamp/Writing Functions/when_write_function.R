# Define example vector x
x <- c(1:10, NA)

# Rewrite this snippet to refer to x
(x - min(x, na.rm = TRUE)) /
  (max(x, na.rm = TRUE) - min(x, na.rm = TRUE))


# Define example vector x
x <- c(1:10, NA)

# Define rng
rng <- range(x, na.rm = TRUE)

# Rewrite this snippet to refer to the elements of rng
(x - min(x, na.rm = TRUE)) /
  (max(x, na.rm = TRUE) - min(x, na.rm = TRUE))


# How many grades in your class are higher than 75?
sum(my_class > 75)

# How many students in your class scored strictly higher than you?
sum(my_class > me)

# What's the proportion of grades below or equal to 64 in the last 5 years?
mean(last_5 <= 64)


# Is your grade greater than 87 and smaller than or equal to 89?
me > 87 & me <= 89

# Which grades in your class are below 60 or above 90?
my_class < 60 | my_class > 90



# What's the proportion of grades in your class that is average?
mean(my_class >= 70 & my_class <= 85)

# How many students in the last 5 years had a grade of 80 or 90?
sum(last_5 == 80 | last_5 == 90)


# Define n_smart
n_smart <- sum(my_class >= 80)

# Code the if-else construct
if (n_smart > 50) {
  print("smart class")
} else {
  print("rather average")
}

# Define prop_less
prop_less <- mean(my_class < me)

# Code the control construct
if (prop_less > 0.9) {
  print("you're among the best 10 percent")
} else if (prop_less > 0.8) {
  print("you're among the best 20 percent")
} else {
  print("need more analysis")
}

# Create top_grades
top_grades <- my_class[my_class >= 85]

# Create worst_grades
worst_grades <- my_class[my_class < 65]

# Write conditional statement
if (length(top_grades) > length(worst_grades)) {
  print("top grades prevail")
}


# Define example vector x
x <- c(1:10, NA)

# Use the function template to create the rescale01 function
rescale01 <- function(x) {
  rng <- range(x, na.rm = TRUE)
  (x - rng[1]) / (rng[2] - rng[1])
}

# Test your function, call rescale using the vector x as the argument
rescale01(x)