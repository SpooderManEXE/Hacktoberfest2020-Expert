from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import colorchooser
root=Tk()
root['bg']='#ffd800'
root.title('Naughts And Crosses')
root.iconbitmap('C:/TicTacToe/icon.ico')
#x begins the game
x_player=True
#count to check for tie
count=0
#list to keep the score
final_score=[0,0]
def colour_change():
	chosen_color=colorchooser.askcolor()[1]
	b1.config(fg='Black',bg=chosen_color)
	b2.config(fg='Black',bg=chosen_color)
	b3.config(fg='Black',bg=chosen_color)
	b4.config(fg='Black',bg=chosen_color)
	b5.config(fg='Black',bg=chosen_color)
	b6.config(fg='Black',bg=chosen_color)
	b7.config(fg='Black',bg=chosen_color)
	b8.config(fg='Black',bg=chosen_color)
	b9.config(fg='Black',bg=chosen_color)
def disable_buttons():
	b1.config(state=DISABLED)
	b2.config(state=DISABLED)
	b3.config(state=DISABLED)
	b4.config(state=DISABLED)
	b5.config(state=DISABLED)
	b6.config(state=DISABLED)
	b7.config(state=DISABLED)
	b8.config(state=DISABLED)
	b9.config(state=DISABLED)

def score(winner):
	global final_score
	if win_player=='X':
		messagebox.showinfo('WE HAVE A WINNER!','Player X Has Won!')
		#player x score incremented
		final_score[0]+=1
		player_x_score.config(text=str(final_score[0]))
	elif win_player=='O':
		messagebox.showinfo('WE HAVE A WINNER!','Player O Has Won!')
		#player o score incremented
		final_score[1]+=1
		player_o_score.config(text=str(final_score[1]))	

def when_clicked(b):
	global x_player,count,winner,win_player
	if b['text']=='' and x_player==True:
		b['text']='X'
		count+=1
		x_player=False
		winner=False
		win_player=''
		if win_check_x(b1['text'],b2['text'],b3['text']):			
			winner=True
			win_player='X'
			disable_buttons()
		elif win_check_x(b4['text'],b5['text'],b6['text']):
			winner=True
			win_player='X'
			disable_buttons()
		elif win_check_x(b7['text'],b8['text'],b9['text']):
			winner=True
			win_player='X'
			disable_buttons()
		elif win_check_x(b1['text'],b4['text'],b7['text']):
			winner=True
			win_player='X'
			disable_buttons()
		elif win_check_x(b2['text'],b5['text'],b8['text']):
			winner=True
			win_player='X'
			disable_buttons()
		elif win_check_x(b3['text'],b6['text'],b9['text']):
			winner=True
			win_player='X'
			disable_buttons()
		elif win_check_x(b1['text'],b5['text'],b9['text']):
			winner=True
			win_player='X'
			disable_buttons()
		elif win_check_x(b3['text'],b5['text'],b7['text']):
			winner=True
			win_player='X'
			disable_buttons()
		if count==9 and winner==False:
			messagebox.showinfo('The Game Is Tied!','It Is A Tie!')
			disable_buttons()	
	elif b['text']=='' and x_player==False:
		b['text']='O'
		count+=1
		x_player=True
		winner=False
		if win_check_o(b1['text'],b2['text'],b3['text']):
			o=win_check_o(b1['text'],b2['text'],b3['text'])
			winner=True
			win_player='O'
			disable_buttons()
		elif win_check_o(b4['text'],b5['text'],b6['text']):
			winner=True
			win_player='O'
			disable_buttons()
		elif win_check_o(b7['text'],b8['text'],b9['text']):
			winner=True
			win_player='O'
			disable_buttons()
		elif win_check_o(b1['text'],b4['text'],b7['text']):
			winner=True
			win_player='O'
			disable_buttons()
		elif win_check_o(b2['text'],b5['text'],b8['text']):
			winner=True
			win_player='O'
			disable_buttons()
		elif win_check_o(b3['text'],b6['text'],b9['text']):
			winner=True
			win_player='O'
			disable_buttons()
		elif win_check_o(b1['text'],b5['text'],b9['text']):
			winner=True
			win_player='O'
			disable_buttons()
		elif win_check_o(b3['text'],b5['text'],b7['text']):
			winner=True
			win_player='O'
			disable_buttons()
		if count==9 and winner==False:
			messagebox.showinfo('The Game Is Tied!','It Is A Tie!')
			disable_buttons()				
	else:
		messagebox.showerror('Space Occupied','Looks Like That Space Is Occupied!')	
	return win_player
	win_player=when_clicked()	

def win_check_x(*lis):
	if lis[0]=='X' and lis[1]=='X' and lis[2]=='X':
		return True
def win_check_o(*lis):
	if lis[0]=='O' and lis[1]=='O' and lis[2]=='O':
		return True		

def reset():
	#buttons assignment
	global b1,b2,b3,b4,b5,b6,b7,b8,b9
	b1=Button(root,text='',height=4,width=7,fg='#ffd800',bg='Black',command=lambda:score(when_clicked(b1)))
	b2=Button(root,text='',height=4,width=7,fg='#ffd800',bg='Black',command=lambda:score(when_clicked(b2)))
	b3=Button(root,text='',height=4,width=7,fg='#ffd800',bg='Black',command=lambda:score(when_clicked(b3)))
	b4=Button(root,text='',height=4,width=7,fg='#ffd800',bg='Black',command=lambda:score(when_clicked(b4)))
	b5=Button(root,text='',height=4,width=7,fg='#ffd800',bg='Black',command=lambda:score(when_clicked(b5)))
	b6=Button(root,text='',height=4,width=7,fg='#ffd800',bg='Black',command=lambda:score(when_clicked(b6)))
	b7=Button(root,text='',height=4,width=7,fg='#ffd800',bg='Black',command=lambda:score(when_clicked(b7)))
	b8=Button(root,text='',height=4,width=7,fg='#ffd800',bg='Black',command=lambda:score(when_clicked(b8)))
	b9=Button(root,text='',height=4,width=7,fg='#ffd800',bg='Black',command=lambda:score(when_clicked(b9)))
	#gridding the buttons
	b1.grid(row=0,column=0,ipadx=10,ipady=10)
	b2.grid(row=0,column=1,ipadx=10,ipady=10)
	b3.grid(row=0,column=2,ipadx=10,ipady=10)
	b4.grid(row=1,column=0,ipadx=10,ipady=10)
	b5.grid(row=1,column=1,ipadx=10,ipady=10)
	b6.grid(row=1,column=2,ipadx=10,ipady=10)
	b7.grid(row=2,column=0,ipadx=10,ipady=10)
	b8.grid(row=2,column=1,ipadx=10,ipady=10)
	b9.grid(row=2,column=2,ipadx=10,ipady=10)

#score frame
global player_x_score,player_o_score,score_frame,player_x_label,player_o_label,player_x_score,player_o_score,reset_button
score_frame=LabelFrame(root,fg='black',bg='#ffd800',text='SCORE',padx=50,pady=10)
player_x_label=Label(score_frame,fg='black',bg='#ffd800',text='PLAYER X:')
player_o_label=Label(score_frame,fg='black',bg='#ffd800',text='PLAYER O:')
player_x_score=Label(score_frame,fg='black',bg='#ffd800',text='')
player_o_score=Label(score_frame,fg='black',bg='#ffd800',text='')
reset_button=Button(score_frame,fg='black',bg='#ffd800',text='RESET',command=reset)
reset_button.grid(row=2,column=3)
player_o_score.grid(row=1,column=4)
player_x_score.grid(row=0,column=4)
player_x_label.grid(row=0,column=3)
player_o_label.grid(row=1,column=3)
score_frame.grid(row=0,column=4,rowspan=3,columnspan=2,padx=10,pady=10)
#menu bar
main_menu=Menu(root)
root.config(menu=main_menu)
#creating main menu item
menu_item=Menu(main_menu)
main_menu.add_cascade(label='File',menu=menu_item)
menu_item.add_command(label='Restart',command=reset)
menu_item.add_separator()
menu_item.add_command(label='Exit',command=root.quit)
#creating edit menu item
edit_menu=Menu(main_menu)
main_menu.add_cascade(label='Edit',menu=edit_menu)
edit_menu.add_command(label='Change Colour',command=colour_change)


reset()

root.mainloop()
