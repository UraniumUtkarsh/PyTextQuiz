import mysql.connector as co
import time
     
def playerin():
    try:
        connection=co.connect(host="localhost",user="root",passwd="root",database="ez")
        cursor=connection.cursor()
        print("\n\t\tExtracting Player info from databas -- \n\n")
        sql="SELECT * FROM player"
        cursor.execute(sql)
        data=cursor.fetchall()
        print("name\tcontact\tscore\ttime")
        for row in data:
            print(row)
        print("\n\n")
    except:
        print("\n\t\tError: Playerinfo cannot be extracted\n")
    return

def highest():
    try:
        connection=co.connect(host="localhost",user="root",passwd="root",database="ez")
        cursor=connection.cursor()
        print("\n\tViewing the player with highest scores\n")
        sql="SELECT score FROM player"
        cursor.execute(sql)
        data=cursor.fetchall()
        highest=max(data)

        sql="SELECT * from player WHERE score='%s'"%highest
        cursor.execute(sql)
        playr=cursor.fetchall()
        print("name\tcontact\tscore\ttime")
        for row in playr:
            print(row)
        print("\n\n")
    except:
        print("\n\t\tError: Highest Playerinfo cannot be extracted\n")
    return

def chk_with_code(): #OK
    try:
        connection=co.connect(host="localhost",user="root",passwd="root",database="ez")
        cursor=connection.cursor()
        code=input("Enter Contact Code: ")
        sql="Select * from player where contact='%s'"%code
        cursor.execute(sql)
        data=cursor.fetchall()
        for row in data:
            print(row)
        if data==[]:
            print("\n\tNo records Found\n")
        connection.close()
    except:
        print("\nError chkcode\n")
    return
        
def history(): #OK
    try:
        connection=co.connect(host="localhost",user="root",passwd="root",database="ez")
        cursor=connection.cursor()
        name=input("Enter name to check all records with given name: ")
        sql="Select * from player where name='%s'"%name
        cursor.execute(sql)
        data=cursor.fetchall()
        for row in data:
            print(row)
        if data==[]:
            print("\n\tNo records Found\n")
        connection.close()
    except:
        print("\nError history\n")
    return

def player(): #OK
    print("\n"*10)
    print("""
                                                    Player Menu

        Select      any      of      the        following~

                                1. Create Profile
                                2. Check Score with Contact code
                                3. See Playing History with your name

                                                                        OR, Press 0 to return back\n""")
    pin=int(input("Player's Choice: "))
    if pin==0:
        return
    elif pin==1:
        profile()
        quiz()#QUIZ called here
        updateScore()
        input("\n\n Press enter to return to Payer Menu...\n")
        return
    elif pin==2:
        chk_with_code() #OK
        input()
        return
    elif pin==3:
        history()#OK
        input()
        return
    else:
        print("\n\tInvalid Choice, Try again\n")
        pass

questions=[]
Options=[]
Answers=[]
Player_local={} #Dictionary

def findQ(): #Internal 1 #OK
    f=open("data.txt",'r')
    fr=f.readlines()
    global questions
    for i in range(len(fr)):
        if (fr[i]).startswith("Que",0,len(fr[i])):
            #print(fr[i])
            questions.append(fr[i])
    f.close()
        

def findOpt(): #Internal 2 #OK
    f=open("data.txt",'r')
    fr=f.readlines()
    global Options
    for i in range(len(fr)):
        if (fr[i]).startswith("Opt",0,len(fr[i])):
            #print(fr[i])
            Options.append(fr[i])
    f.close()

def findAns(): #Internal 3 #OK
    f=open("data.txt",'r')
    fr=f.readlines()
    global Answers
    for i in range(len(fr)):
        if (fr[i]).startswith("Ans",0,len(fr[i])):
            #print(fr[i])
            Answers.append(fr[i])
    f.close()
    
findQ()
findOpt()
findAns()


def addQ(): #Internal 4 #OK
    f=open("data.txt","a")
    global questions
    c=str(len(questions)+1)
    print("\n\tWe already have ",c," Questions!\n")
    add=input("Insert a Question\t")
    form="\nQue"+c+": "+add
    f.write(form)
    print()
    f.close()
    print("\tQuestion Inserted!\n")
    

def addOpt(): #Internal 5 #OK
    f=open("data.txt","a")
    global Options
    c=str(len(Options)+1)
    print("\n\tWe have options saved for ",c," questions!\n")
    add=input("Insert all options seperating with comma\t")
    form="\nOpt"+c+": "+add
    f.write(form)
    print()
    f.close()
    print("\tOptions Inserted!\n")

def addAns(): #Internal 6 #OK
    f=open("data.txt","a")
    global Answers
    c=str(len(Answers)+1)
    print("\n\tWe have ",c," Answers!\n")
    add=input("Insert Answer\t")
    form="\nAns"+c+": "+add
    f.write(form)
    print()
    f.close()
    print("\tAnswer Inserted!\n")

def Check(): #admin #OK
    global questions
    global Options
    global Answers

    if (len(questions))==(len(Options)) and (len(Options))==(len(Answers)):
        return True, len(questions)
    else:
        return False
    
def add(): #admin #OK
    print("\n\t\t\tADDING A NEW QUESTION\n")
    addQ()
    addOpt()
    addAns()
    f=open("data.txt","a")
    fc=f.write("\n")
    print("\n\tA new Question added Successfully!")

def displayOpt(i): #Quiz call #OK
    c=Options[i].split(sep=" ",maxsplit=4)
    for j in c:
        print(j,end="\n")
    print("\n")

def displayAns(i): #OK
    c=Answers[i].split(sep=" ")
    cout=c[-1][:-1]
    cout=cout.lower()
    return cout
    
def quiz(): #OK
    global questions
    global Options
    global Answers

    print("\n"*20)
    chk=Check()
    if chk==False:
        print("\n\t\t Error: Que404 - Error with your data file! Contact Admin!\n")
        return
    else:
        print("\n\n\t\t\t--Starting Quiz--\n\n")
        pass
    
    print("""
    Instructions~
        -- For every correct answer, you will recieve +1 points.
        -- For no answer or wrong answer, you won't be rewarded any points.\n""")
    
    count=0
    for start in range(len(questions)):
        print(questions[start])
        print(displayOpt(start))

        ui=input("Enter your answer: ")
        ui=ui.lower()
        x=displayAns(start)

        print(Answers[start]," is answer to this Question.\n")
        
        if ui==x:
            print("\tCorrect\t+1\n\n")
            count+=1
        elif ui=="":
            print("\tNot Answered!\n\n")
        else:
            print(ui,x,ui==x)
            print("\tIncorrect\t0\n\n")
            pass
        
    print("\n\n\tYou scored: ",count," points.")
    print("\tTotal score: ",len(questions),"\n\n")
    scor="{}/{}".format(count,len(questions))
    global Player_local
    Player_local['score']=scor #Update Dictionary
    return
    
def profile(): #Tested OK
    try:
        connection=co.connect(host="localhost",user="root",passwd="root",database="ez")
        cursor=connection.cursor()
        print("\n\t\t\tSetting up Player Profile\n\n")
        print("""
    Remember
            --> If you dont have any contact, fill 10 digit of your personal choice code so that we can save your record.
            --> Remember the name you use here for future reference regarding score history!
                                                                                                -Team EZ Quiz
                                                        Thank you\n\n""")
        name=input("\tName: ")
        global Player_local
        Player_local['name']=name #update dictionary
        
        contact=input("Contact code: ")
        Player_local['contact']=contact
        t=time.ctime()
        score="N/A"
        val=(name,contact,score,t)

        sql="INSERT INTO player VALUES('%s','%s','%s','%s')"%(val)
        cursor.execute(sql)
        connection.commit()
        connection.close()
        print("\n\tPlayer profile created!\n")
        return
    except:
        print("\n\tError: Profile404 - Profile Setup not running...\n")
        return
                                        
def updateScore(): #Tested OK
    try:
        connection=co.connect(host="localhost",user="root",passwd="root",database="ez")
        cursor=connection.cursor()
        global Player_local #dictionary
        a=Player_local['score']
        b=Player_local['name']
        c=Player_local['contact']
        val=(a,b,c)
        sql="UPDATE player SET score='%s' WHERE name='%s' and contact='%s'"%val
        cursor.execute(sql)
        connection.commit()
        connection.close()
        print("\n\nScore Updated!\n")
    except:
        print("\n\nError - Score cannot be updated!\n")
    return

def admin():
    while True:
        print("\n"*10)
        print("""
                                                EZ Quiz Administration

            Press one of the following numbers as per your choice~

                                            1. Create a new Question Set
                                            2. Show - Player info
                                            3. Show - Highest record.

                                                        OR, Press 0 to Return back.
    \n""")
        ai=int(input("Choice: "))
        if ai==0:
            return
        elif ai==1:
            add() #OK
            input()
        elif ai==2:
            playerin()
            input()
        elif ai==3:
            highest()
            input()
        else:
            print("\n\tInvalid Choice, Try again!\n")
            pass

 
def Menu(): #OK
    while True:
        print("\n"*25)
        print("""
                                                --- Welcome to EZ Quiz ---
                        Who   are   you?

                                        1. Administrator
                                        
                                        2. Player

                                        
                                    If you are None of them, Press 0 to Exit
    \n""")
        cin=int(input("Answer here\t"))
        if cin==0:
            return
        elif cin==1:
            admin() #OK
            input()
        elif cin==2:
            player() #OK
            input()
        else:
            print("\n\tWrong Input")
            print("\tTry again\n\n")
            pass
Menu()#call it to start
