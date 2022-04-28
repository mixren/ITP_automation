from mailmerge import MailMerge
import os
from itp_model import ItpModel

EXT = "docx"

def template_exists(self) -> bool:
    return os.path.exists(self.PATH_VT_TEMPLATE)

def create_word_from_template(path_template: str, path_target_no_ext: str, itp_model: ItpModel):
    path_target = f'{path_target_no_ext}.{EXT}'
    document = MailMerge(path_template)
    # document.get_merge_fields() Check if merge fields exist
    
    document.merge(item = itp_model.item)
    document.merge(vendor_job = itp_model.get_vendor_job())
    document.merge(line = itp_model.line)
    document.merge(document = itp_model.get_document())

    try:
        document.write(path_target)
        print(f"ITP Word successfully generated for {itp_model.drawing}")
    except:
        print(f"Error writing to a '{itp_model.drawing}' Word document. Might be it exists and is opened.")
