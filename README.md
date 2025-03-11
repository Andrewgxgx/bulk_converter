# bulk_converter
a collection of scripts that can convert many files from one file extension to another.
> Note: This does not work on windows, only on macos and linux, if you want this to work on windows, use WSL.

# Quick Start

1. Clone this repo using git clone 

> ```git clone https://github.com/Andrewgxgx/bulk_converter.git```

View the [overview file path](#file-path)
- [Document Conversion Guide](#document-converter)
    - [See supported file extension](#supported-file-extensions)




## Document Converter

> **Requirements** 

To be able to use the document converter, you must have these in your system installe
- python 3
- calibre

1. copy / move all your files that you will convert into the `input` folder. 

2. Then CD into the folder 

`cd 'document converter'` 

3. Then run your python script

    1. supported extension to pdf 

        `python3 xtopdf.py`

    2. supported extension to epub

        `python3 xtoepub.py`

    3. Supported extension to html 

        `python3 xtohtml.pdf`

4. All of the files will be in ./output after it gets converted


### Supported file extensions
1. *.pdf 
2. *.epub
3. *.lit
4. *.mobi
5. *.fb2
6. *.rtf
7. *.html
8. *.txt
9. *.doc
10. *.docx
11. *.odt




---
# Credit
All of these scripts are licensed under MIT license, if you find a bug or something wrong, feel free to open an issue or open a Pull Request.

# NOTE
Please use this responsibly, i will not take any responsibility for any pirated content that is converted using this tool.

This tool is meant for legit use and for digital media collectors, to convert many files easily, if you just need to convert one or two files to another extension, just convert it online or download a specific library that does the job well.


# file path
```
| Bulk_Converter 
    | document converter
        | xtoepub.py
        | xtohtml.py
        | xtopdf.py
    | input
    | output
    | venv
    | LICENSE
    | README.md
```
