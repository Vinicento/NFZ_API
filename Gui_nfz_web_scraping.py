import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from functools import partial

import scrap_functions

print(dir(scrap_functions.basic_searches))


class App:
    def __init__(self, root):
        # setting title
        self.root = root
        self.root.title("undefined")
        # setting window size
        self.start_arguments = []
        self.width = 600
        self.height = 400
        self.screenwidth = root.winfo_screenwidth()
        self.screenheight = root.winfo_screenheight()
        self.alignstr = '%dx%d+%d+%d' % (
        self.width, self.height, (self.screenwidth - self.width) / 2, (self.screenheight - self.height) / 2)
        self.root.geometry(self.alignstr)
        self.root.resizable(width=False, height=False)
        self.root.configure(bg='#ffdfb3')
        self.ft = tkFont.Font(family='Times', size=16, weight='bold')  # Specify font weight as 'bold'

        self.GLabel_40 = tk.Label(root)
        self.GLabel_40["bg"] = "#ffdfb3"
        self.ft = tkFont.Font(family='Times', size=18)
        self.GLabel_40["font"] = self.ft
        self.GLabel_40["fg"] = "#713310"
        self.GLabel_40["justify"] = "center"
        self.GLabel_40["text"] = "Ustawienia"
        self.GLabel_40["font"] = self.ft

        self.GLabel_40.place(x=330, y=20, width=256, height=52)
        #
        self.data_od_placeholder = tk.Entry(root)
        self.data_od_placeholder["bg"] = "#713310"
        self.data_od_placeholder["borderwidth"] = "1px"
        self.ft = tkFont.Font(family='Times', size=13)
        self.data_od_placeholder["font"] = self.ft
        self.data_od_placeholder["fg"] = "#f7c379"
        self.data_od_placeholder["justify"] = "center"
        self.data_od_placeholder.insert(0, "2020")
        self.data_od_placeholder["font"] = self.ft

        # self.data_od_placeholder.place(x=470,y=120,width=70,height=25)

        self.data_do_placeholder = tk.Entry(root)
        self.data_do_placeholder["bg"] = "#713310"
        self.data_do_placeholder["borderwidth"] = "1px"
        self.ft = tkFont.Font(family='Times', size=13)
        self.data_do_placeholder["font"] = self.ft
        self.data_do_placeholder["fg"] = "#f7c379"
        self.data_do_placeholder["justify"] = "center"
        self.data_do_placeholder.insert(0, "2022")
        self.data_do_placeholder["font"] = self.ft

        # self.data_do_placeholder.place(x=380,y=120,width=70,height=25)

        # Label lata od do
        self.label_od = tk.Label(root)
        self.label_od["bg"] = "#ffdfb3"
        self.ft = tkFont.Font(family='Times', size=10)
        self.label_od["font"] = self.ft
        self.label_od["fg"] = "#713310"
        self.label_od["justify"] = "center"
        self.label_od["text"] = "Od:"
        self.label_od["font"] = self.ft

        # self.label_od.place(x=380,y=90,width=70,height=25)

        self.label_do = tk.Label(root)
        self.label_do["bg"] = "#ffdfb3"
        self.ft = tkFont.Font(family='Times', size=10)
        self.label_do["font"] = self.ft
        self.label_do["fg"] = "#713310"
        self.label_do["justify"] = "center"
        self.label_do["text"] = "Do"
        self.label_do["font"] = self.ft
        # self.label_do.place(x=470,y=90,width=70,height=25)
        #

        # aktywator
        self.GButton_438 = tk.Button(root)
        self.GButton_438["activebackground"] = "#a42828"
        self.GButton_438["bg"] = "#713310"
        self.GButton_438["borderwidth"] = "0px"
        self.ft = tkFont.Font(family='Times', size=16)
        self.GButton_438["font"] = self.ft
        self.GButton_438["fg"] = "#f7c379"
        self.GButton_438["justify"] = "center"
        self.GButton_438["text"] = "Stwórz plik"
        self.GButton_438.place(x=30, y=310, width=215, height=40)
        self.GButton_438["highlightbackground"] = "#ffdfb3"  # Add border color here
        self.GButton_438["activebackground"] = "#f7c379"  # Darker hover color
        self.GButton_438["activeforeground"] = "#713310"  # Font color during highlighting
        self.GButton_438["font"] = self.ft

        self.GButton_438["command"] = lambda: self.activator(self.start_arguments)

        def on_enter(event):
            self.GButton_438["bg"] = self.GButton_438["activebackground"]
            self.GButton_438["fg"] = self.GButton_438["activeforeground"]

        # Function to handle mouse leave event
        def on_leave(event):
            self.GButton_438["bg"] = "#713310"
            self.GButton_438["fg"] = "#f7c379"

        # Bind the enter and leave events to the button
        self.GButton_438.bind("<Enter>", on_enter)
        self.GButton_438.bind("<Leave>", on_leave)

        self.path_input = tk.Entry(root)
        self.path_input["bg"] = "#713310"
        self.path_input["borderwidth"] = "1px"
        self.ft = tkFont.Font(family='Times', size=10)
        self.path_input["font"] = self.ft
        self.path_input["fg"] = "#f7c379"
        self.path_input["justify"] = "center"
        self.path_input.insert(0, "testy.xlsx")
        self.path_input["font"] = self.ft
        self.path_input.place(x=260, y=320, width=316, height=30)

        # scieżka pliku
        self.GLabel_420 = tk.Label(root)
        self.GLabel_420["bg"] = "#ffdfb3"
        self.ft = tkFont.Font(family='Times', size=10)
        self.GLabel_420["font"] = self.ft
        self.GLabel_420["fg"] = "#713310"
        self.GLabel_420["justify"] = "center"
        self.GLabel_420["text"] = "Zapisz plik jako:"
        self.GLabel_420["font"] = self.ft
        self.GLabel_420.place(x=260, y=290, width=315, height=30)

        # branches
        self.branches_label = tk.Label(root)
        self.branches_label["bg"] = "#ffdfb3"
        self.ft = tkFont.Font(family='Times', size=10)
        self.branches_label["font"] = self.ft
        self.branches_label["fg"] = "#713310"
        self.branches_label["justify"] = "center"
        self.branches_label["text"] = "Wojewodztwa:"
        self.branches_label["font"] = self.ft

        # self.branches_label.place(x=360,y=170,width=77,height=30)

        self.branches_placeholder = tk.Entry(root)
        self.branches_placeholder["bg"] = "#713310"
        self.branches_placeholder["borderwidth"] = "1px"
        self.ft = tkFont.Font(family='Times', size=13)
        self.branches_placeholder["font"] = self.ft
        self.branches_placeholder["fg"] = "#f7c379"
        self.branches_placeholder["justify"] = "center"
        self.branches_placeholder.insert(0, "01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16")
        self.branches_placeholder["font"] = self.ft

        # self.branches_placeholder.place(x=360,y=200,width=77,height=30)

        # niestałe kod produktu
        self.label_produkty = tk.Label(root)
        self.label_produkty["bg"] = "#ffdfb3"
        self.ft = tkFont.Font(family='Times', size=10)
        self.label_produkty["font"] = self.ft
        self.label_produkty["fg"] = "#713310"
        self.label_produkty["justify"] = "center"
        self.label_produkty["text"] = "Produkty"
        self.label_produkty["font"] = self.ft

        # self.label_produkty.place(x=460,y=170,width=116,height=30)

        self.produkty_placeholder = tk.Entry(root)
        self.produkty_placeholder["bg"] = "#713310"
        self.produkty_placeholder["borderwidth"] = "1px"
        self.ft = tkFont.Font(family='Times', size=13)
        self.produkty_placeholder["font"] = self.ft
        self.produkty_placeholder["fg"] = "#f7c379"
        self.produkty_placeholder["justify"] = "center"
        self.produkty_placeholder["text"] = "03.0000.335.02"
        self.produkty_placeholder["font"] = self.ft

        # self.produkty_placeholder.place(x=460,y=200,width=116,height=30)
        ###########
        # niestałe kod produktu
        self.label_usluga = tk.Label(root)
        self.label_usluga["bg"] = "#ffdfb3"
        self.ft = tkFont.Font(family='Times', size=10)
        self.label_usluga["font"] = self.ft
        self.label_usluga["fg"] = "#713310"
        self.label_usluga["justify"] = "center"
        self.label_usluga["text"] = "Uslugi"
        self.label_usluga["font"] = self.ft

        # self.label_usluga.place(x=360,y=170,width=116,height=30)

        self.usluga_placeholder = tk.Entry(root)
        self.usluga_placeholder["bg"] = "#713310"
        self.usluga_placeholder["borderwidth"] = "1px"
        self.ft = tkFont.Font(family='Times', size=13)
        self.usluga_placeholder["font"] = self.ft
        self.usluga_placeholder["fg"] = "#f7c379"
        self.usluga_placeholder["justify"] = "center"
        self.usluga_placeholder.insert(0, "01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18")
        self.usluga_placeholder["font"] = self.ft

        # self.produkty_usluga.place(x=360,y=200,width=116,height=30)

        # niestałe kod produktu
        self.icd9_produkty = tk.Label(root)
        self.icd9_produkty["bg"] = "#ffdfb3"
        self.ft = tkFont.Font(family='Times', size=10)
        self.icd9_produkty["font"] = self.ft
        self.icd9_produkty["fg"] = "#713310"
        self.icd9_produkty["justify"] = "center"
        self.icd9_produkty["text"] = "kod icd9"
        self.icd9_produkty["font"] = self.ft

        # self.label_produkty.place(x=460,y=170,width=116,height=30)

        self.icd9_placeholder = tk.Entry(root)
        self.icd9_placeholder["bg"] = "#713310"
        self.icd9_placeholder["borderwidth"] = "1px"
        self.ft = tkFont.Font(family='Times', size=13)
        self.icd9_placeholder["font"] = self.ft
        self.icd9_placeholder["fg"] = "#f7c379"
        self.icd9_placeholder["justify"] = "center"
        self.icd9_placeholder["text"] = "wpisz kody"
        self.icd9_placeholder["font"] = self.ft

        # self.produkty_placeholder.place(x=460,y=200,width=116,height=30)
        self.GLabel_198 = tk.Label(root)
        self.GLabel_198["bg"] = "#ffdfb3"
        self.ft = tkFont.Font(family='Times', size=10)
        self.GLabel_198["font"] = self.ft
        self.GLabel_198["fg"] = "#713310"
        self.GLabel_198["justify"] = "center"
        self.GLabel_198["text"] = "Dane do zebrania:"
        self.GLabel_198["font"] = self.ft

        self.GLabel_198.place(x=20, y=160, width=115, height=30)

        self.variable = StringVar(root)
        OPTIONS = ["Kontrakty_szpitale_produkty_leczenie_szpitalne", "liczba_pacjentów_dla_jgp",
                   "wartości_kontraktów_dla_produktów", "liczba hospitalizacji dla produktów w kodzie icd9",
                   "Kontrakty_szpitale_produkty_wszystkie_uslugi"]
        self.variable.set(OPTIONS[0])  # default value

        self.w = tk.OptionMenu(root, self.variable, *OPTIONS)
        self.w["bg"] = "#713310"
        self.w["fg"] = "#f7c379"
        self.w.place(x=20, y=190, width=280, height=30)
        self.current_widgets = []
        self.w["highlightbackground"] = "#ffdfb3"  # Add border color here
        self.w["activebackground"] = "#f7c379"  # Darker hover color
        self.w["activeforeground"] = "#713310"  # Font color during highlighting

        self.variable.trace("w", self.option_changed)
        self.w['menu'].config(bg="#713310", fg="#f7c379")

        self.settings_1 = [[self.label_do, 470, 90, 70, 25], [self.data_od_placeholder, 380, 120, 70, 25],
                           [self.data_do_placeholder, 470, 120, 70, 25], [self.label_od, 380, 90, 70, 25],
                           [self.branches_label, 360, 170, 77, 30], [self.branches_placeholder, 360, 200, 77, 30]]
        # Replace with your actual January widgets
        self.settings_2 = [[self.label_do, 470, 90, 70, 25], [self.data_od_placeholder, 380, 120, 70, 25],
                           [self.data_do_placeholder, 470, 120, 70, 25], [self.label_od, 380, 90, 70, 25],
                           [self.label_produkty, 460, 170, 116, 30], [self.produkty_placeholder, 460, 200, 116, 30],
                           [self.branches_label, 360, 170, 77, 30], [self.branches_placeholder, 360, 200, 77, 30]]
        # Replace with your actual February widgets
        self.settings_3 = [[self.icd9_produkty, 460, 170, 116, 30], [self.icd9_placeholder, 460, 200, 116, 30]]

        self.settings_4 = [[self.label_do, 470, 90, 70, 25], [self.data_od_placeholder, 380, 120, 70, 25],
                           [self.data_do_placeholder, 470, 120, 70, 25], [self.label_od, 380, 90, 70, 25],
                           [self.label_usluga, 460, 170, 116, 30], [self.usluga_placeholder, 460, 200, 116, 30],
                           [self.branches_label, 360, 170, 77, 30], [self.branches_placeholder, 360, 200, 77, 30]]

        self.option_changed()

    def show_widgets(self, widgets):
        for widget in widgets:
            coords = widget[1:5]
            widget[0].place(x=coords[0], y=coords[1], width=coords[2], height=coords[3])  # Set the desired coordinates

    def hide_widgets(self, widgets):
        for widget in widgets:
            try:
                widget[0].place_forget()
            except:
                pass

    def option_changed(self, *args):
        print("changed to ", self.current_widgets)
        self.selected_option = self.variable.get()
        # Hide widgets from the previous selection
        self.hide_widgets(self.current_widgets)

        if self.selected_option == "Kontrakty_szpitale_produkty_leczenie_szpitalne":
            self.current_widgets = self.settings_1
            self.start = scrap_functions.basic_searches.produkt_dla_szpitali
            self.start_arguments = [self.data_od_placeholder.get(), self.data_do_placeholder.get(),
                                    list(self.branches_placeholder.get().split(",")), self.path_input.get()]

        elif self.selected_option == "liczba_pacjentów_dla_jgp":
            self.current_widgets = self.settings_2
            self.start = scrap_functions.basic_searches.pacjenci_na_jgp
            self.start_arguments = [list(self.branches_placeholder.get().split(",")),
                                    list(self.produkty_placeholder.get().split(",")), self.path_input.get()]

        elif self.selected_option == "wartości_kontraktów_dla_produktów":
            self.current_widgets = self.settings_2
            self.start = scrap_functions.basic_searches.pakiet_kody
            self.start_arguments = [self.data_od_placeholder.get(), self.data_do_placeholder.get(),
                                    list(self.branches_placeholder.get().split(",")),
                                    list(self.produkty_placeholder.get()), self.path_input.get()]

        elif self.selected_option == "liczba hospitalizacji dla produktów w kodzie icd9":
            self.current_widgets = self.settings_3
            self.start = scrap_functions.basic_searches.icd_9
            self.start_arguments = [self.icd9_placeholder.get(), self.path_input.get()]

        elif self.selected_option == "kwota_kontraktu_dla_produktu":
            self.current_widgets = self.settings_4
            self.start = scrap_functions.basic_searches.kwota_kontraktu_dla_produktu  # TODO dodac usluge
            self.start_arguments = [self.data_od_placeholder.get(), self.data_do_placeholder.get(),
                                    list(self.branches_placeholder.get().split(",")),
                                    list(self.produkty_placeholder.get()), self.path_input.get()]

        elif self.selected_option == "Kontrakty_szpitale_produkty_wszystkie_uslugi":
            self.current_widgets = self.settings_4
            self.start = scrap_functions.basic_searches.kwota_kontraktów  # TODO dodac usluge
            self.start_arguments = [self.data_od_placeholder.get(), self.data_do_placeholder.get(),
                                    list(self.branches_placeholder.get().split(",")),
                                    list(self.produkty_placeholder.get()), self.path_input.get()]

        # Show widgets for the current selection
        self.show_widgets(self.current_widgets)

    def activator(self, arguments):

        if self.selected_option == "Kontrakty_szpitale_produkty_leczenie_szpitalne":
            self.start_arguments = [int(self.data_od_placeholder.get()), int(self.data_do_placeholder.get()),
                                    list(self.branches_placeholder.get().split(",")), self.path_input.get()]

        elif self.selected_option == "liczba_pacjentów_dla_jgp":
            self.start_arguments = [list(self.branches_placeholder.get().split(",")),
                                    list(self.produkty_placeholder.get().split(",")), self.path_input.get()]

        elif self.selected_option == "wartości_kontraktów_dla_produktów":
            self.start_arguments = [int(self.data_od_placeholder.get()), int(self.data_do_placeholder.get()),
                                    list(self.branches_placeholder.get().split(",")),
                                    list(self.produkty_placeholder.get().split(",")), self.path_input.get()]

        elif self.selected_option == "liczba hospitalizacji dla produktów w kodzie icd9":
            self.start_arguments = [self.icd9_placeholder.get(), self.path_input.get()]

        elif self.selected_option == "Kontrakty_szpitale_produkty_wszystkie_uslugi":
            self.start_arguments = [list(self.usluga_placeholder.get().split(",")), int(self.data_od_placeholder.get()),
                                    int(self.data_do_placeholder.get()),
                                    list(self.branches_placeholder.get().split(",")), self.path_input.get()]

        print(self.start_arguments)
        self.start(*self.start_arguments)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

