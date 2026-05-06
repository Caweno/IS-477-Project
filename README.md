### -- IS-477-Project -- ###

# Title: Investigating the Relationship Between Air Pollution Emissions and Honey Bee Colony Losses in the United States

# Contributors:

• Charlotte Cao (cao52)

• Nanxi Chen (nanxic3)

• Sangshi (Justin) Yang (sangshi2)

# Summary:
**Project description:** Our project investigates the relationship between air pollution emissions and honey bee colony health across the United States. Within the project, we combine datasets from authoritative sources. We collected the honey bee colony data from the United States Department of Agriculture (USDA) National Agricultural Statistics Service. The USDA websites provides trustful information on colony counts, losses, and stress factors. The air pollution data is obtained from the Environmental Protection Agency (EPA) Air Quality System, which records daily pollutant measurements by different national wide monitoring stations. Our project followed a systematic and reproducible cycle of data management, curation, and reproducibility. We categorized every single step into correlated folders to store the data and prepare for data tracking. Also we handle missing values, standardize variables like state and time formats, and aggregate data when needed to align different time scale. These datasets are cleaned, standardized, and merged at the state level to ensure consistency. 

**Motivation:** This project is inspired by a simple observation from our daily lives. While traveling along I-57 toward Chicago, we always see the giant amount of farmland, especially corn fields extending across the landscape. As we were chitchatting with our group members, we were talking about how much modern food production depends on nature working in balance seeing these large systematic agricultural farmlands. That moment of curiosity led us to think more deeply about agriculture, and that leads eventually to honey bees because they play a very important role in the entire food system as pollinators.  

**Research Questions:** According to the Food and Agriculture Organization, honey bees are responsible for pollinating nearly 75% of food crops worldwide, which is a crucial part of agricultural sustainability. However, while digging for more information, there is a rising national problem that draws our attention. Recent reports in the United States show a concerning rise in honey bee colony losses, reaching record-high levels from 2024 – 2025. Besides the known scientific biological factors such as parasites and diseases, it is mentioned that environmental influences, especially air pollution emissions, could considered as a highly potential triggering factor for the honey bees colony. Therefore, we decided to do the project that aims to explore whether there is a measurable relationship between air pollution and honey bee colony health across the United States. 

**Findings:** 

# Data Profile: 

## **Data profile overview :** There are two primary data sources used: (1)The USDA National Agricultural Statistics Service (NASS) Honey Bee Colonies Report, and (2)The EPA Air Quality System (AQS) daily monitoring data.

### **Dataset 1:** USDA NASS Honey Bee Colonies Report: 

**Source:** USDA (National Agricultural Statistics Service) 

**Download URL:** https://esmis.nal.usda.gov/publication/honey-bee-colonies 

**Repository Location:** honey_bee_colonies_2025.csv (root directory) 

**Structure & Content & Characteristic:**  

The data itself is originally published online on a website, and it is free to download with pdf version. In the pdf covers the data record from January 2024 to April 2025. There are factors that could potentially influence the honeybee colonies. We categorize them for the related and unrelated factors. Those stressor factors are not related to our research questions because the stressors like varoa mites, pests and parasites, diseases, and other pesticides are confirmed factors that will influence the honeybee colonies. Therefore, we only need a portion of the information from the pdf.  

We converted the pdf into a csv file for further analysis. Before putting them into the raw data, we did a little preprocessing. There are several columns from the original EPA daily summary files that are removed because they are not relevant to state-level analysis. These include: State Code, County Code, Site Num, Parameter Code, POC, Latitude, Longitude, Datum, Sample Duration, Pollutant Standard, Event Type, 1st Max Value, 1st Max Hour, AQI, Method Code, Method Name, Local Site Name, Address, County Name, City Name, CBSA Name, and Date of Last Change. 

In the raw data file, the “csv honey_bee_colonies_2024_merged” shows all the attributes of the honeybee colonies. There are 137 rows and 17 columns in the csv. Each row represents a state in the U.S in a specific quarter in 2024. The 2025 honeybee colonies csv is also stored in raw data file, named ‘honey_bee_colonies_2025.csv’.Key variables include colony counts, colony losses, additions, and renovation measures. 

After getting the raw data CSVs, we need to merge the data into a more useful csv, and we started our cleaning process by removing the unrelated factors as mentioned above. We kept the attributes that explaining the numbers of changes of honeybees. 

### **Dataset 2:** EPA Air Quality System (AQS) Data: 

**Source:** EPA Air Quality System 

**Download URL:** https://aqs.epa.gov/aqsweb/airdata/download_files.html#Annual 

**Repository Location:** All_Pollutant's_Observation_Changes_from_2024_to_2025 

**Structure & Content & Characteristic:** The second dataset is a massive environmental database containing daily air pollution monitoring data in the United States of America within 2024 and 2025 years. The dataset is recorded in structured CSV files with one day observation of pollutants in particular U.S. states. It contains approximately 2.23 million rows and 10 columns. It consists of the following key fields: state name, parameter name (pollutant name), local observation date, units of measurement, number of observations, percentage of observation completeness, and arithmetic mean pollutant concentration. Additional time-related variables such as month and quarter are included to support seasonal and temporal analysis. The dataset also contains an automatically generated index column (Unnamed: 0) from the CSV export process. 

Data is collected from monitoring stations with uneven spatial coverage—urban states have denser monitoring networks than rural ones. Data completeness varies, and an “observation percent” field is used to indicate measurement reliability. Pollutants are measured in different units, so each is analyzed separately. 

We paid extra attention to the data collection and selection processes. Both datasets are published by U.S. federal government agencies and are in the public domain. The USDA NASS data is aimed to provide an open and objective statistical information for people to use. The EPA AQS data is made freely available through the Clean Air Act's public data requirements. Therefore, there should not be any licensing restriction concerns in our project because our goal is purely for non-commercial academic research purposes. 

As for the ethical concerns, there is a potential ethical concern for each dataset that might needs attention. There is a data suppression in the USDA dataset while we were collecting our data. The USDA withholds some specific values, which were marked as ‘D’ while first publication. The USDA did this intentionally because they want to protect the confidentiality of survey respondents the information of the individual beekeepers. Based on this purpose, we decided to respect these suppressions by treating them as missing values rather than attempting to impute or reverse-engineer the underlying figures. For the EPA data, the data is being collected based on a objective and scientific observation. There is no human integration involved in the stationary observation, so the result of the observation is totally depended on the number of the observation equipment. However, it is worth noting that monitoring station placement decisions can introduce environmental justice considerations: historically underserved or rural communities may have fewer monitoring stations, potentially leading to less representative air quality measurements in those areas. This is a known limitation of the EPA monitoring network and may affect the completeness of our state-level pollution averages. 

# Data Quality:

As discussed in the lecture about the data quality, the data quality is very important. To prevent the data being garbage in garbage out, we paid extra attention to the data quality control. We decided to assess the data quality in different dimensions, including accuracy, completeness, consistency, validity, timeliness, and representativeness. We also considered common data quality issues such as missing values, structural errors, and potential bias in data collection. 

**Accuracy:** The accuracy is a very crucial part in data quality control that it even could be considered as a prerequisite for a data to be used for further analysis. We will exam if our datasets reflect the real-world conditions. Our tow datasets are collected and published by the authorities US government agencies, which increase the overall reliability because there are formal standards and accountability within the organization. The USDA NASS dataset is based on survey data from beekeepers, while the EPA AQS dataset is collected through automated monitoring stations. Therefore, the raw data could be considered as accurate and good to use.  

**Completeness:** Since our research question involves a lot of data, the completeness is important for the general pattern analysis. Overall, we have good completeness in our dataset, but there is some subtle concerns in the dataset of the number of the honeybees. In the USDA dataset, some values are intentionally suppressed and marked as “D.” These are considered missing values and reduce the completeness of the dataset. According to data quality concepts, missing data can significantly affect analysis results and reduce statistical power . Since these values are missing not at random (MNAR), they may introduce bias if not handled carefully. In the EPA dataset, completeness varies across observations. The “observation percent” variable shows how much data is available for each record. Some records have low completeness, meaning the daily average may not be reliable. Therefore, completeness is uneven across both datasets and must be considered in analysis. 

**Consistency:** Consistency refers to whether the data is uniform in format and structure. For the USDA dataset, there may be potential consistency issues because the data was originally published in PDF format and then converted into CSV. This conversion process may lead to structural errors or formatting inconsistencies. We converted this process by ourselves, so this might lead to unconscious misaligned columns or incorrect data types. While removing unrelated variables, we might somehow dropped the related columns, and that might lead to inconsistencies. For the EPA dataset, the data is more structured and standardized, since it is directly downloaded in CSV format. However, there may still be minor inconsistencies, such as differences in pollutant naming or formatting of dates. According to the lecture, these types of syntactic errors can affect data processing and analysis if not standardized. 

**Validity:** The extreme values are a major concern when testing the validity of our data quality. In the USDA dataset, there are some numbers of extreme values, such as unrealistic colony counts or even negative values. If we just delete those values without further examination, the accuracy of the dataset will be compromised, but if we leave those values unnoticed, they would be considered semantic errors because they violate real world logic. There is a kind of dilemma that we can’t tell if the so-called abnormal values should be dropped because we don’t have a confirmed way to test it. In the EPA dataset, validity includes checking whether pollutant values fall within reasonable ranges and whether observation percentages are between 0 and 100. Any violations of these rules indicate data quality problems. Based on the data quality framework, these types of issues are considered constraint violations and should be identified during data profiling. 

**Timeliness:** We believed the timeliness of the data is up-to-date and relevant. Both datasets are relatively recent, covering 2024 and 2025. This makes them suitable for current analysis and reduces concerns about outdated information. Therefore, timeliness is a strength of both datasets. 

**Representativeness:** In the USDA dataset, the data is based on survey responses, which means the research crew of the agriculture department came to the honeybee keepers and gathering the information of the bees. This may not fully represent all beekeepers. Non-response or underreporting can introduce bias. In the EPA dataset, there is a clear issue of uneven spatial coverage. Urban areas tend to have more monitoring stations, while rural areas have fewer. This creates a systematic bias in the data, where pollution measurements may better represent urban environments. According to data quality theory, this type of bias is considered a systematic error that affects the overall distribution of the data. 

# Data Cleaning:

# Findings:

The analysis aims to find the correlations between five major air pollutants: Ozone, Pm2.5, Carbon monoxide, NO₂, and SO₂ and three honeybee colony metrics: Percent Lost, Percent Renovated, and Net Change Rate. We used a panel dataset including approximately 161-167 state-quarter observations and after generating all the necessary visualizations and analyzing their results, the statistically significant patterns are finally found.  

First of all, the strongest and most obvious finding is that: PM2.5 shows a positive correlation with Percent Lost (r = +0.27, p ≈ 5 × 10⁻⁴). This finding keeps remaing significant even after applying a Bonferroni correlation for multiple many other comparisons. What's more, this relationship is further supported by the state-average analysis (r = +0.37, p ≈ 0.013; Spearman ρ = +0.48, p ≈ 0.001). this is the only pollutant that indicates a direct and robust relationship with honeybee colony changes. Additionally, PM2.5 is negatively associated with Net Change Rate (r = −0.20, p ≈ 0.010), which means that higher particulate pollution will lead to negative colony behaviors. This finding is biologicall plausible since pollutant particles like PM2.5 can easily interfere with bees’ olfacotry navigation, therefore impair their respiratory function, and eventually reducing their foraging efficiency and survival.  

Secondly, ozone, on the other hand, presents the largest positive correlation with Net Change Rate (r = +0.48, p ≈ 4 × 10⁻¹¹) and Percent Renovated (r = +0.37, p ≈ 1 × 10⁻⁵). It is also negatively associated with Percent Lost (r = −0.19, p ≈ 0.013; Spearman ρ = −0.33, p ≈ 1 × 10⁻⁵). While these results might initially suggest that Ozone benefits honeybee colonies, several other factors cannnot be ignored, these results might be driven by ecological confounding. Ozone concentrations tend to be higher in warm and sunny regions like sounthern and western United States. Conditions like these will be more favorable for agricultural growth and bee activities, which can partially explain why the phenomenon of increasing colony growth and renovation is obvious in these regions. So, the positive correlation of Ozone is pausibly more likely to be explained by climate and landuse factors rather than any “possible” protective effect of ozone itself.  

Thirdly, carbon monoxide and nitrogen dioxide show weaker but directionally consistent positive associations with Percent Lost in the data (CO: r = +0.23, p ≈ 0.003; NO₂: r = +0.18, p ≈ 0.020). However, these relationships are not statistically significant in the state-average analysis and we eventually decided not to move on with these particles for multiple testing. Based on the current association, these patterns are likely resulted by underlying urbanization gradients, where higher pollution levels can lead to environmental stressors such as habitat fragmentation, rather than direct causal effects. 

Finally, sulfur dioxide exhibits minimal association with colony losses (r ≈ 0), indicating that there is no reliable relationship. 

Overall, among the 15 tested hypotheses, only three relationships remain significant after Bonferroni correction: Ozone and Net Change Rate; Ozone and Percent Renovated; and PM2.5 and Percent Lost. And in these three relationships, the PM2.5–Percent Lost relationship is the most credible, as it is consistent across multiple analytical processes and aligns with established biological mechanisms. 

# Future work:

# Challenges:
