class Task():
	def __init__(self, name, user, duedate, note=None, tags=[]):
		self.name = name
		self.user = user
		self.duedate = duedate
		self.note = note
		self.tags = tags
		self.status = False
		self.created = None
		self.finished = None

	# name handling
	def get_name(self):
		return self.name

	def change_name(self, name):
		self.name = name

	# user handling
	def change_user(self, user):
		self.user = user

	def get_user(self):
		return self.user

	# note handling
	def get_note(self):
		return self.note

	def change_note(self, note):
		self.note = note

	# tags handling
	def get_tags(self):
		return self.tags

	def add_tag(self, tag):
		self.tags.append(tag)

	def remove_tag(self, tag):
		self.tags.remove(tag)

	def get_status(self):
		return self.status

	def set_status(self, status):
		self.status = status

	def get_duedate(self):
		return self.duedate

	def change_duedate(self, duedate):
		self.duedate = duedate
