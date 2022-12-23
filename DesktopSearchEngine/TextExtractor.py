from PyPDF2 import PdfReader
import docx
import re
import nltk
from nltk.corpus import stopwords 
nltk.download('stopwords')

# Read data from PDF files.
def PDF_Reader(path):
	text_list = []
	reader = PdfReader(path)
	number_of_pages = len(reader.pages)
	for i in range(number_of_pages):
		page = reader.pages[i]
		text = page.extract_text()
		# Replacing every non-alphabetic character with a space
		text = re.sub('[^a-zA-Z]+', ' ', text)
		text_list += text.split()
	text_list = list(filter(lambda i: len(i) != 1 and len(i) != 2, text_list))
	updated_list = []
	stopword = stopwords.words('english')
	for word in text_list:
		if word.lower() not in stopword:
			updated_list.append(word.lower())
	return updated_list


# Read data from DOC files.
def Docx_Reader(path):
	text_list = []
	doc = docx.Document(path)
	all_paras = doc.paragraphs
	for para in all_paras:
		# Replacing every non-alphabetic character with a space
		text = re.sub('[^a-zA-Z]+', ' ', para.text)
		text_list += text.split()
	text_list = list(filter(lambda i: len(i) != 1 and len(i) != 2, text_list))
	updated_list = []
	stopword = stopwords.words('english')
	for word in text_list:
		if word.lower() not in stopword:
			updated_list.append(word.lower())
	return updated_list


# Read data from TEXT files.
def txt_Reader(path):
	text_list = []
	with open(path,'r') as f:
		text = f.read()
		# Replacing every non-alphabetic character with a space
		text = re.sub('[^a-zA-Z]+', ' ', text)
		text_list += text.split()
	text_list = list(filter(lambda i: len(i) != 1 and len(i) != 2, text_list))
	updated_list = []
	stopword = stopwords.words('english')
	for word in text_list:
		if word.lower() not in stopword:
			updated_list.append(word.lower())
	return updated_list





