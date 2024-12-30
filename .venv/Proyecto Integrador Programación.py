#Código para hacer problemas de cinemática en física
#El propósito es resolver los problemas en los libros de física, mediante las fórmulas previamente establecidas.

# Importamos todas las librerías necesarias, trabajaré con tres, una para hacer la interfaz y otra para hacer las gráficas.
from tkinter import *
from tkinter import font
import tkinter as tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Hacemos la interfaz para tkinter
root = Tk()
root.title("Kinematic problem solver")

#I feel the file was ignored, i didnt know that was possible


#Establecemos el formato para la ventana
font = font.Font(family="Copperplate Gothic Light", size=10)
root.option_add("*Font", font)
root.config(bg="#51688A")
 # Default font for all widgets
root.option_add("*Foreground", "white")           # Default text color for all widgets
root.option_add("*Background", "#51688A")    # Default background color for all widgets (like labels)
root.option_add("*Button.Background", "#51688A")  # Specific background for buttons
root.option_add("*Button.Foreground", "white")      # Specific text color for buttons
root.option_add("*Entry.Background", "black")


#Variables con las que trabajaré y deberé asignar.
variables = ["vo", "vf", "d", "t", "a", "r", "o", "h", "Clear"]

#Validating entries code
def validate_float(input_value):
  # Allow empty input (for deleting characters)
  if input_value == "":
    return True
  # Check if the input is a valid float
  try:
    float(input_value)
    return True
  except ValueError:
    return False

#Código para permitir no más que números float en las entradas
vcmd = (root.register(validate_float), '%P')

#Entries and labels (Frame 1)
frame1 = tk.Frame(root)
frame1.option_add("*Font", font)
frame1.grid(row=0, column=0, padx=10, pady=10, sticky='NESW')

label1 = Label(frame1, text="Enter the variables you know", font=("Copperplate Gothic Bold", 20, "bold"))
label1.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky = 'NESW')

d_Label = Label(frame1, text='[d] Displacement (meters)')
d_Label.grid(row=1, column =0, columnspan=1, padx=10, pady=2, sticky = 'NESW')
d_entry=Entry(frame1, borderwidth=5, validate='key', validatecommand=vcmd, width=6)
d_entry.grid(row=1, column=1, columnspan=1, padx=10, pady=2, sticky = 'NESW')

vo_Label = Label(frame1, text='[vo] Velocity (meters per second)')
vo_Label.grid(row=2, column =0, columnspan=1, padx=10, pady=2, sticky='NEWS')
vo_Label.grid(row=2, column =0, columnspan=1, padx=10, pady=2, sticky='NEWS')
vo_entry=Entry(frame1, borderwidth=5, validate='key', validatecommand=vcmd, width=6)
vo_entry.grid(row=2, column=1, columnspan=1, padx=10, pady=2, sticky = 'NESW')

vf_Label=Label(frame1, text='[vf] Final Velocity (meters per second)')
vf_Label.grid(row=3, column =0, columnspan=1, padx=10, pady=2, sticky='NESW')
vf_entry=Entry(frame1, borderwidth=5, validate='key', validatecommand=vcmd, width=6)
vf_entry.grid(row=3, column=1, columnspan=1, padx=10, pady=2, sticky = 'NESW')

a_Label = Label(frame1, text='[a] Acceleration (meters per second squared)')
a_Label.grid(row=4, column =0, columnspan=1, padx=10, pady=2, sticky='NEWS')
a_entry=Entry(frame1, borderwidth=5, validate='key', validatecommand=vcmd, width=6)
a_entry.insert(0, "-9.81")
a_entry.grid(row=4, column=1, columnspan=1, padx=10, pady=2, sticky= 'NESW')

t_Label = Label(frame1, text='[t] Time (seconds)')
t_Label.grid(row=5, column =0, columnspan=1, padx=10, pady=2, sticky='NEWS')
t_Label.grid(row=5, column =0, columnspan=1, padx=10, pady=2, sticky='NEWS')
t_entry=Entry(frame1, borderwidth=5, validate='key', validatecommand=vcmd, width=6)
t_entry.grid(row=5, column=1, columnspan=1, padx=10, pady=2, sticky = 'NESW')
t_entry.insert(0, "10")

yi_Label = Label(frame1, text='[yi] Initial y (m)')
yi_Label.grid(row=6, column =0, columnspan=1, padx=10, pady=2, sticky='NEWS')
yi_Label.grid(row=6, column =0, columnspan=1, padx=10, pady=2, sticky='NEWS')
yi_entry=Entry(frame1, borderwidth=5, validate='key', validatecommand=vcmd, width=6)
yi_entry.grid(row=6, column=1, columnspan=1, padx=10, pady=2, sticky = 'NESW')
yi_entry.insert(0, "0")

r_Label = Label(frame1, text='[r] Reach (meters)')
r_Label.grid(row=1, column =2, columnspan=1, padx=10, pady=2, sticky='NEWS')
r_Label.grid(row=1, column =2, columnspan=1, padx=10, pady=2, sticky='NEWS')
r_entry=Entry(frame1, borderwidth=5, validate='key', validatecommand=vcmd, width=6)
r_entry.grid(row=1, column=3, columnspan=1, padx=10, pady=2, sticky = 'NESW')

h_Label = Label(frame1, text='[h] Height (meters)')
h_Label.grid(row=2, column =2, columnspan=1, padx=10, pady=2, sticky='NEWS')
h_Label.grid(row=2, column =2, columnspan=1, padx=10, pady=2, sticky='NEWS')
h_entry=Entry(frame1, borderwidth=5, validate='key', validatecommand=vcmd, width=6)
h_entry.grid(row=2, column=3, columnspan=1, padx=10, pady=2, sticky = 'NESW')

o_Label = Label(frame1, text='[o] Angle (degrees)')
o_Label.grid(row=3, column =2, columnspan=1, padx=10, pady=2, sticky='NEWS')
o_Label.grid(row=3, column =2, columnspan=1, padx=10, pady=2, sticky='NEWS')
o_entry=Entry(frame1, borderwidth=5, validate='key', validatecommand=vcmd, width=6)
o_entry.grid(row=3, column=3, columnspan=1, padx=10, pady=2, sticky = 'NESW')

vfx_Label = Label(frame1, text='[vx] Velocity X (m/s)')
vfx_Label.grid(row=4, column =2, columnspan=1, padx=10, pady=2, sticky='NEWS')
vfx_Label.grid(row=4, column =2, columnspan=1, padx=10, pady=2, sticky='NEWS')
vfx_entry=Entry(frame1, borderwidth=5, validate='key', validatecommand=vcmd, width=6)
vfx_entry.grid(row=4, column=3, columnspan=1, padx=10, pady=2, sticky = 'NESW')
vfx_entry.insert(0, "10")

vfy_Label = Label(frame1, text='[vy] Velocity Y (m/s)')
vfy_Label.grid(row=5, column =2, columnspan=1, padx=10, pady=2, sticky='NEWS')
vfy_Label.grid(row=5, column =2, columnspan=1, padx=10, pady=2, sticky='NEWS')
vfy_entry=Entry(frame1, borderwidth=5, validate='key', validatecommand=vcmd, width=6)
vfy_entry.grid(row=5, column=3, columnspan=1, padx=10, pady=2, sticky = 'NESW')
vfy_entry.insert(0, "50")

xi_Label = Label(frame1, text='[xi] Initial x (m)')
xi_Label.grid(row=6, column =2, columnspan=1, padx=10, pady=2, sticky='NEWS')
xi_Label.grid(row=6, column =2, columnspan=1, padx=10, pady=2, sticky='NEWS')
xi_entry=Entry(frame1, borderwidth=5, validate='key', validatecommand=vcmd, width=6)
xi_entry.grid(row=6, column=3, columnspan=1, padx=10, pady=2, sticky = 'NESW')
xi_entry.insert(0, "0")

label2=Label(frame1, text="What are we solving?", font=("Copperplate Gothic Bold", 15, "bold"))
label2.grid(row=11, column=0, columnspan=6, padx=10, pady=10, sticky='NESW')

### Funciones de los botones, ecuaciones de cinemática
import math as math

def distance(vo, t, a):
  vo = float(vo)
  t = float(t)
  a = float(a)
  d = (vo * t) + ((a/2) * (t ** 2))
  return d

def distance2(vf, vo, a):
  vo = float(vo)
  vf = float(vf)
  a = float(a)
  d = ((vf ** 2) - (vo ** 2)) / (2 * a)
  return d

def initialvelocity(vf, a, t):
  t = float(t)
  vf = float(vf)
  a = float(a)
  vo = vf -a*t
  return vo

def finalvelocity(vo, t, d):
  vo = float(vo)
  t = float(t)
  d = float(d)
  vf = math.sqrt((vo ** 2) + (2 * 9.81 * d))
  return vf

def finalvelocity2(vo, t, a):
  vo = float(vo)
  t = float(t)
  a = float(a)
  vf = vo + a*t
  return vf

def time(vf, vo, a):
  vf=float(vf)
  vo=float(vo)
  a=float(a)
  if a == 0:
    raise ValueError
  t = ((vf - vo) / a)
  return (t)

def acceleration1(vf, vo, t):
  vf = float(vf)
  vo = float(vo)
  t = float(t)
  a = (vf - vo) / t
  return a

def acceleration2(vf, vo, d):
  vf = float(vf)
  vo = float(vo)
  d = float(d)
  a = ((vf ** 2) - (vo ** 2)) / 2 * d
  return a

def height(vo, o, a):
  vo = float(vo)
  o = float(o)
  a= float(a)
  o = math.sin(math.radians(o))
  h = -((vo * o) ** 2) / (2*a)
  return h

def reach(vo, o, a):
  vo = float(vo)
  o = float(o)
  a = float(a)
  y = (math.sin(math.radians(2 * o)))
  r = ((vo ** 2) * y) / (a)
  return r

def angle(vfy, vfx):
  print("Inserte Vf en x en VO y Vf en y en VF")
  vfy= float(vfy)
  vfx = float(vfx)
  o = math.degrees(math.atan(vfy / vfx))
  return o

#Código para el botón que genera la gráfica
def plot(yi, xi, t, a, vfx, vfy):
  fig = Figure(figsize=(5, 4), dpi=100)
  ax = fig.add_subplot(111)

  vfx = float(vfx)
  a=float(a)
  vfy = float(vfy)
  xi = float(xi)
  yi = float(yi)
  t= int(t)
  y = []
  x = []
  tiempos = []
  salto = int(t / 10) #Los valores que voy a graficar, el tiempo máximo serán 10 segundos
  for i in range(0, t, salto):
    tiempos.append(i)
  print(tiempos)
  for i in range(len(tiempos)):
    t = tiempos[i]
    xf = xi + (vfx * t)
    yf = yi + vfy * t + (a / 2) * (t ** 2)
    x.append(xf)
    y.append(yf)
  ax.plot(x, y, label='Datos')
  ax.axhline(0, color='red', linestyle='--', label='y=0')
  canvas = FigureCanvasTkAgg(fig, master=frame3) #El canvas sirve para mostrar el plot
  canvas.draw() #Llamamos a la función
  canvas.get_tk_widget().grid(row=4, column=0, columnspan=1, padx=10, pady=2, sticky='NEWS')

#Main button functions, un sólo programa que reconoce la función de elección y ejecuta la función según la variable
def button_clicked(var_name):
  #Recuperamos los valores que se hayan escrito en al entrada
  result_string.set('Not possible')
  vo = vo_entry.get()
  t = t_entry.get()
  d = d_entry.get()
  vf = vf_entry.get()
  vfy = vfy_entry.get()
  vfx= vfx_entry.get()
  a = a_entry.get()
  o = o_entry.get()
  yi= yi_entry.get()
  xi = xi_entry.get()

  if var_name==("t"): ##Funtion for time
    if vf and vo:  # Check if there's a value
      t=time(vf, vo, a)
      result_string.set(f"The time from Vo to Vf is {t:.3f} seconds")
      error.set("Try another one")
    else:
      error.set("Enter vf and vo!")

  if var_name==("d"): ##Function for displacement
    if vo and t and a:
      d=distance(vo, t, a)
      result_string.set(f"The distance is {d:.3f} meters")
    elif vf and vo and t:
      d=distance2(vf, vo, a)
      result_string.set(f"The distance is {d:.3f} meters")
    else:
      error.set("Enter [vo, t, and a] or [vf, vo, a]")
#
  if var_name==("vo"): ##Funtion for initial velocity
    if vf and a and t:  # Check if there's a value
      vo=initialvelocity(vf, a, t)
      result_string.set(f"The initial velocity is {vo:.3f} m/s")
      error.set("Try another one")
    else:
      error.set("Enter vf, t, a")
#
  if var_name==("vf"): ##Funtion for final velocity
    if vo and t and d:  # Check if there's a value
      vf=finalvelocity(vo, t, d)
      result_string.set(f"The initial velocity is {vf:.3f} m/s")
      error.set("Try another one")
    elif vo and a and t:
      vf= finalvelocity2(vo, t, a)
      result_string.set(f"The final velocity is {vf:.3f} m/s")
      error.set("Try another one")
    else:
      error.set("Enter vo, t, (d/a)")

  if var_name == ("a"):  ##Funtion for acceleration
    if vo and vf and t:  # Check if there's a value
      a=acceleration1(vf, vo, t)
      result_string.set(f"The acceleration is {a:.3f} m/s")
      error.set("Try another one")
    elif vo and vf and d:  # Check if there's a value
      a=acceleration2(vf, vo, d)
      result_string.set(f"The acceleration is {a:.3f} m/s")
      error.set("Try another one")
    else:
      error.set("Enter vf, vo, and (d or t)")

  elif var_name == ("h"):  ##Funtion for time
    if vo and o and a:  # Check if there's a value
      h = height(vo, o, a)
      result_string.set(f"The height is {h:.3f} m")
      error.set("Try another one")
    else:
      error.set("Enter vo and angle")

  elif var_name == ("r"):  ##Funtion for the maximum reach
    if vo and o and a:  # Check if there's a value
      r = reach(vo, o, a)
      result_string.set(f"The maximum reach is {r:.3f} m")
      error.set("Try another one")
    else:
      error.set("Enter vo, angle and acceleration")

  elif var_name == ("o"):  ##Funtion for the angle
    if vfy and vfx:  # Check if there's a value
      o = angle(vfy, vfx)
      result_string.set(f"The launch angle is {o:.3f} m")
      error.set("Try another one")
    else:
      error.set("Enter Final Vx and Vy")

  elif var_name== ("Clear"):
    clear_text()
    result_string.set(f"Choose an option to start")
    error.set("Cleared")

  elif var_name== ("plot"):
    if yi and xi and t and vfx and vfy and a:
      result_string.set("Plotted!")
      error.set("Try other values")
      plot(yi, xi, t, a, vfx, vfy)
    elif vo and yi and xi and t and a and o:
      result_string.set("Plotted3!")
      error.set("Try other values")
      o = float(o)
      vo =float(vo)
      a= float(a)
      ox = math.cos(math.radians(o))
      vfx = vo*ox
      oy = math.sin(math.radians(o))
      vfy= vo*oy
      print(vfy, vfx)
      plot(yi, xi, t, a, vfx, vfy)
    else:
      error.set("Enter time, acceleration, initial positions\nVo or Vix and Viy")


#Crear botones, usamos un sólo ciclo pero cambiamos el texto de las funciones y
# el comando haciendo que reconozca las variables.
frame2 = Frame(frame1) #Lo pongo en un frame distinto para que se vea balanceado, y acomodar los botones en conjunto.
frame2.option_add("*Font", font)
frame2.grid(row=12, column=0, padx=(100,0), pady=0)
for index, var in enumerate(variables):
    row = index // 3
    col = index % 3
    button = Button(frame2, text=var, width=10, height=2, command=lambda v=var: button_clicked(v))
    button.grid(row=row, column=col, padx=5, pady=5,sticky="NSEW")

#Showcase my results
#RESULTADOS
frame3 = Frame(root) #aquí estoy haciendo un frame a la derecha para que se vea todo.
frame3.option_add("*Font", font)
frame3.grid(row=0, column=1, padx=10, pady=10)

result_string= tk.StringVar()
result_string.set('RESULTS')
result=Label(frame3, textvariable=result_string, font=("Copperplate Gothic Bold", 20, "bold"))
result.grid(row=0, column=0, columnspan=1, padx=10, pady=2, sticky='NEWS')

error= tk.StringVar()
error.set('Choose an option to see what you need')
error_label=Label(frame3, textvariable=error, font=("Copperplate Gothic Light", 15))
error_label.grid(row=2, column=0, columnspan=1, padx=10, pady=2, sticky='NEWS')

#EL botón para la gráfica lo pongo en otro frame para que no se encime
button = Button(frame3, text="PLOT", width=10, height=2, command=lambda: button_clicked("plot"))
button.grid(row=1, column=0, padx=5, pady=5,sticky="NSEW")

#Función para vaciar las entradas.

def clear_text():
  vo_entry.delete("0", tk.END)
  vf_entry.delete("0", tk.END)
  d_entry.delete("0", tk.END)
  t_entry.delete("0", tk.END)
  a_entry.delete("0", tk.END)
  r_entry.delete("0", tk.END)
  o_entry.delete("0", tk.END)
  h_entry.delete("0", tk.END)
  #me falta clear otras variables
  vfx_entry.delete("0", tk.END)
  vfy_entry.delete("0", tk.END)
  xi_entry.delete("0", tk.END)
  yi_entry.delete("0", tk.END)

#Finalmente llamamos al mainloop de la interfaz de tikinter con root
root.mainloop()