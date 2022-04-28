from returns.pipeline import is_successful
import managers.word_manager as wm
import managers.excel_manager as em
import managers.file_explorer_manager as fem
from itp_model import ItpModel
from docx2pdf import convert
import concurrent.futures
import functools
import os

TEMPLATE = "repo\\ITP_template.docx"
TARGET_DIR = "generated"

def generate_itp_word(template, target_dir, itp_model: ItpModel):
    target_path_no_ext = os.path.join(target_dir, itp_model.get_document())
    wm.create_word_from_template(template, target_path_no_ext, itp_model)

def read_itp_model_from_excel(path_excel_table: str, excel_sheet_name: str, excel_header_row: int)-> list[ItpModel]:
    dict_res = em.read_from_sheet(path_excel_table, excel_sheet_name, excel_header_row, 'isometric draw', 'drawing no', 'line n')
    if not is_successful(dict_res):
        print(dict_res.failure())
        return None
    dict_unwrapped = dict_res.unwrap()
    #print(f"Found {list(map(len,dict_unwrapped.values()))[0]} drawing names in Excel")
    return [ItpModel(iso, draw, line) for iso, draw, line in list(zip(*dict_unwrapped.values()))]


def run_generator(itp_models: list[ItpModel]):
    target_dir = fem.into_nested_dir('', TARGET_DIR)

    partial_generate_itp = functools.partial(generate_itp_word, TEMPLATE, target_dir)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(partial_generate_itp, itp_models)

    convert(target_dir) # convert to pdf all folder docx


    
'''
path_excel_table = "Z:\\CWT Documents\\2021\\MP21-77 BP101_POX_CS\\MP21-77 MDR Status.xlsx"
test_target_dir = "repo"
test_values = {
        'item': '05-GOX-021-1',
        'drawing': 'CWT.MP21-09-12.00.00',
        'line': '05-GOX-021-UA6G-100-NI'
        }
target_dir = test_target_dir

dict_res = em.read_from_sheet(path_excel_table, 'MDR', 9, 'isometric draw', 'drawing no', 'line n')
if not is_successful(dict_res):
    print(dict_res.failure())
dict_unwrapped = dict_res.unwrap()
print(dict_unwrapped)'''

'''n = 0
for iso, draw, line in zip(*dict_unwrapped.values()):
    itp_model = ItpModel(iso, draw, line)
    target_path_no_ext = os.path.join(test_target_dir, itp_model.get_document())
    generate_itp(template, target_path_no_ext, itp_model)
    n = n+1
    if n ==5:
        break'''

'''        
# just test
itp_model = ItpModel(test_values['item'], test_values['drawing'], test_values['line'])
target_path_no_ext = os.path.join(test_target_dir, itp_model.get_document())
wm.create_word_from_template(TEMPLATE, target_path_no_ext, itp_model)
pass'''