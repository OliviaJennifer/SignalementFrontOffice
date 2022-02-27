# Python program to create a table

from tkinter import *

from Materiel import Materiel


class Table:

    def __init__(self, root):

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial', 16, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])


# take the data


if __name__ == '__main__':
    m=Materiel
    lst = m.getListeM(m)

    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = 6

    # create root window
    root = Tk()
    t = Table(root)
    root.mainloop()
