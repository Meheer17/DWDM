Relation <- lm(diabetes$BloodPressure ~ diabetes$Age)
png(file = "linear_regression.png")
plot(diabetes$Age, diabetes$BloodPressure, col = "green", main = "Linear Regression Analysis",
abline(lm(diabetes$BloodPressure ~ diabetes$Age)), xlab = "Age", ylab = "BloodPressure")