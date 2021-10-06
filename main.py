#importing natural language toolkit for important nlp tasks
import nltk

#importing stopwords of english language in order to remove the words that have no affect on the sentance
from nltk.corpus import stopwords
garbage_words = stopwords.words("english")

#importing porter stemmer in order to convert the words to their root words
from nltk import PorterStemmer
port = PorterStemmer()


# read_file function is made in order to read the lines in the file and store them in a python list
# read_file() takes the path of the file as argument
def read_file(filepath):
    f = open(filepath,"r")
    l = f.readlines()
    for i in range(len(l)):
        x = l[i].split("\n")
        l[i] = x[0]
        l[i] = l[i].lower()
    return l

# the read_tweets function reads the txt files that contains tweets and returns a python list of all the tweets
def read_tweets(filepath):
    l = read_file(filepath)
    for i in range(len(l)):
        x = l[i].split(":")
        l[i] = x[1]
    return l

# read_words() function takes path as argument and returns all the racist words in its root form in a python list
def read_words(filepath):
    l = read_file(filepath)
    for i in range(len(l)):
        l[i] = port.stem(l[i].lower())
    return l

# check_racial function takes in 2 arguments : a sentence and the list of racist words
# check_racial function returns the degree of profanity of the sentence passed as the argument
# I have assumed degree of profanity as the % of racist words in a sentence

def check_racial(sentence,racist):
    words = sentence.split()
    cnt = 0
    total = 0
    for i in range(len(words)):
        word = words[i]
        if(word[-1]=='.'):
            word = word[:-1]
        wd = port.stem(word.lower())
        if(wd in garbage_words):
            continue
        if(wd in racist):
            cnt+=1
        total+=1
    ans = (cnt/total)*100
    ans = round(ans,2)
    return ans

#the main function where we do our important function calls
def main():
    tweets = read_tweets("tweets.txt") #loading the tweets
    racist_words = read_words('racist_words.txt') # loading the racist words
    #printing the degree of profanity of eacht tweet
    for tweet in tweets:
        print(check_racial(tweet,racist_words))

    #let us make the code more robust
    s = input("\n\nTweet something : ")
    print("Degree of profanity of entered tweet : " , check_racial(s,racist_words))

if __name__ == "__main__":
    main()