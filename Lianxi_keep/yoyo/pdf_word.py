from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed


def parse():
    fn = open('F:\管理干部\认知训练营\王烁30天认知训练营学习音频\\30天认知训练营01-06讲\ws00发刊词  直面现实，认知升级.pdf', 'rb')
    parser = PDFParser(fn)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize()
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        resource = PDFResourceManager()
        laparms = LAParams()
        device = PDFPageAggregator(resource, laparms=laparms)
        interpreter = PDFPageInterpreter(resource, device)
        for page in doc.get_pages:
            interpreter.process_page(page)
            layout = device.get_result
            for out in layout:
                if hasattr(out, "get_text"):
                    print(out.get_text)
                    with open('test.txt', 'a') as f:
                        f.write(out.get_text + '\n')


if __name__ == "__main__":
    parse()
