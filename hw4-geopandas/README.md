# Homework 4. Final Project
In this assignment, you will get a chance to put together all of the pieces of this class. 

Due Date: *Friday May 27, 11:59 pm*

## Motivation: NYC Taxi Data
Taxis are widely used in New York City and the recorded information of where and when taxi cabs are requested can be valuable to understand traffic flow and movement patterns in the city. The data used in the attached datasets were collected and provided to the NYC Taxi and Limousine Commission (TLC). The For-Hire Vehicle (“FHV”) trip records include fields capturing the dispatching base license number and the pick-up date, time, and taxi zone location ID (shape file below). These records are generated from the FHV Trip Record submissions made by bases. 

In particular, we will study how the COVID-19 pandemic affected taxi ridership as well as pickup-dropoff location patterns in NYC. We can think of March 2020 to be a sort of natural experiment to understand how increased remote working would change city traffic patterns. The key challenge is that the data that we consider is highly seasonal. Seasonality is a characteristic of a time series in which the data experiences regular and predictable changes that recur every calendar year, as a result we will have to tease out the differences between changes due to seasonality versus changes due to COVID-19.


## Initial Setup
As before, we will provide instructions as if you are all using the CSIL login server. It is your responsibility to translate directions if you are using another platform. Open up a terminal connection to the CSIL login server:
```
ssh linux.cs.uchicago.edu
```
Then, activate your class Python environment:
```
skr@linux2:~$ conda activate cmscm13600-env
```
You'll see your prompt change into:
```
(cmscm13600-env) skr@linux2:~$
```

In your web browser,  accept the assignment using the following link [https://classroom.github.com/a/43wrY1Rg].
You'll be given a dropdown list with a list of CNET ids, please select yours and "accept" the assignment. 
This will create a pre-populated repository for you with the assignment details.
Once the repository is created, you will get a link that looks something like this:
```
https://github.com/CMSC-13600-Data-Engineering/homework-4-final-project-<your github name>
```

Next, we will `clone` this repository to linux.cs.uchicago.edu. *Note* Every year students cut an paste the following instructions without realizing that my CNET id is "skr" and my github username is "sjyk". Please replace those with your own.
```
(cmscm13600-env) skr@linux2:~$ git clone git@github.com:CMSC-13600-Data-Engineering/homework-3-hashing-sjyk.git
```
Enter the cloned repository, and now, you are ready to start your assignment!

Due to the size of the data that we are considering, you will mostly be using the repository to submit your code and use google collab.

## Notebook
All of your work will go into this notebook:
https://colab.research.google.com/drive/1viRjLUiOTbpZJ31pNS69ImkLg7KY1E_M?usp=sharing

## Submission
Download your Google Collab notebook as an ipynb file and add it/push it to this repository.
