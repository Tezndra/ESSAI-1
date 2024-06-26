import csv 					#Importing module to read from a CSV file
from nltk.tokenize import RegexpTokenizer	#Importing module for sentence tokenisation
from nltk.corpus import stopwords		#Importing module for stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

tokenizer = RegexpTokenizer("[\w']+")		#Function to tokenise from regular expression
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
english_stops = set(stopwords.words('english')) #Setting up the function for stopwords

stem = []
lem = []

with open('sample.csv', newline='') as f:	#To open the CSV file and read line by line
  reader = csv.reader(f)			
  for row in reader:
    print(row)
    row = str(row)				#Converting line input to string so that tokeniser can process the function
    row = row.lower()				#Converting string to lower case so that stop words can be used easily.
    row = tokenizer.tokenize(row)		#Using the tokenise function
    print (row)
    print ('\n')	
    words = row
    print (words)
    print ('\n')
    words = [word for word in words if word not in english_stops] #Using the stopwords function				
    print('\n')
    print(words)
    for j in words:
     j=stemmer.stem(j)
     stem.append(j)
     k=lemmatizer.lemmatize(j)
     lem.append(k)
    print('\n')
    print("--------------------------------------------------------")
    print('\n')
    print(stem)
    print('\n')
    print("*********************************************************")
    print('\n')
    print(lem)	
    break








