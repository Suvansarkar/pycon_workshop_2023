class Stack:
	# _instance = None
	#
	# def __new__(cls, *args, **kwargs):
	# 	pass

	def __init__(self):
		self.items = []
	
	def __contains__(self, item: object) -> bool:
	    return item in self.items

	def __add__(self, other: "Stack") -> "Stack":
	    return self.items.extend(other.items)
	
	def __len__(self) -> int:
	    return len(self.items)
	
	def __iter__(self) -> iter:
	    yield from self.items
	
	def __enter__(self):
	    return self
	
	def __exit__(self, exc_type, exc_val, exc_tb):
	    while not self.is_empty():
	        self.pop()

	def __str__(self):
	    return " --> ".join([str(item) for item in self.items])

	def push(self, item: object) -> None:
	    self.items.append(item)

	def pop(self) -> object:
	    if not self.is_empty():
	        return self.items.pop()

	def peek(self) -> object:
	    if self.items.is_empty():
	        print("Stack is empty.")
	    else:
	        return self.items[-1]

	def is_empty(self) -> bool:
		return self.items == []

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.pop()
stack.push(40)
stack.push(50)

print(stack)

print(10 in stack)

for i in stack:
	print(i)

with Stack() as stack2:
	stack2.push(100)
	stack2.push(200)
	stack2.push(300)
	stack2.push(400)
	stack2.push(500)
	print(stack2)
	print(100 in stack2)
	for i in stack2:
		print(i)

print(stack2.is_empty())

l = [1, 2, 3]
print(1 in l)
