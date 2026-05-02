1. Built the full workflow from raw data extraction to final dataset construction
2. Extracted honey bee data from USDA NASS reports using pdfplumber and filtered for 2024
3. Processed ~1.7M daily observations from United States Environmental Protection Agency across five pollutants
4. Converted daily pollution data into quarterly averages to match USDA reporting
5. Merged datasets on State and Quarter using an inner join
6. Produced a dataset with 128 observations and 22 features across 44 states
7. Implemented all steps in a Jupyter Notebook (data_processing.ipynb)
