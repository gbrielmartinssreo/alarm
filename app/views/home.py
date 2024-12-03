import customtkinter as ctk
from utils.resources import get_icon_path
from PIL import Image

class Home(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label = ctk.CTkLabel(self, text="Home")
        self.label.grid(pady=10, padx=10)

        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=2)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((4), weight=1)

        # Obter o caminho correto para o ícone
        self.icon_path = get_icon_path("setting.png")
        self.icon_settings = ctk.CTkImage(Image.open(self.icon_path), size=(24, 24))

        self.button = ctk.CTkButton(self, text="", image=self.icon_settings, width=50, height=50, fg_color="transparent", hover_color="gray", command=self.go_to_settings)
        self.button.grid(row=0, column=4)

    def go_to_settings(self):
        from views.settings import Settings
        self.master.show_view(Settings)
