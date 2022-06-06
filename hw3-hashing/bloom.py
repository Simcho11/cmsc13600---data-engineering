'''bloom.py defines a bloom filter which is an
approximate set membership data structure. You
will implement a full bloom filter in this module 
'''
import array
import binascii
import random
import sympy
import string

def generate_random_string(seed=True):	
	chars = string.ascii_uppercase + string.digits
	size = 10
	return ''.join(random.choice(chars) for x in range(size))

def make_hash(A, B, m):
	def hash(st):
		return (A * (binascii.crc32(bytes(str(st),'utf-8')) & 0xffffffff) + B) % m
	return hash


def get_rand():
	n = random.randint(1, 99999)
	return n


class Bloom(object):

	def __init__(self, m,k, seed=0):
		'''Creates a bloom filter of size m with k 
		   independent hash functions.
		'''
		self.range = m

		self.array = array.array('B', [0] * m)
		self.hashes = self.generate_hashes(m,k,seed)




	def generate_hashes(self, m, k, seed):
		'''Generate *k* independent linear hash functions 
		   each with the range 0,...,m. 

		   m: the range of the hash functions
		   k: the number of hash functions
		   seed: a random seed that controls which A/B linear 
		   parameters are used.

		   The output of this function should be a list of functions
		'''

		hashList = []
		random.seed(seed)
		x = random.randint(1, 99999)

		for i in range(k):
			A = get_rand()
			B = get_rand()
			hashList.append(make_hash(A,B,m))

		return hashList

	def put(self, item):
		retArr = []
		hashList = self.hashes

		for i in range(self.range):
			retArr.append(0)

		for i in hashList:
			hashResult = i(item)
			retArr[hashResult] = 1

		return retArr
			



	def contains(self, item):
		hashList = self.hashes

		for i in hashList:
			hashResult = i(item)
			if self.array == 0:
				return False

		return True