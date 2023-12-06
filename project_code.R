library(ggplot2)
library(magrittr)
library(dplyr)
library(stringr)
library(tidyverse)

project <- project_data

ggplot(project, aes(x = MoonPhaseCat)) +
  geom_bar(fill = "mediumslateblue") +
  labs(title = "Number of Fatalities by Moon Phase Category", x = "Moon Phase Category", y = "Count of Fatalities") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

project <- project %>%
  mutate_all(tolower)
project <- project %>%
  mutate(Type.of.road = ifelse(str_detect(Type.of.road, "35"), "IH-35", Type.of.road))
project <- project %>%
  mutate(Type.of.road = ifelse(str_detect(Type.of.road, "high speed"), "high speed roadway", Type.of.road))

project <- project %>%
  mutate(Type.of.road = ifelse(str_detect(Type.of.road, "use"), "high use roadway", Type.of.road))
project <- project %>%
  mutate(Type.of.road = ifelse(str_detect(Type.of.road, "highspeed"), "high speed roadway", Type.of.road))

#number of fatalities by road type
project %>%
  group_by(Type.of.road) %>%
  summarise(FatalitiesCount = n()) %>%
  ggplot(aes(x = reorder(Type.of.road, FatalitiesCount), y = FatalitiesCount)) +
  geom_bar(fill = "aquamarine3", stat = "identity") +
  labs(title = "Number of Fatalities by Road Type", x = "Road Type", y = "Count of Fatalities") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

#number of fatalities by hour
project$Hour <- as.numeric(project$Hour)

ggplot(project, aes(x = Hour)) +
  geom_line(stat = "count", color = "darkslateblue", size = 1.5) +
  labs(title = "Number of Fatalities by Hour", x = "Hour", y = "Count of Fatalities") +
  theme_minimal() +
  theme(
    panel.grid.major = element_blank(),
    panel.grid.minor = element_blank(),
    panel.background = element_rect(fill = "white"),
    axis.line = element_line(color = "black"),
    axis.text = element_text(size = 10),
    axis.title = element_text(size = 12, face = "bold"),
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5),
    legend.position = "none")
project <- project %>%
      mutate(Suspected.Impairment = ifelse(str_detect(Suspected.Impairment, "bic"), "bicyclist", Suspected.Impairment))
project <- project %>%
      mutate(Suspected.Impairment = ifelse(str_detect(Suspected.Impairment, "both"), "both", Suspected.Impairment))
project <- project %>%
      mutate(Suspected.Impairment = ifelse(str_detect(Suspected.Impairment, "driver"), "driver", Suspected.Impairment))
project <- project %>%
      mutate(Suspected.Impairment = ifelse(str_detect(Suspected.Impairment, "unk"), "unknown", Suspected.Impairment))
project <- project %>%
      mutate(Suspected.Impairment = ifelse(str_detect(Suspected.Impairment, "ped"), "pedestrian", Suspected.Impairment))
project <- project %>%
      mutate(Suspected.Impairment = ifelse(str_detect(Suspected.Impairment, "none"), "none", Suspected.Impairment))
    
#number of fatalities by suspected impairment
project$Suspected.Impairment <- fct_reorder(project$Suspected.Impairment, project$Number.of.Fatalities, .fun = sum, .desc = TRUE)
    
ggplot(project, aes(x = Suspected.Impairment)) +
      geom_bar(fill = "plum4", color = "black", size = 0.7, alpha = 0.8) +
      labs(title = "Number of Fatalities by Suspected Impairment", x = "Suspected Impairment", y = "Count of Fatalities") +
      theme_minimal() +
      theme(
        axis.text.x = element_text(angle = 45, hjust = 1, vjust = 1),
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.background = element_rect(fill = "white"),
        axis.line = element_line(color = "black"),
        legend.position = "none")

#number of fatalities by weekday/weekend
project$Number.of.Fatalities <- as.numeric(project$Number.of.Fatalities)

project <- project %>%
  mutate(Weekday = ifelse(Day %in% c("sat", "sun"), "Weekend", "Weekday"))

# Aggregate the data to get the count of fatalities for each weekday/weekend
agg_data <- project %>%
  group_by(Weekday) %>%
  summarise(Fatalities = sum(Number.of.Fatalities))

# Create a bar plot
ggplot(agg_data, aes(x = Weekday, y = Fatalities, fill = Weekday)) +
  geom_bar(stat = "identity", position = "dodge", color = "black") +
  labs(title = "Number of Fatalities by Weekday/Weekend", x = "Day of Week", y = "Count of Fatalities") +
  scale_fill_manual(values = c("Weekday" = "seagreen3", "Weekend" = "purple1")) +
  theme_minimal()

project <- project %>%
  mutate(DL.Status.incident = ifelse(str_detect(DL.Status.incident, "suspended"), "suspended", DL.Status.incident))
project <- project %>%
  mutate(DL.Status.incident = ifelse(str_detect(DL.Status.incident, "exp"), "expired", DL.Status.incident))
project <- project %>%
  mutate(DL.Status.incident = ifelse(str_detect(DL.Status.incident, "no"), "no licence", DL.Status.incident))
project <- project %>%
  mutate(DL.Status.incident = ifelse(str_detect(DL.Status.incident, "ok"), "valid", DL.Status.incident))
project <- project %>%
  mutate(DL.Status.incident = ifelse(str_detect(DL.Status.incident, "unk"), "unknown", DL.Status.incident))
project <- project %>%
  mutate(DL.Status.incident = ifelse(str_detect(DL.Status.incident, "invalid"), "invalid", DL.Status.incident))
project <- project %>%
  mutate(DL.Status.incident = ifelse(str_detect(DL.Status.incident, "supsended"), "suspended", DL.Status.incident))

#number of fatalities by driver's license status
ggplot(project, aes(x = DL.Status.incident, fill = DL.Status.incident)) +
  geom_bar(stat = "count", position = "dodge", color = "black") +
  labs(title = "Number of Fatalities by Driver's Licence Status",
       x = "Driver's License Status",
       y = "Count of Fatalities") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1),
        legend.position = "none")

project <- project %>%
  mutate(Killed.driver.pass = ifelse(str_detect(Killed.driver.pass, "both"), "both", Killed.driver.pass))
project <- project %>%
  mutate(Killed.driver.pass = ifelse(str_detect(Killed.driver.pass, "motorcycle"), "motorcyclist", Killed.driver.pass))
project <- project %>%
  mutate(Killed.driver.pass = ifelse(str_detect(Killed.driver.pass, "ped"), "pedestrian", Killed.driver.pass))
project <- project %>%
  mutate(Killed.driver.pass = ifelse(str_detect(Killed.driver.pass, "driver & passenger"), "driver and passenger", Killed.driver.pass))
project <- project %>%
  mutate(Killed.driver.pass = ifelse(str_detect(Killed.driver.pass, "mc driver"), "motorcyclist", Killed.driver.pass))
project <- project %>%
  mutate(Killed.driver.pass = ifelse(str_detect(Killed.driver.pass, "driver (other)"), "other driver", Killed.driver.pass))
project <- project %>%
  mutate(Killed.driver.pass = ifelse(str_detect(Killed.driver.pass, ""), "both", Killed.driver.pass))

# Create a line graph
ggplot(project, aes(x = Dist, y = ..count.., group = 1)) +
  geom_line(stat = "count", color = "skyblue") +
  labs(title = "Number of Fatalities by Phase",
       x = "Phase",
       y = "Count of Fatalities") +
  theme_minimal()

model <- lm(Number.of.Fatalities ~ Type.of.road, data = project)
rsquared <- summary(model)$r.squared
adjusted_rsquared <- summary(model)$adj.r.squared
standard_error <- summary(model)$sigma
cat("R-squared value:", rsquared, "\n")
cat("Adjusted R-squared:", adjusted_rsquared, "\n")
cat("Standard Error:", standard_error, "\n")

model <- lm(Number.of.Fatalities ~ Hour, data = project)
rsquared <- summary(model)$r.squared
adjusted_rsquared <- summary(model)$adj.r.squared
standard_error <- summary(model)$sigma
cat("R-squared value:", rsquared, "\n")
cat("Adjusted R-squared:", adjusted_rsquared, "\n")
cat("Standard Error:", standard_error, "\n")

model <- lm(Number.of.Fatalities ~ Suspected.Impairment, data = project)
rsquared <- summary(model)$r.squared
adjusted_rsquared <- summary(model)$adj.r.squared
standard_error <- summary(model)$sigma
cat("R-squared value:", rsquared, "\n")
cat("Adjusted R-squared:", adjusted_rsquared, "\n")
cat("Standard Error:", standard_error, "\n")

model <- lm(Number.of.Fatalities ~ Day, data = project)
rsquared <- summary(model)$r.squared
adjusted_rsquared <- summary(model)$adj.r.squared
standard_error <- summary(model)$sigma
cat("R-squared value:", rsquared, "\n")
cat("Adjusted R-squared:", adjusted_rsquared, "\n")
cat("Standard Error:", standard_error, "\n")

model <- lm(Number.of.Fatalities ~ DL.Status.incident, data = project)
rsquared <- summary(model)$r.squared
adjusted_rsquared <- summary(model)$adj.r.squared
standard_error <- summary(model)$sigma
cat("R-squared value:", rsquared, "\n")
cat("Adjusted R-squared:", adjusted_rsquared, "\n")
cat("Standard Error:", standard_error, "\n")

ggplot(project, aes(x = Age)) +
  geom_density(fill = "cyan4", color = "black") +
  labs(title = "Traffic Fatalities by Age of the Moon",
       x = "Age",
       y = "Density") + theme_minimal()