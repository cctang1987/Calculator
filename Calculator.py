from tkinter import*


main = Tk()
main.title('計算機')

equ = StringVar()
equ.set('0')

def clear():
    equ.set('0')

def Delete():
    print(equ.set(equ.get()[:-1]))
    print(type(equ))
    print(equ)
    print(equ.get())
    #equ.set()[:-1]

def show(buttonstring):
    content = equ.get()
    if content == '0':
        content = ''
    equ.set(content + buttonstring)

def calculate():
    equ.set(eval(equ.get()))



label = Label(main, width = 25, height = 2, relief = 'raised', textvariable = equ)
label.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)

Button(main, text = 'C', width = 5, command = clear).grid(row = 1, column = 0)
Button(main, text = 'DEL', width = 5, command = Delete).grid(row = 1, column = 1)
Button(main, text = '%', width = 5, command = lambda:show('%')).grid(row = 1, column = 2)
Button(main, text = '/', width = 5, command = lambda:show('/')).grid(row = 1, column = 3)
Button(main, text = '7', width = 5, command = lambda:show('7')).grid(row = 2, column = 0)
Button(main, text = '8', width = 5, command = lambda:show('8')).grid(row = 2, column = 1)
Button(main, text = '9', width = 5, command = lambda:show('9')).grid(row = 2, column = 2)
Button(main, text = '*', width = 5, command = lambda:show('*')).grid(row = 2, column = 3)
Button(main, text = '4', width = 5, command = lambda:show('4')).grid(row = 3, column = 0)
Button(main, text = '5', width = 5, command = lambda:show('5')).grid(row = 3, column = 1)
Button(main, text = '6', width = 5, command = lambda:show('6')).grid(row = 3, column = 2)
Button(main, text = '-', width = 5, command = lambda:show('-')).grid(row = 3, column = 3)
Button(main, text = '1', width = 5, command = lambda:show('1')).grid(row = 4, column = 0)
Button(main, text = '2', width = 5, command = lambda:show('2')).grid(row = 4, column = 1)
Button(main, text = '3', width = 5, command = lambda:show('3')).grid(row = 4, column = 2)
Button(main, text = '+', width = 5, command = lambda:show('+')).grid(row = 4, column = 3)
Button(main, text = '0', width = 5, command = lambda:show('0')).grid(row = 5, column = 0, columnspan = 2)
Button(main, text = '.', width = 5, command = lambda:show('.')).grid(row = 5, column = 2)
Button(main, text = '=', width = 5, command = calculate, bg = 'yellow').grid(row = 5, column = 3)

main.mainloop()