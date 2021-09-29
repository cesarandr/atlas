class User():
	def __init__(self, name, password):
		self.name = name
		self.password = password
		self.number_of_tasks = 0
		self.tasks_completed = 0
		self.created = None

	def __generate_id():
		# placeholder till implemented
		return -1

	def change_name(self, name):
		self.name = name

	def get_name(self):
		return self.name

	def change_password(self, old_password, new_password):
		if old_password == self.password:
			self.password = new_password
			return True
		else:
			return False
