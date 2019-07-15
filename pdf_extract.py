#pdf extract

import PyPDF2

import configparser
config = configparser.RawConfigParser()
config.read('config.ini')

filename = config.get('Local', 'pfd_file_path')
print (filename)


def extractPdfText(filePath=''):

    # Open the pdf file in read binary mode.
    fileObject = open(filePath, 'rb')

    # Create a pdf reader .
    pdfFileReader = PyPDF2.PdfFileReader(fileObject)

    # Get total pdf page number.
    totalPageNumber = pdfFileReader.numPages
    print(totalPageNumber)

    # Print pdf total page number.
    print('This pdf file contains totally ' + str(totalPageNumber) + ' pages.')

    currentPageNumber = 0
    text = ''
    print (currentPageNumber)
    # Loop in all the pdf pages.
    while(currentPageNumber < totalPageNumber ):

        # Get the specified pdf page object.
        pdfPage = pdfFileReader.getPage(currentPageNumber)

        # Get pdf page text.
        text = text + pdfPage.extractText()

        # Process next page.
        currentPageNumber += 1
      
    return text

if __name__ == '__main__': 
 
    pdfText = extractPdfText(filename)
    print('There are ' + str(pdfText.__len__()) + ' word in the pdf file.')
    print(pdfText)

