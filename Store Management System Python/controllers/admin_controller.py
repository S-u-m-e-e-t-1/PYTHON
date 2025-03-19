import tkinter as tk
from models.inventory_model import InventoryModel
from models.dealer_model import DealerModel
from models.staff_model import StaffModel
from models.bill_model import BillModel
from models.salary_model import SalaryModel

class AdminController:
    def __init__(self, parent):
        self.parent = parent
        self.inventory_model = InventoryModel()
        self.dealer_model = DealerModel()
        self.staff_model = StaffModel()
        self.salary_model = SalaryModel()
        self.bill_model = BillModel()

    def product_dashboard(self):
        self.inventory_model.open_product_dashboard(self.parent)

    def dealer_dashboard(self):
        self.dealer_model.open_dealer_dashboard(self.parent)

    def staff_dashboard(self):
        self.staff_model.open_staff_dashboard(self.parent)

    def view_salary(self):
        self.salary_model.open_salary_dashboard(self.parent)

    def view_bills(self):
        self.bill_model.open_bills_dashboard(self.parent)

    def logout(self):   
        self.parent.destroy()
