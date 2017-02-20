import mysql.connector
import random

def dialog(scene):
    if (scene==1):
        print("The following events take place in 25.4.2016 Helsinki. Im state agent Jack Power and today is the longest day of my life.")
        print("...")
        print("It is twelve o’clock on a sunny monday afternoon, when Jack is heading to the work. Around the corner there is a pharmacy, where you can get some medicine for your drug addiction. Visiting the pharmacy will take 15 minutes.")
        print("A Go straight to work or B go to pharmacy.")
    elif (scene==2):
        print("The time is 12:20. You arrive to CTU, you secretaire gives you a message from the division.")
        print("The message says: According to intelligence service the Terrorist are planning to strike somewhere in Helsinki during the next 24 hours.")
        print("Your mission is to find out who is behind this attack, find the bomb and stop the Terrorist")
        print("")
        print("-The Division")
    elif (scene==3):
        print("The time is 12.05. You arrive to CTU, you secretaire gives you a message from the division.")
        print("The message says: According to intelligence service the Terrorist are planning to strike somewhere in Helsinki during the next 24 hours.")
        print("Your mission is to find out who is behind this attack, find the bomb and stop the Terrorist.")
        print("")
        print("-The Division")
    elif (scene==4):
        print("You are on zero knowledge for the possible attack so the investigations should be started somewhere familiar with already known people who might have some connections and information.")
        print("")
        print("First locations to start investigating are: the PRISON of Sörnäinen, the Secret PUB and the MOSQUE of Itis. For more information of the locations you can use a command desc place name.")
    elif(scene==5):
        print("Now that you have selected your first destination you have to select your starting gear from the armory before you go to your mission. Keep in mind that the gear you select might have influence on upcoming events.")
    elif(scene==6):
        print("You step into to the pub and its half lit,\n your old friend is laughin in the back corner and making shadows\"Jaack! hohhohohohoo, good to see you!, what's on your mind?\"")
        print("You can TALK with your old FRIEND or you can GO to other locations, use DESC to see other locations available")
    elif(scene==7):
        print("In prison yard inmates are haunting you with their eyes as you walk in. ")
        print("\"Interrigation room 2 open\"\nSays the guard inside.")
        print("")
        print("Now its you and the GangBoss in the small room with concrete walls")
        print("GangBoss:\"So Jack Power, the man who put me in here and now you need something from me. Small world ha?\nOkay tell me all ready i cant wait to hear this \"")
        print("A:Strangle that arrogant shit mouth\nB:Ask him about his knowledge of attacks")
        
    else:
        print("")

###########################################################################PLACES################################################################################

def talkBAR(command2):
    valueDrugs="null"
    print("Jack:\"I am investigating a terrorist threat and hopefully preventing their attack in helsinki.\n informant says the strike is scheluded today!\"")
    print("...")
    print("Formercolleg:\"I would love to help you, but my since i quit the job in CTU,\n i haven't slept so well and i started using some meds, now it’s hard to function without them.\"")
    print("A: give your ol' buddy some DRUGS\nB:Keep all your drugs to your self")
    while(command2!= "a" and "b"):
        command = input("Give your command: ").lower()
        command2 = parser(command)
        if(command2 == "a"):
            print("a")
            checkDrugs(valueDrugs)
            if(checkDrugs(valueDrugs)==4):
                 print("Formercolleg:\"Thanks! know GO to the PRISON and interrogate the GangBoss. I have a feeling that he won’t crack in face to face conversation.\nToo much eyes there \"")
                 drug = "drugs"
                 dropitem(drug)
            else:
                print("I'm sorry jack but it seems like I can't help you, maybe you can get me some and we'll check later if I have the info.")
        elif(command2 == "b"):
            print("I'm sorry jack but it seems like I can't help you, maybe you can get me some and we'll check later if I have the info.")
        else:
            print("Only A and B are suitable commands")

        
def pub(command2):
    valueKnife="null"
    fight=random.randint(0,9)#randomoidaan taistelu
    if (fight>4):#ajetaan taistelun ehto
        print("You step into the bar and random guy throws himself onto you, he has a pool cue and he will surely use it!")
        checkKnife(valueKnife)#tarkistaa tietokannasta onko puukkoa
        if (checkKnife(valueKnife) == 3):#jos on
            print("Luckily you drew your knife and stabbed him before he was able to do anything")
            number=6
            dialog(number)
            while(command2 != "talk friend" and "go prison" and "go itis" and "go ctu"):
                command = input("Give your command: ").lower()
                command2 = parser(command)
                if(command2 == "talk"):
                    talkBAR(command)
                elif(command2 == "go prison"):
                    print("prison")
                elif(command2 == "go itis"):
                    print("itis")
                elif(command2 == "go ctu"):
                    print("ctu")
                else:
                    print("you can only use CAPS commands")
                    dialog(number)
                    
        else:
            print ("You had no knife and the guy with the pool cue killed you\nGAME OVER")
            clueOne=4
    else:
        number=6
        dialog(number)
        while(command2 != "talk friend" and "go prison" and "go itis" and "go ctu"):
                command = input("Give your command: ").lower()
                command2 = parser(command)
                if(command2 == "talk"):
                    talkBAR(command)
                elif(command2 == "go prison"):
                    print("prison")
                elif(command2 == "go itis"):
                    print("itis")
                elif(command2 == "go ctu"):
                    print("ctu")
                else:
                    print("you can only use CAPS commands")
                    dialog(number)

def prison(command2):
    number = 7
    dialog(number)
    valuePhone="null"
    while(command2 != "a" and "b"):
        print("A:Strangle that arrogant shit mouth\nB:Ask him about his knowledge of attacks")
        command = input("Give your command: ").lower()
        command2 = parser(command)
        if(command2=="a"):
            print("you're just about to get his wimpipe crushed when the guards show up and walk you out of the prison")
            #pitäää tappaa ohjelma
        elif(command2=="b"):
            print("Jack:\"What do you know about the attacks scheluded to happen here in Helsinki today, dont lie to me. Im not your enemy unless you want me to be")
            print("")
            print("GangBoss:\"Im not affraid you as my enemy, and i can't say shit here. Im dead man allready for getting in this kinda interrigation\"")
            while(argument != "a" and "b"):
               print("A: Give him non lethal amount of cyanide.\nB: Threaten to go after his family if he doesn't help")
               command = input("Give your command: ").lower()
               argument = parser(command)
               if(argument=="a"):
                   print("Jack:\"You are running out of time, i don't have time to play games with you (gave cyanide)\"")
                   print("Man starts trembling and screaming. he kick and punches into air and begs you to stop this, but at the same time he is smiling arrogant as ever.\nInfluence wears off little by little")
                   while(arg2 != "a" and "b"):
                       print("A: do it again\B: Stop")
                       command = input("Give your command: ").lower()
                       arg2 = parser(command)
                       if(arg2 == "a"):
                           print("Man starts to turn blue and yellow as he's being tortured. Game face is also fading away and he's showing some remorse")
                           while(arg3 != "a" and "b"):
                               print("A: do it again\B: Stop")
                               command = input("Give your command: ").lower()
                               arg3 = parser(command)
                               if(arg3 == "a"):
                                   print("guards walk you out of the prison as you're being too violent")
                               elif(arg3=="b"):
                                   print("GangBoss:\"Okay DROP me your cellphone \nA guy from Tallinn knows something for sure \nI will arrange you a meeting at the sea with him.\"")
                                   checkPhone(valuePhone)
                                   if(valuePhone == 8):
                                       #avataan meri
                                       print("now GO to your boat in KAUPPATORI")
                                   else:
                                       print("YOU DIDN'T BRING YOU PHONE? well it's GG now")
                                       #kill game
                       elif(argument=="b"):
                           print("Game over you chicken, you didnt't get the info and the city will blow up")
                       else:
                           print("Use the CAPS commands")
               elif(argument=="b"):
                   print("Game over you chicken, you didnt't get the info and the city will blow up")
               else:
                   print("Use the CAPS commands")
                
        else:
            print("you can only use CAPS commands")

def itis(command2):
    itemloop=0
    print("in Mosque people are acting suspiciously nice and one of the Muslims requests your help, task would be done in 30 min. ")
    while(command2 != "a" and "b"):
        print("A: you help the muslim B: don't help")
        command = input("Give your command: ").lower()
        command2 = parser(command)
        if(command2 == "a"):
            print("Muslim gives you some description medicine which has in his words\"DRUG like influence\"")
            checkDrugs(valueDrugs)
            countItems(itemloop)
            while(itemloop > 4):
                if(checkDrugs(valueDrugs)==4):
                    print("looks like you already have drugs")
                else:
                    while("drop" not in command2):
                        print("You have too many items, DROP something from your items")
                        showItems()
                        command = input("Give your command: ").lower()
                        command2 = parser(command)
            if(checkDrugs(valueDrugs)==4):
                print("now GO investigate somewhere else: PRISON,PUB,CTU")
            else:
                item="drugs"
                getitem("drugs")
        elif(command2 == "b"):
            print("You are wasting your time, no terrorist here")
            checkDrugs(valueDrugs)
            if(checkDrugs(valueDrugs)==4):
                print("GO investigate somewhere else: PRISON,PUB,CTU")
            else:
                print("You don't have any drugs for your addiction")
                #gameover
            
            




###########################################################################SQL################################################################################

def countItems(itemloop):
    cur = db.cursor()
    sql = "select count(itemid) from jack;"
    try:
        cur.execute(sql)
        itemCount = cur.fetchone()
        itemloop = itemCount[0]
        return itemloop
    except:
        db.rollback
def showItems():
    cur = db.cursor()
    sql = "select item.name from jack,item where jack.itemid like item.id;"
    cur.execute(sql)
    items = cur.fetchall()
    data = items[0]
    print(len(data))
    for row in data:
        print(row)
        print("")
    return

def describe():
    cur=db.cursor()
    sql= "select location.name, location.description from location, map where location.id=map.locationid and map.open=1;"
    cur.execute(sql)
    data = cur.fetchall()
    print(len(data))
    for row in data:
        print(row)
        print("")
    return

def checkKnife(valueKnife):
    cur = db.cursor()
    knifeCheck = "select itemid from jack where itemid like 3;"
    try:
        cur.execute(knifeCheck)
        knifeData = cur.fetchone()
        if knifeData[0]==3:
            valueKnife=3
            return valueKnife
        else:
            print("error")
            return "null"
    except:
        db.rollback

def checkPhone(valuePhone):
    cur = db.cursor()
    phoneCheck = "select itemid from jack where itemid like 3;"
    try:
        cur.execute(phoneCheck)
        phoneData = cur.fetchone()
        if phoneData[0]==8:
            valuePhone=8
            return valuePhone
        else:
            print("Sorry you don't seem to have a phone in your inventory")
            return "null"
    except:
        db.rollback                                         

def checkDrugs(valueDrugs):
    cur = db.cursor()
    drugCheck = "select itemid from jack where itemid like 4;"
    try:
        cur.execute(drugCheck)
        knifeData = cur.fetchone()
        if knifeData[0]==4:
            valueDrugs=4
            return valueDrugs
        else:
            print("You have no drugs")
            return "null"
    except:
        db.rollback

def dropitem(item):
    cur = db.cursor()
    sql = "select id from item where name like '" + item + "';"
    jackitem = "select itemid from jack;"
    try:
        cur.execute(sql)
        data = cur.fetchone()
        print(data)
        cur.execute(jackitem)
        data2=cur.fetchall()
        print(data2)
        for row in data2:
            print(row)
            if data == row:
                cur.execute("delete from jack where itemid=%s"%(data[0]))
                db.commit()

    except:
        db.rollback()
    return


def getitem(item):
    cur = db.cursor()
    sql = "select id from item where name like '" + item + "';"
    countWear = "select count(jack.itemid) from jack,wearable where jack.itemid = wearable.itemid"
    countUse = "select count(jack.itemid) from jack,useable where jack.itemid = useable.itemid"
    try:
        cur.execute(sql)
        data = cur.fetchone()
        print(data)
        useid = "select count(itemid) from useable where itemid= %s;"%(data[0])
        wearid = "select count(itemid) from wearable where itemid= %s;" % (data[0])
        cur.execute(countWear)
        wear=cur.fetchone()
        cur.execute(countUse)
        use = cur.fetchone()
        cur.execute(wearid)
        print("wearid executed")
        wearDublicate=cur.fetchone()
        print(wear)
        print(wearDublicate)
        if wearDublicate [0]==1:
            if(wear[0] < 2):
                sql2 = ("INSERT INTO jack "
               "(itemid) "
               "VALUES (%s)") % (data[0])
                cur.execute(sql2)
                db.commit()
                cur.close()
                print("wearable picked")
                print(data[0])
            else:
                print("you have too many wearable items")
        else:
            if use[0] < 2:
                cur.execute(sql)
                data = cur.fetchone()
                sql2 = ("INSERT INTO jack (itemid) VALUES (%s);"%(data[0]))
                cur.execute(sql2)
                aa="select * from jack;"
                cur.execute(aa)
                jep = cur.fetchone()
                print(jep)

                print("useable picked")
            else:
                print("you have too many useable items")

    except:
        db.rollback()

    return

def go(item):
    cur = db.cursor()
    sql = "select id, x, y from location where name like %@'" + item + "'@%;"
    start = "select location.x, location.y from location, jack where jack.locationid = location.id;"
    try:
        cur.execute(sql)
        data = cur.fetchone()
        if(data==None):
            print("You can't go there!")
        else:
            print(data)
            cur.execute(start)
            data2 = cur.fetchone()
            tulos=(math.sqrt(((data[1]-data2[0])**2)+((data[2]-data2[1])**2)))
            print(tulos)
            sql2 = "update jack set locationid = %s where id = 1;"%(data[0])
            cur.execute(sql2)
    except:
        db.rollback()
    return

def use(item):
    cur = db.cursor()
    sql = "select id from item where name like %'" + item + "'%;"
    rule = "select itemid from jack;"
    try:
        cur.execute(sql)
        data = cur.fetchone()
        cur.execute(rule)
        data3 = cur.fetchall()
        print(data3)
        print(data)
        if data == None:
            print("there is no such item in the game")
        else:
            sql2 = "select * from useable where itemid = %s;" % (data[0])
            cur.execute(sql2)
            data2 = cur.fetchone()
            print(data2)
            for i in range (4):
                if data3[i] == data[0]:
                    if data2[1] == 1:
                        print("ääni")
                    if data2[2] == 1:
                        print("dmg")
                    if data2[3] == 1:
                        print("matka")
                    if data2[4] == 1:
                        print("valo")
                        light()

    except:
        db.rollback()
    return

def openloc():
    cur=db.cursor()
    sql= "select location.name, location.description from location, map where location.id=map.locationid and map.open=1;"
    cur.execute(sql)
    data = cur.fetchall()
    for row in data:
        print(row)
    return

###########################################################################PARSER################################################################################

def parser(command):
    commands = ["go", "pick", "drop", "exam", "use", "talk", "a", "b", "c", "desc"] #villen taulu
    word = "null"
    if (command == ""):
        return;
    else:
        comList = command.split()#jakaa parametrin osiin
        com = comList[0];#tallentaa nollan
        del comList[0]#poistaa nolland listasta
        item = " ".join(str(x) for x in comList)
        for i in range(len(commands)):
            if com == commands[i]: #jos nolla on commandsien arvo
                word = i #word saa sen arvon joka on com on commandsissa

    if word == 0: #palauttaa sen mitä com vastaa taulusta
        go(item)
        return command
    elif word == 1:
        print("pick")
        getitem(item)
        return "pick"
    elif word == 2:
        print("drop")
        return "drop"
    elif word == 3:
        print("exam")
        return "exam"
    elif word == 4:
        use(item)
        return "use"
    elif word == 5:
        print("talk")
        return "talk"
    elif word == 6:
        print("a")
        return "a"
    elif word == 7:
        print("b")
        return "b"
    elif word == 9:
        describe()
        return "desc"
    else:
        print("EI TOIMI")
        return "EI TOIMI"

###########################################################################CHAPTERS################################################################################

def chapterOne():
    scene=1                                                                                             #dialog asetetaan ykköseki
    command="null"
    loopend=0
    proceed=0#komento alustetaan
    valueKnife="null"
    itemloop="null"
    itempick="null"
    dialog(scene)                                                                                       #dialogi soitetaan
    clueOne = 0                                                                                         #Vihjeet alustetaan
    while(proceed!=1):                                                               #looppaa kunnes a tai b
        command = input("Give your command: ").lower()                                                  #ottaa komennon ja muuttaa sen pieneksi
        command2 = parser(command)                                                                                 #parseroi
        if(command2 =="a"):
            number=2                                                                                    #dialogi kakkoseksi
            dialog(number)
            proceed=1#soitetaan kakkonen
        elif(command2 =="b"):
            number=3                                                                                    #dialogi kolmonen
            dialog(number)
            command="get drugs"
            parser(command)
            proceed=1#soitetaan
        else:
            print("Please check your typing, the answer can only be A or B")                            #valitetaan
    number=4                                                                                            #nelone kasettiin
    dialog(number)#soitetaan
    while(loopend != 1):#looppaa kunnes sopiva vastaus
        command = input("Give your command: ").lower()
        command2 = parser(command)
        if(command2 == "go pub"):
            loopend = 1
        elif(command2 == "go prison"):
            loopend = 1
        elif(command2 == "go itis"):
            loopend = 1
        else:
            loopend = 0
        print(command2)
    number=5#vitonen sisään
    dialog(number)#soitetaan
    while(countItems(itemloop)!=5):
        countItems(itemloop)
        print("You can PICK items from: GLOCK, COMBATKNIFE, FLASHLIGHT, SUNGLASSES, CELLPHONE, KEVLARWEST, KEVLARHELMET, LEATHERJACKET and FLAMEBEANIE")
        itempick = input("Give your command: ").lower()
        parser(itempick)
    if (command2 == "go pub"):#jos pubi
        pub(command2)                            
    elif(command2 == "go prison"):#jos vankila
        prison(command2)
    elif(command2 == "go itis"):#jos itis
        itis(command2)
    else:
        print("pillu")

################################################################################################################

db = mysql.connector.connect(host="127.0.0.1",
                             user="root",
                             passwd="K4pp4",
                             db="JPbase",
                             buffered=True)
chapterOne()
