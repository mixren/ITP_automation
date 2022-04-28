import tkinter as tk
from my_mdr_panel import MyMdrPanel
import managers.generate_manager as gm
from tkinter import messagebox

class MyTkWindow:
    TITLE="CWT ITP Generator"

    def __init__(self):
        self.root = tk.Tk()
        self.root.title(self.TITLE)
        
        self.lbl_template = tk.Label(master=self.root, text="")
        self.lbl_template.grid(row=0, column=0, pady=6, padx=50)

        self.frm_mdr_table = tk.Frame(master=self.root)
        self.frm_mdr_table.grid(row=1, column=0, pady=6, padx=50)

        self.template_panel = MyMdrPanel(self.root, self.frm_mdr_table)

        # "Generate" button
        self.btn_generate = tk.Button(master=self.root, width=30, height=2, text="Generate docx + pdf", command=self.generate)
        self.btn_generate.grid(row=2, column=0, pady=14)

        # Result Label
        self.lbl_result = tk.Label(master=self.root, fg="grey", font=('Arial', 10))
        self.lbl_result.grid(row=3, column=0)

        self.initial_setup()

    def initial_setup(self):
        self.template_panel.initial_setup('MDR', '9')

    def start(self):
        self.root.mainloop()

    def generate(self):
        table = self.template_panel.ent_template.get()
        sheet = self.template_panel.ent_sheet.get()
        header = self.template_panel.ent_header.get()
        itp_models = gm.read_itp_model_from_excel(table, sheet, int(header))
        if itp_models != None:
            print(f"Found {len(itp_models)} drawing names in Excel")
            response = messagebox.askokcancel("askokcancel", f"Found {len(itp_models)} drawing names in Excel. Generate ITPs?")
            if response != 1:
                print(f"Cancelled")
            else:
                gm.run_generator(itp_models)
                print("End.\n")
    