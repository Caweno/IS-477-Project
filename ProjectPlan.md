Project Plan: Investigating the Correlation Between Air Pollution Emissions and Honey Bee Colony Losses in the United States (2024-2025) 

Team Members & Responsibility:  

All members come up with the project topic together, and each member is responsible for some more detailed things. 

Charlotte Cao (cao52): Project Planning, Data Acquisition, Coordinator(33% of the work) 

Nanxi Chen (nanxic3): Data Cleaning & Integration (33% of the work) 

Sangshi Yang (sangshi2): Data Analysis (33% of the work) 

Introduction 

Honeybees play a vital role in world agriculture with almost 75% of food crops depending on pollinators to some degree. However, recent trends in the world's managed honeybee populations have shown worrying trends over recent years. Data collected from the survey carried out during the 2024 to 2025 period indicated that the annual loss of colonies for the honeybees rose to 55.6%, the highest to date. The collection of data has been initiated during the period of 2010 to 2011. 

However, the environmental stress factors might not be considered as the most influential factors on the quality of the nectar because the varroa mites are still considered to be the most common stress factor, the environmental stress could still somehow directly or indirectly influence the health conditions of the bees because it could influence the nectar. Our project aims to find out if there is a scientific correlation between the emission of pollutants by each state from 2024 to 2025 and the death of the bee colonies. 

Research Questions 

Is there a statistically significant correlation between air pollution emissions in each state and honeybee colony changing rates in the United States during 2024-2025? 

Datasets 

There will be three major datasets in the project, which are being extracted from the authoritive sources on official website, including the Agriculture Department of the United States and so on. The specific explanation of each datasets will be provided below: 

 

 

Dataset 1: USDA NASS Honey Bee Colonies Report 

https://esmis.nal.usda.gov/publication/honey-bee-colonies 

The first dataset comes from the United States Department of Agriculture's National Agricultural Statistics Service (NASS). The dataset covers 44 states individually plus an aggregate category for other states, with data reported at the quarterly level. The report was released in August 2025, and it provided the honey bee colonies changes based on a quarter frequencies. To be more specific, the report contains the number of bees, the losses, additions, and renovations across U.S. states from January 2024 through June 2025. The report also includes detailed breakdowns of colony health stressors, including Varroa mites, other pests and parasites, diseases, pesticides, and unknown factors. More importantly, there is a trend showing that the colonies lost with colony collapse disorder symptoms is facing a huge increase in Q1 2025 compared to Q1 2024. 

 

Dataset 2: Apiary Inspectors of America (AIA) Beekeeping Survey 

https://apiaryinspectors.org/US-beekeeping-survey-24-25 

The second dataset is conducted by the Apiary Inspectors of America in collaboration with Auburn University. The survey is based on the responses from a large number of beekeepers. They have approximately 220,000 bees, and this represents 8.4% of the estimated 2.6 million colonies in the whole united states. This dataset complements the USDA data by providing a different methodology and additional breakdowns by beekeeper scale. 

 

Dataset 3: EPA Emissions State Aggregation Data 

https://campd.epa.gov/data/custom-data-download 

The third dataset comes from the U.S. Environmental Protection Agency's Clean Air Markets Program Data (CAMPD). The dataset contains a national level of the air-quality monitor, including the common pollution factors such as SO2, CO2 mass, NOx mass, and so on. However, the dataset focuses on more of the emissions from regulated facilities instead of ambient air quality measurements. So in the future analysis, we might need to adjust what information we extract and analyze based on our research needs. 

 

Data Integration Strategy 

In this case, we chose all three data sets because they share a common geographical identifier, states in the United States of America. While the USDA and AIA data sets use state names and abbreviations, respectively, the EPA data set makes use of two-letter state codes. As a result, we normalize state codes in all data sets by aggregating the EPA monthly data into annual data per state, extracting data from the USDA PDF report using Python libraries, and finally merging data sets using pandas with state code as the primary key. 

Timeline
Week7: Project planning - Decide research question and find datasets 

Week8: Data acquisition, convert PDF file to csv files - Download datasets, setup GitHub repo and extract tables from PDF 

Week9: Spring break 

Week10: Data Cleaning & Integration - Standardize variables in each dataset and handle missing values

Week11: Exploratory Data Analysis - Generate summary statistics and identify potential outliers

Week12: Statistical Analysis & Visualization - Calculate correlations and build regression models 

Week13: Documentation - Write methodology and add any further code comments 

Week14: Final Repor - Compile final findings and write conclusions 

Week15: Presentation - Create slides, rehearse, prepare for Q&A 

We will hold weekly team meetings to review progress and coordinate tasks. All work will be tracked through GitHub. 

Constraints 

After browsing the datasets we selected, a number of limitations are detected and have to be stated ahead. Firstly, it should be noted that the EPA data set comprises point source emission data, not ambient data, thereby reflecting industrial output, not chemical composition in the ambient environment in which the bees are operating. While ambient data is preferable, it should also be noted that the EPA’s AQS system is not operational during this data collection period. Secondly, it should also be noted that there is a lack of temporal alignment in these data sets, insofar as the USDA data set runs from January 2024 to June 2025, the AIA data set runs from April 2024 to April 2025, and the EPA data set runs monthly through 2024. There are also missing data points in this data set, insofar as there are 50-75 missing data points in some states in the EPA data set, and some data points are missing in order to maintain confidentiality. Although the analysis might eventually indicate a certain correlation, it should also be noted that correlation does not necessarily imply causation, especially insofar as a variety of factors, such as climate change or land use change, these factors could also play a role in these outcomes. 

Gaps 

Ambient Air Quality Data  

There is no information directly given with regard to the concentrations of these air pollutants. If the EPA AQS service is available, then the information provided with regard to the concentrations of PM2.5 and ozone can be used to improve the analysis. 

Pesticide Use Data  

According to the USDA , Exposure to Pesticides are one of the major factors impacting bee health; current evidence related to the pesticide type, in each state, is not readily available by the USDA as it will be reported in 2026 when USGS publishes their National Pesticide Synthesis Project.  

Climate Data  

Moreover, weather conditions may influence the health of bees as well as the emissions. If there is time, it is possible to use the climate data offered by the NOAA to control for the potential effects.  

Technical Skills  

We are not familiar with geospatial analysis tools,for example Folium and Geopandas. It is possible to familiarize ourselves with these tools during weeks 4-5 of the course. 

 
