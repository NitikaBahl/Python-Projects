import os
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk

def load_image(image_path):
    """Load an image from the specified path."""
    print(f"Loading image from: {image_path}")
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image not found or unable to load: {image_path}")
    print("Image loaded successfully.")
    return image

def convert_to_grayscale(image):
    """Convert a BGR image to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def blur_image(image, kernel_size=(5, 5)):
    """Apply Gaussian blur to the image."""
    return cv2.GaussianBlur(image, kernel_size, 0)

def edge_detection(image):
    """Apply Canny edge detection to the image."""
    return cv2.Canny(image, 100, 200)

def invert_colors(image):
    """Invert the colors of the image."""
    return cv2.bitwise_not(image)

def save_image(image, output_path):
    """Save the image to the specified path."""
    success = cv2.imwrite(output_path, image)
    if success:
        print(f"Image saved to: {output_path}")
    else:
        print(f"Error saving image to: {output_path}")

def show_image(image, title):
    """Display an image in a Tkinter window."""
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    photo = ImageTk.PhotoImage(image)

    window = tk.Toplevel()
    window.title(title)
    label = tk.Label(window, image=photo)
    label.image = photo  # Keep a reference to avoid garbage collection
    label.pack()

def process_image(image_path, operation):
    """Process the image based on the selected operation."""
    try:
        image = load_image(image_path)

        if operation == "Grayscale":
            processed_image = convert_to_grayscale(image)
        elif operation == "Blur":
            processed_image = blur_image(image)
        elif operation == "Edge Detection":
            processed_image = edge_detection(image)
        elif operation == "Invert Colors":
            processed_image = invert_colors(image)
        else:
            raise ValueError("Invalid operation selected.")

        show_image(image, "Original Image")
        show_image(processed_image, f"{operation} Image")

        # Save the processed image
        base_name = os.path.basename(image_path)
        name, ext = os.path.splitext(base_name)
        current_directory = os.getcwd()
        processed_image_path = os.path.join(current_directory, f"{name}_{operation.lower().replace(' ', '_')}{ext}")
        save_image(processed_image, processed_image_path)

        # Update status
        status_var.set(f"{operation} image processed and saved.")

    except ValueError as e:
        messagebox.showerror("Error", str(e))

def open_file():
    """Open a file dialog to select an image."""
    global file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        # Show the selected image in the preview
        image = load_image(file_path)
        show_image(image, "Selected Image")
        # Enable the process button
        process_button.config(state=tk.NORMAL)
        # Display image size
        height, width, _ = image.shape
        status_var.set(f"Loaded image: {os.path.basename(file_path)} (Size: {width}x{height})")

def process_selected_image():
    """Process the selected image based on the dropdown selection."""
    selected_operation = operation_var.get()
    if selected_operation:
        process_image(file_path, selected_operation)

def reset_application():
    """Reset the application to its initial state."""
    global file_path
    file_path = None
    operation_var.set('')
    process_button.config(state=tk.DISABLED)
    status_var.set("Application reset. Please load an image.")

def create_gui():
    """Create the main GUI window."""
    global file_path, operation_var, process_button, status_var

    root = tk.Tk()
    root.title("Image Processing Application")

    # Create a frame for the controls
    control_frame = tk.Frame(root)
    control_frame.pack(pady=20)

    # Dropdown for operations
    operation_var = tk.StringVar()
    operation_label = tk.Label(control_frame, text="Select Operation:")
    operation_label.grid(row=0, column=0, padx=5)

    operation_dropdown = ttk.Combobox(control_frame, textvariable=operation_var)
    operation_dropdown['values'] = ("Grayscale", "Blur", "Edge Detection", "Invert Colors")
    operation_dropdown.grid(row=0, column=1, padx=5)

    # Open Image button
    open_button = tk.Button(control_frame, text="Open Image", command=open_file)
    open_button.grid(row=0, column=2, padx=5)

    # Process button
    process_button = tk.Button(control_frame, text="Process Image", command=process_selected_image, state=tk.DISABLED)
    process_button.grid(row=0, column=3, padx=5)

    # Reset button
    reset_button = tk.Button(control_frame, text="Reset", command=reset_application)
    reset_button.grid(row=0, column=4, padx=5)

    # Status bar
    status_var = tk.StringVar()
    status_label = tk.Label(root, textvariable=status_var, relief=tk.SUNKEN, anchor='w')
    status_label.pack(fill=tk.X, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()