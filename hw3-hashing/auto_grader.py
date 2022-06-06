import random
import string

from bloom import *

def generate_random_string(seed=True):	
	chars = string.ascii_uppercase + string.digits
	size = 10
	return ''.join(random.choice(chars) for x in range(size))

def test_hash_generation():
	b = Bloom(5,10)

	try:
		assert(len(b.hashes) == 10)
	except:
		print('[#1] Failure the number of generated hashes is wrong')

	try:

		for h in b.hashes:
			h(generate_random_string())

	except:
		print('[#2] The hashes are not properly represented as a lambda')


	s = generate_random_string()

	try:
		for h in b.hashes:
			assert(h(s) == h(s))
	except:
		print('[#3] Hashes are not deterministic')


	try:
		b = Bloom(100,10)
		b1h = b.hashes[0](s)
		b = Bloom(100,10)
		b2h = b.hashes[0](s)

		assert(b1h == b2h)

	except:
		print('[#4] Seeds are not properly set')


	try:
		b = Bloom(100,10)

		for h in b.hashes:
			for i in range(10):
				assert( h(generate_random_string())< 100 )

	except:
		print('[#5] Hash exceeds range')


	try:
		b = Bloom(1000,2)
		s = generate_random_string()
		bh1 = b.hashes[0](s)
		bh2 = b.hashes[1](s)

		assert(bh1 != bh2)

	except:
		print('[#6] Hashes generated are not independent')

def test_put():
	try:
		b = Bloom(100,10,seed=0)
		b.put('the')
		b.put('university')
		b.put('of')
		b.put('chicago')
	except:
		print('[#7] Unexpected Put() Result')

def test_put_get():

	try:
		b = Bloom(100,5,seed=0)
		b.put('the')
		b.put('quick')
		b.put('brown')
		b.put('fox')
		b.put('jumped')
		b.put('over')
		b.put('the')
		b.put('lazy')
		b.put('dog')

		results = [b.contains('the'),\
				   b.contains('cow'), \
				   b.contains('jumped'), \
				   b.contains('over'),\
				    b.contains('the'), \
				    b.contains('moon')]
	except:
		print('[#8] Unexpected contains result')

test_hash_generation()
test_put()
test_put_get()



