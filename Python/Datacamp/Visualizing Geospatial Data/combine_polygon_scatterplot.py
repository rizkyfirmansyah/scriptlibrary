# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Scatterplot 3
plt.scatter(father_son.fheight, father_son.sheight,  c = 'yellow', edgecolor = 'darkblue')
plt.grid(True)
plt.xlabel('father height (inches)')
plt.ylabel('son height (inches)')
plt.title('Son Height as a Function of Father Height')

# Show your plot
plt.show()

# Import geopandas
import geopandas as gpd 

# Read in the services district shapefile and look at the first few rows.
service_district = gpd.read_file(shapefile_path)
print(service_district.head())

# Print the contents of the service districts geometry in the first row
print(service_district.loc[0, 'geometry'])


# Import packages
import geopandas as gpd
import matplotlib.pyplot as plt

# Plot the Service Districts without any additional arguments
service_district.plot()
plt.show()

# Plot the Service Districts, color them according to name, and show a legend
service_district.plot(column = 'name', legend = True)
plt.show()



# Plot the service district shapefile
service_district.plot(column='name')

# Add the chicken locations
plt.scatter(x=chickens.lng, y=chickens.lat, c = 'black')

# Show the plot
plt.show()



# Plot the service district shapefile
service_district.plot(column='name', legend=True)

# Add the chicken locations
plt.scatter(x=chickens.lng, y=chickens.lat, c = 'black', edgecolor='white')

# Add labels and title
plt.title('Nashville Chicken Permits')
plt.xlabel('longitude')
plt.ylabel('latitude')

# Add grid lines and show the plot
plt.grid(True)
plt.show()

