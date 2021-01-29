import tkinter as tk
import tkinter.font as font

from components_start.start_page import StartPage


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Fonts
        self.title_font = font.Font(family='Arial', size='18', weight='bold')
        self.label_font = font.Font(family='Arial', size='15', weight='bold')

        # Frame frame_container
        self.frame_container = tk.Frame(self)
        self.frame_container.pack(side="top", fill="both")

        # List of pages and their numbers in the self.frames list
        '''StartPage = 0
        '''
        self.frames = [StartPage]

        # Initial frame
        self._frame = None

        # Set initial frame to LoginPage
        self.show_frame(0)

        # Center window and make proper size of it
        self.center_window_on_screen()

        # Used for notification about low stock
        self.first_start = True

    # Show a frame for the given page name
    def show_frame(self, page_number):
        frame_object = self.frames[page_number]
        new_frame = frame_object(parent=self.frame_container, controller=self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    # Function which defines size of window and centres it on the screen
    def center_window_on_screen(self):
        width, height = 400, 440
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Centres windows and makes appropriate windows size
        x_cord = int((screen_width / 2) - (width / 2))
        y_cord = int((screen_height / 2) - (height / 2))
        self.geometry("{}x{}+{}+{}".format(width, height, x_cord, y_cord))


if __name__ == "__main__":
    app = App()
    app.mainloop()
