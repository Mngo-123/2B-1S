import tkinter as tk
from PIL import Image, ImageTk
import pygame
import os

# Initialize main Tkinter window
root = tk.Tk()
root.title("2 Buttons 1 Song")
root.geometry("650x450")

# Initialize Pygame audio mixer
pygame.mixer.init()

# Audio playback functions
def play_mp3():
    file_name = 'Lovers Theme.mp3'
    if os.path.exists(file_name):
        pygame.mixer.music.load(file_name)
        pygame.mixer.music.play()
        status_label.config(text="Status: Now Playing 'Lovers Theme.mp3'", fg="#aeffae")
    else:
        status_label.config(text=f"Error: '{file_name}' not found!", fg="#ff8888")

def stop_mp3():
    pygame.mixer.music.stop()
    status_label.config(text="Status: Music Stopped", fg="white")

# --- Background Image Setup ---
bg_image_path = 'choclate ice scerma.jpg'

# Create a background label that stays at the very bottom layer
bg_label = tk.Label(root)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Variables to keep track of current dimensions and tasks
last_w, last_h = 0, 0
update_running = False

def resize_background(event=None):
    """Core function to safely resize and redraw the image frame"""
    global last_w, last_h
    
    # Fetch accurate current dimensions of the root window
    w = root.winfo_width()
    h = root.winfo_height()
    
    # Avoid unnecessary re-rendering if dimensions haven't changed
    if w == last_w and h == last_h:
        return
    last_w, last_h = w, h

    if os.path.exists(bg_image_path):
        img = Image.open(bg_image_path)
        # Use BILINEAR for ultra-smooth real-time tracking while dragging
        img_resized = img.resize((w, h), Image.Resampling.BILINEAR)
        photo = ImageTk.PhotoImage(img_resized)
        bg_label.config(image=photo)
        bg_label.image = photo 
    else:
        bg_label.config(bg="#5c3a21")

def start_live_loop(event):
    """Triggered on click/configure to bypass the Windows dragging loop freeze"""
    global update_running
    if event.widget == root and not update_running:
        update_running = True
        live_update_loop()

def live_update_loop():
    """Forces Tkinter to update the image frame independently every 15ms"""
    global update_running
    if update_running:
        resize_background()
        root.update_idletasks() # Explicitly paint the screen
        
        # Keep checking for changes dynamically every 15 milliseconds
        # If no changes happen for 1 second, the loop goes to sleep to save CPU
        root.after(15, live_update_loop)

def stop_live_loop(event):
    """Turns off the active loop when user lets go or stops moving window"""
    global update_running
    update_running = False
    # Apply a high-quality LANCZOS polish as a final touch when resizing ends
    w, h = root.winfo_width(), root.winfo_height()
    if os.path.exists(bg_image_path):
        img = Image.open(bg_image_path).resize((w, h), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        bg_label.config(image=photo)
        bg_label.image = photo

# Bind native Tkinter loops to maintain drawing cycles during active drags
root.bind('<Configure>', start_live_loop)
root.bind('<ButtonRelease-1>', stop_live_loop)

# --- Permanent Overlay Panel ---
control_panel = tk.Frame(root, bg="#2b1810", bd=2, relief="ridge")
control_panel.place(relx=0.5, rely=0.5, anchor="center", width=400, height=220)

title_label = tk.Label(control_panel, text="2 Buttons 1 Song", font=("Arial", 18, "bold"), fg="white", bg="#2b1810")
title_label.pack(pady=15)

status_label = tk.Label(control_panel, text="Status: Ready", font=("Arial", 11, "italic"), fg="white", bg="#2b1810")
status_label.pack(pady=10)

btn_frame = tk.Frame(control_panel, bg="#2b1810")
btn_frame.pack(pady=15)

play_btn = tk.Button(btn_frame, text="Play Song 🎵", command=play_mp3, width=12, font=("Arial", 11, "bold"), bg="#5c3a21", fg="white", activebackground="#7a4f31", bd=2)
play_btn.pack(side=tk.LEFT, padx=10)

stop_btn = tk.Button(btn_frame, text="Stop 🛑", command=stop_mp3, width=12, font=("Arial", 11, "bold"), bg="#d9534f", fg="white", activebackground="#c9302c", bd=2)
stop_btn.pack(side=tk.LEFT, padx=10)

root.mainloop()
