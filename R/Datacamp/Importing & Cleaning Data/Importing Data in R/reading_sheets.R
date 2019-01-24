'''
When working with XLConnect, the first step will be to load a workbook in your R session with loadWorkbook(); this function will build a "bridge" between your Excel file and your R session.

'''

# Load the XLConnect package
library("XLConnect")

# Build connection to urbanpop.xlsx: my_book
my_book <- loadWorkbook("urbanpop.xlsx")

# Print out the class of my_book
print(class(my_book))

'''

Just as readxl and gdata, you can use XLConnect to import data from Excel file into R.

To list the sheets in an Excel file, use getSheets(). To actually import data from a sheet, you can use readWorksheet(). Both functions require an XLConnect workbook object as the first argument.
'''

# List the sheets in my_book
getSheets(my_book)

# Import the second sheet in my_book
print(readWorksheet(my_book, sheet = 2))

my_book <- loadWorkbook("urbanpop.xlsx")
sheets <- getSheets(my_book)
all <- lapply(sheets, readWorksheet, object = my_book)
str(all)


#
# Import columns 3, 4, and 5 from second sheet in my_book: urbanpop_sel
urbanpop_sel <- readWorksheet(my_book, sheet = 2, startCol = 3, endCol = 5)

# Import first column from second sheet in my_book: countries
countries <- readWorksheet(my_book, sheet = 2, startCol = 1, endCol = 1)

# cbind() urbanpop_sel and countries together: selection
selection <- cbind(countries, urbanpop_sel)


## adapting sheets

'''
createSheet()
writeWorksheet()
saveWorkbook()
renameSheet()
removeSheet()

Where readxl and gdata were only able to import Excel data, XLConnect\'s approach of providing an actual interface to an Excel file makes it able to edit your Excel files from inside R. In this exercise, you\'ll create a new sheet. In the next exercise, you\'ll populate the sheet with data, and save the results in a new Excel file.
'''


# Add a worksheet to my_book, named "data_summary"
createSheet(my_book, name = "data_summary")

# Use getSheets() on my_book
getSheets(my_book)


# Create data frame: summ
sheets <- getSheets(my_book)[1:3]
dims <- sapply(sheets, function(x) dim(readWorksheet(my_book, sheet = x)), USE.NAMES = FALSE)
summ <- data.frame(sheets = sheets,
                   nrows = dims[1, ],
                   ncols = dims[2, ])

# Add data in summ to "data_summary" sheet
writeWorksheet(my_book, summ, sheet = "data_summary")

# Save workbook as summary.xlsx
saveWorkbook(my_book, file = "summary.xlsx")


# Rename "data_summary" sheet to "summary"
renameSheet(my_book, "data_summary", "summary")

# Print out sheets of my_book
getSheets(my_book)

# Save workbook to "renamed.xlsx"
saveWorkbook(my_book, file = "renamed.xlsx")

