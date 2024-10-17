import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


class AIModel:
    def classify_image(self, image_path):
       
        if "cat" in image_path:
            return "Cat"
        elif "dog" in image_path:
            return "Dog"
        elif "bird" in image_path:
            return "bird"
        elif "tiger" in image_path:
            return "tiger"
        elif "burger" in image_path:
            return "burger"
        elif "snake" in image_path:
            return "snake"
        elif "pizza" in image_path:
            return "pizza"
    
        else:
            return "Unknown Object"

# Tkinter
class BaseApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image detection")
        self.geometry("500x500")
        self.setup_ui()

    def setup_ui(self):
        raise NotImplementedError("Subclasses should implement this method")

#  multiple inheritance
class ImageClassifierApp(BaseApp, AIModel):
    def __init__(self):
        super().__init__()


    def setup_ui(self):
        # Encapsulation
        self.upload_button = tk.Button(self, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=20)

        self.image_label = tk.Label(self)
        self.image_label.pack()

        self.result_label = tk.Label(self, text="Result: ", font=("Arial", 20))
        self.result_label.pack(pady=20)

       
        self.clear_button = tk.Button(self, text="Clear Result", command=self.clear_result)
        self.clear_button.pack(pady=10)

    # Polymorphism
    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            img = Image.open(file_path)
            img = img.resize((300, 300))
            img_tk = ImageTk.PhotoImage(img)

            self.image_label.config(image=img_tk)
            self.image_label.image = img_tk  

           
            classification = self.classify_image(file_path)
            self.result_label.config(text=f"Result: {classification}")
        else:
            messagebox.showerror("Error", "No file selected")

    # overriding
    def clear_result(self):
        self.image_label.config(image='')
        self.result_label.config(text="Result: ")

def log_classification(method):
    def wrapper(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        with open("classification_log.txt", "a") as log_file:
            log_file.write(f"Classified as: {result}\n")
        return result
    return wrapper


class LoggedAIModel(AIModel):
    @log_classification
    def classify_image(self, image_path):
        return super().classify_image(image_path)

# Multiple inheritance
class FinalApp(ImageClassifierApp, LoggedAIModel):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    app = FinalApp()
    app.mainloop()
