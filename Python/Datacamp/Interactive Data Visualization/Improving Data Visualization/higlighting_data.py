# Hardcoding a highlight

# You are working with the city of Houston to look at the relationship between sulfur dioxide (SO2) and nitrogen dioxide (NO2) pollution, specifically, pollution in the most recent year data was collected (2014). You have singled out a particularly bad day, November 26th, where there was a bad spike in the SO2 levels. To draw the viewers attention to this bad day, you will highlight it in a bright orangish-red and color the rest of the points gray.

# Modify the list comprehension to color the value corresponding to the 330th day (November 26th) of the year 2014 to orangered and the rest of the points to lightgray.

houston_pollution = pollution[pollution.city  ==  'Houston']

# Make array orangred for day 330 of year 2014, otherwise lightgray
houston_colors = ['orangered' if (day  ==  330) & (year  ==  2014) else 'lightgray' 
                  for day,year in zip(houston_pollution.day, houston_pollution.year)]

sns.regplot(x = 'NO2',
            y = 'SO2',
            data = houston_pollution,
            fit_reg = False, 
            # Send scatterplot argument to color points
            scatter_kws = {'facecolors': houston_colors, 'alpha': 0.7})
plt.show()

# Programmatically creating a highlight

# use sns.scatterplot() instead of sns.regplot(). This is because sns.scatterplot() can take a non-color vector as its hue argument and colors the points automatically while providing a helpful legend.

#  if you need the original list unchanged when the new list is modified, you can use copy() method. This is called shallow copy.

houston_pollution = pollution[pollution.city  ==  'Houston'].copy()

# Find the highest observed O3 value
max_O3 = houston_pollution.O3.max()

# Make a column that denotes which day had highest O3
houston_pollution['point type'] = ['Highest O3 Day' if O3  ==  max_03 else 'Others' for O3 in houston_pollution.O3]

# Encode the hue of the points with the O3 generated column
sns.scatterplot(x = 'NO2',
                y = 'SO2',
                hue = 'point type',
                data = houston_pollution)
plt.show()

# Comparing with two KDEs

"""
Imagine that you work for the premier air-filter provider. Your company has asked you to build a report that looks into why 2012 was a particularly good year for sales of your ozone (O3) filter. You downloaded some helpful pollution data from the USGS, and you want to make a concise visualization that compares the general pattern of O3 pollution for 2012 to all other years on record.

To do this, you can build two overlaid kernel density estimation plots (KDEs): one for 2012 O3 data and one for all other years.
"""

# Filter dataset to the year 2012
sns.kdeplot(pollution[pollution.year == 2012].O3, 
            # Shade under kde and add a helpful label
            shade = True,
            label = '2012')

# Filter dataset to everything except the year 2012
sns.kdeplot(pollution[pollution.year != 2012].O3, 
            # Again, shade under kde and add a helpful label
            shade = True,
            label = 'other years')
plt.show()

# Improving your KDEs

"""
One way of enhancing KDEs is with the addition of a rug plot. Rug plots are little dashes drawn beneath the density that show precisely where each data point falls. Adding a rug plot is particularly useful when you don't have a ton of data.

With small amounts of data you often have gaps along your support with no data, and it can be hard to tell whether a non-zero KDE line means data was present or is due to a wide kernel. A rug plot helps address this.

Let's return to the sns.distplot() function to draw two KDEs: one looking at the data for Vandenberg Air Force Base and the other looking at all the other cities in the pollution data. Since there is much less data contributing to the shape of the Vandenberg plot, add a rug plot beneath it.
"""

sns.distplot(pollution[pollution.city == 'Vandenberg Air Force Base'].O3, 
             label = 'Vandenberg', 
             # Turn of the histogram and color blue to stand out
             hist = False,
             color = 'steelblue', 
             # Turn on rugplot
             rug = True)
# Rug plots can improve KDEs as they help you see those gaps that you may have otherwise assumed were filled with data. In this plot, the rug plot shows that there is a small, but not neglible gap, in the data around O3 = 0.065

sns.distplot(pollution[pollution.city != 'Vandenberg Air Force Base'].O3, 
             label = 'Other cities',
             # Turn off histogram and color gray
             hist = False,  
             color = 'gray')
plt.show()

# Beeswarms

"""
Build a beeswarm plot using sns.swarmplot() that looks at the Ozone levels for all the cities in the pollution data for the month of March. To make the beeswarm a bit more legible, decrease the point size to avoid the overcrowding caused by the many points drawn on the screen. Last, since you've done some manipulation of the data to make this plot, provide a title to help the reader orient with what they are viewing.

"""

# Filter data to just March
pollution_mar = pollution[pollution.month == 3]

# Plot beeswarm with x as O3
sns.swarmplot(y = "city",
              x = 'O3', 
              data = pollution_mar, 
              # Decrease the size of the points to avoid crowding 
              size = 3)

# Give a descriptive title
plt.title('March Ozone levels by city')
plt.show()

## Beeswarms are a nice (and nice looking) way of comparing a bunch of classes to each other. In the plot, you can see that Vandenberg on average has high O3 levels in March. However, Houston has a much wider range and can sometimes reach much higher levels. 

# Additionally, you can also get a sense of data quantities. Here, you see that Des Moines and Fairbanks have far fewer observations than the other sites.


# A basic text annotation

"""
On the current scatter plot, you can see a particularly prominent point that contains the largest SO2 value observed for August. This point is Cincinnati on August 11th, 2013; however, you would not be able to learn this information from the plot in its current form. Basic text annotations are great for pointing out interesting outliers and giving a bit more information. Draw the readers attention to this Cincinnati value by adding a basic text annotation that gives a bit of the background about this outlier.
"""

# Draw basic scatter plot of pollution data for August
sns.scatterplot(x = 'CO', y = 'SO2', data = pollution[pollution.month  ==  8])

# Label highest SO2 value with text annotation
plt.text(0.57, 41,
         'Cincinnati had highest observed\nSO2 value on Aug 11, 2013', 
         # Set the font to large
         fontdict = {'ha': 'left', 'size': 'large'})
plt.show()


# Arrow annotations

# Query and filter to New Years in Long Beach
jan_pollution = pollution.query("(month  ==  1) & (year  ==  2012)")
lb_newyears = jan_pollution.query("(day  ==  1) & (city  ==  'Long Beach')")

sns.scatterplot(x = 'CO', y = 'NO2',
                data = jan_pollution)

# Point arrow to lb_newyears & place text in lower left 
plt.annotate('Long Beach New Years',
             xy = (lb_newyears.CO, lb_newyears.NO2), # Use the CO and NO2 column values from the lb_newyears DataFrame to place the endpoint of the arrow.
             xytext = (2, 15), 
             # Shrink the arrow to avoid occlusion
             arrowprops = {'facecolor':'gray', 'width': 3, 'shrink': 0.03},
             backgroundcolor = 'white')
plt.show()

## Using arrows with annotations is a great way to keep your text in a nice point-free area of the plot while precisely calling out a given point in a more-crowded location. In this plot, there is what appears to be a slightly higher than normal quantity of NO2 in the air compared to usual. The viewer's attention is driven to the point of interest at first rather than the more obvious outliers, thus kicking off their exploration of the chart in a guided way.


# Combining annotations and color

# Make a vector where Long Beach is orangered; else lightgray
is_lb = ['orangered' if city  ==  'Long Beach' else 'lightgray' for city in pollution['city']]

# Map facecolors to the list is_lb and set alpha to 0.3
sns.regplot(x = 'CO',
            y = 'O3',
            data = pollution,
            fit_reg = False,
            scatter_kws = {'facecolors':is_lb, 'alpha': 0.3})

# Add annotation to plot
plt.text(1.6, 0.072, 'April 30th, Bad Day')
plt.show() 


# Great! List comprehensions are a great tool for quickly controlling colors or other aspects for a plot. It's often easier and cleaner to directly pass a vector of the desired aesthetics to your plot rather than adding a new column to your DataFrame (for instance in this example a column containing True or False for if a city is Long Beach) and then telling your plot how to map that column to aesthetics.


# Using a custom categorical palette

"""
When you have a line chart with lots of categories choosing your palette carefully is essential. Often default palettes have very similar hues, that are hard to differentiate when spread over the small surface of a line. ColorBrewer palettes are built with this in mind and keep the colors as distinct as possible.

In this exercise, you will make a line plot of the O3 values over the year of 2013 for all the cities where the color of each line is encoded by city. You will use the ColorBrewer palette 'Set2' to improve upon the default color scheme.
"""

# Filter our data to Jan 2013
pollution_jan13 = pollution.query('year  ==  2013 & month  ==  1')

# Color lines by the city and use custom ColorBrewer palette
sns.lineplot(x = "day", 
             y = "CO", 
             palette = "Set2",
             hue = "city", 
             linewidth = 3,
             data = pollution_jan13)
plt.show()


# Dealing with too many categories

"""
Sometimes you may be short on figure space and need to show a lot of data at once. Here you want to show the year-long trajectory of every pollutant for every city in the pollution dataset. Each pollutant trajectory will be plotted as a line with the y-value corresponding to standard deviations from year's average. This means you will have a lot of lines on your plot at once -- way more than you could separate clearly with color.

To deal with this, you have decided to highlight on a small subset of city pollutant combinations (wanted_combos). This subset is the most important to you, and the other trajectories will provide valuable context for comparison. To focus attention, you will set all the non-highlighted trajectories lines to of the same 'other' color.

"""

# Choose the combos that get distinct colors
wanted_combos = ['Vandenberg Air Force Base NO2', 'Long Beach CO', 'Cincinnati SO2']

# Assign a new column to DataFrame for isolating the desired combos
city_pol_month['color_cats'] = [x if x in wanted_combos else 'other' for x in city_pol_month['city_pol']]

# Plot lines with color driven by new column and lines driven by original categories
sns.lineplot(x = "month",
             y = "value",
             hue = 'color_cats',
             units = 'city_pol', # Use the units argument to determine how, i.e., from which column, the data points should be connected to form each line.
             estimator = None,
             palette = 'Set2',
             data = city_pol_month)
plt.show()

## Here by subsetting our colors to be those that you care about you can make a bit more sense of the spaghetti of lines. You see that Long Beach has a bathtub shape for its CO values: going from more than four standard deviations above mean CO values to below average and then back up to more than three standard deviations above by the end of the year. Whereas Vandenberg stays way below average for the entire year. 

## While the best solution for this plot may be to not plot the other lines at all, they can often provide valuable context for the data of interest.



# Coloring ordinal categories

"""
You are working for the Des Moines city council to assess the associations of various pollutant levels in the city. The two most important pollutants are SO2 and NO2 but CO is also of interest. You've only been allowed enough space for a single plot for your part of the report.

You start with a scatter plot of the SO2 and NO2 values as they are most important and then decide to show the CO values using a color scale corresponding to CO quartiles. By binning the continuous CO values, you have turned CO into an ordinal variable that can illuminate broad patterns without requiring much effort from the viewer to compare subtly different shades.
"""

# Divide CO into quartiles
pollution['CO quartile'] = pd.qcut(pollution['CO'], q = 4, labels = False)

# Filter to just Des Moines
des_moines = pollution.query("city  ==  'Des Moines'")

# Color points with by quartile and use ColorBrewer palette
sns.scatterplot(x = 'SO2',
                y = 'NO2',
                hue = 'CO quartile', 
                  data = des_moines,
                palette = 'GnBu')
plt.show()

## By simplifying the color encoding to just four distinct values, you get a clear picture of the patterns between CO, SO2, and NO2. Here you see the low quartiles of CO seem to relate with NO2 and appear much less related to the SO2 values. By categorizing the continuous color variable, you allow the viewer to investigate patterns along a third variable in a clear and simple way at the expense of some precision: a tradeoff that is often worth it.


# Choosing the right variable to encode with color

"""
You're tasked with visualizing pollution values for Long Beach and nearby cities over time. The supplied code makes the below (hard-to-read plot), which consists of maximum pollution values (provided as max_pollutant_values) with the bars colored by the city.

You can quickly improve this with a few tweaks. By modifying the cities shown to only those in the western half of the country you will avoid clutter. Next, swapping the color-encoding from city to year allows you to use an ordinal palette, saving the reader from continually referring to the legend to check which color corresponds to which city.
"""

# Reduce to just cities in the western half of US
cities = ['Fairbanks', 'Long Beach', 'Vandenberg Air Force Base', 'Denver']

# Filter data to desired cities
city_maxes = max_pollutant_values[max_pollutant_values.city.isin(cities)]

# Swap city and year encodings
sns.catplot(x = 'city', hue = 'year',
              y = 'value', row = 'pollutant',    
              # Change palette to one appropriate for ordinal categories
              data = city_maxes, palette = 'BuGn',
              sharey = False, kind = 'bar')
plt.show()

## Wonderful! By simply switching just a few values, the plot is much clearer, and the presentation has more impact. Also, the use of hue as the years go on puts a greater emphasis on the later (more recent) years.

