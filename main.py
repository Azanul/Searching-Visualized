from exponential_search import search as ES

from OFA import *

tk.title("Search Visualized")

generate()

entry = Entry(tk, textvariable=search_val, font=('calibre', 10, 'normal'))

reset = Button(tk, text='Reset', bd='5', command=reset)

btn1 = Button(tk, text='Shuffle', bd='5', command=shuffle)

btn2 = Button(tk, text='Exponential Search', bd='5', command=ES)

entry.place(x=710, y=5)

reset.place(x=710, y=35)

btn1.place(x=710, y=65)

btn2.place(x=710, y=95)

tk.mainloop()
