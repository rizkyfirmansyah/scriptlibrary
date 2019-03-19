# Call length() on each element of logs
lapply(logs, length)

# Call class() on each element of logs
lapply(logs, class)

# Define get_timestamp()
get_timestamp <- function(x) {
  x$timestamp
}

# Apply get_timestamp() over all elements in logs
lapply(logs, get_timestamp)

# Have lapply() use an anonymous function
lapply(logs, function(x) { x$timestamp })

"""
This means that you can assign `[[` to the FUN argument to lapply(), and add a third argument to lapply(), which will be passed as an argument to the `[[` function.
"""
# Replace the anonymous function with `[[` 
lapply(logs, `[[`, "timestamp")

# Use sapply() to select the success element from each log: results
results <- sapply(logs, `[[`, "success")

# Call mean() on results
mean(results)

# Use sapply() to select the details element from each log
sapply(logs, `[[`, "details")

# Implement function get_failure_loc
get_failure_loc <- function(x) {
  if (x$success) {
    return(NULL)
  } else {
    return(x$details$location)
  }
}

# Use sapply() to call get_failure_loc on logs
sapply(logs, get_failure_loc)

"""
You can think of vapply() as the secure version of sapply(). Where sapply() tries to simplify the result, you have to explicitly mention what the outcome of the function you're applying will be with vapply().

"""

# Convert the sapply call to vapply
vapply(logs, length, FUN.VALUE = integer(1))

# Convert the sapply call to vapply
vapply(logs, `[[`, "success", FUN.VALUE = logical(1))

# Convert the sapply() call to a vapply() or lapply() call
vapply(logs, `[[`, c("details", "message"), FUN.VALUE = character(1))

# Convert the sapply() call to a vapply() or lapply() call
lapply(logs, function(x) { x$details })


# Return vector with uppercase version of message elements in log entries
extract_caps <- function(x) {
  toupper(x$details$message)
}

# Apply extract_caps function on logs
vapply(logs, extract_caps, FUN.VALUE = character(1))

