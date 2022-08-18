import re

pt_ocr_result = '''Aptio Setup 1234  000 3333 0000 0000 name
                    Aptio Setup 1000  000 3333 0000 0000 name
                    Aptio Setup 1000  000 3333 0000 0000 name
                    Aptio Setup 1000  000 3333 0000 0000 name'''
num = '([0-9]{4})'
dos = re.search(num,pt_ocr_result)
print(str(dos)[-6:-2])
