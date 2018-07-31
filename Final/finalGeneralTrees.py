import tkinter as tk
import ListNode

num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]


class genTrees(tk.Tk):
	
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		
		win = tk.Frame(self)
		win.pack(side='top', fill='both', expand=True)
		
		win.grid_columnconfigure(0, weight=1)
		win.grid_rowconfigure(0, weight=1)
		
		self.frames = {}
		
		for f in (StartPage, NextPage):
			
			frame = f(win, self)
			self.frames[f] = frame
			frame.grid(column=0, row=0, sticky='NEWS')
			self.show_frames(f)
		
	def show_frames(self, cont):
		frame = self.frames[cont]
		frame.tkraise()
		
class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		L = tk.Label(self, text='Start', font='Verdana 18 bold')
		L.pack()

		
		oM = tk.OptionMenu(self, num[0], *num)
		oM.pack()

	
		c = tk.Listbox(self)
		c.pack(anchor="cent")
		
		b = tk.Button(self, text='Next', command= lambda: controller.tree(3))
		b.pack(anchor="s")

class NextPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		L = tk.Label(self, text='This is a possible word generator', font='Verdana 18 bold')
		L.pack()
		b = tk.Button(self, text='Generator', command= lambda: controller.show_frames(StartPage))
		b.pack()

class triTree:

    def __init__(self, size = None):
        self.size = size
        self.node = ListNode()

    def shuff(self, a):
        for i in range(len(a)):
            yield i
        
    def tree(self):
        
        size = self.size
     
        for a in range(size):        
            node = self.node
            left = node.left
            mid = node.mid
            right = node.right

            for char in alpha[:size]:
                
                                    
                node.left = ListNode(char + alpha[a])
                left = node.left
                   
                    
                node.mid = ListNode(char + alpha[a])
                mid = node.mid
                
                
                node.right = ListNode(char + alpha[a])
                right = node.right
                       
                print(left.item, mid.item, right.item)
 

c = genTrees()
c.mainloop()
