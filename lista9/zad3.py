import matplotlib.pyplot as plt
import numpy as np
import math

# values
v0 = float(input("Podaj predkosc poczatkowa: "))
alpha = float(input("Podaj kat rzutu: "))
alpha = math.radians(alpha)
g = 9.81
v0x = v0 * math.cos(alpha)
v0y = v0 * math.sin(alpha)


h_max = (v0y**2)/(2*g)
print("Maksymalna wysokosc na jaka wzniesie sie cialo: ", h_max)

x_max = ((v0**2)*math.sin(2*alpha))/g
print("Zasieg rzutu: ", x_max)

time_total = (2*v0*math.sin(alpha))/g
print("Czas całkowity: ", time_total)


time = list(np.arange(0, time_total+0.01, 0.01))
vx_t = [v0x for t in time]
vy_t = [v0y-g*t for t in time]
x_t = [v0x*t for t in time]
y_t = [v0y*t-(g*(t**2)/2) for t in time]
y_x = [(X*math.tan(alpha))-(g*(X**2)/(2*(v0x**2))) for X in x_t]


fig, (p1, p2, p3) = plt.subplots(3)
p1.plot(time, vx_t, time, vy_t)
p1.set(xlabel="t [s]", ylabel="v [m/s]")
p1.legend(["vx(t)", "vy(t)"])
p1.title.set_text("Predkosc chwilowa w kierunku pionowym i poziomym po czasie t")
p1.grid()

p2.plot(time, x_t, time, y_t)
p2.set(xlabel="t [s]", ylabel="x,y [m]")
p2.legend(["x(t)", "y(t)"])
p2.title.set_text("Polozenie od czasu")
p2.grid()

p3.plot(x_t, y_x)
p3.set(ylabel="y [m]", xlabel="x [m]")
p3.title.set_text("Tor rzutu ukosnego")
p3.grid()
plt.tight_layout()
plt.show()
