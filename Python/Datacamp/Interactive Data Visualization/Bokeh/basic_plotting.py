"""

In Bokeh, visual properties of shapes are called glyphs. The visual properties of these glyphs such as position or color can be assigned single values, for example x=10 or fill_color='red'.

"""

# A simple scatter plot

# Import figure from bokeh.plotting
from bokeh.plotting import figure

# Import output_file and show from bokeh.io
from bokeh.io import output_file, show

# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a circle glyph to the figure p
p.circle(fertility, female_literacy)

# Call the output_file() function and specify the name of the file
output_file('fert_lit.html')

# Display the plot
show(p)


# A scatter plot with different shapes

# Create the figure: p
p = figure(x_axis_label='fertility', y_axis_label='female_literacy (% population)')

# Add a circle glyph to the figure p
p.circle(fertility_latinamerica, female_literacy_latinamerica)

# Add an x glyph to the figure p
p.x(fertility_africa, female_literacy_africa)

# Specify the name of the file
output_file('fert_lit_separate.html')

# Display the plot
show(p)

## As you have seen, it is quite straightforward to add multiple glyph functions to the same Bokeh figure object.


# Customizing your scatter plots

"""
The three most important arguments to customize scatter glyphs are color, size, and alpha. Bokeh accepts colors as hexadecimal strings, tuples of RGB values between 0 and 255, and any of the 147 CSS color names. Size values are supplied in screen space units with 100 meaning the size of the entire figure.

The alpha parameter controls transparency. It takes in floating point numbers between 0.0, meaning completely transparent, and 1.0, meaning completely opaque.
"""

# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a blue circle glyph to the figure p
p.circle(fertility_latinamerica, female_literacy_latinamerica, color='blue', size=10, alpha=0.8)

# Add a red circle glyph to the figure p
p.circle(fertility_africa, female_literacy_africa, color='red', size=10, alpha=0.8)

# Specify the name of the file
output_file('fert_lit_separate_colors.html')

# Display the plot
show(p)



## Glyphs - Lines

# Import figure from bokeh.plotting
from bokeh.plotting import figure

# Create a figure with x_axis_type="datetime": p
p = figure(x_axis_type='datetime', x_axis_label='Date', y_axis_label='US Dollars')

# Plot date along the x axis and price along the y axis
p.line(date, price)

# Specify the name of the output file and show the result
output_file('line.html')
show(p)


# Lines and markers

# Import figure from bokeh.plotting
from bokeh.plotting import figure

# Create a figure with x_axis_type='datetime': p
p = figure(x_axis_type='datetime', x_axis_label='Date', y_axis_label='US Dollars')

# Plot date along the x-axis and price along the y-axis
p.line(date, price)

# With date on the x-axis and price on the y-axis, add a white circle glyph of size 4
p.circle(date, price, fill_color='white', size=4)

# Specify the name of the output file and show the result
output_file('line.html')
show(p)


# Patches

"""
In Bokeh, extended geometrical shapes can be plotted by using the patches() glyph function. The patches glyph takes as input a list-of-lists collection of numeric values specifying the vertices in x and y directions of each distinct patch to plot.

In this exercise, you will plot the state borders of Arizona, Colorado, New Mexico and Utah. The latitude and longitude vertices for each state have been prepared as lists.

Your job is to plot longitude on the x-axis and latitude on the y-axis. The figure object has been created for you as p.
"""


# Create a list of az_lons, co_lons, nm_lons and ut_lons: x
x = [az_lons, co_lons, nm_lons, ut_lons]

# Create a list of az_lats, co_lats, nm_lats and ut_lats: y
y = [az_lats, co_lats, nm_lats, ut_lats]

# Add patches to figure p with line_color=white for x and y
p.patches(x, y, line_color='white')

# Specify the name of the output file and show the result
output_file('four_corners.html')
show(p)


# Plotting data from NumPy arrays

"""
In this exercise, you'll generate NumPy arrays using np.linspace() and np.cos() and plot them using the circle glyph.

np.linspace() is a function that returns an array of evenly spaced numbers over a specified interval. For example, np.linspace(0, 10, 5) returns an array of 5 evenly spaced samples calculated over the interval [0, 10]. np.cos(x) calculates the element-wise cosine of some array x.
"""

# Import numpy as np
import numpy as np

# Create array using np.linspace: x
x = np.linspace(0, 5, 100)

# Create array using np.cos: y
y = np.cos(x)

# Add circles at x and y
p.circle(x, y)

# Specify the name of the output file and show the result
output_file('numpy.html')
show(p)


# Plotting data from Pandas DataFrames

"""
Bokeh can plot floating point numbers, integers, and datetime data types. In this example, you will read a CSV file containing information on 392 automobiles manufactured in the US, Europe and Asia from 1970 to 1982.
"""

# Import pandas as pd
import pandas as pd

# Read in the CSV file: df
df = pd.read_csv('auto.csv')

# Import figure from bokeh.plotting
from bokeh.plotting import figure

# Create the figure: p
p = figure(x_axis_label='HP', y_axis_label='MPG')

# Plot mpg vs hp by color
p.circle(df.hp, df.mpg, color=df['color'], size=10)

# Specify the name of the output file and show the result
output_file('auto-df.html')
show(p)


# The Bokeh ColumnDataSource (continued)

"""
You can create a ColumnDataSource object directly from a Pandas DataFrame by passing the DataFrame to the class initializer.
"""


# Import the ColumnDataSource class from bokeh.plotting
from bokeh.plotting import ColumnDataSource

# Create a ColumnDataSource from df: source
source = ColumnDataSource(df)

# Add circle glyphs to the figure p
p.circle('Year', 'Time', source=source, color='color', size=8)

# Specify the name of the output file and show the result
output_file('sprint.html')
show(p)


# Selection and non-selection glyphs

"""
In this exercise, you're going to add the box_select tool to a figure and change the selected and non-selected circle glyph properties so that selected glyphs are red and non-selected glyphs are transparent blue.
"""

# Create a figure with the "box_select" tool: p
p = figure(x_axis_label='Year', y_axis_label='Time', tools='box_select')

# Add circle glyphs to the figure p with the selected and non-selected properties
p.circle(x='Year', y='Time', source=source, selection_color='red', nonselection_alpha=0.1)

# Specify the name of the output file and show the result
output_file('selection_glyph.html')
show(p)


# Hover glyphs

# import the HoverTool
from bokeh.models import HoverTool

# Add circle glyphs to figure p
p.circle(x, y, size=10,
         fill_color='grey', alpha=0.1, line_color=None,
         hover_fill_color='firebrick', hover_alpha=0.5,
         hover_line_color='white')

# Create a HoverTool: hover
hover = HoverTool(tooltips=None, mode='vline')

# Add the hover tool to the figure p
p.add_tools(hover)

# Specify the name of the output file and show the result
output_file('hover_glyph.html')
show(p)


# Colormapping

#Import CategoricalColorMapper from bokeh.models
from bokeh.models import CategoricalColorMapper

# Convert df to a ColumnDataSource: source
source = ColumnDataSource(df)

# Make a CategoricalColorMapper object: color_mapper
color_mapper = CategoricalColorMapper(factors=['Europe', 'Asia', 'US'],
                                      palette=['red', 'green', 'blue'])

# Add a circle glyph to the figure p
p.circle('weight', 'mpg', source=source,
            color=dict(field='origin', transform=color_mapper),
            legend='origin')

# Specify the name of the output file and show the result
output_file('colormap.html')
show(p)


