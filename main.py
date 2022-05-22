def criptText(text):
    print('Text to encript: ' + text)
    finalText = ''
    for letter in text:
        finalText +=letter + 'x'
    return finalText
    
def decriptText(text):
    print('Text to decript: ' + text)
    finalText = ''
    counter = 0
    for letter in text:
        if counter %2 == 0:
            finalText += letter
        counter += 1
    return finalText

def criptFile():
    file = open('text.txt','r')
    text = file.read()
    file.close()
    cripedtText = criptText(text)
    file = open('text.txt', 'w')
    file.write(cripedtText)
    file.close()
    
#criptFile()

#result = decriptText('Txexxxtxox xpxrxuxexbxax xpxaxrxax xexnxcxrxixpxtxaxrx')
#file = open('text.txt', 'w')
#file.write(result)
#file.close()

criptFile()
