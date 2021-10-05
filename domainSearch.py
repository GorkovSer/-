import socket,threading
import homoglyphs as hg


print("Введите ключевые слова:")
a = input()
a = a.split(' ')
chars=list(a)

def dnsRequest(chars):
    domainZones=['.com', '.ru', '.net', '.org', '.info', '.cn', '.es', '.top', '.au', '.pl', '.it', '.uk', '.tk', '.ml', '.ga', '.cf', '.us', '.xyz', '.top', '.site', '.win', '.bid']
    checklist=[]
    readyList=[]

    def request(name):# функция подключения
        
        try:
            addr = socket.gethostbyname(name)
            print(name + ': ' + addr)
        except:
            pass


    def addChar(name):# функциям составления словоря (добавление буквы)
        for listElements in name:
            for characters in range(97,123,1):
                checklist.append(listElements+chr(characters))
            

    def dellChar(name):# функциям составления словоря (удаление символа)
        for listElements in name:
            for characters in range(0,len(listElements),1):
                checklist.append(listElements[:characters] + listElements[characters+1:] )


    def addCom(name):# функциям составления словоря (добовление точки)
        for listElements in name:
            for characters in range(1,len(listElements),1):
                checklist.append(listElements[:characters] +'.'+ listElements[characters:])


    def hgAdd(name):
        for listElements in name:
            homoglyphs = hg.Homoglyphs(categories=('LATIN', 'CYRILLIC'))  # alphabet loaded here
            checklist.extend(homoglyphs.get_combinations(listElements))


    def dnsConstruct(lis,domainZones):
        for listElements in lis:
            for elements in domainZones:
                readyList.append(listElements+elements) 


    addChar(chars)
    dellChar(chars)
    addCom(chars)
    hgAdd(chars)
    dnsConstruct(checklist,domainZones)
    for chars in readyList:
        t = threading.Thread(target=request, kwargs={'name': chars, })  # Создаём поток

        t.start()
        
dnsRequest(chars)