def criptText(text):
    print('Text to encript: ' + text)
    finalText = ''
    for letter in text:
        ascii = ord(letter)
        ascii += 1
        finalText += chr(ascii)
    return finalText
    
def decriptText(text):
    print('Text to decript: ' + text)
    finalText = ''
    for letter in text:
        ascii = ord(letter)
        ascii -= 1
        finalText += chr(ascii)
    return finalText

def criptFile():
    file = open('text.txt','r')
    text = file.read()
    file.close()
    cripedtText = criptText(text)
    file = open('text.txt', 'w')
    file.write(cripedtText)
    file.close()
    
def decriptFile():
    file = open('text.txt','r')
    text = file.read()
    file.close()
    cripedtText = decriptText(text)
    file = open('text.txt', 'w')
    file.write(cripedtText)
    file.close()
    
#criptFile()

#result = decriptText('Txexxxtxox xpxrxuxexbxax xpxaxrxax xexnxcxrxixpxtxaxrx')
#file = open('text.txt', 'w')
#file.write(result)
#file.close()

decriptFile()
