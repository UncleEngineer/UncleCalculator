#UncleCalculator.py
from tkinter import *
from tkinter import ttk, messagebox #theme of Tk
import webbrowser

GUI = Tk()
GUI.title('Uncle Calculator V.0.1')
GUI.geometry('800x740')
GUI.iconbitmap('unclecalculator.ico')
#### FONT ####
FONT1 = ('impact',30)
FONT2 = ('Angsana New',20)
FONT3 = ('Angsana New',30,'bold')


###########
menubar = Menu(GUI)
GUI.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label='Exit',command=GUI.quit)
menubar.add_cascade(label='File',menu=filemenu)

mathmenu = Menu(menubar,tearoff=0)
mathmenu.add_command(label='คำนวณความหนาแน่นเหล็ก')
mathmenu.add_command(label='คำนวณพื้นที่สามเหลี่ยม')
mathmenu.add_command(label='ตารางเหล็ก')

menubar.add_cascade(label='Calculate',menu=mathmenu)

def Contact():
	url = 'https://www.facebook.com/UncleEngineer'
	webbrowser.open(url)
def Youtube():
	url = 'https://www.youtube.com/UncleEngineer'
	webbrowser.open(url)

helpmenu = Menu(menubar,tearoff=0)
helpmenu.add_command(label='ติดต่อเรา',command=Contact)
helpmenu.add_command(label='ดูผลงาน',command=Youtube)
menubar.add_cascade(label='Help',menu=helpmenu)
###########



# TAB

Tab = ttk.Notebook(GUI)

T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)

Tab.pack(fill=BOTH,expand=1)

img_t1 = PhotoImage(file='t1.png')
img_t2 = PhotoImage(file='t2.png')
img_t3 = PhotoImage(file='t3.png')


Tab.add(T1,text='คำนวณพื้นที่วงกลม',image=img_t1,compound='left')
Tab.add(T2,text='ปริมาตร',image=img_t2,compound='left')
Tab.add(T3,text='Help',image=img_t3,compound='left')


### TAB1

L = ttk.Label(T1,text='กรุณากรอกรัศมีวงกลม (เมตร)',font=FONT2).pack(pady=10)

v_radius = StringVar() # กรอกเสร็จเก็บจุดนี้

E1 = ttk.Entry(T1,textvariable=v_radius,font=FONT1)
E1.pack(pady=20)
E1.focus()

def Calculate(event=None):
	try:
		unit = 'ตร.ม.'
		radius = float(v_radius.get())
		pi = 3.1416
		calc = pi * (radius**2)
		text = 'วงกลมรัศมี: {} (เมตร) มีพื้นที่ทั้งหมด {:,.2f} {}'.format(radius,calc,unit)
		print(text)
		v_result.set(text)
		v_radius.set('')
	except:
		messagebox.showwarning('กรอกตัวเลข','กรุณากรอกตัวเลขเท่านั้น')
		v_radius.set('')
		E1.focus()


B1 = ttk.Button(T1,text='Calculate',command=Calculate)
B1.pack(ipadx=20,ipady=10)

# Check Enter
E1.bind('<Return>',Calculate)

v_result = StringVar()
v_result.set('----ผลลัพธ์----')
R1 = ttk.Label(T1,textvariable=v_result,font=FONT3,foreground='green')
R1.pack(pady=20)



### TAB2

img = PhotoImage(file='beam.png')
beam_img = ttk.Label(T2,image=img)
beam_img.pack()


L = ttk.Label(T2,text='กรุณากรอกระยะตามภาพ',font=FONT2).pack(pady=10)


FTB = Frame(T2) # FTB = Frame of Table 
FTB.pack()

v_cube1 = StringVar()
v_cube2 = StringVar()
v_cube3 = StringVar()




L = ttk.Label(FTB,text='( 1 )',font=FONT1).grid(row=0,column=0,pady=10,padx=10)
ET21 = ttk.Entry(FTB,textvariable=v_cube1,font=FONT1,width=10)
ET21.grid(row=0,column=1,pady=10)

L = ttk.Label(FTB,text='( 2 )',font=FONT1).grid(row=1,column=0,pady=10,padx=10)
ET22 = ttk.Entry(FTB,textvariable=v_cube2,font=FONT1,width=10)
ET22.grid(row=1,column=1,pady=10)

L = ttk.Label(FTB,text='( 3 )',font=FONT1).grid(row=2,column=0,pady=10,padx=10)
ET23 = ttk.Entry(FTB,textvariable=v_cube3,font=FONT1,width=10)
ET23.grid(row=2,column=1,pady=10)



def CalculateCube(event=None):
	try:
		v1 = float(v_cube1.get())
		v2 = float(v_cube2.get())
		v3 = float(v_cube3.get())
		calc = v1 * v2 * v3
		print(calc)
		text = 'ปริมาตร ({}x{}x{}) ทั้งหมด: {:,.3f} ลบ.ม.'.format(v1,v2,v3,calc)
		v_result2.set(text)
	except:
		messagebox.showwarning('กรอกตัวเลข','กรุณากรอกตัวเลขเท่านั้น')
		v_cube1.set('')
		v_cube2.set('')
		v_cube3.set('')
		ET21.focus()


B2 = ttk.Button(T2,text='Calculate Cube',command=CalculateCube)
B2.pack(ipadx=20,ipady=10)


ET21.bind('<Return>',lambda x:ET22.focus())
ET22.bind('<Return>',lambda x:ET23.focus())
ET23.bind('<Return>',CalculateCube)


v_result2 = StringVar()
v_result2.set('----ปริมาตร----')
R2 = ttk.Label(T2,textvariable=v_result2,font=FONT3,foreground='green')
R2.pack(pady=20)


FL = Frame(T3)
FL.place(x=250,y=250)

L = ttk.Label(FL,text='สนใจพัฒนาฟังชั่นเพิ่มเติม',font=FONT2).pack(pady=10)
L = ttk.Label(FL,text='ติดต่อเพจ: ลุงวิศวกร สอนคำนวณ',font=FONT2).pack(pady=10)


GUI.mainloop()