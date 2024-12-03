
import customtkinter as ctk

class Home(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label = ctk.CTkLabel(self, text="Home")
        self.label.grid(pady=10, padx=10)

        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=2)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((4), weight=1)

        self.button = ctk.CTkButton(self, text="Settings", command=self.go_to_settings)
        self.button.grid(row=0, column=4)

    def go_to_settings(self):
        from views.settings import Settings
        self.master.show_view(Settings)
