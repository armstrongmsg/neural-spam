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
IS_SPAM = "1"
IS_NOT_SPAM = "-1"

# SPANS TRIGGER WORDS
# From website: http://blog.hubspot.com/blog/tabid/6307/bid/30684/The-Ultimate-List-of-Email-SPAM-Trigger-Words.aspx
AVOID_SPAM_WORDS_COMMERCE = ["as seen on","buy","buy direct","buying judgments","clearance","order","order status","orders shipped by","shopper"]
AVOID_SPAM_WORDS_PERSONAL = ["dig up dirt on friends","meet singles","score with babes"]
AVOID_SPAM_WORDS_EMPLOYMENTS = ["additional income","be your own boss","compete for your business","double your","earn $","earn extra cash","earn per week","expect to earn","extra income","home based","home employment","homebased business","income from home","make $","make money","money making","online biz opportunity","online degree","opportunity","potential earnings","university diplomas","while you sleep","work at home","work from home"]
AVOID_SPAM_WORDS_FINANCIAL_GENERAL = ["$$$","affordable","bargain","beneficiary","best price","big bucks","cash","cash bonus","cashcashcash","cents on the dollar","cheap","check","claims","collect","compare rates","cost","credit","credit bureaus","discount","earn","easy terms","f r e e","free","fast cash","for just $","hidden assets","hidden charges","income","incredible deal","insurance","investment","loans","lowest price","million dollars","money","money back","mortgage","mortgage rates","no cost","no fees","one hundred percent free","only $","pennies a day","price","profits","pure profit","quote","refinance","save $","save big money","save up to","serious cash","subject to credit","they keep your money","no refund!","unsecured credit","unsecured debt","us dollars","why pay more?"]
AVOID_SPAM_WORDS_FINANCIAL_BUSINESS = ["accept credit cards","cards accepted","check or money order","credit card offers","explode your business","full refund","investment decision","no credit check","no hidden costs","no investment","requires initial investment","sent in compliance","stock alert","stock disclaimer statement","stock pick"]
AVOID_SPAM_WORDS_FINANCIAL_PERSONAL = ["avoid bankruptcy","calling creditors","collect child support","consolidate debt and credit","consolidate your debt","eliminate bad credit","eliminate debt","financially independent","get out of debt","get paid","lower interest rate","lower monthly payment","lower your mortgage rate","lowest insurance rates","pre-approved","refinance home","social security number","your income"]
AVOID_SPAM_WORDS_GENERAL = ["acceptance","accordingly","avoid","chance","dormant","freedom","here","hidden","home","leave","lifetime","lose","maintained","medium","miracle","never","passwords","problem","remove","reverses","sample","satisfaction","solution","stop","sucess","teen","wife"]
AVOID_SPAM_WORDS_GREETINGS = ["dear","friend","hello"]
AVOID_SPAM_WORDS_MARKETING = ["ad","auto email removal","bulk email","click","click below","click here","click to remove","direct email","direct marketing","form","increase sales","increase trafic","increase your sales","internet market","internet marketing","marketing","marketing solution","mass email","member","month trial offer","more internet traffic","multi level marketing","notspam","one time mailing","online marketing","open","opt it","performance","removal instructions","sale","sales","search engine listings","search engines","subscribe","the following form","this isn't junk","this isn't spam","undisclosed recipient","unsubscribe","visit our website","we hate spam","web traffic","will not believe your eyes"]
AVOID_SPAM_WORDS_MEDICAL = ["cures baldness","diagnostics","fast viagra delivery","human growth hormone","life insurance","lose weight","lose weight spam","medicine","no medical exams","online pharmacy","removes wrinkles","reverses aging","stop snoring","valium","viagra","vicodin","weight loss","xanax"]
AVOID_SPAM_WORDS_NUMBERS = ["#1","100% free","100% satisfied","4U","50% off","billion","billion dollars","join millions","join millions of americans","million","one hundred percent guaranteed","thousands"]
AVOID_SPAM_WORDS_OFFERS = ["being a member","bliing address","call","cannot be combined with any other offer","confidentially on all orders","deal","financial freedom","gilf certificate","giving away","guarantee","have you been turned down?","if only it were that easy","important information ragarding","in accordance with laws","long distance phone offer","mail in order form","message contains","name brand","nigerian","no age restrictions","no catch","no clain forms","no disappointment","no experience","no gimmick","no inventory","no middleman","no obligation","no purchase necessary","no questions asked","no selling","no string attached","no-obligation","not intended","obligation","off shore","offer","per day","per week","priority mail","prize","prizes","produced and sent out","reserves the right","shopping spree","stuff on sale","terms and conditions","the best rates","they're just giving it away","trial","unlimited","unsolicited","vacation","vacation offers","warranty","we honor all","weekend getaway","what are you waiting for?","who really wins?","win","winner","winning","won","you are a winner!","you have been selected","you're a winner!"]
AVOID_SPAM_WORDS_CALL_TO_ACTION = ["cancel at any time","compare","copy accurately","get","give it away","print form signature","print out and fax","ee for yourself","sign up free today"]
AVOID_SPAM_WORDS_FREE = ["free","free access","free cell phone","free consultation","free dvd","free gift","free grant money","free hosting","free installation","free instant","free investment","free leads","free membership","free money","free offer","free preview","free priority mail","free quote","free sample","free trial","free website"]
AVOID_SPAM_WORDS_DESCRIPTION = ["all natural","all new","amazing","certified","congratulations","drastically reduced","fantastic deal","for free","guaranteed","it's effective","outstanding values","promise you","real thing","risk free","satisfaction guaranteed"]
AVOID_SPAM_WORDS_SENSE_OF_URGENCY = ["acess","act now","apply now","apply online","call free","call now","can't live without","do it today","don't delete","don't hesitate","for instant acess","for only","for you","get it now","get started now","great offer","info you requested","information you requested","instant","limited time","new customers only","now","now only","offer expires","once in lifetime","now only","offer expires","once in lifetime","one time","only","order now","order today","please read","special promotion","supplies are limited","take action now","time limited","urgent","while supplies last"]
AVOID_SPAM_WORDS_NOUNS = ["addresses on cd","beverage","bonus","brand new pager","cable converter","casino","celebrity","copy dvds","laser printer","legal","luxury car","new domain extensions","phone","rolex","stainless steel"]

SPAM_TRIGGER_WORDS = [AVOID_SPAM_WORDS_COMMERCE,AVOID_SPAM_WORDS_PERSONAL,AVOID_SPAM_WORDS_EMPLOYMENTS,AVOID_SPAM_WORDS_FINANCIAL_GENERAL,AVOID_SPAM_WORDS_FINANCIAL_BUSINESS,AVOID_SPAM_WORDS_FINANCIAL_PERSONAL,AVOID_SPAM_WORDS_GENERAL,AVOID_SPAM_WORDS_GREETINGS,AVOID_SPAM_WORDS_MARKETING,AVOID_SPAM_WORDS_MEDICAL,AVOID_SPAM_WORDS_NUMBERS,AVOID_SPAM_WORDS_OFFERS,AVOID_SPAM_WORDS_CALL_TO_ACTION,AVOID_SPAM_WORDS_FREE,AVOID_SPAM_WORDS_DESCRIPTION,AVOID_SPAM_WORDS_SENSE_OF_URGENCY,AVOID_SPAM_WORDS_NOUNS]

class EmailAttributes:
	def get_number_of_spam_words_occurrences(self, string):
		occurrences = 0
		for avoid_word_list in SPAM_TRIGGER_WORDS:
			for avoid_word in avoid_word_list:
				if avoid_word in string.lower():
					occurrences += 1
		return occurrences

	def calculate_number_of_spam_words_in_body(self, body):
		occurrences = 0
		for body_line in body:
			occurrences += self.get_number_of_spam_words_occurrences(body_line)
		return occurrences

	def get_total_number_of_words(self, subject, body):
		words_subject = len(subject.split())
		words_body = 0

		for body_line in body:
			words_body += len(body_line.split())

		return words_subject + words_body
	
	def get_total_of_receivers(self, body):
		total_of_receivers = 1
		if len(body) > 0:
			receivers = body[0]
			total_of_receivers = receivers.count("@")
		
			if(total_of_receivers) == 0:
				total_of_receivers = 1
		
		return total_of_receivers

	def calculate_contains_links(self, body):
		link_patterns = ["http", "http:", "https", "https:"]
		for line in body:
			for pattern in link_patterns:
				if pattern in line:
					return True
		return False

	def __init__(self, subject, body):
		self.subject = subject
		self.body = body
		self.number_of_spam_words_in_subject = self.get_number_of_spam_words_occurrences(subject)
		self.number_of_spam_words_in_body = self.calculate_number_of_spam_words_in_body(body)
		self.total_number_of_words = self.get_total_number_of_words(subject, body)
		self.total_of_receivers = self.get_total_of_receivers(body)
		self.contains_links = self.calculate_contains_links(body)

	def get_subject(self):
		return self.subject

	def get_number_of_spam_words_in_subject(self):
		return self.number_of_spam_words_in_subject

	def get_total_number_of_words_in_email(self):
		return self.total_number_of_words

	def get_number_of_spam_words_in_body(self):
		return self.number_of_spam_words_in_body

	def get_total_of_receivers_in_body(self):
		return self.total_of_receivers
	
	def get_contains_links(self):
		return self.contains_links

	def __str__(self):
		result_string = ""
		result_string += str(self.get_number_of_spam_words_in_subject()) 
		result_string += ", " + str(self.get_total_number_of_words_in_email())
		result_string += ", " + str(self.get_number_of_spam_words_in_body())
		result_string += ", " + str(self.get_total_of_receivers_in_body())
		if self.get_contains_links():
			result_string += ", 1"
		else:
			result_string += ", 0"

		return result_string

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

	body = file.readlines()
	return EmailAttributes(subject, body)

def get_attributes(input_file_path, is_spam):
	input_file = open(input_file_path, "r")
	attributes = extract_attributes(input_file, is_spam)
	input_file.close()
	return attributes

if __name__ == "__main__":
	args = sys.argv
	args_treatment(args)
	input_file_path = args[INDEX_INPUT_FILE_PATH]
	is_spam = args[INDEX_IS_SPAM]
	print get_attributes(input_file_path, is_spam)
