import tkinter as tk
from tkinter import ttk

# Function to update text based on user choice
def update_text(answer):
    if answer == "Indeed":
        source_link = "https://example.com/why-programming-matters"
        points = "\n• AI still relies on programmers to build and refine models.\n• Custom AI solutions require coding knowledge.\n• Understanding algorithms helps in debugging and fine-tuning AI.\n• High-paying jobs still demand programming expertise."
    else:
        source_link = "https://example.com/ai-no-code-future"
        points = "\n• No-code platforms enable AI-driven solutions.\n• AI models can generate their own code.\n• Businesses prioritize AI-assisted tools over manual programming.\n• AI can automate most traditional programming tasks."

    # Update the text areas
    source_label.config(text=f"Source: {source_link}")
    bullet_points.config(text=points)

# Create main window
root = tk.Tk()
root.title("Programming in the AI Era: Essential or Obsolete?")
root.geometry("600x400")
root.configure(bg="#f1f1f1")

# Main Question
question_label = tk.Label(root, text="Is learning to program still essential in the age of AI?", 
                          font=("Arial", 14, "italic"), bg="#f1f1f1", wraplength=500, justify="center", fg="#000000")
question_label.pack(pady=10)

# Opinion Text Area
opinion_label = tk.Label(root, text="Your Stupid Opinion:", font=("Arial", 12), bg="#f0f0f0")
opinion_label.pack()
opinion_text = tk.Text(root, height=50, width=50, wrap="word")
opinion_text.pack(pady=5)

# Buttons Frame
buttons_frame = tk.Frame(root, bg="#f0f0f0")
buttons_frame.pack(pady=10)

yes_button = ttk.Button(buttons_frame, text="Yeah", command=lambda: update_text("Yeah"))
yes_button.grid(row=0, column=0, padx=10)

no_button = ttk.Button(buttons_frame, text="Nah", command=lambda: update_text("Nah"))
no_button.grid(row=0, column=1, padx=10)

# Text Display Areas
source_label = tk.Label(root, text="Source: [Click a button to view]", font=("Roboto", 10, "bold"), fg="red", bg="#f1f1f1")
source_label.pack(pady=5)

bullet_points = tk.Label(root, text="• Supporting points will appear here.", font=("Arial", 11), bg="#f0f0f0", justify="right", wraplength=550)
bullet_points.pack(pady=5)

# Run the app
root.mainloop()
