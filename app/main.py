
import customtkinter as ctk
from views.home import Home


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Alarme")
        self.geometry("800x600")

        self.current_view = None
        self.show_view(Home)

    def show_view(self, view_class):
        """Troca a tela exibida na janela principal."""
        if self.current_view is not None:
            self.current_view.destroy()
        self.current_view = view_class(self)
        self.current_view.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
