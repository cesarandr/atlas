import argparse

class Input():

	def get_input():

		parser = argparse.ArgumentParser(prog="atlas", description="A programm to reach your goals")
		subparsers = parser.add_subparsers(title="subcommands")

		# sheet commands
		sheet_parser = subparsers.add_parser("sheet", help="manage your sheets")
		sheet_subparsers = sheet_parser.add_subparsers()

		create_sheet_parser = sheet_subparsers.add_parser("create", help="create a new sheet")
		create_sheet_parser.add_argument("sheetname", action="store", help="set the sheetname")

		delete_sheet_parser = sheet_subparsers.add_parser("delete", help="delete an existing sheet")
		delete_sheet_parser.add_argument("sheetname", action="store", help="define sheet to delete")

		# task commands
		task_parser = subparsers.add_parser("task", help="manage your tasks")
		task_subparser = task_parser.add_subparsers()

		create_task_parser = task_subparser.add_parser("create", help="create a new task")
		create_task_parser.add_argument("name", action="store", help="name the task")
		create_task_parser.add_argument("user", action="store", help="assign a user to the task")
		create_task_parser.add_argument("duedate", action="store", help="set a deadline")

		delete_task_parser = task_subparser.add_parser("delete", help="delete an existing task")
		delete_task_parser.add_argument("task", action="store", help="define task to delete")


		# user commands
		user_parser = subparsers.add_parser("user", help="manage your users")
		user_subparser = user_parser.add_subparsers()

		create_user_parser = user_subparser.add_parser("create", help="create a new user")
		create_user_parser.add_argument("username", action="store", help="set username")
		create_user_parser.add_argument("password", action="store", help="set password of user")

		delete_user_parser = user_subparser.add_parser("delete", help="delete an existing user")
		delete_user_parser.add_argument("username", action="store", help="define user to delete")

		args = parser.parse_args()

		return args
