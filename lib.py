import os, os.path
from datetime import datetime
from py_compile import compile


def get_date(now):
	date_info_scheme = '[{day}\\{month}\\{year} {hour}:{minute}:{second}]'
	return date_info_scheme.format(day=now.day ,month=now.month, year = now.year, hour=now.hour, minute = now.minute, second = now.second)


def compile_file(directory):
	compile(directory, directory+'c')
	now = datetime.now()
	print(get_date(now) +' COMPILED '+directory)
	os.remove(directory)
	global operation_counter


def compile_files(directories):
	for directory in directories:

		if (len(directory) - directory.rfind('.py') == 3) and (os.path.isfile(directory)):  #cheking that it is python file
			compile_file(directory)
			
		if os.path.isdir(directory):
			if directory != '__pycache__':
				os.chdir(directory)
				compile_files(os.listdir())
				os.chdir('..')
			else:
				rmtree(directory)
				global operation_counter
				print(get_date(datetime.now()) + ' REMOVED ' + directory)

