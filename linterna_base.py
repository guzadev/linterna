import tkinter as tk

def create_adjustable_bright_bar():
    root = tk.Tk()
    root.overrideredirect(True)           # Sin bordes
    root.configure(bg="white")            # Fondo blanco
    root.attributes("-topmost", True)     # Siempre encima

    # Refuerza que la ventana se mantenga al frente cada segundo
    def keep_on_top():
        root.lift()
        root.after(1000, keep_on_top)

    keep_on_top()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    MIN_HEIGHT = 20
    MAX_HEIGHT = screen_height

    bar_height = tk.IntVar(value=50)      # Altura inicial

    def update_geometry():
        height = bar_height.get()
        root.geometry(f"{screen_width}x{height}+0+{screen_height - height}")

    def increase_height(event=None):
        if bar_height.get() + 10 <= MAX_HEIGHT:
            bar_height.set(bar_height.get() + 10)
            update_geometry()

    def decrease_height(event=None):
        if bar_height.get() - 10 >= MIN_HEIGHT:
            bar_height.set(bar_height.get() - 10)
            update_geometry()

    root.bind("<Escape>", lambda e: root.destroy())
    root.bind("<Up>", increase_height)
    root.bind("<Down>", decrease_height)

    update_geometry()
    root.mainloop()

create_adjustable_bright_bar()
