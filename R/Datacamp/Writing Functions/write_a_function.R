# Define ratio() function
ratio <- function(x, y) {
  # body
  x / y
}

# Call ratio() with arguments 3 and 4
ratio(3, 4)

# 2nd element in tricky_list
typeof(tricky_list[[2]])

# Element called x in tricky_list
typeof(tricky_list[["x"]])

# 2nd element inside the element called x in tricky_list
typeof(tricky_list[["x"]][[2]])


# Guess where the regression model is stored
names(tricky_list)

# Use names() and str() on the model element
names(tricky_list$model)
str(tricky_list$model)

# Subset the coefficients element
tricky_list$model[["coefficients"]]

# Subset the wt element
tricky_list$model[["coefficients"]][["wt"]]


# Replace the 1:ncol(df) sequence
for (i in seq_along(df)) {
  print(median(df[[i]]))
}

# Create an empty data frame
empty_df <- data.frame()

# Repeat for loop to verify there is no error
for (i in seq_along(empty_df)) {
  print(median(empty_df[[i]]))
}


"""
Before you start the loop, you must always allocate sufficient space for the output, let's say an object called output. This is very important for efficiency: if you grow the for loop at each iteration (e.g. using c()), your for loop will be very slow.

A general way of creating an empty vector of given length is the vector() function. It has two arguments: the type of the vector (\"logical\", \"integer\", \"double\", \"character\", etc.) and the length of the vector.

Then, at each iteration of the loop you must store the output in the corresponding entry of the output vector, i.e. assign the result to output[[i]]. (You might ask why we are using double brackets here when output is a vector. It's primarily for generalizability: this subsetting will work whether output is a vector or a list.)
"""
# Create new double vector: output
output <- vector("double", ncol(df))

# Alter the loop
for (i in seq_along(df)) {
  # Change code to store result in output
  output[i] <- median(df[[i]])
}

# Print output
output