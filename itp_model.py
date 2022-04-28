
class ItpModel:
    '''
        'item': '05-GOX-021-1',
        'drawing': 'CWT.MP21-09-12.00.00',
        'line': '05-GOX-021-UA6G-100-NI'
    '''

    def __init__(self, item, drawing, line) -> None:
        self.item = item
        self.drawing = drawing
        self.line = line

    def get_document(self):
        '''Example: CWT.MP21-09-12.00.00.ITP'''
        return f"{self.drawing}.ITP"

    def get_vendor_job(self):
        '''Example: CWT.MP21-09-12'''
        return self.drawing.split(".0", 1)[0]

    
