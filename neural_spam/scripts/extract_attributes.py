# indentation = tab

import sys
import os.path

# constants
INDEX_INPUT_FILE_PATH = 1
INDEX_IS_SPAM = 2
IS_SPAM = "1"
IS_NOT_SPAM = "0"

class EmailAttributes:
	def __init__(self, subject):
		self.subject = subject

	def get_subject(self):
		return self.subject

	def __str__(self):
		return "" + self.subject

def args_treatment(args):
	if len(args) != 3:
		print "Numero incorreto de argumentos!!!"
		exit()

	input_file_path = args[INDEX_INPUT_FILE_PATH]
	if not os.path.exists(input_file_path):
		print "Arquivo de entrada nao existe!!!"
		exit()

	is_spam = args[INDEX_IS_SPAM]
	if is_spam != IS_SPAM and is_spam != IS_NOT_SPAM:
		print "Argumento is-spam tem valor invalido!!!"
		exit()

def extract_attributes(file, is_spam):
	first_line = file.readline()
	# get the content after the first colon
	colon_index = first_line.find(":")
	subject = first_line[colon_index + 1:]
	# removing the final newline
	subject = subject.replace("\n", "")
	# removing spaces
	subject = subject.strip()
	return EmailAttributes(subject)

args = sys.argv
args_treatment(args)
input_file_path = args[INDEX_INPUT_FILE_PATH]
is_spam = args[INDEX_IS_SPAM]

input_file = open(input_file_path, "r")
attributes = extract_attributes(input_file, is_spam)
input_file.close()
print attributes

