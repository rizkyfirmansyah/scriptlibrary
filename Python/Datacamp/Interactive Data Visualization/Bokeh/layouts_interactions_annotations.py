# Creating rows of plots

# Import row from bokeh.layouts
from bokeh.layouts import row

# Create the first figure: p1
p1 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a circle glyph to p1
p1.circle('fertility', 'female_literacy', source=source)

# Create the second figure: p2
p2 = figure(x_axis_label='population', y_axis_label='female_literacy (% population)')

# Add a circle glyph to p2
p2.circle('population', 'female_literacy', source=source)

# Put p1 and p2 into a horizontal row: layout
layout = row(p1, p2)

# Specify the name of the output_file and show the result
output_file('fert_row.html')
show(layout)


# Creating columns of plots

# Import column from the bokeh.layouts module
from bokeh.layouts import column

# Create a blank figure: p1
p1 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add circle scatter to the figure p1
p1.circle('fertility', 'female_literacy', source=source)

# Create a new blank figure: p2
p2 = figure(x_axis_label='population', y_axis_label='female_literacy (% population)')

# Add circle scatter to the figure p2
p2.circle('population', 'female_literacy', source=source)

# Put plots p1 and p2 in a column: layout
layout = column(p1, p2)

# Specify the name of the output_file and show the result
output_file('fert_column.html')
show(layout)


# Nesting rows and columns of plots

# Import column and row from bokeh.layouts
from bokeh.layouts import column, row

# Make a column layout that will be used as the second row: row2
row2 = column([mpg_hp, mpg_weight], sizing_mode='scale_width')

# Make a row layout that includes the above column layout: layout
layout = row([avg_mpg, row2], sizing_mode='scale_width')

# Specify the name of the output_file and show the result
output_file('layout_custom.html')
show(layout)


# Creating gridded layouts

"""
Regular grids of Bokeh plots can be generated with gridplot.

In this example, you're going to display four plots of fertility vs female literacy for four regions: Latin America, Africa, Asia and Europe.

Your job is to create a list-of-lists for the four Bokeh plots that have been provided to you as p1, p2, p3 and p4. The list-of-lists defines the row and column placement of each plot.
"""

# Import gridplot from bokeh.layouts
from bokeh.layouts import gridplot

# Create a list containing plots p1 and p2: row1
row1 = [p1, p2]

# Create a list containing plots p3 and p4: row2
row2 = [p3, p4]

# Create a gridplot using row1 and row2: layout
layout = gridplot([row1, row2])

# Specify the name of the output_file and show the result
output_file('grid.html')
show(layout)


# Starting tabbed layouts

"""
Tabbed layouts can be created in Bokeh by placing plots or layouts in Panels.

In this exercise, you'll take the four fertility vs female literacy plots from the last exercise and make a Panel() for each.
"""


# Import Panel from bokeh.models.widgets
from bokeh.models.widgets import Panel

# Create tab1 from plot p1: tab1
tab1 = Panel(child=p1, title='Latin America')

# Create tab2 from plot p2: tab2
tab2 = Panel(child=p2, title='Africa')

# Create tab3 from plot p3: tab3
tab3 = Panel(child=p3, title='Asia')

# Create tab4 from plot p4: tab4
tab4 = Panel(child=p4, title='Europe')


# Displaying tabbed layouts

"""
Tabbed layouts are collections of Panel objects. Using the figures and Panels from the previous two exercises, you'll create a tabbed layout to change the region in the fertility vs female literacy plots.

Your job is to create the layout using Tabs() and assign the tabs keyword argument to your list of Panels. The Panels have been created for you as tab1, tab2, tab3 and tab4.

After you've displayed the figure, explore the tabs you just added! The "Pan", "Box Zoom" and "Wheel Zoom" tools are also all available as before.
"""

# Import Tabs from bokeh.models.widgets
from bokeh.models.widgets import Tabs

# Create a Tabs layout: layout
layout = Tabs(tabs=[tab1, tab2, tab3, tab4])

# Specify the name of the output_file and show the result
output_file('tabs.html')
show(layout)


# Linked axes

"""
Linking axes between plots is achieved by sharing range objects.

In this exercise, you'll link four plots of female literacy vs fertility so that when one plot is zoomed or dragged, one or more of the other plots will respond.

The four plots p1, p2, p3 and p4 along with the layout that you created in the last section have been provided for you.

Your job is link p1 with the three other plots by assignment of the .x_range and .y_range attributes.

After you have linked the axes, explore the plots by clicking and dragging along the x or y axes of any of the plots, and notice how the linked plots change together.
"""

# Link the x_range of p2 to p1: p2.x_range
p2.x_range = p1.x_range

# Link the y_range of p2 to p1: p2.y_range
p2.y_range = p1.y_range

# Link the x_range of p3 to p1: p3.x_range
p3.x_range = p1.x_range

# Link the y_range of p4 to p1: p4.y_range
p4.y_range = p1.y_range

# Specify the name of the output_file and show the result
output_file('linked_range.html')
show(layout)


# Linked brushing

"""
By sharing the same ColumnDataSource object between multiple plots, selection tools like BoxSelect and LassoSelect will highlight points in both plots that share a row in the ColumnDataSource.

In this exercise, you'll plot female literacy vs fertility and population vs fertility in two plots using the same ColumnDataSource.

After you have built the figure, experiment with the Lasso Select and Box Select tools. Use your mouse to drag a box or lasso around points in one figure, and notice how points in the other figure that share a row in the ColumnDataSource also get highlighted.

Before experimenting with the Lasso Select, however, click the Bokeh plot pop-out icon to pop out the figure so that you can definitely see everything that you're doing.
"""

# Create ColumnDataSource: source
source = ColumnDataSource(data)

# Create the first figure: p1
p1 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female literacy (% population)',
            tools='box_select,lasso_select')

# Add a circle glyph to p1
p1.circle('fertility', 'female literacy', source=source)

# Create the second figure: p2
p2 = figure(x_axis_label='fertility (children per woman)', y_axis_label='population (millions)',
            tools='box_select,lasso_select')

# Add a circle glyph to p2
p2.circle('fertility', 'population', source=source)

# Create row layout of figures p1 and p2: layout
layout = row(p1, p2)

# Specify the name of the output_file and show the result
output_file('linked_brush.html')
show(layout)


# How to create legends

"""
Legends can be added to any glyph by using the legend keyword argument.
"""

# Add the first circle glyph to the figure p
p.circle('fertility', 'female_literacy', source=latin_america, size=10, color='red', legend='Latin America')

# Add the second circle glyph to the figure p
p.circle('fertility', 'female_literacy', source=africa, size=10, color='blue', legend='Africa')

# Specify the name of the output_file and show the result
output_file('fert_lit_groups.html')
show(p)


# Positioning and styling legends

"""
Properties of the legend can be changed by using the legend member attribute of a Bokeh figure after the glyphs have been plotted.
"""


# Assign the legend to the bottom left: p.legend.location
p.legend.location = 'bottom_left'

# Fill the legend background with the color 'lightgray': p.legend.background_fill_color
p.legend.background_fill_color = 'lightgray'

# Specify the name of the output_file and show the result
output_file('fert_lit_groups.html')
show(p)


# Adding a hover tooltip

"""
Working with the HoverTool is easy for data stored in a ColumnDataSource.

In this exercise, you will create a HoverTool object and display the country for each circle glyph in the figure that you created in the last exercise. This is done by assigning the tooltips keyword argument to a list-of-tuples specifying the label and the column of values from the ColumnDataSource using the @ operator.

The figure object has been prepared for you as p.

After you have added the hover tooltip to the figure, be sure to interact with it by hovering your mouse over each point to see which country it represents.
"""


# Import HoverTool from bokeh.models
from bokeh.models import HoverTool

# Create a HoverTool object: hover
hover = HoverTool(tooltips=[('Country', '@Country')])

# Add the HoverTool object to figure p
p.add_tools(hover)

# Specify the name of the output_file and show the result
output_file('hover.html')
show(p)