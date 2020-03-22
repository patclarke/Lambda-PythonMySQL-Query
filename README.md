# Lambda-PythonMySQL-Query
Python script to connect and query MYSQL database and return the results in Json. 

# Setup
* Imported pymysql zip file to Lambda (See notes section for how to)
* Lambda function uses Python 3.7 Runtime
* Lambda function is connected to API Gateway 
* Lambda function is in the Same VPC and Subnet as RDS instance
* RDS instance has security group set to allow port 3306 from the VPC Subnet

# Overview
Setup an API that returns Json formatted results from a serverless python application that makes a database connection to RDS via Lambda. 

# What needs to be added
* Passing a paramater to the API and have python use that paramater to run a function.


# Notest
### How to import pymysql to Lambda
* download the files we need to the current directory
```
pip install pymysql -t .
```
* zip the directory
```
zip -r MyPythonLambda.zip * 
```
* from the AWS dashboard in your Lambda Function.
* Navigate to the "Function Code". Below that you will see "Code entry type".
* Click the drop down box and upload zip file. (WARNING this will erase any code you currently have in your function)