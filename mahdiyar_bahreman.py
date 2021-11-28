import sys
from tkinter import *
from tkinter import messagebox

board = Tk()
board.title('CSC-120 Tic Tac Toe')

button_clicked = True
counter = 0

def main():
	global button1, button2, button3, button4, button5, button6, button7, button8, button9
	global button_clicked, counter
	button_clicked = True
	counter = 0

	button1 = Button(board, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: button_click(button1))
	button2 = Button(board, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: button_click(button2))
	button3 = Button(board, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: button_click(button3))

	button4 = Button(board, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: button_click(button4))
	button5 = Button(board, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: button_click(button5))
	button6 = Button(board, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: button_click(button6))

	button7 = Button(board, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: button_click(button7))
	button8 = Button(board, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: button_click(button8))
	button9 = Button(board, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: button_click(button9))

	button1.grid(row=0, column=0)
	button2.grid(row=0, column=1)
	button3.grid(row=0, column=2)

	button4.grid(row=1, column=0)
	button5.grid(row=1, column=1)
	button6.grid(row=1, column=2)

	button7.grid(row=2, column=0)
	button8.grid(row=2, column=1)
	button9.grid(row=2, column=2)

main()

def check_win():
	global winner
	winner = False

	if button1["text"] == "X" and button2["text"] == "X" and button3["text"]  == "X":
		button1.config(bg="red")
		button2.config(bg="red")
		button3.config(bg="red")
		winner = True
		messagebox.showinfo("Game", "X Wins!")
		turnButtonsOff()
	elif button4["text"] == "X" and button5["text"] == "X" and button6["text"]  == "X":
		button4.config(bg="red")
		button5.config(bg="red")
		button6.config(bg="red")
		winner = True
		messagebox.showinfo("Game", "X Wins!")
		turnButtonsOff()

	elif button7["text"] == "X" and button8["text"] == "X" and button9["text"]  == "X":
		button7.config(bg="red")
		button8.config(bg="red")
		button9.config(bg="red")
		winner = True
		messagebox.showinfo("Game", "X Wins!")
		turnButtonsOff()

	elif button1["text"] == "X" and button4["text"] == "X" and button7["text"]  == "X":
		button1.config(bg="red")
		button4.config(bg="red")
		button7.config(bg="red")
		winner = True
		messagebox.showinfo("Game", "X Wins!")
		turnButtonsOff()

	elif button2["text"] == "X" and button5["text"] == "X" and button8["text"]  == "X":
		button2.config(bg="red")
		button5.config(bg="red")
		button8.config(bg="red")
		winner = True
		messagebox.showinfo("Game", "X Wins!")
		turnButtonsOff()

	elif button3["text"] == "X" and button6["text"] == "X" and button9["text"]  == "X":
		button3.config(bg="red")
		button6.config(bg="red")
		button9.config(bg="red")
		winner = True
		messagebox.showinfo("Game", "X Wins!")
		turnButtonsOff()

	elif button1["text"] == "X" and button5["text"] == "X" and button9["text"]  == "X":
		button1.config(bg="red")
		button5.config(bg="red")
		button9.config(bg="red")
		winner = True
		messagebox.showinfo("Game", "X Wins!")
		turnButtonsOff()

	elif button3["text"] == "X" and button5["text"] == "X" and button7["text"]  == "X":
		button3.config(bg="red")
		button5.config(bg="red")
		button7.config(bg="red")
		winner = True
		messagebox.showinfo("Game", "X Wins!")
		turnButtonsOff()
	
	#----------------O----------------

	elif button1["text"] == "O" and button2["text"] == "O" and button3["text"]  == "O":
		button1.config(bg="red")
		button2.config(bg="red")
		button3.config(bg="red")
		winner = True
		messagebox.showinfo("Game", "O Wins!")
		turnButtonsOff()
	elif button4["text"] == "O" and button5["text"] == "O" and button6["text"]  == "O":
		button4.config(bg="red")
		button5.config(bg="red")
		button6.config(bg="red")
		winner = True
		messagebox.showinfo("Game", "O Wins!")
		turnButtonsOff()

	elif button7["text"] == "O" and button8["text"] == "O" and button9["text"]  == "O":
		button7.config(bg="red")
		button8.config(bg="red")
		button9.config(bg="red")
		winner = True
		messagebox.showinfo("Game", "O Wins!")
		turnButtonsOff()

	elif button1["text"] == "O" and button4["text"] == "O" and button7["text"]  == "O":
		button1.config(bg="red")
		button4.config(bg="red")
		button7.config(bg="red")
		winner = True
		messagebox.showinfo("Game", "O Wins!")
		turnButtonsOff()

	elif button2["text"] == "O" and button5["text"] == "O" and button8["text"]  == "O":
		button2.config(bg="red")
		button5.config(bg="red")
		button8.config(bg="red")
		winner = True
		messagebox.showinfo("Game", "O Wins!")
		turnButtonsOff()

	elif button3["text"] == "O" and button6["text"] == "O" and button9["text"]  == "O":
		button3.config(bg="red")
		button6.config(bg="red")
		button9.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
		turnButtonsOff()

	elif button1["text"] == "O" and button5["text"] == "O" and button9["text"]  == "O":
		button1.config(bg="red")
		button5.config(bg="red")
		button9.config(bg="red")
		winner = True
		messagebox.showinfo("Game", "O Wins!")
		turnButtonsOff()

	elif button3["text"] == "O" and button5["text"] == "O" and button7["text"]  == "O":
		button3.config(bg="red")
		button5.config(bg="red")
		button7.config(bg="red")
		winner = True
		messagebox.showinfo("Game", "O Wins")
		turnButtonsOff()

	if counter == 9 and winner == False:
		messagebox.showinfo("Game", "It's a Tie!")
		turnButtonsOff()
				
def button_click(b_utton):
	global button_clicked, counter

	if b_utton["text"] == " " and button_clicked == True:
		b_utton["text"] = "X"
		button_clicked = False
		counter += 1
		check_win()
	elif b_utton["text"] == " " and button_clicked == False:
		b_utton["text"] = "O"
		button_clicked = True
		counter += 1
		check_win()
	else:
		messagebox.showerror("Game", "PICK A DIFFERENT BOX!" )

def turnButtonsOff():
	button1.config(state=DISABLED)
	button2.config(state=DISABLED)
	button3.config(state=DISABLED)
	button4.config(state=DISABLED)
	button5.config(state=DISABLED)
	button6.config(state=DISABLED)
	button7.config(state=DISABLED)
	button8.config(state=DISABLED)
	button9.config(state=DISABLED)

board.mainloop()