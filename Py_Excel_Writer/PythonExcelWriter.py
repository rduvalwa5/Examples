'''
Created on Jun 3, 2021
@author: rduvalwa2

https://pypi.org/project/XlsxWriter/

https://xlsxwriter.readthedocs.io

MaxBookPro17OSX:~ rduvalwa2$ pip install XlsxWriter
Collecting XlsxWriter
  Downloading https://files.pythonhosted.org/packages/2c/ce/74fd8d638a5b82ea0c6f08a5978f741c2655a38c3d6e82f73a0f084377e6/XlsxWriter-1.4.3-py2.py3-none-any.whl (149kB)
     |████████████████████████████████| 153kB 4.1MB/s 
Installing collected packages: XlsxWriter
Successfully installed XlsxWriter-1.4.3
WARNING: You are using pip version 19.3.1; however, version 21.1.2 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
MaxBookPro17OSX:~ rduvalwa2$ pip install --upgrade pip
Collecting pip
  Downloading https://files.pythonhosted.org/packages/cd/82/04e9aaf603fdbaecb4323b9e723f13c92c245f6ab2902195c53987848c78/pip-21.1.2-py3-none-any.whl (1.5MB)
     |████████████████████████████████| 1.6MB 4.7MB/s 
Installing collected packages: pip
  Found existing installation: pip 19.3.1
    Uninstalling pip-19.3.1:
      Successfully uninstalled pip-19.3.1
Successfully installed pip-21.1.2
MaxBookPro17OSX:~ rduvalwa2$ 

'''
#import xlsxwriter
import xlsxwriter

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('demo2.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 20)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Write some simple text.
worksheet.write('A1', 'Hello')

# Text with formatting.
worksheet.write('A2', 'World', bold)

# Write some numbers, with row/column notation.
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)

# Insert an image.
worksheet.insert_image('B5', 'logo.png')

workbook.close()