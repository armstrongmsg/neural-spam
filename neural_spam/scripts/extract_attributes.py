# indentation = tab

import sys
import os.path

##
## ATTENCION: USE COMMENTS! THIS IS NOT JAVA! LET EVERYONE UNDERSTAND WHAT THE FUCK ARE YOU DOING!
## WORK EASIER, MAKE EVERYONE HAPPY: DO DOCUMENTATION!
##

# constants
INDEX_INPUT_FILE_PATH = 1
INDEX_IS_SPAM = 2
IS_SPAM = 1
IS_NOT_SPAM = -1
LEARNIG_RATE = 1
THRESHOLD = 0 #it might be in other file, because, this value will change on neural network trainning

# SPANS TRIGGER WORDS
# From website: http://blog.hubspot.com/blog/tabid/6307/bid/30684/The-Ultimate-List-of-Email-SPAM-Trigger-Words.aspx
AVOID_SPAM_WORDS_COMMERCE = ["as seen on","buy","buy direct","buying judgments","clearance","order","order status","orders shipped by","shopper"]
AVOID_SPAM_WORDS_PERSONAL = ["dig up dirt on friends","meet singles","score with babes"]
AVOID_SPAM_WORDS_EMPLOYMENTS = ["additional income","be your own boss","compete for your business","double your","earn $","earn extra cash","earn per week","expect to earn","extra income","home based","home employment","homebased business","income from home","make $","make money","money making","online biz opportunity","online degree","opportunity","potential earnings","university diplomas","while you sleep","work at home","work from home"]
AVOID_SPAM_WORDS_FINANCIAL_GENERAL = ["$$$","affordable","bargain","beneficiary","best price","big bucks","cash","cash bonus","cashcashcash","cents on the dollar","cheap","check","claims","collect","compare rates","cost","credit","credit bureaus","discount","earn","easy terms","f r e e","free","fast cash","for just $","hidden assets","hidden charges","income","incredible deal","insurance","investment","loans","lowest price","million dollars","money","money back","mortgage","mortgage rates","no cost","no fees","one hundred percent free","only $","pennies a day","price","profits","pure profit","quote","refinance","save $","save big money","save up to","serious cash","subject to credit","they keep your money","no refund!","unsecured credit","unsecured debt","us dollars","why pay more?"]
AVOID_SPAM_WORDS_FINANCIAL_BUSINESS = []
AVOID_SPAM_WORDS_FINANCIAL_PERSONAL = ["avoid bankruptcy","calling creditors","collect child support","consolidate debt and credit","consolidate your debt","eliminate bad credit","eliminate debt","financially independent","get out of debt","get paid","lower interest rate","lower monthly payment","lower your mortgage rate","lowest insurance rates","pre-approved","refinance home","social security number","your income"]
AVOID_SPAM_WORDS_GENERAL = []
AVOID_SPAM_WORDS_GREETINGS = ["dear","friend","hello"]
AVOID_SPAM_WORDS_MARKETING = []
AVOID_SPAM_WORDS_MEDICAL = []
AVOID_SPAM_WORDS_NUMBERS = []
AVOID_SPAM_WORDS_OFFERS = []
AVOID_SPAM_WORDS_CALL_TO_ACTION = ["cancel at any time","compare","copy accurately","get","give it away","print form signature","print out and fax","ee for yourself","sign up free today"]
AVOID_SPAM_WORDS_FREE = []
AVOID_SPAM_WORDS_DESCRIPTION = []
AVOID_SPAM_WORDS_SENSE_OF_URGENCY = []
AVOID_SPAM_WORDS_NOUNS = []

SPAM_TRIGGER_WORDS = [AVOID_SPAM_WORDS_COMMERCE,AVOID_SPAM_WORDS_PERSONAL,AVOID_SPAM_WORDS_EMPLOYMENTS,AVOID_SPAM_WORDS_FINANCIAL_GENERAL,AVOID_SPAM_WORDS_FINANCIAL_BUSINESS,AVOID_SPAM_WORDS_FINANCIAL_PERSONAL,AVOID_SPAM_WORDS_GENERAL,AVOID_SPAM_WORDS_GREETINGS,AVOID_SPAM_WORDS_MARKETING,AVOID_SPAM_WORDS_MEDICAL,AVOID_SPAM_WORDS_NUMBERS,AVOID_SPAM_WORDS_OFFERS,AVOID_SPAM_WORDS_CALL_TO_ACTION,AVOID_SPAM_WORDS_FREE,AVOID_SPAM_WORDS_DESCRIPTION,AVOID_SPAM_WORDS_SENSE_OF_URGENCY,AVOID_SPAM_WORDS_NOUNS]



#it might be in other file, because, these values will change on neural network trainning
# it might be an array or class
WEI_SUBJECT_LENGTH = 1
WEI_SUBJECT_TRIGGER_WORDS = 1


#

class EmailAttributes:
	def __init__(self, subject):
		self.subject = subject

	def get_subject(self):
		return self.subject

	def __str__(self):
		return "\"" + self.subject + "\""

# class used to neural network trainning
class Email:
	# attributes: instance of EmailAttributes
	# spam: boolean if is a spam or a ham
	def __init__(self, attributes, spam):
		self.attributes = attributes
		self.spam = spam
	def get_attributes(self):
		return attributes
	def get_spam(self):
		return spam


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

#Emails: Email Array
def learning(emails):
	for (email in emails):
		while (True):
			#Checking parameters
			#it might be a while or for here, checking all attributes and weights, but, I don't know how to do it now...
			# w1,w2,w3... are local weigths
			w1 = len(email.get_attribute().get_subject()) * WEI_SUBJECT_LENGTH
			avoid = 0;
			for (avoid_word in SPAM_TRIGGER_WORDS):
				if (avoid_word in email.get_attribute().get_subject().lower()):
					avoid = 1;
			w2 = avoid * WEI_SUBJECT_TRIGGER_WORDS
			
			# sum all weights
			w = w1+w2
			
			#check threshold
			espected = 0
			descovered = 0
			if (w > THRESHOLD):
				if(email.get_spam()):
					break
				else:
					espected = IS_SPAM
					descovered = IS_NOT_SPAM
			else:
				if not(email.get_spam()):
					break
				else:
					espected = IS_NOT_SPAM
					descovered = IS_SPAM
			
			# weight adjustment
			# do not change
			WEI_SUBJECT_LENGTH = WEI_SUBJECT_LENGTH + ((LEARNIG_RATE*len(email.get_attribute().get_subject()))*(espected-descovered))
			WEI_SUBJECT_TRIGGER_WORDS = WEI_SUBJECT_TRIGGER_WORDS + ((LEARNING_RATE*avoid)*(espected-descovered))
			THRESHOLD = THRESHOLD + ((LEARNING_RATE*(-1))*(espected-descovered))
		



args = sys.argv
args_treatment(args)
input_file_path = args[INDEX_INPUT_FILE_PATH]
is_spam = args[INDEX_IS_SPAM]

input_file = open(input_file_path, "r")
attributes = extract_attributes(input_file, is_spam)
input_file.close()
print attributes

