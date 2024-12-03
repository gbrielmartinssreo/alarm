
import customtkinter as ctk

class Settings(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        self.label = ctk.CTkLabel(self, text="Settings")
        self.label.grid(column=1, row=0)

        self.button = ctk.CTkButton(self, text="Back", command=self.go_to_home)
        self.button.grid(row=1, column=1)

    def go_to_home(self):
        from views.home import Home
        self.master.show_view(Home)
