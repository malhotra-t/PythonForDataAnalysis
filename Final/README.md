## Final Submission
In this submission, I have done analysis on the data downloded from US government's website (https://www.usaspending.gov/DownloadCenter/API/Pages/fpds.aspx) which tracks the money spent by its internal departments on the contracts given to outside vendors. The download was done with the help of website's API. There are 4 main folders:
### 1. FetchData:
This folder contains 2 iPython notebooks:
i. US Spending - Fetch Data: This notebook contains code to make calls to API of US government website. This API provides us with multiple ways of making requests for data based on different parameters and the level of details we want. I have used the link 'https://www.usaspending.gov/fpds/fpds.php?detail=b&fiscal_year=2015&stateCode=TX&max_records=10' which has the following parameters:
- detail=b
This signifies that level of detail is 'basic'
- fiscal_year=2015
This takes the year for which we want the data. I have taken the data for 2016 & 2017.
- stateCode=TX
This takes as input the state code for which we want the data. I have requested the data for states MA and PA.
- max_records=10
This is the number of records per file. I set it to 100 per file.
In this notebook there are 2 functions followed by the funtion call. The first function is to find out the total number of records for a particular set of parameters passed in the above link. The second function uses this total number of records to find out the number of files that will be downloaded by dividing it by 100(max_records). Using these functions iteratively I create a directory structure of the form 'year/stateCode/file.xml' to save the files for year 2016 & 2017 for states MA & PA.

ii. ConvertXmlToDataFramePickle: Once the data was downloaded into a directory structure, I converted the data in XML files into a dataframe and then saved the dataframe as a '.pickle' file which could be easily used for further analysis without going over 1.3GB of data again and again. 
Please Note: This pickle file has not been committed on GitHub due to size restrictions as Github only allows files of size upto 100MB. This size of this file was 405MB. In order to run the analysis again using this pickle file, you need to download it from here (...) and save it at this path in your system (...).

### 2. Data: This folder contains 2 folders for years 2016 and 2017. Each of these folders further contain 2 folders for states MA and PA which have all the XML files. 

### 3. Extra: This folder contains the US govt. website's data dictionary in the form of a pdf file (USAspending.govDataDictionary.pdf) which explains terminology used in the XML files in the form of tags.  

### 4. Analysis: This folder consists of 3 analysis done of the pickle file created in the above steps.
#### Analysis 1:
