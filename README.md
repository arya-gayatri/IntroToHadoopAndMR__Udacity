# Introduction to Hadoop and MapReduce
----------s

## Introduction
This repository contains source code for the assignments of Udacity's course, [Introduction to Hadoop and MapReduce](https://www.udacity.com/course/ud617)<br>

I have developed Hadoop MapReduce code for the 2 problem statements [3 questions each] in `Python`.<br>

## Instructions for Virtual Machine download and setup
Please refer [instructions document](IntroductiontoHadoopandMapreduce-VMsetup.doc) provided by Course Instructors for details on the Hadoop Virtual Machine [VM henceforth] setup required for running these examples.<br>
As mentioned in the above document, VM image with Hadoop installed and preconfigured, can be downloaded from [Udacity CDN](http://content.udacity-data.com/courses/ud617/Cloudera-Udacity-Training-VM-4.1.1.c.zip). 

Credentials to login to this Virtual Machine are: `training` / `training`.

## Data
### Input Files
~~Input files for the problem statements [ProblemStatement#1](ProblemStatement1/0_Input) and [ProblemStatement#2](ProblemStatement2/0_Input) have also been uploaded to GitHub.~~<br> 

These input compressed archives can also be downloaded from Udacity servers. Please check [here](http://content.udacity-data.com/courses/ud617/purchases.txt.gz) for input file for Problem Statement 1 and [here](http://content.udacity-data.com/courses/ud617/access_log.gz) for Problem Statement 2.<br>

### Output Files
The output is the Hadoop MR Job output which is obtained after processing and analyzing the specific question.

## [Problem Statement1](ProblemStatement1)
Execution steps are also documented for running the following in [Python](ProblemStatement1/Python/0_P1_Exec_Steps_Py.sh)

### Question#1
Instead of breaking the sales down by store, instead give us a sales breakdown by product category across all of our stores.

1. What is the value of total sales for the following categories?
	- Toys
	- Consumer Electronics

#### Code
##### Python variant
[`P1Q1_Mapper.py`](ProblemStatement1/Python/P1Q1_Mapper.py) and [`P1Q1_Reducer.py`](ProblemStatement1/Python/P1Q1_Reducer.py)

### Question#2
Find the monetary value for the highest individual sale for each separate store.

1. What are the values for the following stores?
	- Reno
	- Toledo
	- Chandler

#### Code
##### Python variant
[`P1Q2_Mapper.py`](ProblemStatement1/Python/P1Q2_Mapper.py) and [`P1Q2_Reducer.py`](ProblemStatement1/Python/P1Q2_Reducer.py)

### Question#3
Find the total sales value across all the stores, and the total number of sales. Assume there is only one reducer.

1. Find
	- Total sales value across all the stores
	- Total number of sales

#### Code
##### Python variant
[`P1Q3_Mapper.py`](ProblemStatement1/Python/P1Q3_Mapper.py) and [`P1Q3_Reducer.py`](ProblemStatement1/Python/P1Q3_Reducer.py)

## [Problem Statement2](ProblemStatement2):
Execution steps are also documented for running the following in either [Python](ProblemStatement2/Python/0_P2_Exec_Steps_Py.sh) or [Java](ProblemStatement2/Java/0_P2_Exec_Steps_Java.sh).

### Question#1
Write a MapReduce program which will display the number of hits for each different file on the Web site.

1. Find
	- How many hits were made to the page: /assets/js/the-associates.js?

#### Code
##### Python variant
[`P2Q1_Mapper.py`](ProblemStatement2/Python/P2Q1_Mapper.py) and [`P2Q1_Reducer.py`](ProblemStatement2/Python/P2Q1_Reducer.py)

### Question#2
Write a MapReduce program which determines the number of hits to the site made by each different IP Address.
	
1. Find
	- How many hits were made by the IP address: 10.99.99.186?

#### Code
##### Python variant
[`P2Q2_Mapper.py`](ProblemStatement2/Python/P2Q2_Mapper.py) and [`P2Q2_Reducer.py`](ProblemStatement2/Python/P2Q2_Reducer.py)

### Question#3
Find the most popular file on the Web site. In other words, the file which had the most hits. Your Reducer should just write out the name of the file and number of hits into HDFS.

1. Find
	- Full path to the most popular file?
	- Number of hits to that file?

#### Code
##### Python variant
[`P2Q3_Mapper.py`](ProblemStatement2/Python/P2Q3_Mapper.py) and [`P2Q3_Reducer.py`](ProblemStatement2/Python/P2Q3_Reducer.py)