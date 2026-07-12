import customtkinter as ctk
from component import GradientButton

app = ctk.CTk()
btn = GradientButton(app, text="Click Me")
btn.pack(padx=20, pady=20)

if __name__ == "__main__":
    app.mainloop()
