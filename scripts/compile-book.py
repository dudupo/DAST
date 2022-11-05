def main():
    root = "../tex/lectures-TA/"
    notes = [ "lec-01.tex", "lec-02-v2.tex", "lec-03.tex" ]
    book = "" 
    for i,chapter in enumerate(notes) :
        content = open(f"{root}{chapter}","r").read()   
        content = content.replace("title", "section")
        content = content.replace("abstract", "paragraph")
        content = content.replace("\maketitle", "")
        if i > 0:
            content = content.replace("\input{../texlib/head}", "")
        if i < len(notes) - 1 :
            content = content.replace("\input{../texlib/tail}", "")
        book += content
    open(f"{root}book.tex", "w+").write(book)
    
if __name__ == "__main__":
    main()
