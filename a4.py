#Aaryan Sharma
#101230220




datafile = "harry.txt"

def load_datafile(datafile): 
    '''takes a file that has been requested, and returns the contents of that file in lowercase'''
    try :
        file = open(datafile,"r")
        information = file.read()
        informationstr = information.lower()
        return informationstr
    except FileNotFoundError:
        print("Invalid File; Not Found")
    

data = load_datafile(datafile)


def load_wordfile(wordfile):
    '''takes postive or negative wordfile, and appends it to a list. if file does not except, prints statement'''
    try:
        poswordlist = []
        with open(wordfile,"r") as words:
            for word in words:
                word = word.strip('\n')
                poswordlist.append(word)
        return poswordlist
    
    except FileNotFoundError:
        print("Invalid File; Not Found")




punct_list = ['.',',','?','!',':',';','%','#','@','$','(',')','[',']']
def remove_punctions(punct_list,data):
    '''removes all punctions within the file, that are also in the list'''
    for i in punct_list:
        data = data.replace(i,'')
    return data

data = remove_punctions(punct_list,data)


stop_words = ['the', 'a','an','is', 'are', 'of', 'at', 'on', 'by', 'this', 'is', 
'to', 'in', 'and', 'with', 'or', 'every']

def remove_keywords(stop_words,data):
    '''removes all words within the file, that are also within the list '''
    data = data.split()
    for i in stop_words:
       
        if i in data:
            for word in data:
                if word == i:
                    data.remove(word)
    
    datastring = ''
    datastring = " ".join(data)

    return datastring
        
data = remove_keywords(stop_words,data)

def count_all(data):
    '''counts all characters in data including spaces, not including spaces, and all the words in the data'''
    
    
    total_char = 0
    total_words = 0
    total_letters=0

    for characters in data:
        total_char+=1

    data = data.split()
    
        
    for words in data:
        total_words+=1
        
        for letters in words:
            total_letters+=1
    


    return (total_char,total_words,total_letters)   



def unique_words(data):
    '''if word already exists within the list, increment number of times word shows by 1, otherwise add the word to the list'''
    splitted = data.split(" ")
    wordcounter = []
    checked = []
    for word in splitted:
        if word not in checked:
            wordcounter.append([word, 1])
        else:
            for element in wordcounter:
                if element[0] == word:
                    element[1] += 1
        checked.append(word)
    return wordcounter

unique_words(data)
all_unique_words = unique_words(data)


def frequency_dict(data):
    '''prints the frequency of words, so if ___ words show up once, adds the word to a frequency'''
    
    newdata = unique_words(data)

    diction = {}

    for i in newdata:
        quicklist=[]
        if i[1] in diction:
            existing = diction[i[1]]
            
            diction[i[1]]= existing + " " + i[0]
        else:
            diction[i[1]]=i[0]
    
    for keys in diction:
        diction[keys] = diction[keys].split()
    
    return diction




def most_common_word(data):
    '''finds the most common word within the data, and returns it, with the number of times it shows'''
    wordlist = unique_words(data)
    
    common_value = 0
    full = ''
    for i in wordlist:
        
        
        if i[1] > common_value:
            common_value = i[1]
            full = i
        else:
            pass
    
    return full
    
word = most_common_word(data)


x= 'the'
def word_pairs(data, x):
    '''for x being in the file, takes every word that comes after selected x word'''
    data = data.split()
    poslist = []
    wordpair = []


    for i in range(len(data)):
        if data[i] == x:
            poslist.append(i)

    for pos in poslist:
        value = data[pos+1]
        wordpair.append(value)        

    return wordpair




def sentiment_analysis_1(datafile):
    '''all functions for the first algorithm, which appends required statements into a file.'''

    
    prefixdatafile = 'prefix_' + datafile
    
    with open(prefixdatafile,'w') as newfile:

        

        newfile.write('sentiment analysis for ')

        newfile.write(datafile)


        newfile.write('\nText analysis')
        
        
        
        data = load_datafile(datafile)
        
        

        newfile.write('\n')
        values = count_all(data)
        totalcharacters = values[0]
        totalwords = values[1]
        totalletters = values[2]

        newfile.write('\nTotal chars: ')
        newfile.write(str(totalcharacters))
        newfile.write('\nTotal words: ')
        newfile.write(str(totalwords))
        newfile.write('\nTotal chars without spaces: ')
        newfile.write(str(totalletters))
        

        
        
        
       
        
        newfile.write('\nText removing following punctuations\n')
        punct_list = ['.',',','?','!',':',';','%','#','@','$','(',')','[',']']
        newfile.write(str(punct_list))
        data = remove_punctions(punct_list,data)
        newfile.write('\n')
        newfile.write(data)
        
        
        newfile.write('\nText after removing the following stop words\n')
        stop_words = ['the', 'a','an','is', 'are', 'of', 'at', 'on', 'by', 'this', 'is', 
        'to', 'in', 'and', 'with', 'or', 'every']
        newfile.write(str(stop_words))
        data = remove_keywords(stop_words,data)
        newfile.write('\n')
        newfile.write('\n')
        newfile.write(data)
        
        

        data = data.split()
        

        wordfile = "negativewords.txt"
        load_wordfile(wordfile)
        negativewords = load_wordfile(wordfile)

        wordfile = "positivewords.txt"
        load_wordfile(wordfile)
        positivewords = load_wordfile(wordfile)
        
        total_positive_words = 0
        total_negative_words = 0
        total_neutral_words = 0

        positivewordslist = []
        negativewordslist = []
        neutralwordlist = []

        for i in data:
            if i in positivewords:
                total_positive_words+=1
                positivewordslist.append(i)
            
        for i in data:
            if i in negativewords:
                total_negative_words+=1
                negativewordslist.append(i)

        for i in data:
            if i not in positivewords and i not in negativewords:
                neutralwordlist.append(i)
                total_neutral_words+=1


        


        sentiment = ''
        if total_positive_words > total_negative_words:
            sentitement = 'sentiment is positive'
        elif total_negative_words > total_positive_words:
            sentiment = 'sentiment is negative'
        else:
            sentiment = 'sentiment is neutral'
        
        
        newfile.write('\nWord counts\n')
        newfile.write('Positive word count: ')
        newfile.write(str(total_positive_words))
        newfile.write('\n')
        newfile.write(str(positivewordslist))

        newfile.write('\n')

        newfile.write('\nNegative word count: ')
        newfile.write(str(total_negative_words))
        newfile.write('\n')
        newfile.write(str(negativewordslist))
        
        newfile.write('\n')

        newfile.write('\nNeutral word count: ')
        newfile.write(str(total_neutral_words))
        newfile.write('\n')
        newfile.write(str(neutralwordlist))

        newfile.write('\n')
        newfile.write('\n')
        newfile.write(sentiment)

        newfile.write('\n')
        newfile.write('\n')
        newfile.write('End of file')

sentiment_analysis_1(datafile)



def sentiment_analysis_2(datafile):
    '''all functions for the first algorithm, which appends required statements into a file.'''

    
    prefixdatafile = 'prefix_' + datafile
    
    with open(prefixdatafile,'w') as newfile:

        datafile = "invisibleMan.txt"

        newfile.write('sentiment analysis for ')

        newfile.write(datafile)


        newfile.write('\nText analysis')
        
        
        
        data = load_datafile(datafile)
        
        

        newfile.write('\n')
        values = count_all(data)
        totalcharacters = values[0]
        totalwords = values[1]
        totalletters = values[2]

        newfile.write('\nTotal chars: ')
        newfile.write(str(totalcharacters))
        newfile.write('\nTotal words: ')
        newfile.write(str(totalwords))
        newfile.write('\nTotal chars without spaces: ')
        newfile.write(str(totalletters))
        

        
        
        
       
        
        newfile.write('\nText removing following punctuations\n')
        punct_list = ['.',',','?','!',':',';','%','#','@','$','(',')','[',']']
        newfile.write(str(punct_list))
        data = remove_punctions(punct_list,data)
        newfile.write('\n')
        newfile.write(data)

        newfile.write('\nText after removing the following stop words\n')
        stop_words = ['the', 'a','an','is', 'are', 'of', 'at', 'on', 'by', 'this', 'is', 
        'to', 'in', 'and', 'with', 'or', 'every','an', 'the', 'of', 'for', 'in', 'on', 'we', 'us', 'she',' he']
        newfile.write(str(stop_words))
        data = remove_keywords(stop_words,data)
        newfile.write('\n')
        newfile.write('\n')
        newfile.write(data)


        commonword = most_common_word(data)
        newfile.write('\n')
        newfile.write('Most common word and value: ')
        newfile.write(commonword)



def main():
    '''calls the two sentiment analysis functions'''
    datafile = "harryPotter.txt"
    sentiment_analysis_1(datafile)

    datafile = 'invisibleMan.txt'
    sentiment_analysis_2(datafile)

if __name__== '__main__' :
    main()








