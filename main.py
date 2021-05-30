from tkinter import *

import random



names = []
global questions_answers
asked=[]
score=0

questions_answers = {

  1:['You are handed the responsibility playing the music at a party, Which song are you playing first?','California love by Tupac','Take o Me by A-ha', 'Sky by Playboi Carti', 'Levitating by Dua Lipa'],
  2:['If you were given $25,000 and a plane ticket to any destination of your choice, which location would you pick?','Bali','Japan', 'Greece','Paris'],
  3:['What is your favourite Genre (Movie/Series wise)','Action', 'Horror', 'Comdey', 'A little bit of everything'],
  4:['Who knows you the best?','No one', 'My parent(s)','A sibling', 'A friend'],
  5:['What is the thing you would never say to another person?','Comment n the way they look','Comment on their past/personal life', 'Comment on their career decisions','Swear at them'],
  6:['What is your greatest achievement?','Having loving Friends and or Family', 'Exceeding with good grades',''],
  7:['If something in your house breaks, what is the first thing you do?','Try fix it on my own', 'Hide the evidence from your parents','Call someone to help you', 'Cry'],
  8:['Pick a favourite childhood classic..','Pokemon','Adventure time','Rug rats','Blues clues'],
  9:['What your favourite game as a kid?', 'Tag', 'Hide and Seek','Spotlight','Musical chairs'],
  10:['What do you prefer?','A book','A movie', 'A theater'],

}


class Quiz:
    def __init__(self, parent):#constructor, The __init__() function is called automatically every time the class is being used to create a new object.
 
        background_color="#6bbf59"# to set it as background color for all the label widgets

        #frame set up
        self.quiz_frame=Frame(parent, bg = background_color, padx=50, pady=50)
        #padx, pady How many pixels to pad widget, horizontally (x) and vertically (y), outside widget's borders.
        self.quiz_frame.grid()#This geometry manager organizes widgets in a table-like structure in the parent widget.
               
        #widgets goes below
        self.heading_label = Label(self.quiz_frame, text="Which Celebrity fits your personality?", font=("Comfortaa","18","bold"),bg=background_color,fg="#FFFFFF")
        self.heading_label.grid(column=0 ,row=0, padx=20)
        self.var1=IntVar() #holds value of radio buttons
        
        #label for name
        self.user_label = Label(self.quiz_frame, text="Name ", font=("Comfortaa","16","bold"),bg= background_color,fg="#FFFFFF")
        self.user_label.grid(column=0, row=1,)
      
        
        #entry box
        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid(row=3,column=0)
        
        

         #label for age
        self.user_label2 = Label(self.quiz_frame, text="Age ", font=("Comfortaa","16", "bold"),bg=background_color,fg="#FFFFFF")
        self.user_label2.grid(row=4,column=0) 
        
        #entry box
        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid(row=5)
        
        #continue button
        self.continue_button = Button(self.quiz_frame, text="Start", font=("Comfortaa", "13", "bold"), bg="#fff2cc",command=self.name_collection)
        self.continue_button.grid(row=6,padx=10,pady=10)   

        #cancel button
        self.cancel_button = Button(self.quiz_frame, text="Cancel", font=("Comfortaa", "13", "bold"), bg="#ea9999", command=self.name_collection)
        self.cancel_button.grid(row=7,column=0)

        
        #image
        #logo = PhotoImage(file="road.gif")
        #self.logo = Label(self.quiz_frame, image=logo)  
        #self.logo.grid(row=4,padx=20, pady=20) 
       

    def name_collection(self):
        name=self.entry_box.get()
        names.append(name) #add name to names list declared at the beginning
        self.continue_button.destroy()
        self.entry_box.destroy() #Destroy name frame then open the quiz runner
      
           

if __name__ == "__main__":
    root = Tk()
    root.title("Which celebrity fits your personality?") 

    quiz_instance = Quiz(root) #instantiation, making an instance of the class Quiz
    root.mainloop()#so the frame doesnt dissapear
 
    
"""Whenever the Python interpreter reads a source file, it does two things:

it sets a few special variables like __name__, and then
it executes all of the code found in the file.

If you are running your module (the source file) as the main program, e.g. guiQuizPart1.py
the interpreter will assign the hard-coded string "__main__" to the __name__ variable

https://www.youtube.com/watch?v=sugvnHA7ElY

"""

