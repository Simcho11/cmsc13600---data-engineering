# cmsc13600
This is a repository of the homeworks I completed as a part of CMSC13600 - Data Engineering. These homeworks were completed Spring of 2022 and were all done in Python.

## HW1: SQL and Relational Data Modeling
This assignment focused on working with relational databases with SQL and Python. We were given a relational database of a video rental store and had to link its tables in order to solve problems.

**Successes**
- Got a perfect score
- SQL queries all return the data I want

**Room for Improvement**
- Lots of messy Python

**Takeaways**
- Got very comfortable using SQL

## HW2: Entity Resolution
In this homework assignment I was tasked with matching products from a Google catalogue to an Amazon catalogue. Because the tables were not layed out in the same manner and had slightly different data for each product, I had to use entity resolution techniques such as Jaccard simularity and Levenshtein (edit) distance.

**Successes**
- Got a perfect score (over 50% match rate in under 5 minutes)

**Room for Improvement**
- Python is extremely messy
- Could certainly be more optimized - yields almost bare minimum results
- Other more advanced techniques would have worked better

**Takeaways**
- Experience working with data sets that don't work well with each other
- Better understanding of entity resolution and its application

## HW3: Bloom Filter
In this assignment I took a concept I already knew well (hashing) and made it more complicated by implementing a bloom filter.

**Successes**
- Created a program that can generate bloom filters as well as put things into a bloom filter and check to see if something is in a bloom filter

**Room for Improvement**
- Could've had a "better looking" solution by using lambdas

**Takeaways**
- Learned what a bloom filter was
- Better understanding of the idea behind hashing and how it works

## HW4: NYC Taxi Data
This assignment utilized GeoPandas (and rtrees)to analyze New York taxi data pre and post pandemic in order to determine certain impacts the pandemic had on New York. Used a New York shapefile as well as taxi and business longitude and latitude coordinates to determine certain truths about the impact of the pandemic.

**Successes**
- Successfully utilized GeoPandas and rtrees to answer all the questions

**Room for Improvement**
- Certain solutions run for a long time (unoptimized)

**Takeaways**
- This was a very challenging assignment and I was proud of myself for completing it
- Learned what rtrees were
- Got practice using GeoPandas for the first time

