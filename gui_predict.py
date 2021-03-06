from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.toolsThickness = 10
        self.rgb = "#%02x%02x%02x" % (255, 0, 0)
        self.coordinates = []

        self.pack(expand=1, fill=BOTH)
        self.createWidgets()

        master.bind('+', self.thicknessPlus)
        master.bind('-', self.thicknessMinus)

    def createWidgets(self):
        tk_rgb = "#%02x%02x%02x" % (128, 192, 200)

        self.leftFrame = Frame(self, bg=tk_rgb)
        self.leftFrame.pack(side=LEFT, fill=Y)

        # -----------------------------------------------
        self.entryFrame = Frame(self.leftFrame)
        self.entryFrame.grid(row=1, column=0,
                             sticky=NW, pady=20, padx=3)

        Button(self.leftFrame,text='Select Color', command=self.set_Color).grid(row=1, column=0,
                             sticky=NW, pady=20, padx=3)


        # ----------------------------------------------

        self.labelThickness = Label(
            self.leftFrame,
            text="line thickness:")
        self.labelThickness.grid(row=3,
                                 column=0, pady=5 , padx=3,sticky=NW)

        self.myScale = Scale(
            self.leftFrame, from_=1, to=25,
            orient=HORIZONTAL,
            command=self.setThickness
        )
        self.myScale.set(self.toolsThickness)
        self.myScale.grid(
            row=4, column=0,
            pady=20, padx=20, sticky=S,
        )

        Button(self.leftFrame, text='dismiss', command=self.dismiss).grid(row=5, column=0, sticky=NW, pady=5, padx=3)
        Button(self.leftFrame, text='Predict', command=self.predict).grid(row=6, column=0, sticky=NW, pady=5, padx=3)

        # ----------------------------------------------------------------------
        self.myCanvas = Canvas(self, width=800,
                               height=500, relief=RAISED, borderwidth=5)
        self.myCanvas.pack(side=RIGHT,expand=1, fill=BOTH)
        self.myCanvas.bind("<B1-Motion>", self.draw)
        self.myCanvas.bind("<Button-1>", self.setPreviousXY)
        #self.myCanvas.bind("<ButtonRelease-1>", self.buttonReleased)

    # ----------------------------------------------------------------------
    def setThickness(self, event):
        print(self.myScale.get())
        self.toolsThickness = self.myScale.get()

    def setPreviousXY(self, event):
        print("now")
        self.previousX = event.x
        self.previousY = event.y

    def draw(self, event):
        self.myCanvas.create_line(self.previousX, self.previousY,
                                      event.x, event.y,
                                      width=self.toolsThickness,
                                      fill=self.rgb)
        self.previousX = event.x
        self.previousY = event.y
        self.coordinates.append([self.previousX, self.previousY])



    def delteAll(self):
        self.myCanvas.delete("all")

    def thicknessPlus(self, event):
        if self.toolsThickness < 25:
            self.toolsThickness += 1
            self.myScale.set(self.toolsThickness)

    def thicknessMinus(self, event):
        if 1 < self.toolsThickness:
            self.toolsThickness -= 1
            self.myScale.set(self.toolsThickness)

    def set_Color(self):
        color = askcolor()
        self.rgb=(color[1])

    def dismiss(self):
        print(self.coordinates)
        # complete this function
        #pass the coordinates list to the hmm classifier
        #pop up message with the returned gesture class
        self.delteAll()
        self.coordinates = []

    def predict(self):
        messagebox.showinfo("Predicted gesture", "class:")


root = Tk()
root.title("Draw")
app = Application(root)
root.mainloop()
