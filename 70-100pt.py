#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")

# Create your "enemies" here, before the class


class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "red")
       	    self.up.grid(row=0,column=0)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="left", background= "orange")
       	    self.left.grid(row=0,column=1)
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="right", background= "yellow")
       	    self.right.grid(row=0,column=2)
       	    self.right.bind("<Button-1>", self.rightClicked)
       	    
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="down", background= "green")
       	    self.down.grid(row=0,column=3)
       	    self.down.bind("<Button-1>", self.downClicked)
       	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=RIGHT)
       	    # call the animate function to start our recursion
       	    self.animate()
	
	def animate(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    
	    # Uncomment this when you're ready to test out your animation!
	    #drawpad.after(10,self.animate)
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
		
        def leftClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-20,0)
	   
	def rightClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,20,0)
	   
	def downClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,20)

circle = drawpad.create_oval(10, 10, 50, 50, fill='green')
direction = 1

rectangle = drawpad.create_rectangle(20, 200, 50, 250, fill='black')
direction = 1

square = drawpad.create_rectangle(20, 300, 50, 350, fill='purple')
direction = 1

def animate():
    global direction
    
    x1, y1, x2, y2 = drawpad.coords(circle)
    if x2 > drawpad.winfo_width(): 
        drawpad.move(circle,-800,0)
    elif x1 < 0:
        direction = 10
    
    drawpad.move(circle,direction,0)
    

    x1, y1, x2, y2 = drawpad.coords(rectangle)
    if x2 > drawpad.winfo_width(): 
        drawpad.move(rectangle,-400,0)
    elif x1 < 0:
        direction = 10
    
    drawpad.move(rectangle,direction,0)
    
    x1, y1, x2, y2 = drawpad.coords(square)
    if x2 > drawpad.winfo_width(): 
        drawpad.move(square,-600,0)
    elif x1 < 0:
        direction = 10
    
    drawpad.move(square,direction,0)
    
    drawpad.after(1, animate)
    
animate()



app = MyApp(root)
root.mainloop()