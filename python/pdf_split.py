# coding: utf-8
# Purpose: 古籍PDF从中间切割，并重新组合
# Author: MinYi
# Create Time: 2021.09.04 17：15
from PyPDF2 import PdfFileWriter, PdfFileReader
from copy import copy
import sys


def op(input_file_path):
    output_file_path = input_file_path[:-4] + '-new.pdf'
    input_file = open(input_file_path, 'rb')
    input_stream = PdfFileReader(input_file)
    output_stream = PdfFileWriter()
    outlines = input_stream.getOutlines()
    total_pages = input_stream.getNumPages()
    flag = 0

    while flag < total_pages:
        # print(flag)
        page = input_stream.getPage(flag)
        page_left = page
        # 注意：简单的assignment会导致左、右切割操作同一页面对象
        page_right = copy(page)

        # 左页面
        page_left.mediaBox.upperRight = (
            page_left.mediaBox.getUpperRight_x() / 2,
            page_left.mediaBox.getUpperRight_y())

        # 右页面
        page_right.mediaBox.lowerLeft = (
            page_right.mediaBox.getLowerRight_x() / 2,
            page_right.mediaBox.getLowerRight_y())

        page_right.mediaBox.upperLeft = (
            page_right.mediaBox.getUpperRight_x() / 2,
            page_right.mediaBox.getUpperRight_y())

        output_stream.addPage(page_right)
        output_stream.addPage(page_left)

        # 如何实现添加书签
        # for s in list(outlines):
        #    print(s['/Title'], s['/Page']['/Contents'])
        # outputStream.addBookmark(s['/Title'], s['/Page']['/Contents'])
        flag = flag + 1

    # 添加书签
    # 二级书签如何添加？
    book_tag_info = []
    # 程序還需要改進
    ref = None
    for s in outlines:
        try:
            page_number = input_stream.getDestinationPageNumber(s) + 1
            title = s.title
            # book_tag_info.append(s.title, page_number)
            ref = output_stream.addBookmark(s.title, page_number*2 - 1)
        except Exception as e:
            print(e, 'error')
            for m in s:
                page_number = input_stream._getPageNumberByIndirect(m.page)
                output_stream.addBookmark(m.title, page_number*2, parent=ref)

    with open(output_file_path, "wb") as output_file:
        output_stream.write(output_file)

    input_file.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} <FILE_NAME>')
        print(f'Example: python {sys.argv[0]} F:/pdf/聊斋志异.十六卷.清.蒲松龄.撰.清乾隆三十一年青柯亭刊本.普清.pdf')
        exit(1)
    else:
        file_name = sys.argv[1]
        op(file_name)
