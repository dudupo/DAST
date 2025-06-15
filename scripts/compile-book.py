from os import system
def main():
    root = "../tex/lectures-TA/"
    notes = [ "lec-00.tex","lec-00-peaks.tex", "../../lyx/ex0-2024.tex", "lec-01.tex", "lec-02-v2.tex",  "../../lyx/ex2-2024.tex", "lec-reserves.tex", "lec-bst.tex", "../../lyx/ex4-2024.tex", "lec-probability.tex", "../../lyx/ex6-2024.tex" , "lec-03.tex", "lec-05.tex", "lec-08.tex", "lec-10.tex" , "lec-mst.tex", "lec-12.tex" ]
    book = "" 
    for i,chapter in enumerate(notes) :
        content = open(f"{root}{chapter}","r").read()   
        content = content.replace("title", "chapter")
        content = content.replace("abstract", "paragraph")
        content = content.replace("\\maketitle", "")
        content = content.replace("\\begin{algbox}", "\n%")
        content = content.replace("\\end{algbox}", "")
        content = content.replace("\\input{../tex/texlib/tail}", "")
        content = content.replace("\\input{../tex//texlib/tail}", "")
        content = content.replace("\\input{../tex/texlib/head}", "")
        content = content.replace("\\input{../tex/texlib/pack}", "")
        content = content.replace("\\input{../tex/lectures-TA/newcommands.tex}", "")
        content = content.replace("\\addbibresource{../tex/lectures-TA/sample.bib}", "")
        if "lyx" in chapter:
            content = content.replace("\\section", "\\subsection")
            content = content.replace("\\chapter", "\\section")
        
        if i > 0:
            content = content.replace("\\input{../texlib/head}", "")
            content = content.replace("\\input{../texlib/head.tex}", "")
            content = content.replace("\\begin{document}", "")
        if i < len(notes) - 1 :
            content = content.replace("\\input{../texlib/tail}", "")
            content = content.replace("\\end{document}", "")
        book +=  content 
        #book += r"""\newpage"""
    open(f"{root}book.tex", "w+").write(book)
    #system(f"./compile_doc.sh {root}book.tex")
    
if __name__ == "__main__":
    main()
