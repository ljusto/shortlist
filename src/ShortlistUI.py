__author__ = 'Lambert Justo'

from tkinter import *
from tkinter.ttk import *
from src.Link import Link
from src.Entry import Entry
from src.ShortlistQueue import ShortlistQueue

class ShortlistUI(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.SLqueue = ShortlistQueue()
        self.tree = None
        self.root = parent
        self.root.title("Shortlist")
        self.main_pane = PanedWindow(self.root, height=600, width=800, orient=VERTICAL)
        self.main_pane.pack(fill=BOTH, expand=1)
        self.shortlist_pane = PanedWindow(self.main_pane, orient=VERTICAL,
                                     height=500, width=800)
        self.shortlist_canvas = Canvas(self.main_pane)
        self.shortlist_canvas.pack()
        self.shortlist_canvas.grid(row=0, column=0, sticky=N+E+W+S)
        self.main_pane.add(self.shortlist_pane)
        self.button_pane = PanedWindow(self.main_pane, orient=VERTICAL,
                                      height=100, width=800)
        self.main_pane.grid_propagate(False)
        self.main_pane.add(self.button_pane)
        self.render_shortlist_pane()
        self.render_button_pane()

    def on_double_click(self, event):
        try:
            item = self.tree.item(self.tree.focus())
            val = self.SLqueue.fetch_by_text(item['values'][0], True).get_text()
            self.clipboard_clear()
            self.clipboard_append(val)
            self.render_shortlist_pane()
        except IndexError:
            pass
        except TclError:
            pass


    def render_shortlist_pane(self):
        if self.tree is not None:
            self.tree.destroy()
        self.tree = Treeview(self.shortlist_canvas, height=600)
        self.tree["columns"] = ("#1", "#2")
        self.tree.column("#0", width=0)
        self.tree.column("#1", width=400)
        self.tree.column("#2", width=400)
        self.tree.heading("#1", text="Text")
        self.tree.heading("#2", text="Title (if link)")
        for elem in self.SLqueue.get_queue():
            if isinstance(elem, Link):
                self.tree.insert("", 0, text="", values=(elem.get_text(), elem.get_title()))
            else:
                self.tree.insert("", 0, text="", values=(elem.get_text(), elem.get_text()))

        self.tree.bind("<Double-1>", self.on_double_click)
        self.tree.pack()

    def render_button_pane(self):
        add_button = Button(self.button_pane, text="Add to Shortlist", command=self.add_to_shortlist)
        copy_all_selection = Button(self.button_pane, text="Copy all to clipboard", command=self.copy_all)
        # todo: fix button height!
        self.button_pane.add(copy_all_selection)
        self.button_pane.add(add_button)

    def copy_all(self):
        self.clipboard_clear()
        output = ""
        print(self.SLqueue.get_queue())
        while (self.SLqueue.get_queue() != []):
            elem = self.SLqueue.fetch_by_index(len(self.SLqueue.get_queue()) - 1, True) # get the first element
            output += str(elem.get_text()) + "\n"
        self.clipboard_append(output)
        self.render_shortlist_pane()

    def add_to_shortlist(self):
        try:
            text = self.clipboard_get()
            # good enough to check for url
            if ("http" == text[0:4]):
                new = Link(text)
            else:
                new = Entry(text)
            self.clipboard_clear()
            self.SLqueue.push(new)
            self.render_shortlist_pane()
        except TclError:
            print("tcl error by adding to shortlist")

if __name__ == "__main__":
    top = Tk()
    app = ShortlistUI(top)
    top.mainloop()
