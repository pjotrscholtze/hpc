#!/bin/python3
from typing import List

class Cell:
    def __init__(self, contents: str, prepending: str="", appending: str=""):
        self.contents = contents
        self.prepending = prepending
        self.appending = appending

    def latex(self) -> str:
        return self.prepending + self.contents + self.appending

class Row:
    def __init__(self, cells: List[Cell]=[]):
        self.cells = cells

    def latex(self) -> str:
        return "            " + (" & ".join([cell.latex() for cell in self.cells])) + " \\\\"

class Table:
    def __init__(self, rows: List[Row]=[], caption: str="", label: str="", 
        size: str="", alignment: str=""):
        self.rows = rows
        self.caption = caption
        self.label = label
        self.size = size
        self.alignment = alignment

    @property
    def _header_lines(self) -> List[str]:
        lines = [
            "\\begin{table}[ht!]",
        ]
        if self.caption: lines += ["    \caption{\\textit{%s}}" % self.caption]
        if self.label: lines += ["    \label{%s}" % self.label]
        size_argument = ""
        if self.size: size_argument = self.size

        if self.alignment and not size_argument:
            size_argument = "{}"

        lines += [
            "    \\begin{tabularx}%s{%s}" % (size_argument, self.alignment)
        ]

        return lines + ["        \hline"]
        
    @property
    def _footer_lines(self) -> List[str]:
        return [
            "        \hline",
            "    \end{tabularx}",
            "\end{table}"
        ]

    def latex(self) -> str:
        lines = self._header_lines

        for row in self.rows: lines += [row.latex()]

        return "\n".join(lines + self._footer_lines)

class TableBuilder:
    def __init__(self, caption: str="", label: str="", size: str="", 
        alignment: str="", zebra_rows: List[tuple]=[], 
        heading_style: (str,str,) = None):
        self.caption = caption
        self.label = label
        self.size = size
        self.alignment = alignment
        self.rows = []
        self.zebra_rows = zebra_rows
        self.heading_style = heading_style

    def add_raw_row(self, contents: List[str]):
        prepending, appending = "", ""
        if self.zebra_rows:
            prepending, appending = self.zebra_rows[len(self.rows) % len(self.zebra_rows)]
        self.rows.append(Row([Cell(cell, prepending, appending) for cell in contents]))
    
    def set_raw_header(self, cell_contents: List[str]):
        cells = []

        prepending, appending = "", ""
        if self.heading_style: prepending, appending = self.heading_style 
        for content in cell_contents:
            cells += [Cell(content, prepending, appending)]
        if not self.rows:
            self.rows = [Row(cells)]
        self.rows[0] = Row(cells)

    def get_table(self) -> Table:
        return Table(self.rows, self.caption, self.label, self.size, self.alignment)

if __name__ == "__main__":
    # tbl = Table(rows = [Row()])
    tb = TableBuilder(heading_style=("{", "}"))
    tb.set_raw_header(["a","b"])
    tbl = tb.get_table()
    # tbl.rows[0].cells = [Cell("test")]

    print(tbl.latex())