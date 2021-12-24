##############
# Linked Lists

# * resource: https://realpython.com/linked-lists-python/

# Notes

# * Different than normal lists because it is a store of references to elements where as normal lists are contiguous blocks of memory
# * Linked lists only know what's next
##############

class LinkedList:
	def __init__(self, nodes=None):
		# the only information you need to store is where the list starts (the head)
		self.head = None
		
		# the addition of the nodes argument allows use to quickly create a linked list from an iterable
		if nodes is not None:
			# use the first element at the end of the list of nodes as the head
			node = Node(data=nodes.pop(0))
			self.head = node
			
			# connect the remaining nodes in the list and join them to our new head
			for n in nodes:
				# with the first iteration, append nodes to the current head
				# with next iterations, append the following nodes to the previous node
				node.next = Node(data=n)
				# set the new current node node as the one that was just appended
				node = node.next
				# continue with the rest of the nodes

	
	def __repr__(self):
		node = self.head
		nodes = []
		while node is not None:
			nodes.append(node.data)
			node = node.next
		nodes.append("None")
		return " --> ".join(nodes)

	# we can create the traversal behaviour to a linked list as such
	def __iter__(self):
		node = self.head
		while node is not None:
			# yield the next node
			yield node
			# if the node list ends with a None, the while loop ends
			node = node.next

	def add_first(self, node):
		""" adding/inserting nodes to the head/beginning of the list """
		# pushes the previous head down towards the right side of the list
		# Thus, the next property of the current node is the previous head node, if we're going from left to right
		node.next = self.head
		# the newly added node is now the head of the list, on the left hand side
		self.head = node
	
	def add_last(self, node):
		# in the case that there are no nodes in the linked list
		if self.head is None:
			self.head = node
			return
		
		# traverse the whole list until you reach the end
		# we had yield from before, so we keep the state of the end of the nodes
		# that is, until the for loop raises a StopIteration exception. Next, you want to set the 
		# current_node as the last node on the list.
		# finally, you want to add the new node as the next value of that current_node.
		# iterate through self, which has an __iter__ method
		for current_node in self:
			pass

		current_node.next = node

	# adding between two nodes adds a layer of complexity because linked lists behave differently than normal lists, and you need a different
	# implementation for:
	# 1) inserting after an existing node
	# 2) inserting before an existing node.

	def add_after_existing_node(self, target_node_data, new_node):
		"""
		Adds node after the target node, given it's data value
		"""
		if self.head is None:
			raise Exception("List is empty")
		
		for node in self:
			if node.data == target_node_data:
				new_node.next = node.next
				node.next = new_node
				return
		
		raise Exception(f"Node with data {target_node_data} not found.")


# create another class to represent each node of the linked list
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	
	def __repr__(self):
		return self.data


def main():
	# implementing the Linked list
	first = Node("a")

	second = Node("b")
	third = Node("c")
	ll = LinkedList()

	ll.head = first
	print(ll)

	first.next = second
	second.next = third

	print(ll)

	bob = LinkedList(["1", "3", "5", "5", "1000"])
	print(bob)


def traverse_linked_list():
	ll = LinkedList(list(map(str, [1, 6, 3, 1, 6, 33, 3333])))

	for node in ll:
		print(node)


def showcase_add_node_first():
	ll = LinkedList(list(map(str, [1, 6, 3, 1, 6, 33, 3333])))
	ll.add_first(Node("foobar"))
	print(ll)

def showcase_add_node_last():
	rl = LinkedList(list(map(str, [1, 6, 3, 1, 6, 33, 3333])))
	rl.add_first(Node("foobar"))
	rl.add_last(Node("raiju"))
	print(rl)

def showcase_add_after():
	rl = LinkedList(list(map(str, [1, 6, 3, 1, 6, 33, 3333])))
	rl.add_after_existing_node("33", Node("Shai Halud"))
	print(rl)


if __name__ == "__main__":
	main()
	print("-----------")
	traverse_linked_list()
	print("-----------")
	showcase_add_node_first()
	print("-----------")
	showcase_add_node_last()
	print("-----------")
	showcase_add_after()
	print("-----------")
	print("-----------")
	print("-----------")
