#Creator: Donnie Gray
#File: CharDisplay
#Language: Python
#Purpose: This is meant to handle most of the GUI functionality of the program. Object definitions will be elsewhere, but screen settings and button functionality will be here.


from tkinter import *
from tkinter import ttk


charScreen = Tk()
charScreen.title("Dandy Char Sheet: ")

#overFrame is the frame being used for the whole screen
overFrame = ttk.Frame(charScreen, padding = "3 15 300 12")
overFrame.grid(column = 0, row = 0, sticky = (N, W, E, S))
charScreen.columnconfigure(0, weight = 1)
charScreen.rowconfigure(0, weight = 1)
#scale = ttk.Scale(charScreen, resolution = 2)


#Frames in row A: Name, Player, Race, total level
#top row
titleFrame = ttk.Frame(overFrame, padding = 0)
titleFrame.grid(column = 0, row = 0, sticky = (N, W, E, S))

#Add a listener for this box so the title can change when the character name is changed
character = StringVar()
charTxt = ttk.Entry(titleFrame, width = 20, textvariable = character)
charTxt.grid(column = 0, row = 0, sticky = (N, W, E, S))
ttk.Label(titleFrame, text = "Character Name").grid(column = 0, row = 1, sticky = (W, E))


playerFrame = ttk.Frame(overFrame, padding = 0)
playerFrame.grid(column = 1, row = 0, sticky = (N, W, E, S))

player = StringVar()
playTxt = ttk.Entry(playerFrame, width = 20, textvariable = player)
playTxt.grid(column = 0, row = 0, sticky = (N, W, E, S))
ttk.Label(playerFrame, text = "Player Name").grid(column = 0, row = 1, sticky = (W, E))


raceFrame = ttk.Frame(overFrame, padding = 0)
raceFrame.grid(column = 2, row = 0, sticky = (N, W, E, S))

race = StringVar()
raceTxt = ttk.Entry(raceFrame, width = 10, textvariable = race)
raceTxt.grid(column = 0, row = 0, sticky = (N, W, E, S))
ttk.Label(raceFrame, text = "Race").grid(column = 0, row = 1, sticky = (W, E))


lvlFrame = ttk.Frame(overFrame, padding = 0)
lvlFrame.grid(column = 3, row = 0, sticky = (N, W, E, S))

level = StringVar()
lvlTxt = ttk.Entry(lvlFrame, width = 2, textvariable = level)
lvlTxt.grid(column = 0, row = 0, sticky = (N, W, E, S))
ttk.Label(lvlFrame, text = "Total Level").grid(column = 0, row = 1, sticky = (W, E))



#statFrame Start
statFrame = ttk.Frame(overFrame, padding = 0)
statFrame.grid(column = 0, row = 1, sticky = (N, W, E, S))

strS = StringVar()
strFrame = ttk.Frame(statFrame, padding = "5 5 5 5")
strFrame.grid(column = 0, row = 0, sticky = (N, W, E, S))
strTxt = ttk.Entry(strFrame, width = 2, textvariable = strS)
strTxt.grid(column = 0, row = 0, sticky = (N, W, E, S))
ttk.Label(strFrame, text = "STR").grid(column = 0, row = 1, sticky = (W, E))


dex = StringVar()
dexFrame = ttk.Frame(statFrame, padding = "5 5 5 5")
dexFrame.grid(column = 0, row = 1, sticky = (N, W, E, S))
dexTxt = ttk.Entry(dexFrame, width = 2, textvariable = dex)
dexTxt.grid(column = 0, row = 0, sticky = (N, W, E, S))
ttk.Label(dexFrame, text = "DEX").grid(column = 0, row = 1, sticky = (W, E))

con = StringVar()
conFrame = ttk.Frame(statFrame, padding = "5 5 5 5")
conFrame.grid(column = 0, row = 2, sticky = (N, W, E, S))
conTxt = ttk.Entry(conFrame, width = 2, textvariable = con)
conTxt.grid(column = 0, row = 0, sticky = (N, W, E, S))
ttk.Label(conFrame, text = "CON").grid(column = 0, row = 1, sticky = (W, E))

intS = StringVar()
intFrame = ttk.Frame(statFrame, padding = "5 5 5 5")
intFrame.grid(column = 0, row = 3, sticky = (N, W, E, S))
intTxt = ttk.Entry(intFrame, width = 2, textvariable = intS)
intTxt.grid(column = 0, row = 0, sticky = (N, W, E, S))
ttk.Label(intFrame, text = "INT").grid(column = 0, row = 1, sticky = (W, E))

wis = StringVar()
wisFrame = ttk.Frame(statFrame, padding = "5 5 5 5")
wisFrame.grid(column = 0, row = 4, sticky = (N, W, E, S))
wisTxt = ttk.Entry(wisFrame, width = 2, textvariable = wis)
wisTxt.grid(column = 0, row = 0, sticky = (N, W, E, S))
ttk.Label(wisFrame, text = "WIS").grid(column = 0, row = 1, sticky = (W, E))


cha = StringVar()
chaFrame = ttk.Frame(statFrame, padding = "5 5 5 5")
chaFrame.grid(column = 0, row = 5, sticky = (N, W, E, S))
chaTxt = ttk.Entry(chaFrame, width = 2, textvariable = cha)
chaTxt.grid(column = 0, row = 0, sticky = (N, W, E, S))
ttk.Label(chaFrame, text = "CHA").grid(column = 0, row = 1, sticky = (W, E))

#Frame B1 -> skills




#Frame B2 -> HP/Max HP, AC, init, speed

#Frames in row A: Name, Player, Race, total level

#stat bonus = (stat - 10) / 2 (floor)

for child in overFrame.winfo_children():
    child.grid_configure(padx=5, pady=5)


intTxt.focus()

charScreen.mainloop()

