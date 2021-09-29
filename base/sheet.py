class Sheet():
	def __init__(self, name):
		self.name = name
		self.tasks = []
		self.status = False
		self.created = None # going to be a date
		self.finished = None #  going to be a date

	# name handling
	def get_name(self):
		return self.name

	def change_name(self, name):
		self.name = name

	# task handling
	def add_task(self, task):
		if task not in self.tasks:
			self.tasks.append(task)
			return True
		else:
			return False

	def remove_task(self, task):
		if task in self.tasks:
			self.tasks.remove(task)
			return True
		else:
			return False

	def get_tasks(self):
		return self.tasks

	# status handling
	def get_status(self):
		return self.status

	def set_status(self, status):
		self.status = status

	def display(self):
		print(f"Name: {self.name}")
		print("---------------------------------------------------------")
		for task in self.tasks:
			print(f"- {task.get_name()} {task.get_note()} {task.get_status()} {task.get_duedate()}")
