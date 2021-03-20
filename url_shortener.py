repo = {} #repository for urls and new shorten ids
domain = 'kratki.com' # domain of the new url after shortening
id = 1 # new ids will be given by a counter. The number will be encoded in 62decimal code. 
letters_low = [chr(char) for char in range(ord('a'),ord('z')+1)] #all letter lower
letters_up = [chr(char) for char in range(ord('A'),ord('Z')+1)] #all letter upper
numbers = [str(num) for num in range(10)] #all numbers
alphanum = numbers+letters_low+letters_up #all alfanumeric characters
base = len(alphanum) # base 62 for encoding

def shorten(url):
    '''insert full link to get a kratki.com short link'''
    global id, repo
    
    def encode(id): #encoder from base 10 to base 62
        result = [] #coding output list
        while id > 0: #formula for encoding from base 10 to base x; ex. for HEX numbers on base 16
            position = id % base #index of the character, for the alphanum list
            id = id // base #new id for the while loop
            result.insert(0,alphanum[position])
        return ''.join(result)
    
    if url in repo: #verify if url is in repository
        short = repo[url] #shorten part of new url, if old url present in repository
    else:
        short = encode(id) #shorten part of new url with new id
        repo[url] = short #insert url and id in repository
        id += 1 #id counter grow by 1
    
    return f'{domain}/{short}' #new short link with new domain
print(shorten('google.com'))
print(shorten('yahoo.com'))
