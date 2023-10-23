import tkinter as tk
import os
from PIL import Image, ImageTk

class Slideshow:
    def __init__(self, root):
        self.root = root
        self.images = []
        self.current_image = 0

        # Load all images from the directory
        for filename in os.listdir(R"E:\WALLPAPER\19-wall"):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                image = Image.open(os.path.join(R"E:\WALLPAPER\19-wall", filename))
                self.images.append(ImageTk.PhotoImage(image))

        # Create a label to display the images
        self.label = tk.Label(root)
        self.label.pack()

        # Start the slideshow
        self.show_image()

    def show_image(self):
        # Display the current image
        self.label.config(image=self.images[self.current_image])

        # Move to the next image
        self.current_image += 1
        if self.current_image >= len(self.images):
            self.current_image = 0

        # Schedule the next image to be displayed after 2 seconds
        self.root.after(2000, self.show_image)

# Create a Tkinter window and start the slideshow
root = tk.Tk()
root.geometry("800x600")
slideshow = Slideshow(root)
root.mainloop()