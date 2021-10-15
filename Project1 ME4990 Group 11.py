from tkinter import*
from PIL import ImageTk, Image 
import numpy as np

##############Manometer as a class####################

class Manometer:
  def __init__(self):
    #################Variables###############
    self.root = Tk()  
    self.root.geometry("800x430") 
    self.h1 = IntVar()

    self.h2 = IntVar()
    self.vari = StringVar() 
    self.var = DoubleVar()
    self.sel = StringVar()
    self.photo = PhotoImage(file = r"Capture (1).png")
    self.custom_liquid = IntVar()
    self.dens_label = IntVar()


######################################################

################## GUI Features ########################

    self.title = Label(self.root, text ='Determining the input pressure from a Manometer', font = "100")
    self.title.place(x= 200,y = 1)

    self.sub_title = Label(self.root, text ='Select fluid type and manometer heights \n Press the SI or English button to calculate the pressure')
    self.sub_title.place(x= 225,y = 30)

#left side manometer
    self.left_manometer = Scale( self.root, variable = self.h1, from_ = 999, to = 0,orient = VERTICAL, fg = "black", troughcolor = 'cyan', sliderlength = 5, activebackground = 'blue' ) 
#left manometer location
    self.left_manometer.place(x = 1, y = 151)



#right side manometer
    self.right_manometer = Scale( self.root, variable = self.h2, from_ = 999, to = 0, orient = VERTICAL, fg = "black", troughcolor = 'cyan', sliderlength = 5, activebackground = 'blue') 
#right manometer location
    self.right_manometer.place(x = 105, y = 151)


# using picture of a u tube. Button command is to subtract the left manometer height from the right side  
    self.b2 = Button(self.root, command = self.get_pressure_cel,  image = self.photo)
    self.b2.place(x = 25, y = 255)

# farenheit button
    self.b3 = Button(self.root, command = self.get_pressure_fahren,  text = 'English')
    self.b3.place(x = 25, y = 375)



#label that displays the get_pressure_cel function
    self.l2 = Label(self.root, borderwidth=1, relief="solid")
    self.l2.place(x= 200 , y = 150) 


#label that displays the get_pressure_far function
    self.l3 = Label(self.root, borderwidth=1, relief="solid")
    self.l3.place(x= 200 , y = 150) 


#label above the radio buttons for fluid type selection
    self.fluid_label = Label(self.root, text ='Types of Fluids:', font = "50")
    self.fluid_label.place(x= 200,y = 200)

##label that displays density value
    self.dens_label = Label(self.root)
    self.dens_label.place(x=350, y = 300)


#radio buttons that feed density value to the get_pressure functions

#water
    self.w_button = Radiobutton(self.root, text="Water", variable=self.var, value=998,command=self.info).place(x=200, y = 225)
#oil
    self.o_button = Radiobutton(self.root, text="Oil", variable=self.var, value=640.5,command=self.info).place(x=200,y=250)
#air
    self.a_button = Radiobutton(self.root, text="Air", variable=self.var, value=1.2,command=self.info).place(x=200,y=275)

    self.m_button = Radiobutton(self.root, text="Mercury", variable=self.var, value=13560,command=self.info).place(x=200,y=300)

    self.h_button = Radiobutton(self.root, text="Helium", variable=self.var, value=146.2,command=self.info).place(x=200,y=325)

    self. r_button = Radiobutton(self.root, text="R-134a", variable=self.var, value=1207,command=self.info).place(x=200,y=350)

    self.c_button = Radiobutton(self.root, text="Carbon Dioxide", variable=self.var, value=298,command=self.info).place(x=200,y=375)




################ Functions ####################
#function that gives the pressure reading to the left manometer in celsius 

  def get_pressure_cel(self):
      
    # sel = "Vertical Scale Value = " + str(h1.get()) 
    self.cel = 'The inlet pressure to the left manometer is ' + str(round((self.h1.get() - self.h2.get()) * 9.81 *  (self.var.get())/1000,2)) + ' kPa'
    self.l2.config(text = self.cel, font =("Arial", 13))
    self.l3.config(text = '')

#function that gives the pressure reading to the left manometer in farenheit
  def get_pressure_fahren(self):

    self.farhen = 'The inlet pressure to the left manometer is ' + str(round(((self.h1.get() - self.h2.get()) * 9.81 *  (self.var.get())/1000)/6.895 , 2)) + ' psi'
    self.l3.config(text = self.farhen, font =("Arial", 13)) 
    self.l2.config(text = '')

#function that shows the density value of the selected 
  def info(self):
   self.selection = "The selected fluid has a density of " + str(self.var.get()) + " kg/m^3" + ' or ' + str(round(self.var.get()/16.018463,1)) + ' slug/ft^3'
   self.dens_label.config(text = self.selection)



##Start Program###
Project1 = Manometer()






