from typing import List

y = 10

def sum(a, b):
	global y
	y = 12
	return a + b + y


ALPHA = "abcdefghijklmnopqrstuvwxyz"
HEIGHTS = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]

def designerPdfViewer(h: List[int], word: str) -> int:
	""" 
	Parameters
	----------
	:params : Integer array
	:params word (str): word from user input

	Return
	------
	area (int): Area of highlighted PDF text per word in mm^2
	"""
	c = []

	mapper = {a: _h for a, _h in zip(ALPHA, h)}
	for l in word:
		c.append(mapper[l])

	return max(c) * len(word)


_ = designerPdfViewer(HEIGHTS, "torn")


arr = [1, 2, 3, 4, 5]

def rotLeft(a: List[int], d: int) -> List[int]:
	"""
	Parameters
	----------
	:params a (List[int]): Array of integers
	:params d (int): Integer factor by which to rotate the elements of `a` by

	Returns
	-------
	List[int]: Same input array of ints rotated by a factor of d

	"""


	v = -d % len(a)

	new_arr = a[v:] + a[:v]

	# for k, v in track:
	# 	if v-d < 0:
	# 		v = len(a) + (v-d) - 1
	# 		new_arr.append(a[v])
	# 	else:
	# 		new_arr.append(v-d)

	return new_arr 

res = rotLeft(arr, 5)


"""
Notes to use when problem solving
* space and time complexity
* use appropriate data structures
* explain yourself
* talk through aprticular ideas and your reasoning
* plan and schedule out your coding sessions
* target medium to hard problems
* set aside time to review what you've practiced
* make cheat sheets and flash cards to review later on

Remember your goal:
* aim to confidently solving two questions while thinking aloud - in about 35 minutes

Set a time constraint when you practice problems:
* practice coding solutions to medium and hard problems in less than 15 minutes each to help you be ready for contrains during the interview

Practice talking through the problem space and possible solution before you dive in and talk through your decisions out loud as you code.

Understand the types of problems you may encounter
Problems may focus on edge cases. YOu might be ased to parse some data format or mini language. Your answers demonstrate your ability to handle multiple states in your head.
Problems may test how well you know how things work under the hood. For example you might be asked to implement well-known library functions.

Areas of weakness:
* different algorithms, algorithmic techniques, such as sorting, divide and conquer, recurision, etc
* data structures, particular yhose used most often (array, stack/queue, hashset/hashmap/hashtable/dictioanry, tree/binary tree/inverse a binary tree, heap, graph, etc)
* O memory contrains on the complexity of the algorithm you're writing and its running time as expressed by Big-O notation
* design patterns in general
8 recursion, graph theory, tree traversal combinatorial problems and so on

Generall avoid solutions with lots of edge cases or huge if/else blocks
Deciding between iteration and recursion can be an important step

"""

if __name__ == "__main__":
	print(res)