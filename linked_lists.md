# Linked Lists

* resource: https://realpython.com/linked-lists-python/

## Linked Lists

* Different than normal lists because it is a store of references to elements where as normal lists are contiguous blocks of memory
* Linked lists only know what's next
* Each element is called a *Node* and each *Node* has tow properties:
	* Data: contains the value to be stored in the code
	* Next: contains a reference to the next node in the list
* linked list is a collection of nodes
* first node is called the head. It is the entry point or starting point of every iteration through the list.
* last node has it's `next` propery set to `None` or `null`
* They be used with Applications to 
	* queues
	* stacks
	* graphs

## Queues

Building on top of the idea of linked lists, `queues` are similar to `stacks` only in how the elements are retrieved. For queues, you use FIFO (first in, first out) retrieval, which means that the first element that was inserted is the first element to be retrieved. 

In the diagram above, you can see the front and rear elements of the queue. When you append new elements to the queue, they’ll go to the rear end. When you retrieve elements, they’ll be taken from the front of the queue.

Because of the way elements are inserted or retrieved from the edges of queues, linked lists are one of the most convenient ways to implement these data structures.

**Think of**: A queue to a line at starbucks. First come first serve.

![Queue](https://files.realpython.com/media/Group_6_3.67b18836f065.png)

## Stacks

Building on top of the idea of linked lists, `stacks` are similar to queues except in how they retrieve elements. Elements of a stack are retrieved via the LIFO (last in, first out) approach.

Because of the way elements are inserted or retrieved from the edges of stacks, linked lists are one of the most convenient ways to implement these data structures.

**Think of**: Getting a chip in a can of pringles.

![Stack](https://files.realpython.com/media/Group_7_5.930e25fcf2a0.png)

## Graphs

Graphs can be used to show releationships between objects or to represent different types of networks. For example, a visual representation of a graph - such as a DAG, might look like the image below.

![Graph](https://files.realpython.com/media/Group_20.32afe2d011b9.png)

There are different ways to implement graphs lik the above, but one of the most comon is to use an **adjacent list**. An **adjacent list** is in essence, a list of linked lists where each vertex of the graph is stored alongside a collection of connected vertices:

```
Vertex	Linked List of Vertices
1		2 → 3 → None
2		4 → None
3		None
4		5 → 6 → None
5		6 → None
6		None
```

Or in a dict:

```
graph = {
1: [2, 3, None],
2: [4, None],
3: [None],
4: [5, 6, None],
5: [6, None],
6: [None]
}
```

Linked lists are the preferred implementation of `graphs` in terms of efficiency when compared to a data structure such as an `adjacency graph`. 


## Insertions for Linked lists in Python

Insertions at the head:

	list.insert()

Insertions at the rear:

	list.append()

## Deletions for linked lists in Python

Deletions at the head:

	list.remove()

Deletions at the end:

	list.pop()


Linked lists, on the other hand, are much more straightforward when it comes to insertion and deletion of elements at the beginning or end of a list, where their time complexity is always constant: O(1).

For this reason, linked lists have a performance advantage over normal lists when implementing a queue (FIFO), in which elements are continuously inserted and removed at the beginning of the list. But they perform similarly to a list when implementing a stack (LIFO), in which elements are inserted and removed at the end of the list.

## Implementing Queues and Stacks in Python with Collections

The built-in python moduled `collections` has a perfect object to implement linked lists for applications such as queues and stacks, using the `deque` object.

### Queues and Deque
```
from collections import deque

# takes an iterable
# Mary was first to the line, and Joanne the last

queue = deque(["Mary", "Susan", "Joanne])

# It's Mary's turn to have a seat
queue.popleft()

# now there's seating for Susan and Joanne, the couple

queue.popleft(); queue.popleft()
```

### Stacks and Deque

The idea is more or less the same, however it follows a LIFO approach, like a pringles can of chips. In the example below, we have a random user's search history in their browser.

1. Visits Real Python’s website
2. Navigates to Pandas: How to Read and Write Files
3. Clicks on a link for Reading and Writing CSV Files in Python

```
from collections import deque
history = deque()

history.appendleft("https://realpython.com/")
history.appendleft("https://realpython.com/pandas-read-write-files/")
history.appendleft("https://realpython.com/python-csv/")
history
```

Supposed you wanted to go back to the previous article you've visited using the `back` key or `Back` button - knowing that you have a stack and want to remove elements using LIFO, you can do the following:

```
>>> history.popleft()
'https://realpython.com/python-csv/'

>>> history.popleft()
'https://realpython.com/pandas-read-write-files/'

>>> history
deque(['https://realpython.com/'])
```

