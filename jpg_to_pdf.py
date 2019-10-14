from fpdf import FPDF
from PIL import Image
import os

#ver1
'''
def makePdf(pdfFileName, listPages, dir = ''):
    if (dir):
        dir += "/"

    cover = Image.open(dir + str(listPages[0]) + ".jpg")
    width, height = cover.size

    pdf = FPDF(unit = "pt", format = [width, height])
    for page in listPages:
        pdf.add_page()
        pdf.image(dir + str(page) + ".jpg", 0, 0)

    pdf.output(dir + pdfFileName + ".pdf", "F")

im1 = "D09HH00010-00001-i"
im2 = "D09HH00010-00002-i"
im3 = "D09HH00010-00003-i"
im4 = "D09HH00010-00004-i"
im5 = "D09HH00010-00005-i"
im6 = "D09HH00010-00006-i"
im7 = "D09HH00010-00007-i"
im_list = [im1,im2,im3,im4,im5,im6,im7]

makePdf('newPDF', im_list, dir = '')
'''

#ver2

def makePdf(jpgFileName):
    cover = Image.open(jpgFileName)
    width, height = cover.size

    pdf = FPDF(unit = "pt", format = [width, height])
    pdf.add_page()
    pdf.image(jpgFileName, 0, 0)
    path=os.path.abspath('.')
    pdfFilenName=jpgFileName
    pdfFilenName=pdfFilenName.replace('.jpg','.pdf')
    pdf.output(pdfFilenName, "F")
'''
for i in range (1,8):
    pageName="D09HH00010-0000"+str(i)
    newPDF="newPDF"+str(i)
    makePdf(newPDF,pageName , dir = '')
'''
def scan_files(directory,prefix=None,postfix=None):
    files_list=[]
    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(root,special_file))
            elif prefix:
                if special_file.startswith(prefix):
                        files_list.append(os.path.join(root,special_file))
            else:
                files_list.append(os.path.join(root,special_file))
    return files_list


path = os.path.abspath('.')
list=scan_files(path,prefix=None,postfix='.jpg')
print('running...')
if list:
    for name in list:
        makePdf(name)
        os.remove(name)
    print ('finished')










 
