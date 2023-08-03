# pip install barcode
# pip install python-barcode

from barcode import EAN13
from barcode.writer import ImageWriter  # ------------->> To get the image of the barcode

num_brcd = int(input("Enter number of barcodes : "))
num = range(num_brcd)     #  --------------->>  to get given amount of barcodes
options = dict(compress=True)

for i in num:
    id = input("Enter a 13-digit number as barcode ID: ")
    my_brcd = EAN13(id, writer=ImageWriter())   # --------->>  Object of EAN13
    f_nm = input("Enter a file name to save barcodes: ")
    my_brcd.save(f_nm, options)