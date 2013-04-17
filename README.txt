Repo dedicado à descrição psicofísica da música no áudio digital e implementações.

Versão atual no arquivo dissertacaoCorrigida.pdf. Link direto:
https://github.com/ttm/dissertacao/blob/msc/dissertacaoCorrigida.pdf?raw=true

Pastas relevantes:
scripts: scripts de provas de conceito e figuras, com implementações de quase todas as equações da dissertação.
figuras: figuras da dissertação.



======================
contatos:

#labmacambira @ Freenode:
http://webchat.freenode.net/?channels=#labmacambira
e
renato (ponto) fabbri _@_ GMAIL (ponto) com

logs de aa +msc

=====================
Para obtenção do arquivo PDF atual:
$ pdflatex dissertacao.tex
$ bibtex dissertacao
$ pdflatex dissertacao.tex
$ pdflatex dissertacao.tex
$ pdftk A=dissertacao.pdf B=ficha.pdf C=referencias-\ renato1.pdf cat A1-3 B1 A5-126 C1-7 A134-255 output dissertacaoCorrigida.pdf
