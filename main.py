from tkinter import *

def grey(image: PhotoImage):
    for x in range(image.width()):
        for y in range(image.height()):
            r, g, b = image.get(x, y)
            grey = int((r + g + b) / 4)
            image.put("#%02x%02x%02x" % (grey, grey, grey), (x, y))

window = Tk()

image = PhotoImage(master=window, file="anime.png").zoom(2)
label  = Label(master=window, image=image)
label.pack()

button = Button(master=window, command=lambda: grey(image),
                font=("Arial", 14),
                text="Bearbeiten")
button.pack(fill=X)

window.mainloop()