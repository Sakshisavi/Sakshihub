#CHATBOX FOR EXAMS
import time
while True:
    print("****************************************")
    s="*********Welcome to ExamChatbox********"
    for x in s:
        print(x,end='')
        time.sleep(0.1)
    print("I am here to prepare you for exams")
    print("I can ask you Questions related to Computer Science/Information practices")
    print("""I have a pop quiz for you
              For every correct answer : +4
              For every Incorrect answer:-1
              There are total 10 Questions in this quiz.""")

    H=str(input("Shall we start:"))
    if H.lower() == "yes":# It allows lower case letters as well
            print("Q1 Who is the fathers of Computer")
            print("""A.Charles Babbage
    B.Alan Turing
    C.Ted Hoff
    D.None of the above""")
    else :
        print("OK,Maybe next time")
            
    A=input("Enter Your Choice:")

    Point=0
    if A=="A"or A=="a":# Self note1: You can use this too -(if A.upper() == "A":)

              print("Correct","well Done")
              Point+=4
              print("Here's the next question")
    elif A=="B"or A=="b":#Same here as well as Selfnote1
              print("Incorrect ,","The answer is A  ,","Good try,it was a close call.")
              Point-=1
    else:
        print("Incorrect","The Answer is A","Don't worry we'll get it next time")
        Point-=1
    print("""Q2 Father of Modern Computer....
          A.Charles Babbage
          B.Alan Turing
          C.Ted Hoff
          D.None of the above""")
    B=input("Enter your choice:")
    R= ("correct,let's proceed with the next question")
    W= ("Incorrect")
    if B.upper()=="B":
        print("correct","let's proceed with the next question")
        Point+=4
    else:
        print("Incorrect","The Answer is B")
        Point-=1
    print("""Q3 The most fastest and most expensive computer are...
          A.Super Computers
          B.Quantum Computers
          C.Mainframe Computers
          D.Micro Computers""")
    C=input("Enter your choice:")
    if C.upper()=="A":
        print(R)
        Point+=4
    else:
        print(W,"The correct answer is A")
        Point-=1
    print("""Q4 The chip used in computers,is made of
          A.Silicon
          B.Iron Oxide
          C.Chronium
          D.None of this""")
    D=input("Enter your choice:")
    if D.upper()=="A":
        print(R)
        Point+=4
    else:
        print(W,"The Answer is A")
        Point-=1
    print("""Q5 FORTRAN stans for
          A.Formal Translator
          B.Formative Translation
          C.Formal Transaction
          D.Formula Translation""")
    E=input("Enter your choice:")
    if E.upper()=="D":
        print(R)
        Point+=4
    else:
        print(W,"The correct answer is D")
        Point-=1
    print("""Q6 C programming language was devloped by..
          A.Charles Babbage
          B.Larry Wall
          C.James Gosling
          D.Dennis Ritchie""")
    F=input("Enter your choice")
    if F.upper()=="D":
        print(R)
        Point+=4
    else:
        print(W,"The correct answer is D")
        Point-=1
    print("""Q7 Which of the following commands is used in MS-Word to underline the statement..
          A. Underline
          B. U
          C. I
          D. P""")
    G=input("Enter your choice")
    if G.upper()=="B":
        print(R)
        Point+=4
    else:
        print(W,"The correct answer is B")
        Point-=1
    print("""Q8 Which of the following should be used to move a paragraph from one place to another
    in a word document?
          A.Copy and Paste
          B.Cut and Paste
          C.Delete and retype
          D.Find and replace""")
    H=input("Enter your choice:")
    if H.upper()=="B":
        print(R)
        Point+=4
    else:    
        print(W,"The correct answer is B")
        Point-=1
    print("""Q9 To Protect yourself from computer hacker intrusions,
          you should install a....
          A.Firewall
          B.Mailer
          C.Macro
          D.Script""")
    I=input("Enter your choice:")
    if I.upper()=="A":
        print(R)
        Point+=4
    else:
        print(W,"The correct answer is A")
        Point-=1
    print("""Q10 Which Software is used to make a presentation ?
          A.Microsoft Excel
          B.Microsoft Word
          C.Microsoft Power Point
          D.Microsoft Access""")
    J=input("Enter your choice:")
    if J.upper()=="C":
        print("Correct,with this we have completed our 10 question pop quiz")
        Point+=4
    else:
        print(W,"The correct answer is C")
        Point-=1
    print("Your total point is",Point)
    A1=input("Do you want to try this quiz again(Yes/No):")
    if A1.upper()=="YES":
        print("Thanks for Playing Goodbye!,Keep Practicing.")
    else:
        print("Play again some other time..")
        break
    
    
    



   
 


    


    






    
          
          
          
