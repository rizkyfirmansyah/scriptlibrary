# Getting rid of unnecessary color

# Hard to read scatter of CO and NO2 w/ color mapped to city
# sns.scatterplot('CO', 'NO2',
#                 alpha = 0.2,
#                 hue = 'city',
#                 data = pollution)

# Setup a facet grid to separate the cities apart
g = sns.FacetGrid(data = pollution,
                  col = 'city',
                  col_wrap = 3)

# Map sns.scatterplot to create separate city scatter plots
g.map(sns.scatterplot, 'CO', 'NO2', alpha = 0.2)
plt.show()

## Excellent! This new faceted plot removes the pretty colors but becomes a whole lot more informative. In certain situations, if you can take something that is encoded in color and encode it in position instead, you often will increase the legibility of your chart. The balance between attractiveness and utility is something you need to balance in every plot you make.


# Fixing Seaborn's bar charts

# Seaborn's default values for the colors of bars in a bar chart are not ideal for the most accurate perception. By drawing each bar as a different color, there is a risk of the viewer seeing two identical sized bars as different sizes as people tend to see some colors as 'larger' than others.

# We discussed two easy ways to fix this. First, to put a border around the bars; second, change all bar colors to the same value. Try both of these solutions on our pollution data.

import numpy as np

sns.barplot(y = 'city', x = 'CO', 
              estimator = np.mean,
            ci = False,
              data = pollution,
              # Add a border to the bars
            edgecolor = "black")
plt.show()

import numpy as np

sns.barplot(y = 'city', x = 'CO', 
              estimator = np.mean,
            ci = False,
              data = pollution,
              # Replace border with bar colors
            color = 'cadetblue')
plt.show()

## Adding borders is an easy and quick way to improve default bar charts without sacrificing some of the trippy colors. Spending a tiny bit more time to adjust the default colors will result in a more accurate and easy to read chart.


# Making a custom continuous palette

"""
You are interested in the pollution levels of Cincinnati for the year 2014. Specifically, you're interested in CO and NO2, so you make a simple scatter plot to show the relationship between the two pollutants.

However, there may be some interesting information in how the value of O3 relates to the two plotted pollutants, so you decide to color the points by their O3 levels. To do this, you need to define an appropriate continuous palette and map your O3 column to it in your scatter plot.
"""

# Filter the data
cinci_2014 = pollution.query("city  ==  'Cincinnati' & year  ==  2014")

# Define a custom continuous color palette
color_palette = sns.light_palette('orangered',
                                  as_cmap = True)

# Plot mapping the color of the points with custom palette
sns.scatterplot(x = 'CO',
                y = 'NO2',
                hue = 'O3', 
                  data = cinci_2014,
                palette = color_palette)
plt.show()


## Judging by the plot, there doesn't appear to be much of an association of O3 to either CO or NO2. By adding color to this simple scatter plot, you added a large amount of information on a previously un-visualized variable to the chart while still maintaining high precision in your main goal of comparing the CO and NO2 values to each other.


# Customizing a diverging palette heatmap

"""
The default color scheme used by Seaborn's heatmap() doesn't give the value of 0 any special treatment. This is fine for instances when 0 isn't special for the variable you're visualizing but means you will need to customize the palette 0 is special, such as when it represents a neutral value.

For this visualization, you want to compare all the cities against the average pollution value for CO in November 2015. (As is provided in the DataFrame nov_2015_CO).

To do this, use a heat map to encode the number of standard deviations away from the average each city's CO pollution was for the day. You'll need to replace the default palette by creating your own custom diverging palette and passing it to the heatmap and informing the function what your neutral value is.
"""

# Define a custom palette
color_palette = sns.diverging_palette(250, 0, as_cmap = True)

# Pass palette to plot and set axis ranges
sns.heatmap(nov_2015_CO,
            cmap = color_palette,
            center = 0,
            vmin = -4,
            vmax = 4)
plt.yticks(rotation = 0)
plt.show()

## Instantly, you can see that Vandenberg Air Force Base always has below average CO values whereas Long Beach, especially towards the end of the month, has much higher than average values. By correctly mapping the zero-point of our values you can immediately pick out patterns in our data in the context of a meaningful data anchor-point.


# Adjusting your palette according to context

"""
You've been asked to make a figure for your company's website. The website has a slick black theme, and it would be pretty jarring if your plot were white. To make your plot match the company aesthetic, you can swap the background to a black one with plt.style.use("dark_background").

The figure you've been asked to make plots O3 values during October 2015 for various cities (provided as oct_2015_o3). You will plot this as a heatmap with the color of each cell encoding how many standard deviations from the overall average O3 value the measurement falls. Due to the website's dark background, you will want to adjust your color palette to encode null value (or 0 standard deviations from the mean) as dark rather than the default white.
"""

# Dark plot background
plt.style.use("dark_background")

# Modify palette for dark background
color_palette = sns.diverging_palette(250, 0,
                                      center = 'dark',
                                      as_cmap = True)

# Pass palette to plot and set center
sns.heatmap(oct_2015_o3,
            cmap = color_palette,
            center = 0)
plt.yticks(rotation = 0)
plt.show()

## Not only does the black background make this chart look very cool, it helps the patterns really pop out. Furthermore, matching the null-value to the background of the chart makes it much more natural to read. You can easily see that Fairbanks has much lower than average O3 pollution values than the rest of the cities and that Houston has much higher values, especially in the earlier days of the month.

