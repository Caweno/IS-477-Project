### -- IS-477-Project -- ###

# Title: Investigating the Relationship Between Air Pollution Emissions and Honey Bee Colony Losses in the United States

# Contributors:

• Charlotte Cao (cao52)
• Nanxi Chen (nanxic3)
• Sangshi (Justin) Yang (sangshi2)

# Summary:
Project description: Our project investigates the relationship between air pollution emissions and honey bee colony health across the United States. Within the project, we combine datasets from authoritative sources. We collected the honey bee colony data from the United States Department of Agriculture (USDA) National Agricultural Statistics Service. The USDA websites provides trustful information on colony counts, losses, and stress factors. The air pollution data is obtained from the Environmental Protection Agency (EPA) Air Quality System, which records daily pollutant measurements by different national wide monitoring stations. Our project followed a systematic and reproducible cycle of data management, curation, and reproducibility. We categorized every single step into correlated folders to store the data and prepare for data tracking. Also we handle missing values, standardize variables like state and time formats, and aggregate data when needed to align different time scale. These datasets are cleaned, standardized, and merged at the state level to ensure consistency. 

Motivation: This project is inspired by a simple observation from our daily lives. While traveling along I-57 toward Chicago, we always see the giant amount of farmland, especially corn fields extending across the landscape. As we were chitchatting with our group members, we were talking about how much modern food production depends on nature working in balance seeing these large systematic agricultural farmlands. That moment of curiosity led us to think more deeply about agriculture, and that leads eventually to honey bees because they play a very important role in the entire food system as pollinators.  

Research Questions: According to the Food and Agriculture Organization, honey bees are responsible for pollinating nearly 75% of food crops worldwide, which is a crucial part of agricultural sustainability. However, while digging for more information, there is a rising national problem that draws our attention. Recent reports in the United States show a concerning rise in honey bee colony losses, reaching record-high levels from 2024 – 2025. Besides the known scientific biological factors such as parasites and diseases, it is mentioned that environmental influences, especially air pollution emissions, could considered as a highly potential triggering factor for the honey bees colony. Therefore, we decided to do the project that aims to explore whether there is a measurable relationship between air pollution and honey bee colony health across the United States. 

Findings: 

# Data Profile: 

Data profile overview: There are two primary data sources used: (1)The USDA National Agricultural Statistics Service (NASS) Honey Bee Colonies Report, and (2)The EPA Air Quality System (AQS) daily monitoring data. 

Dataset 1: USDA NASS Honey Bee Colonies Report: 

Source: USDA (National Agricultural Statistics Service) 
Download URL: https://esmis.nal.usda.gov/publication/honey-bee-colonies 
Repository Location: honey_bee_colonies_2025.csv (root directory) 

Structure & content:  

The data itself is originally published online on a website, and it is free to download with pdf version. In the pdf covers the data record from January 2024 to April 2025. There are factors that could potentially influence the honeybee colonies. We categorize them for the related and unrelated factors. Those stressor factors are not related to our research questions because the stressors like varoa mites, pests and parasites, diseases, and other pesticides are confirmed factors that will influence the honeybee colonies. Therefore, we only need a portion of the information from the pdf.  

We converted the pdf into a csv file for further analysis. Before putting them into the raw data, we did a little preprocessing. There are several columns from the original EPA daily summary files that are removed because they are not relevant to state-level analysis. These include: State Code, County Code, Site Num, Parameter Code, POC, Latitude, Longitude, Datum, Sample Duration, Pollutant Standard, Event Type, 1st Max Value, 1st Max Hour, AQI, Method Code, Method Name, Local Site Name, Address, County Name, City Name, CBSA Name, and Date of Last Change. 

In the raw data file, the “csv honey_bee_colonies_2024_merged” shows all the attributes of the honeybee colonies. There are 137 rows and 17 columns in the csv. Each row represents a state in the U.S in a specific quarter in 2024. The 2025 honeybee colonies csv is also stored in raw data file, named ‘honey_bee_colonies_2025.csv’.Key variables include colony counts, colony losses, additions, and renovation measures. 

After getting the raw data CSVs, we need to merge the data into a more useful csv, and we started our cleaning process by removing the unrelated factors as mentioned above. We kept the attributes that explaining the numbers of changes of honeybees. 

# Data Quality:

# Data Cleaning:

# Findings:

# Future work:

# Challenges:

# Reproducing:

# References:

# 
