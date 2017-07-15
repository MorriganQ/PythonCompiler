import os, os.path
from .lib import compile_file, compile_files


class Directory():

			
	def __init__(self, directory):

		self.directory = directory


	def is_exists(self):

		if os.path.isdir(str(self)):
			return True
		return False

	def is_dir(self):

		if os.path.isdir(str(self)):
				return True
		return False

	def __str__(self):
		if type(self.directory) == str:
			return self.directory
		return None

def compile(directory_obj):

	if directory_obj.is_exists():
		if directory_obj.is_dir():

			os.chdir(str(directory_obj))
			directories = os.listdir()

			compile_files(directories)

		else:

			compile_file(directory_obj)

	else:

		print("Directory is not exists")
