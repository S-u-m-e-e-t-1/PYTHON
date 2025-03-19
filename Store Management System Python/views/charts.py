
import tkinter as tk
from tkinter import Frame
from utils.chart_generator import create_bar_chart

class ChartView:
    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        content_frame = Frame(self.parent, bg="#f0f8ff")
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)

        chart_titles = ["Sales Overview", "Profit Analysis", "Customer Growth", "Market Trends"]
        chart_data = [[10, 25, 30, 15], [5, 15, 20, 10], [50, 60, 70, 80], [100, 80, 60, 40]]
        categories = ["Q1", "Q2", "Q3", "Q4"]

        for i, title in enumerate(chart_titles):
            chart_frame = Frame(content_frame, bg="white", relief="ridge", borderwidth=2)
            chart_frame.pack(fill="both", expand=True, padx=10, pady=10)
            create_bar_chart(chart_frame, title, chart_data[i], categories)