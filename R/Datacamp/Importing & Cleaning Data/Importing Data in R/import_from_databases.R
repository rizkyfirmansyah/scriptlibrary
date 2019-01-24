'''
After you\'ve successfully connected to a remote MySQL database, the next step is to see what tables the database contains. You can do this with the dbListTables() function.
'''

# Load the DBI package
library(DBI)

# Connect to the MySQL database: con
con <- dbConnect(RMySQL::MySQL(), 
                 dbname = "tweater", 
                 host = "courses.csrrinzqubik.us-east-1.rds.amazonaws.com", 
                 port = 3306,
                 user = "student",
                 password = "datacamp")

# Build a vector of table names: tables
tables <- dbListTables(con)

# Display structure of tables
str(tables)

# Import the users table from tweater: users
users <- dbReadTable(con, "users")

# Print users
print(users)


# Import all tables
tables <- lapply(table_names, dbReadTable, conn = con)

# Print out tables
print(tables)

'''
dbGetQuery()

'''

# Import tweat_id column of comments where user_id is 1: elisabeth
elisabeth <- dbGetQuery(con, "SELECT tweat_id FROM comments WHERE user_id = 1")

# Print elisabeth
print(elisabeth)


# Connect to the database
library(DBI)
con <- dbConnect(RMySQL::MySQL(),
                 dbname = "tweater",
                 host = "courses.csrrinzqubik.us-east-1.rds.amazonaws.com",
                 port = 3306,
                 user = "student",
                 password = "datacamp")

# Import post column of tweats where date is higher than '2015-09-21': latest
latest <- dbGetQuery(con, "SELECT post FROM tweats WHERE date > '2015-09-21'")

# Print latest
print(latest)


# Create data frame short
short <- dbGetQuery(con, "SELECT id, name FROM users WHERE CHAR_LENGTH(name) < 5")

# Print short
print(short)

'''
dbSendQuery()
dbFetch()
dbClearResult()
dbDisconnect()
above 3 functions equals to dbGetQuery()


'''

# Send - Fetch - Clear
# Connect to the database
library(DBI)
con <- dbConnect(RMySQL::MySQL(),
                 dbname = "tweater",
                 host = "courses.csrrinzqubik.us-east-1.rds.amazonaws.com",
                 port = 3306,
                 user = "student",
                 password = "datacamp")

# Send query to the database
res <- dbSendQuery(con, "SELECT * FROM comments WHERE user_id > 4")

# Use dbFetch() twice. In the first call, import only two records of the query result by setting the n argument to 2. In the second call, import all remaining queries (don't specify n)

dbFetch(res, n = 2)
dbFetch(res)


# Clear res
dbClearResult(res)

