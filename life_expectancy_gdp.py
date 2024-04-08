#Importing the necessary files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading in the data
df = pd.read_csv("D:\\Coding Projects\\Python Projects\\Codecademy Projects\\Life-Expectancy-and-GDP-Starter\\Life-Expectancy-and-GDP-Starter\\all_data.csv")

#Here's the data for each country
chile_data = df[df["Country"] == "Chile"]
china_data = df[df["Country"] == "China"]
germany_data = df[df["Country"] == "Germany"]
mexico_data = df[df["Country"] == "Mexico"]
usa_data = df[df["Country"] == "United States of America"]
zimbabwe_data = df[df["Country"] == "Zimbabwe"]

#Print out columns of the dataframe
#print(df.columns)
#print(df["Country"])

#Life Expectancy vs GDP
#Scatterplot for Chile
sns.scatterplot(data=chile_data, x=chile_data["GDP"], y=chile_data["Life expectancy at birth (years)"])
plt.title("Life Expectancy and Nominal GDP, Chile")
plt.xlabel("GDP (US Dollars)")
plt.ylabel("Life expectancy at birth (years)")
plt.figure()

#Scatterplot for China
sns.scatterplot(data=china_data, x=china_data["GDP"], y=china_data["Life expectancy at birth (years)"])
plt.title("Life Expectancy and Nominal GDP, China")
plt.xlabel("GDP (US Dollars)")
plt.ylabel("Life expectancy at birth (years)")
plt.figure()

#Scatterplot for Germany
sns.scatterplot(data=germany_data, x=germany_data["GDP"], y=germany_data["Life expectancy at birth (years)"])
plt.title("Life Expectancy and Nominal GDP, Germany")
plt.xlabel("GDP (US Dollars)")
plt.ylabel("Life expectancy at birth (years)")
plt.figure()

#Scatterplot for Mexico
sns.scatterplot(data=mexico_data, x=mexico_data["GDP"], y=mexico_data["Life expectancy at birth (years)"])
plt.title("Life Expectancy and Nominal GDP, Mexico")
plt.xlabel("GDP (US Dollars)")
plt.ylabel("Life expectancy at birth (years)")
plt.figure()

#Scatterplot for America
sns.scatterplot(data=usa_data, x=usa_data["GDP"], y=usa_data["Life expectancy at birth (years)"])
plt.title("Life Expectancy and Nominal GDP, United States")
plt.xlabel("GDP (US Dollars)")
plt.ylabel("Life expectancy at birth (years)")
plt.figure()

#Scatterplot for Zimbabwe
sns.scatterplot(data=zimbabwe_data, x=zimbabwe_data["GDP"], y=zimbabwe_data["Life expectancy at birth (years)"])
plt.title("Life Expectancy and Nominal GDP, Zimbabwe")
plt.xlabel("Year")
plt.ylabel("Life expectancy at birth (years)")
plt.figure()


#Life Expectancy vs Year
#Scatterplot for Chile
sns.scatterplot(data=chile_data, x=chile_data["Year"], y=chile_data["Life expectancy at birth (years)"])
plt.title("Life Expectancy, Chile 2000-2015")
plt.xlabel("Year")
plt.ylabel("Life expectancy at birth (years)")
plt.figure()

#Scatterplot for China
sns.scatterplot(data=china_data, x=china_data["Year"], y=china_data["Life expectancy at birth (years)"])
plt.title("Life Expectancy, China 2000-2015")
plt.xlabel("Year")
plt.ylabel("Life expectancy at birth (years)")
plt.figure()

#Scatterplot for Germany
sns.scatterplot(data=germany_data, x=germany_data["Year"], y=germany_data["Life expectancy at birth (years)"])
plt.title("Life Expectancy, Germany 2000-2015")
plt.xlabel("Year")
plt.ylabel("Life expectancy at birth (years)")
plt.figure()

#Scatterplot for Mexico
sns.scatterplot(data=mexico_data, x=mexico_data["Year"], y=mexico_data["Life expectancy at birth (years)"])
plt.title("Life Expectancy, Mexico 2000-2015")
plt.xlabel("Year")
plt.ylabel("Life expectancy at birth (years)")
plt.figure()

#Scatterplot for America
sns.scatterplot(data=usa_data, x=usa_data["Year"], y=usa_data["Life expectancy at birth (years)"])
plt.title("Life Expectancy, United States 2000-2015")
plt.xlabel("Year")
plt.ylabel("Life expectancy at birth (years)")
plt.figure()

#Scatterplot for Zimbabwe
sns.scatterplot(data=zimbabwe_data, x=zimbabwe_data["Year"], y=zimbabwe_data["Life expectancy at birth (years)"])
plt.title("Life Expectancy, Zimbabwe 2000-2015")
plt.xlabel("Year")
plt.ylabel("Life expectancy at birth (years)")
plt.show()
plt.clf()


#Splitting data into two groups
selected_countries = df[df["Country"].isin(["United States of America", "China", "Germany", "Mexico", "Chile"])]

#Scatterplot for all countries
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x=df["Year"], y=df["Life expectancy at birth (years)"], hue="Country")
plt.title("Life expectancy over time for selected countries, 2000-2015")
plt.xlabel("Year")
plt.ylabel("Life Expectancy at birth (years)")

#Scatterplot for Germany, Chile, America, China, and Mexico
plt.figure(figsize=(10, 6))
sns.lineplot(data=selected_countries, x=df["Year"], y=df["Life expectancy at birth (years)"], hue="Country")
plt.title("Life expectancy over time for selected countries, 2000-2015")
plt.xlabel("Year")
plt.ylabel("Life Expectancy at birth (years)")

#GDP vs Year

#Splitting countries into three groups
selected_countries1 = df[df["Country"].isin(["United States of America", "China", "Germany"])]
selected_countries2 = df[df["Country"].isin(["Mexico", "Chile", "Zimbabwe"])]
selected_countries3 = df[df["Country"].isin(["Zimbabwe"])]

#Scatterplot for all countries
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x=df["Year"], y=df["GDP"], hue="Country")
plt.title("GDP over time for selected countries, 2000-2015")
plt.xlabel("Year")
plt.ylabel("Gross Domestic Product")

#Scatterplot for each group of countries
#America, China, Germany
plt.figure(figsize=(10, 6))
sns.lineplot(data=selected_countries1, x=df["Year"], y=df["GDP"], hue="Country")
plt.title("GDP over time for the United States, China, and Germany, 2000-2015")
plt.xlabel("Year")
plt.ylabel("Gross Domestic Product")

#Mexico, Chile, Zimbabwe
plt.figure(figsize=(10, 6))
sns.lineplot(data=selected_countries2, x=df["Year"], y=df["GDP"], hue="Country")
plt.title("GDP over time for Mexico, Chile, and Zimbabwe, 2000-2015")
plt.xlabel("Year")
plt.ylabel("Gross Domestic Product")

#Zimbabwe
plt.figure(figsize=(10, 6))
sns.lineplot(data=selected_countries3, x=df["Year"], y=df["GDP"], hue="Country")
plt.title("GDP over time for Zimbabwe, 2000-2015")
plt.xlabel("Year")
plt.ylabel("Gross Domestic Product")
plt.show()
plt.clf()
