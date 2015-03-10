import os
import sys
from subprocess import call
from extract_attributes import *

HAM = "-1"
SPAM = "1"

# primeiro argumento: diretorio com os e-mails ham
ham_directory = sys.argv[1]
# segundo argumento: diretorio com os e-mails spam
spam_directory = sys.argv[2]
# arquivo de resultados
output_file = sys.argv[3]

# lista os e-mails ham
ham_files = os.listdir(ham_directory)

output = open(output_file, "w")

#Definição de atributos no ARFF
output.write("@RELATION spam\n")
output.write("@ATTRIBUTE spam trigger subject\n")
output.write("@ATTRIBUTE spam trigger body\n")
output.write("@ATTRIBUTE body size\n\n")
output.write("@DATA\n")

for file_name in ham_files:
	# constroi o absolute path do arquivo
	file_name_full_path = ham_directory + os.sep + file_name
	string_attributes = str(get_attributes(file_name_full_path, HAM))
	# concatena os atributos do arquivo com o marcador de is-spam e escreve na saida
	output.write(string_attributes + "," + HAM + "\n")

spam_files = os.listdir(spam_directory)

for file_name in spam_files:
	file_name_full_path = spam_directory + os.sep + file_name
	string_attributes = str(get_attributes(file_name_full_path, SPAM))
	output.write(string_attributes + "," + SPAM + "\n")

output.close()
