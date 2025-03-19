import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def create_bar_chart(frame, title, data, categories):
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.bar(categories, data, color="skyblue")
    ax.set_title(title)
    ax.set_ylabel("Values")
    ax.set_xlabel("Categories")

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)

