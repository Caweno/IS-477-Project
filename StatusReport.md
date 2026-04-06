Progress Update on Project Tasks 

Over the past three weeks, with following the timeline we planned before and the feedback received, our team has made substantial progress in completing the foundational stages of the project.  

During the data acquisition phase, all needed and relevant datasets were collected, downloaded. The USDA honeybee dataset required additional steps since we can only download PDF formatted file from the website. Based on prior feedback, we refined our dataset selection to focus on ambient air quality metrics. Therefore, instead of Emissions State Aggregation Data, we downloaded the EPA Air Quality dataset (pollutants including: PM2.5, Ozone, CO, SO2, NO2) from United States Environmental Protection Agency (https://aqs.epa.gov/aqsweb/airdata/download_files.html#Annual). The datasets were downloaded directly in CSV format, allowing us to further filter and clean them more effectively.  

The data cleaning process including standardizing variable names, removing unnecessary columns and ensuring consistency across different datasets. For the EPA dataset, we filtered key variables: State Name, Parameter Name, Date Local	, Units of Measure, Observation Count, Observation Percent, and Arithmetic Mean. While removing those redundant variables: State Code, County Code, Site Num, Parameter Code, POC, Latitude, Longitude, Datum, Sample Duration, Pollutant Standard, Event Type, 1st Max Value, 1st Max Hour, AQI, Method Code, Method Name, Local Site Name, Address, County Name, City Name, CBSA Name and Date of Last Change. For the USDA dataset, we structured colony-related variables and combined separated 2024 data into the same csv file and finally get the combined file.  

Updated Timeline 

Week  

Task 

Description 

7（complete） 

Project planning 

Decide research question and find datasets 

8（complete） 

Data acquisition, convert PDF file to csv files 

Download datasets, setup GitHub repo and extract tables from PDF 

9（complete） 

Spring break 

10（complete） 

Data Cleaning & Integration 

Standardize variables in each dataset and handle missing values 

11（in progress） 

Exploratory Data Analysis 

Generate summary statistics and identify potential outliers 

12 

Statistical Analysis & Visualization 

Calculate correlations and build regression models 

13 

Documentation 

Write methodology and add any further code comments 

14 

Final Report 

Compile final findings and write conclusions 

15 

Presentation 

Create slides, rehearse, prepare for Q&A 

Changes to Project Plan 

After receiving feedback from the TA, we made several important revisions to improve the relevance of our datasets and the appropriateness of our analytical approach. First, in terms of data selection, we replaced the previously used EPA Emissions State Aggregation dataset with outdoor air quality data from the U.S. Environmental Protection Agency (EPA). This dataset provides daily measurements of pollutants collected from monitoring stations across the United States, offering more direct and high-resolution environmental exposure information that is relevant to bee colony conditions . Specifically, we focus on PM2.5 as our primary pollutant variable and introduce an additional pollutant (such as ozone, NO2, SO2, CO, Pb, or PM10) to enable comparative analysis. These pollutants are part of the EPA’s “criteria pollutants,” which are widely used indicators of air quality and environmental health . 

In addition, we removed the Apiary Inspectors of America (AIA) Beekeeping Survey dataset because it overlaps with the USDA honey bee dataset and does not provide sufficiently distinct information for analysis. Instead, incorporating multiple pollutant datasets allows us to shift toward a more meaningful research design that examines how different environmental factors relate to changes in bee colonies. The EPA Air Quality System (AQS), which serves as the underlying database for these datasets, is considered a comprehensive and reliable repository of air pollution data collected nationwide . 

We also revised our analytical methodology based on the TA’s recommendation. Due to the limited sample size of our dataset, regression models are not statistically appropriate, as they may lead to unreliable or overfitted results. As a result, we will utilize techniques based on correlation, such as Pearson correlation and Spearman correlation. The former will enable us to establish the presence of linear correlations between the concentration of pollutants and the number of bee colonies. On the other hand, Spearman correlation will help us detect the presence of any monotonic correlation, which is more durable to non-linear relationships. 

As far as work flow goes, the project can be divided into three steps – data acquisition, data cleaning and analysis. First, all of the 2024 data about pollution levels (PM2.5 + another pollutant type) will be obtained on the website of EPA AirData. All data should be summarized for each day per monitoring site; thus, all of it needs to be normalized in terms of formatting and units used. Second, the USDA NASS Honey Bee Colonies Report, which is published in PDF format, will be reformatted into a CSV database for further use in our research. Third, both databases will be standardized and cleaned up in case of some issues with alignment, such as presence of missing variables. If necessary, we can also aggregate the pollution data on a daily basis to coincide with the bee database. 

In conclusion, the cleaned datasets are merged and analyzed based on Pearson and Spearman correlations to uncover possible links between the concentrations of pollutants and variations in bees’ colonies. This analysis aims at determining the pollutant which has the closest connection with variations in bee populations and getting comparative information about their effects on the environment. The output will consist of the full dataset, codes for the data analysis, and an interpretation report explaining the data used, methodology, findings, limitations, and future work. 

 

Encountered Challenges  

During the project, we encountered several challenges related to data availability, data quality, and dataset integration.  

The problem was associated with the lack of some data. The problem of having missing or incomplete data is quite common for air quality datasets since the lack of data in air pollution studies can be quite large, according to previous research. This means that there should be special approaches employed in such cases to either get rid of missing data or aggregate it into something useful. 

The problem we had was the alignment in terms of time and structure in regard to the datasets used. The EPA’s pollution dataset uses a daily frequency, but the USDA’s honey bee dataset uses a frequency that is higher. This posed a challenge as we had to combine the pollution dataset with a larger timeframe, thus possibly losing variability and effects of the environment on bee population. 

Further, challenges were experienced in the conversion and preparation of the datasets in their appropriate formats. The first one is that of USDA honey bee dataset, which was initially in PDF format and had to undergo conversion to CSV file format. This step carried the danger of errors in the alignment of values within the columns. 

Lastly, the limitations in our research were those concerning the sample size and the scope of analysis. Once all datasets were merged depending on location and time, the resulting sample had a limited number of observations; consequently, it was not feasible to conduct regression analysis due to its complexity. Therefore, we opted for correlation analysis rather than regression due to several limitations. Although correlation analysis is less complex compared to regression analysis, it does not allow for any inference of cause and effect relationships. 

 
