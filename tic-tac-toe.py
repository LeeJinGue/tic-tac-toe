from tkinter import *
def printWinner():
     if player=="X":
           print("Winner : O")
     elif player=="O":
           print("Winner : X")
     quit()
​
def winLost():
     if list[0]["text"] == list[1]["text"] == list[2]["text"] != "     ":
           printWinner()
     elif list[3]["text"] == list[4]["text"] == list[5]["text"] != "     ":
           printWinner()
     elif list[6]["text"] == list[7]["text"] == list[8]["text"] != "     ":
           printWinner()
     elif list[0]["text"] == list[3]["text"] == list[6]["text"] != "     ":
           printWinner()
     elif list[1]["text"] == list[4]["text"] == list[7]["text"] != "     ":
           printWinner()
     elif list[2]["text"] == list[5]["text"] == list[8]["text"] != "     ":
           printWinner()
     elif list[0]["text"] == list[4]["text"] == list[8]["text"] != "     ":
           printWinner()
     elif list[2]["text"] == list[4]["text"] == list[6]["text"] != "     ":
           printWinner()
​
def checked(i) :
      global player
      button = list[i]

      if button["text"] != "     " :
            return
      button["text"] = player 
      button["bg"] = "yellow"

      if player == "X" :
            player = "O"
            button["bg"] = "yellow"
      else :
            player = "X"
            button["bg"] = "lightgreen"

window = Tk()
player = "X"
list= []

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)

window.mainloop()


