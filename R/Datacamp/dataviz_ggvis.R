## GGVIS

# The ggvis packages is loaded into the workspace already

# Change the code below to make a graph with red points
mtcars %>% ggvis(~wt, ~mpg, fill := "red") %>% layer_points()

# Change the code below draw smooths instead of points
mtcars %>% ggvis(~wt, ~mpg) %>% layer_smooths()

# Change the code below to make a graph containing both points and a smoothed summary line
mtcars %>% ggvis(~wt, ~mpg) %>% layer_points() %>% layer_smooths()


Every ggvis graph contains 4 essential components: data, a coordinate system, marks and corresponding properties. By changing the values of each of these components you can create a vast array of unique plots.


# Adapt the code: show bars instead of points
pressure %>% ggvis(~temperature, ~pressure) %>% layer_bars()

# Adapt the code: show lines instead of points
pressure %>% ggvis(~temperature, ~pressure) %>% layer_lines()

# Extend the code: map the fill property to the temperature variable
pressure %>% ggvis(~temperature, ~pressure, fill = ~temperature) %>% layer_points()
# Extend the code: map the size property to the pressure variable
pressure %>% ggvis(~temperature, ~pressure, fill= ~temperature, size = ~pressure) %>% layer_points()

