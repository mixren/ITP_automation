import tkinter as tk
import tkinter.filedialog as fd

class MyMdrPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        self.lbl_template = tk.Label(self.frame, text = "MDR Excel Table: ")
        self.ent_template = tk.Entry(self.frame, width = 50)
        self.btn_template = tk.Button(self.frame, text="Select", command=self.select_template_file)

        self.frm_sheet_header = tk.Frame(master=self.frame)
        self.frm_sheet = tk.Frame(master=self.frm_sheet_header)
        self.frm_header = tk.Frame(master=self.frm_sheet_header)
        self.lbl_sheet = tk.Label(self.frm_sheet, text = "Sheet: ")
        self.ent_sheet = tk.Entry(self.frm_sheet, width = 15)
        self.lbl_header = tk.Label(self.frm_header, text = "Header: ")
        self.ent_header = tk.Entry(self.frm_header, width = 5)

        self.lbl_template.grid(row=0, column=0, sticky="w", padx=10)
        self.ent_template.grid(row=0, column=1, sticky="w", padx=10)
        self.btn_template.grid(row=0, column=2, sticky="w", padx=10)
        self.frm_sheet_header.grid(row=1, columnspan=2, pady=10, padx=10)

        self.frm_sheet.grid(row=0, column=0, sticky="e", padx=10)
        self.frm_header.grid(row=0, column=1, sticky="e", padx=10)
        self.lbl_sheet.grid(row=0, column=0, sticky="e", padx=10)
        self.ent_sheet.grid(row=0, column=1, sticky="e", padx=10)
        self.lbl_header.grid(row=0, column=0, sticky="e", padx=10)
        self.ent_header.grid(row=0, column=1, sticky="e", padx=10)


    def initial_setup(self, sheet:str, header:str):
        self.ent_sheet.delete(0, tk.END)
        self.ent_sheet.insert(0, sheet)
        self.ent_header.delete(0, tk.END)
        self.ent_header.insert(0, header)
    
    def select_template_file(self):
        path = fd.askopenfilename(title="Select MDR Exel Table", filetypes=[("Excel files","*.xlsx")])
        if path:
            self.ent_template.delete(0, tk.END)
            self.ent_template.insert(0, path)
            self.ent_template.xview_moveto(1)