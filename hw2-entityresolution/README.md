# HW2: Entity Resolution

*Friday April 27, 2022 11:59 PM*

Entity Resolution is the task of disambiguating manifestations of real world entities in various records or mentions by linking and grouping. For example, there could be different ways of addressing the same person in text, different addresses for businesses, or photos of a particular object. In this assignment, you will link two product catalogs.

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

In your web browser,  accept the assignment using the following link [https://classroom.github.com/a/g4-qfRaP].
You'll be given a dropdown list with a list of CNET ids, please select yours and "accept" the assignment. 
This will create a pre-populated repository for you with the assignment details.
Once the repository is created, you will get a link that looks something like this:
```
https://github.com/CMSC-13600-Data-Engineering/homework-2-er-<your github name>
```

Next, we will `clone` this repository to linux.cs.uchicago.edu. *Note* Every year students cut an paste the following instructions without realizing that my CNET id is "skr" and my github username is "sjyk". Please replace those with your own.
```
(cmscm13600-env) skr@linux2:~$ git clone git@github.com:CMSC-13600-Data-Engineering/homework-2-er-sjyk.git
```
Enter the cloned repository, and now, you are ready to start your assignment!

You will also need to fetch the datasets used in this homework assignment:
```
https://www.dropbox.com/s/vq5dyl5hwfhbw98/Amazon.csv?dl=0
https://www.dropbox.com/s/fbys7cqnbl3ch1s/Amzon_GoogleProducts_perfectMapping.csv?dl=0
https://www.dropbox.com/s/o6rqmscmv38rn1v/GoogleProducts.csv?dl=0
```
Download each of the files and put it into your `hw2` folder.

Your goal is to match likely corresponding entities in both datasets. We have provided you helpeer functions to load the data.
A matching is a pairing between id's in the Google catalog and the Amazon catalog that refer to the same product. Both datasets have an 'id' field that can be used.

The ground truth is listed in the file `Amzon_GoogleProducts_perfectMapping.csv`. Your job is to construct a list of pairs of `(amazon.id, google.id)`. These matchings can be evaluated for accuracy using the `eval_matching` function:
```
>>> my_matching = [('b000jz4hqo', http://www.google.com/base/feeds/snippets/11125907881740407428'),...]
>>> {'false positive': 0.9768566493955095, 'false negative': 0.43351268255188313, 'accuracy': 0.04446992095577143}
```
False positive refers to the false positive rate, false negative refers to the false negative rate, and accuracy refers to the overall accuracy.

## Assignment
Your job is write the `match` function in `analzye.py`. You can run your code by running:
```
python3 auto_grader.py
```
Running the code will print out a result report as follows (accuracy, precision, and recall):
```
----Accuracy----
0.5088062622309197 0.6998654104979811 0.3996925441967717
---- Timing ----
168.670348 seconds

```
*For full credit, you must write a program that achieves at least 50% accuracy in less than 5 mins on a standard laptop.*

The project is complete unstructured and it is up to you to figure out how to make this happen. Here are some hints:

* The amazon product database is redundant (multiple same products), the google database is essentially unique. 

* Jaccard similarity will be useful but you may have to consider "n-grams" of words (look at the lecture notes!) and "cleaning" up the strings to strip formatting and punctuation.

* Price and manufacturer will also be important attributes to use.

## Submission
After you finish the assignment you can submit your code with:
```
$ git add analyze.py
$ git commit -m 'My submission'
$ git push
```

DO NOT commit the datasets. 
