# Acquainting yourself with the data

# iris is available from the datasets package

# Reveal number of observations and variables in two different ways
str(iris)
dim(iris)

# Show first and last observations in the iris data set
head(iris)
tail(iris)

# Summarize the iris data set
summary(iris)


# Basic prediction model

"
As we briefly discussed in the video, there could be a relationship between a worker's age and his wage. Older workers tend to have more experience on average than their younger counterparts, hence you could expect an increasing trend in wage as workers age. So we built a linear regression model for you, using lm(): lm_wage. This model predicts the wage of a worker based only on the worker's age.

With this linear model lm_wage, which is built with data that contain information on workers' age and their corresponding wage, you can predict the wage of a worker given the age of that worker. For example, suppose you want to predict the wage of a 60 year old worker. You can use the predict() function for this. This generic function takes a model as the first argument. The second argument should be some unseen observations as a data frame. predict() is then able to predict outcomes for these observations.
"

# The Wage dataset is available

# Build Linear Model: lm_wage (coded already)
lm_wage <- lm(wage ~ age, data = Wage)

# Define data.frame: unseen (coded already)
unseen <- data.frame(age = 60)

# Predict the wage for a 60-year old worker
predict(lm_wage, unseen)
## Based on the linear model that was estimated from the Wage dataset, you predicted the average wage for a 60 year old worker to be around 124 USD a day. That's not bad! Head over to the next video to receive a short introduction on several machine learning techniques!

