# Homework 3. Bloom Filter
This homework assignment introduces an advanced use of hashing called a Bloom filter. 

Due Date: *Wed May 11, 11:59 pm*

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

In your web browser,  accept the assignment using the following link [https://classroom.github.com/a/Vpk0hIIi].
You'll be given a dropdown list with a list of CNET ids, please select yours and "accept" the assignment. 
This will create a pre-populated repository for you with the assignment details.
Once the repository is created, you will get a link that looks something like this:
```
https://github.com/CMSC-13600-Data-Engineering/homework-3-hashing-<your github name>
```

Next, we will `clone` this repository to linux.cs.uchicago.edu. *Note* Every year students cut an paste the following instructions without realizing that my CNET id is "skr" and my github username is "sjyk". Please replace those with your own.
```
(cmscm13600-env) skr@linux2:~$ git clone git@github.com:CMSC-13600-Data-Engineering/homework-3-hashing-sjyk.git
```
Enter the cloned repository, and now, you are ready to start your assignment!

## A Simple Hash Function
In this assignment, you will be implementing a basic data structure that uses hashing. A key part of this data structure will be to generate a set of "independent" hash functions. We'll walk you through the conceptual process and you'll have to make the details work out.

Here is a code snippet for a simple hash function. The code defines a function hashcode that takes a string and outputs a hashcode for it. It is parameterized by two large random numbers A and B.
```
import binascii
import random

# maximum integer value
MAXINT = 2**32-1

# We need the next largest prime number above MAXINT
NEXTPRIME = 4294967311

# Two numbers that parametrize the hash
A = random.randint(0, MAXINT)
B = random.randint(0, MAXINT)

def hashcode(st):
    val = binascii.crc32(bytes(str(st),'utf-8')) & 0xffffffff
    return (A * val + B) % NEXTPRIME

print(hashcode('the bear'))
print(hashcode('a bear'))
print(hashcode('the bear'))
```
For different random choices of A and B, the hashcodes are said to be "independent" refer to [https://en.wikipedia.org/wiki/K-independent_hashing]. 

## Bloom filter
A Bloom filter is a space-efficient probabilistic data structure, conceived by Burton Howard Bloom in 1970, that is used to test whether an element is a member of a set. False positive matches are possible, but false negatives are not – in other words, a query returns either "possibly in set" or "definitely not in set." Elements can be added to the set, but not removed (though this can be addressed with the counting Bloom filter variant); the more items added, the larger the probability of false positives. All of the necessary parts that you need to write are marked with *TODO*.

Here's how the basic Bloom filter works:

### Initialization
* An empty Bloom filter is initialized with an array of *m* elements each with value 0.
* Generate *k* independent hash functions whose output domain are integers {0,...,m}.

### Adding An Item e
* For each hash function calculate the hash value of the item "e" (should be a number from 0 to m).
* Treat those calculated hash values as indices for the array and set each corresponding index in the array to 1 (if it is already 1 from a previous addition keep it as is).

### Contains An Item e
* For each hash function calculate the hash value of the item "e" (should be a number from 0 to m).
* Treat those calculated hash values as indices for the array and retrieve the array value for each corresponding index. If any of the values is 0, we know that "e" could not have possibly been inserted in the past.

## TODO 1. Generate K independent Hash Functions
Your first task is to write the function `generate_hashes`. This function is a higher-order function that returns a list of *k* random hash functions each with a range from 0 to *m*. Here are some hints that will help you write this function.

* Step 1. Review the "linear" hash function described above and write a helper function that generates such a hash function for a pre-defined A and B. How would you restrict the domain of this hash function to be with 0 to m?

* Step 2. Generate k of such functions with different random settings of A and B. Pay close attention to how many times you call "random.x" because of how the seeded random variable works.

* Step 3. Return the functions themselves so they can be applied to data. Look at the autograder to understand what inputs these functions should take. 

## TODO 2. Put
Write a function that uses the algorithm listed above to add a string to the bloom filter. In pseudo-code:
* For each of the k hash functions:
* Compute the hash code of the string, and store the code in i
* Set the ith element of the array to 1

## TODO 3. Get
Write a function that uses the algorithm listed above to test whether the bloom filter possibly contains the string. In pseudo-code:
* For each of the k hash functions:
* Compute the hash code of the string, and store the code in i
* if the ith element is 0, return false
* if all code-indices are 1, return true

## Testing and Submission
We've provided an autograder script `autograder.py` which runs a bunch of interesting tests. The autograder is not comprehensive but it is a good start. It's up to you to figure out what the test do and why they work. Due to the randomized nature of this assignment, it is hard to get an autograder that works in all cases!

After you finish the assignment you can submit your code with:
```
$ git add bloom.py
$ git commit -m 'My submission'
$ git push
```

