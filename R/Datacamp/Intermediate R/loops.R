# Print the structure of logs
str(logs)

# Use list subsetting to print the details part of 11th logs entry
logs[[11]]$details

# Print the class of the timestamp component of the first entry
class(logs[[1]]$timestamp)

# Initialize the iterator i to be 1
i <- 1

# Code the while loop
while (logs[[i]]$success) {
  print(i)
  i <- i + 1
}


# Adapt the while loop
i <- 1
while (logs[[i]]$success) {
  print(logs[[i]]$details$message)
  i <- i + 1
}

# Initialize i and found
i <- 1
found <- FALSE

# Code the while loop
while (!found) {
  if (!logs[[i]]$success && logs[[i]]$details$location == "waste") {
    print("found")
    found <- TRUE  
  } else {
    print("still looking")
    i <- i + 1
  }
}

# Code a for loop that prints the timestamp of each log
for (log in logs) {
  print(log$timestamp)
}

# Finish the for loop: add date element for each entry
for (i in 1:length(logs)) {
  logs[[i]]$date <- as.Date(logs[[i]]$timestamp)
}

# Print first 6 elements in logs
head(logs)

"""
Your plant manager approaches you and asks for a report on all failures that are available in the logs list. Instead of the entire list, she is only interested in the failures. Get to work to generate what she asks for!

Just a tip before you get to it: If you have a list of lists a and want to add a list b to it, you can use c(a, list(b)).

"""

# Intialize empty list: failures
failures <- list()

# Finish the for loop: add each failure to failures
for (log in logs) {
  if (!log$success) {
    failures <- c(failures, list(log))
  }
}

# Display the structure of failures
str(failures)