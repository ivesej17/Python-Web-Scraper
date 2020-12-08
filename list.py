class Node:
	def __init__(self,data=None):
		self.data=data
		self.next=None

class List:
	def __init__(self):
		self.head=Node()

	# Adds new Node containing 'data' to the end of the linked list.
	def append(self,data):
		new_Node=Node(data)
		cur=self.head
		while cur.next!=None:
			cur=cur.next
		cur.next=new_Node

	# Returns the size (integer) of the linked list.
	def size(self):
		cur=self.head
		total=0
		while cur.next!=None:
			total+=1
			cur=cur.next
		return total

	# Prints out the linked list in traditional Python list format.
	def display(self):
		elems=[]
		cur_Node=self.head
		while cur_Node.next!=None:
			cur_Node=cur_Node.next
			elems.append(cur_Node.data)
		print(elems)

	# Returns the value of the Node at 'index'.
	def get(self,index):
		if index>=self.size() or index<0: # added 'index<0' post-video
			print("ERROR: 'Get' Index out of range!")
			return None
		cur_idx=0
		cur_Node=self.head
		while True:
			cur_Node=cur_Node.next
			if cur_idx==index: return cur_Node.data
			cur_idx+=1

	# Deletes the Node at index 'index'.
	def erase(self,index):
		if index>=self.size() or index<0: # added 'index<0' post-video
			print("ERROR: 'Erase' Index out of range!")
			return
		cur_idx=0
		cur_Node=self.head
		while True:
			last_Node=cur_Node
			cur_Node=cur_Node.next
			if cur_idx==index:
				last_Node.next=cur_Node.next
				return
			cur_idx+=1

	# Allows for bracket operator syntax (i.e. a[0] to return first item).
	def __getitem__(self,index):
		return self.get(index)


	def insert(self,index,data):
		if index>=self.size() or index<0:
			return self.append(data)
		cur_Node=self.head
		prior_Node=self.head
		cur_idx=0
		while True:
			cur_Node=cur_Node.next
			if cur_idx==index:
				new_Node=Node(data)
				prior_Node.next=new_Node
				new_Node.next=cur_Node
				return
			prior_Node=cur_Node
			cur_idx+=1

	# Inserts the Node 'Node' at index 'index'. Indices begin at 0.
	# If the 'index' is greater than or equal to the size of the linked
	# list the 'Node' will be appended.
	def insert_Node(self,index,Node):
		if index<0:
			print("ERROR: 'Erase' Index cannot be negative!")
			return
		if index>=self.size(): # append the Node
			cur_Node=self.head
			while cur_Node.next!=None:
				cur_Node=cur_Node.next
			cur_Node.next=Node
			return
		cur_Node=self.head
		prior_Node=self.head
		cur_idx=0
		while True:
			cur_Node=cur_Node.next
			if cur_idx==index:
				prior_Node.next=Node
				return
			prior_Node=cur_Node
			cur_idx+=1

	# Sets the data at index 'index' equal to 'data'.
	# Indices begin at 0. If the 'index' is greater than or equal
	# to the size of the linked list a warning will be printed
	# to the user.
	def set(self,index,data):
		if index>=self.size() or index<0:
			print("ERROR: 'Set' Index out of range!")
			return
		cur_Node=self.head
		cur_idx=0
		while True:
			cur_Node=cur_Node.next
			if cur_idx==index:
				cur_Node.data=data
				return
			cur_idx+=1
