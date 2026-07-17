import zipfile, re, os
base = os.getcwd()
files = ['26-02_curricolo-europeo.docx', '16-10 Curricolo.docx']
for f in files:
    p = os.path.join(base, f)
    print('===', f, '===')
    with zipfile.ZipFile(p) as z:
        xml = z.read('word/document.xml').decode('utf-8', errors='ignore')
    text = re.sub(r'<[^>]+>', '\n', xml)
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('&amp;', '&')
    print(text[:30000])
    print('\n')
