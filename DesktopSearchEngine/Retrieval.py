from DB_File import file_retrival, file_time_stamps_retrival, word_retrival
import datetime

# retives the file names and extensions we searched
def f_retrival(f_name):

	rows = file_retrival(f_name)
	updated_rows = []
	# Extracting filepaths based on matching file/extension names
	for row in rows:
		updated_rows.append(row[0])
	rows = []
	# Extracting timestamp for the corresponding filepath
	for row in updated_rows:
		rows  += file_time_stamps_retrival(row)
	# Returning top 5 results based on most recent created time stamp	
	rows.sort(key=lambda x: x[2],reverse=True)
	for i in range(len(rows)):
		if i > 5:
			break
		print(rows[i][1],datetime.datetime.fromtimestamp(rows[i][2]))


# retrives the words we searched
def w_retrival(w_name):
	rows = word_retrival(w_name)
	updated_rows = []
	# Extracting filepath
	for row in rows:
		updated_rows.append(row[1])
	rows = []
	# Extracting timestamp for the corresponding filepath
	for row in updated_rows:
		rows += file_time_stamps_retrival(row)
	# Returning top 5 results based on most recent created time stamp	
	rows.sort(key=lambda x: x[2],reverse = True)
	for i in range(len(rows)):
		if i > 5:
			break
		print(rows[i][1],datetime.datetime.fromtimestamp(rows[i][2]))



if __name__ == '__main__':
	print("Press 1 for file search or extension of file")
	print("press 2 for words search")
	val = int(input())
	if val == 1:
		f_name = input("Enter file name")
		f_retrival(f_name.lower())
	if val == 2:
		# Since we are limiting the search to unigrams, bigrams & trigrams
		print("Caution! You can enter maximum 3 words")
		word = input("Enter the words")
		w_retrival(word.lower())
