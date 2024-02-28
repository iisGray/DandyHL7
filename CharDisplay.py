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



#statFrame Start B0
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
skillFrame = ttk.Frame(overFrame, padding = 0)
skillFrame.grid(column = 1, row = 1, sticky = (N, W, E, S))

#add variable to checkbox text later that updates based on current char's total add
acroChk = ttk.Checkbutton(skillFrame, text = "Acrobatics (Dex)")
acroChk.grid(column = 0, row = 0, sticky = (W, E))

ahChk = ttk.Checkbutton(skillFrame, text = "Animal Handling (Wis)")
ahChk.grid(column = 0, row = 1, sticky = (W, E))

arChk = ttk.Checkbutton(skillFrame, text = "Arcana (Int)")
arChk.grid(column = 0, row = 2, sticky = (W, E))

athChk = ttk.Checkbutton(skillFrame, text = "Athletics (Str)")
athChk.grid(column = 0, row = 3, sticky = (W, E))

dcpChk = ttk.Checkbutton(skillFrame, text = "Deception (Cha)")
dcpChk.grid(column = 0, row = 4, sticky = (W, E))

hisChk = ttk.Checkbutton(skillFrame, text = "History (Int)")
hisChk.grid(column = 0, row = 5, sticky = (W, E))

insChk = ttk.Checkbutton(skillFrame, text = "Insight (Wis)")
insChk.grid(column = 0, row = 6, sticky = (W, E))

inmChk = ttk.Checkbutton(skillFrame, text = "Intimidation (Cha)")
inmChk.grid(column = 0, row = 7, sticky = (W, E))

invChk = ttk.Checkbutton(skillFrame, text = "Investigation (Int)")
invChk.grid(column = 0, row = 8, sticky = (W, E))

medChk = ttk.Checkbutton(skillFrame, text = "Medicine (Wis)")
medChk.grid(column = 0, row = 9, sticky = (W, E))

natChk = ttk.Checkbutton(skillFrame, text = "Nature (Int)")
natChk.grid(column = 0, row = 10, sticky = (W, E))

perChk = ttk.Checkbutton(skillFrame, text = "Perception (Wis)")
perChk.grid(column = 0, row = 11, sticky = (W, E))

prfChk = ttk.Checkbutton(skillFrame, text = "Performance (Cha)")
prfChk.grid(column = 0, row = 12, sticky = (W, E))

prsChk = ttk.Checkbutton(skillFrame, text = "Persuasion (Cha)")
prsChk.grid(column = 0, row = 13, sticky = (W, E))

relChk = ttk.Checkbutton(skillFrame, text = "Religion (Int)")
relChk.grid(column = 0, row = 14, sticky = (W, E))

sltChk = ttk.Checkbutton(skillFrame, text = "Sleight of Hand (Dex)")
sltChk.grid(column = 0, row = 15, sticky = (W, E))
#begging for typos here, but we'll see
stlChk = ttk.Checkbutton(skillFrame, text = "Stealth (Dex)")
stlChk.grid(column = 0, row = 16, sticky = (W, E))

surChk = ttk.Checkbutton(skillFrame, text = "Survival (Wis)")
surChk.grid(column = 0, row = 17, sticky = (W, E))

#Frame B2 -> HP/Max HP, AC, init, speed

#Frames in row A: Name, Player, Race, total level

#stat bonus = (stat - 10) / 2 (floor)

for child in overFrame.winfo_children():
    child.grid_configure(padx=5, pady=5)


intTxt.focus()

charScreen.mainloop()

