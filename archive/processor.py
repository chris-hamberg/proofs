from pprint import pprint
import os

DIR  = 'LaTeX/2.4 Sequences and Summations'
DOC  = '2.4 compilation/2.4 compilation.tex'
PRE1 = r'''\documentclass[preview]{standalone}
\usepackage{amssymb, amsthm}
\usepackage{mathtools}
\usepackage{bm}
\usepackage{xcolor}


'''
THEOREM = r'\newtheorem*{theorem*}{Theorem}'
LEMMA   = r'\newtheorem*{lemma*}{Lemma}'
PRE2 = r'''
\renewcommand\qedsymbol{$\blacksquare$}


\begin{document}


'''


class Theorem:

    def __init__(self, name, oname, begin, end, data):
        self.name     = name
        self.oname    = oname
        self.begin    = begin
        self.end      = end
        self.data     = data
        self.preamble = PRE1 + THEOREM + PRE2
        self.init()

    def init(self):
        self.directory = self.name.split(' ')[-1]
        self.file  = self.name.split(' ')[-1] + '.tex'
        self.path  = os.path.join(self.directory, self.file)

    def makedir(self):
        if not os.path.exists(self.directory):
            os.mkdir(os.path.join(DIR, self.directory))

    def makefile(self):
        with open(os.path.join(DIR, self.path), 'w') as fhand:
            fhand.write(self.preamble)
            fhand.write(self.data + '\n\n')
            fhand.write(r'\end{document}')

    def __repr__(self):
        start = self.data.index('\n')
        end   = len(self.data)
        return f'{self.name}: {self.data[start:50]} ... {self.data[end-50:]}'


class Lemma(Theorem):
    
    def __init__(self, name, oname, begin, end, data):
        self.name     = name
        self.oname    = oname
        self.begin    = begin
        self.end      = end
        self.data     = data
        self.preamble = PRE1 + LEMMA + PRE2
        self.init()

    def init(self):
        self.directory = self.name.split(' ')[-1]+'L'
        self.file  = self.name.split(' ')[-1] + 'L.tex'
        self.path  = os.path.join(self.directory, self.file)


class Document:

    def __init__(self, directory=DIR, document=DOC):

        self.directory = directory
        self.document  = document
        self.path = os.path.join(self.directory, self.document)

        with open(self.path, 'r') as fhand:
            self.chapter = fhand.read()

        self.backup()
        self.bounds()
        self.blocks()

    def backup(self):
        directory, file = self.document.split(os.sep)
        name = 'BACKUP_'+file
        target = os.path.join(self.directory, directory, name)
        if not os.path.exists(target):
            with open(target, 'w') as fhand:
                fhand.write(self.chapter)

    def bounds(self):
        self.limits = []
        for line in self.chapter.split('\n'):
            if '% =====' in line:
                self.limits.append(self.chapter.index(line))
        self.limits.append(self.chapter.index(line))

    def rename(self, name):
        name = name.split('.')
        if len(name[-1]) == 3:
            pass
        elif len(name[-1]) == 2:
            try:
                int(name[-1])
            except ValueError as alpha:
                name[-1] = name[-1].zfill(3)
        else:
            name[-1] = name[-1].zfill(2)
        return ''.join(name)            

    def blocks(self):
        self.theorems = []
        length = len(self.limits) - 1
        for i in range(length):
            extract = self.chapter[self.limits[i]:self.limits[i+1]]
            if r'\begin{proof}' not in extract:
                continue
            name = extract.split('\n')[0].replace('=', '')
            name = name.replace('%', '').strip()
            newname = self.rename(name).rstrip()
            begin = self.limits[i]
            end = extract.index('\end{proof}') + len('\end{proof}') + begin
            data = '\n'.join(self.chapter[begin:end].split('\n')[1:])
            data = data.replace(name.split(' ')[-1], newname.split(' ')[-1])
            if r'\begin{theorem*}' in extract:
                self.theorems.append(
                        Theorem(newname, name, begin, end, data)
                        )
            else:
                self.theorems.append(
                        Lemma(newname, name, begin, end, data)
                        )

def patch(doc):
    with open(doc.path, 'w') as fhand:
        fhand.write(doc.chapter)

def main():
    doc = Document()
    for theorem in reversed(doc.theorems):
        theorem.makedir()
        theorem.makefile()
        if isinstance(theorem, Lemma):
            delimiter = r'\begin{lemma*}'
        else:
            delimiter = r'\begin{theorem*}'
        index = doc.chapter[theorem.begin:].index(
                delimiter) + theorem.begin
        doc.chapter = doc.chapter.replace(
                doc.chapter[index:theorem.end],
                f'\input{{../{theorem.path}}}\n'
                )
        doc.chapter = doc.chapter.replace(theorem.oname, theorem.name)
        #input(theorem.data)
    #print(doc.chapter)
    patch(doc)

if __name__ == '__main__':
    main()
