             Analysing COVID_19_Data

This project delves into the analysis of sample data pertaining to covid_19 cases recorded between January 2019 and December 2020.The dataset is provided in CSV format.

  Importing and analysising CSV data using pandas
  
import pandas as pd
url = 'https://drive.google.com/file/d/1SzmRIwlpL5PrFuaUe_1TAcMV0HYHMD_b/view'
file_id = url.split('/')[-2]
dwn_url=https://drive.google.com/uc?id= + file_id
df = pd.read_csv(dwn_url)
df.columns = df.columns.str.lower()
#print(df.head())
df
To import a csv file into a pandas dataframe from a google drive link.Url is downloaded as a shareable link which file_id is extracted from link.'https://drive.google.com/uc?id=' is the URL for Google Drive's direct download link,the id parameter in the URL is the unique ID of the file that you want to download.Once you have the direct download URL, you can use it to import the CSV file into a pandas dataframe using the pd.read_csv() function.The line df.columns = df.columns.str.lower() is used to convert all the column names in the pandas dataframe df to lowercase. This can be useful for ensuring consistency and easier handling of column names.

     Extract and Load datasets into robust structured Postgres Database
To accomplish this task,pandas library in Python to retrieve the 'Covid_19_data.csv' file and load it into a database.Next, import the necessary libraries:
 
 # from sqlalchemy import create_engine then 
 
 # create a database engine to establish a connection to your PostgreSQL database:engine=create_engine("postgresql://user_name:password@localhost:5432/covid_19_data")

# Connect to the PostgreSQL database 'engine.connect()' method establishes and returns a connection object (conn) to the PostgreSQL database. You can then use this connection object to interact with the database.

# Load the data into the table df.to_sql('covid_19_data',con=engine,if_exists='replace') with the desired table name in the PostgreSQL database. The if_exists='replace' argument ensures that the table is created and replaces it if it already exists.

from sqlalchemy import create_engine
engine=create_engine("postgresql://user_name:password@localhost:5432/covid_19_data")
engine.connect()
df.to_sql('covid_19_data',con=engine,if_exists='replace')
    This script will create a table called 'covid_19_data' in your PostgreSQL database and load the data from the CSV file into that table.

    Requirements
  - Pandas
  - SQLAlchemy
  - Python 3.x
  - PostgreSQL

  In summary,make sure you have the necessary permissions to connect to the database and perform the desired operations. :smile: # CAPSTONE_PROJECT
