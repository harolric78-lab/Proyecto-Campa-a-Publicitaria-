p = r'C:\Users\LA RUEDA\Desktop\Poyectos Matcom\Proyecto de campana publicitaria\make_pdf_academic.py'
s = open(p, encoding='utf-8').read()
s = s.replace('"])', '"]))')
open(p, 'w', encoding='utf-8').write(s)
print('done')
