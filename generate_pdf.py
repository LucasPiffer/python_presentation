import pdfkit

pdfkit.from_url('http://google.com', 'piffer.pdf')
# pdfkit.from_file('test.html', 'out.pdf')
# pdfkit.from_string('Hello!', 'out.pdf')