import random,sqlite3,pyperclip


import tkinter.messagebox
from tkinter import *
from tkinter import filedialog




window=Tk()
window.title('Program')
window.geometry('600x600')






letters=[' ','α','β','γ',
         'δ','ε','ζ','η','θ','ι','κ','λ','μ','ν','ξ','ο','π','ρ',
         'σ','τ','υ','φ','χ','ψ','ω','ς','Α','Β','Γ','Δ','Ε','Ζ','Η','Θ','Ι','Κ','Λ','Μ','Ν','Ξ','Ο','Π','Ρ',
         'Σ','Τ','Υ','Φ','Χ','Ψ','Ω',
         'a','b','c','d',
         'e','f','g','h','i','j','k','l','m','n','o','p','q','r',
         's','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
         'R','S','T','U','V','W','X','Y','Z',
         'ά','έ','ή','ί',
         'ό','ύ','ώ','ϊ','1','2','3','4','5','6','7','8','9','0',
         '!','@','#','$',
         '%','^','&','*','(',')','.',',','/'
         ]


          

#-------------------------CODING---------------------------------------------------------------------------------------------


def copy():
          pyperclip.copy(p)
          tkinter.messagebox.showinfo('Notice','Your code is copied at clipboard')



def enr():
          global texti
          global name
          texti=name.get()
          ent()                    

def enc():
          global name
          name=StringVar()
          box=Entry(window,textvariable=name,width='60').place(x=150,y=150)

          lable7=Label(window,text='Place Your Text Here:').place(x=30,y=150)

          button=Button(window,text='DONE',command=enr).place(x=250,y=180)
          
def ent():
          global texti,p
          text=[]
          code=[]
          final=[]
          test=[]
          numbers=[]
          for i in range (len(texti)):
                    text.append(texti[i])
          for i in range (0,133):
                    numbers.append(i)
          for i in range(0,133):
                    x=random.choice(numbers)
                    code.append(x)
                   
                    for z in range(len(numbers)):
                             
                              if x==numbers[z]:
                                        u=z
                                        
                    del numbers[u]
          
          for i in range(len(text)):
                    for j in range(len(letters)):
                              if text[i]==letters[j]:
                                        final.append(code[j])


                                        
          for i in range (len(final)):
                              test.append(letters[final[i]])
          p=''
          for i in range(len(test)):
                    p=p+test[i]
          for i in range(0,133):
                    
                    p=p+letters[code[i]]
          lable3=Label(window,text='The Code is:').pack(side=LEFT)
          lable3=Label(window,text=p,width='60').pack(side=LEFT,fill=X)
          button5 =Button(window,text='COPY',command=copy).place(x=280,y=280)
          
          
#----------------------DECODING--------------------------------------------------                       
opened=False        
def dec():
          global p2,p,opened
          coded=[]
          code1=[]
          code2=[]
          final2=[]
          ans=[]
          numbers=[]
          try:
                    x=p
          except Exception:
                    tkinter.messagebox.showinfo('WARNING','You did not copy or open a text')
                    
          if not opened == True:
                    p=pyperclip.paste()
          else:
                    opened==False
          lable7=Label(window,text='Your Decode Code is :').place(x=25,y=340)
          lable8=Label(window,text=p).place(x=200,y=340)
#----------------------------------------------------------------------------------

                    
#-------HEART----------------------------------------------------------------------
          for i in range(-133,0):
                    coded.append(p[i])

          for i in range (0,133):
                    for j in range(0,133):
                              if coded[i]==letters[j]:
                                        code1.append(j)
          for i in range(len(p)-133):
                    code2.append(p[i])
          for i in range(len(code2)):
                    for j in range (0,133):
                              if code2[i]==letters[j]:
                                        final2.append(j)          
          p2=''
          for i in range(len(final2)):
                    for j in range(0,133):
                             if final2[i]==code1[j]:
                                       q=j
                    
          
                    ans.append(letters[q])
          for i in range(len(ans)):
                    p2=p2+ans[i]                    

          lable11=Label(window,text='Final Text :',font=(20)).place(x=150,y=390)          
          lable10=Label(window,text=p2,font=(15)).place(x=150,y=460)
          opened=False
#-----------------------------------------------------------------------------------


#                        ---USER-----------





def user():
          userwn=Tk()
          userwn.title('User')

          
          userwn.geometry('300x200')
          connection=sqlite3.connect('test2.db')
          cursor=connection.cursor()
          cursor.execute('CREATE TABLE IF NOT EXISTS test2(username TEXT,password REAL)')
          
          
          
          
          
          
          def ent():
                    global t1,t2
                    t1=usus.get()
                    t2=paspas.get()
                    print(t1,t2,'k')         
                    cursor.execute('INSERT INTO test2 (username,password) VALUES(?,?)',(t1,t2))
                    connection.commit()
                    cursor.close()
                    connection.close()
          


          usus=StringVar()
          paspas=StringVar()
          heading=Label(userwn,text='Create a User !',font=('arial',20,'bold')).pack()
          label_user=Entry(userwn,textvariable=usus).pack()
          
          label_pass=Entry(userwn,textvariable=paspas).pack()

          ent=Button(userwn,text='Enter',command=ent()).pack()
          



          
          
          
          




          
#                       --------------------

def close():
          
          quit()

def save():
          print('g')
def op():
          global p,opened
          window.file=filedialog.askopenfilename()
          f=open(window.file,'r')
          p=f.read()
          f.close()
          opened=True
          tkinter.messagebox.showinfo('Notify','Your file was opened')
          dec()


#----------------------MENU-----------------------------------------------------------------          

menu=Menu(window)

window.config(menu=menu)

subm=Menu(menu)
subm1=Menu(menu)

menu.add_cascade(label='File',menu=subm)


subm.add_command(label='Open',command=op)
subm.add_command(label='Save',command=save)
subm.add_separator()
subm.add_command(label='Quit',command=close)

menu.add_cascade(label='User',menu=subm1)
subm1.add_command(label='Create User',command=user)


#--------------------------------------------------------------------------------------------------




          
heading=Label(window,text='Welcome !',font=('arial',35,'bold')).pack()
copy_rights=Label(window,text='Copyrights by Dimitris Tramanztas',bd=1,
                  relief=SUNKEN,anchor=W).pack(side=BOTTOM,fill=X)



            
button=Button(window,text='Code',command=enc,width='30').pack()
button1=Button(window,text='DeCode',command=dec,width='30').pack()

window.mainloop()        
         
                  
          









