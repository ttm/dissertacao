# encoding: utf-8

import os

# antes de tudo, instale o pandoc: sudo apt-get install pandoc
# ele eh um canivete suico para formatos de documentos
# mais em http://johnmacfarlane.net/pandoc/

# convertemos cada arquivo .tex do diretorio abaixo
# e para mostrar as equacoes, usamos mathjax

tex = ['introducao',
       'devEresultados',
       'conclusoes',
       'codigoProcedimentos',
       'codigoPecas',
       'FIGGUScode',
       'fmam',
       'musicaExtra']

titulo = 'Música no áudio digital: descrição psicofísica e caixa de ferramentas'
autor = 'Renato Fabbri'
instituicao = 'Universidade de São Paulo <br /> Instituto de Física de São Carlos <br />  Departamento de Física e Informática <br /> Grupo de Física Computacional e Instrumentação Aplicada'
orientador = 'Prof. Dr. Osvaldo Novais de Oliveira Junior'
coorientador = 'Prof. Dr. Luciano da Fontoura Costa'

for t in tex:
    os.system('pandoc ../%s.tex -s --listings --mathjax=http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML -o %s.html' % (t,t))

# geramos um index simples apontando para cada arquivo html gerado

index = open('index.html', 'w')

index.write('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><title>%s</title></head><body><h1>%s</h1><h2>%s</h2><h3>%s</h3><ul>' % (titulo, titulo, autor, instituicao))
for t in tex:
    index.write('<li><a href="%s.html">%s</li>' % (t, t.capitalize()))
index.write('</ul></body></html>')
