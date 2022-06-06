# HW1: SQL and Relational Data Modeling
In this assignment, you will practice working with relational databases, or data management systems that represent data as linked tables (rows/columns) of data.  SQLite is an open-source, zero-configuration, self-contained, stand-alone, relational database engine designed to be embedded into an application. While it is not completely realistic for largee-scale data analysis scenarios much of the syntax will be the same as other systems.

* Due Wednesday, April 13 11:59pm*

## Getting Started
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

In your web browser,  accept the assignment using the following link [https://classroom.github.com/a/8_LrMWFL].
You'll be given a dropdown list with a list of CNET ids, please select yours and "accept" the assignment. 
This will create a pre-populated repository for you with the assignment details.
Once the repository is created, you will get a link that looks something like this:
```
https://github.com/CMSC-13600-Data-Engineering/homework-1-sql-<your github name>
```

Next, we will `clone` this repository to linux.cs.uchicago.edu. *Note* Every year students cut an paste the following instructions without realizing that my CNET id is "skr" and my github username is "sjyk". Please replace those with your own.
```
(cmscm13600-env) skr@linux2:~$ git clone git@github.com:CMSC-13600-Data-Engineering/homework-1-sql-sjyk.git
```
Enter the cloned repository, and now, you are ready to start your assignment!

## The Sakila Database and SQLite Command Line
We will use a standard "demo" database for this homework assignment. The Sakila sample database is designed to represent a DVD rental store. A description of the database can be found here:
[https://dev.mysql.com/doc/sakila/en/sakila-introduction.html]. Before you get started, please skim through the documentation for this database. In particular, we want you to look at [https://dev.mysql.com/doc/sakila/en/sakila-structure.html]. Read those notess very carefully as it will help you with your assignment. 

SQLite has a command line interface that can be used to explore a database before writing any formal code. First, enter your recently cloned repository:
```
(cmscm13600-env) skr@linux2:~$ cd homework-1-sql-sjyk.git
```
Then, run the following command
```
(cmscm13600-env) skr@linux2:~/homework-1-sql-sjyk.git/$ sqlite3 sqlite-sakila.db
SQLite version 3.24.0 2018-06-04 14:10:15
Enter ".help" for usage hints.
sqlite>
```
This command will open up a command line interface where you can type in SQLite commands to learn more about the data.

### (TODO 1) Data Description Commands
We will now ask several questions about the schema of this database and how the data are organized. You will have to read [https://www.sqlitetutorial.net/sqlite-commands/] to determine what commands to run to get these answers. Write down your answers in "TODO1.txt" with each answer on a separate line.  

1. Write the command that lists all the tables in the Sakila database
2. In the "country" table, what is the data type for "country.country_id"?
3. On what attribute does the "staff" table join with the "store" table?
4. Which column in the "film_text" table can have a null value?


### (TODO 2) Basic SQL Commands
Now, we will ask you to answer a few questions that require SQL queries over the dataset. Write your answers in TODO2.txt. 

1. A marketing consultant is asking you some questions about rental pricing in the Sakila store. They want to understand how many titles (distinct films) there are at each price point. Write a SQL statement that counts the number of films per rental price point.
2. Modify your answer to (1) and now write a SQL statement that counts the total number of DVDs in inventory per rental price point.
3. Modify your answer to (2) and write a SQL statement that counts that counts the total number of DVDs in inventory per rental price point that are "Action" movies.
4. Write a SQL statement to find all actors that have acted in at least 5 Horror films.


You can exit the SQLite command line by running:
```
sqlite> .exit
```

## Connecting SQLite to Python
Relational databases are so ubiquitous that every programming language has an interface to link with ushc databases. In the next exercise, you will write a program to determine the relationship between Sakila's inventory and their rentals. All of your code will go into `stocking.py`. But, before we do that, we will discuss some of the basics of loading SQL data into Python.

The first thing that you will do is to create connection to the database:
```
import sqlite3
con = sqlite3.connect('sqlite-sakila.db')
```
Based on this example, write code to connect to the database with Python by filling in `connect()` in `stocking.py`.

Using this connection, we can execute queries over this database. Consider the following query that lists out all of the actors in the database. I need to write the SQL query as a string, and then run `con.execute(query)` to get the result.
```
query = '''select * from actor;
		'''
data = con.execute(query) 
```

The result is a iterable collection of rows:
```
for row in data:
	print(row)

(1, u'PENELOPE', u'GUINESS', u'2021-03-06 15:51:59')
(2, u'NICK', u'WAHLBERG', u'2021-03-06 15:51:59')
(3, u'ED', u'CHASE', u'2021-03-06 15:51:59')
...
(198, u'MARY', u'KEITEL', u'2021-03-06 15:52:00')
(199, u'JULIA', u'FAWCETT', u'2021-03-06 15:52:00')
(200, u'THORA', u'TEMPLE', u'2021-03-06 15:52:00')
```
You need to keep track of your SQL query to know what each column represents, for example the following prints out the first names:
```
for row in data:
	print(row[1])
```

### TODO 3. Creating An Inventory Dataset
Your task in the next TODO is to create a dataset that analyzes the inventory of this store. Your code will go into `inventory_dataset()` and will take as input a SQLite connection and output a Pandas DataFrame with the following properties:

		* Each row of the DataFrame will correspond to a distinct film 
		* There will be a column film name ("name")
	   	* There will be a column that has the number of copies in the inventory ("inv_copies")
	   	* There will be a column that has number of times the film has been rented out ("rentals")
	   	* There will be a column that has the rental price ("rental_rate")
	   	* There will be a column that has the replacement price ("replacement_price")

Hint, to do this, you might have to write multiple SQL queries (though it can definitely be done with a single one)! 

### Testing and Submission
To test your code, run
```
(cmscm13600-env) skr@linux2:~/homework-1-sql-sjyk.git/$ python stocking.py
```
which will produce a CSV file output of your inventory dataset. Due to the nature of SQL where rows might be in slightly different orders and columns might not be named in exactly the same way, there won't be an autograder for this assignment and we'll grade based on visual inspection (trust us, it causes more issues than it solves).
To submit your code, add the following files:
```
(cmscm13600-env) skr@linux2:~/homework-1-sql-sjyk$ git add stocking.py TODO1.txt TODO2.txt
```
```
(cmscm13600-env) skr@linux2:~/homework-1-sql-sjyk$ git commit -m'my submission'
```
```
(cmscm13600-env) skr@linux2:~/homework-1-sql-sjyk$ git push
```
