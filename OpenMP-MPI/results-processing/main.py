import read_slurms
from typing import List
from read_slurms import Result
from latex_generator import TableBuilder

def get_table_content_per_core() -> List[List[Result]]:
    tables = {} 
    for result in read_slurms.get_results():
        result = result # type: Result
        if result.cores not in tables:
            tables[result.cores] = []

        tables[result.cores] += [result]

    res = [tables[2]]
    for k in tables:
        res.append(tables[k])
    return res

def make_table(content: List[Result]):
    header_row = ["R"]

    raw_header_items = []
    for item in content:
        if "N: " + str(item.size_n) not in raw_header_items:
            raw_header_items.append("N: " + str(item.size_n))

    raw_header_items = sorted(raw_header_items)
    header_row += [str(item) for item in raw_header_items]

    keyed_content = {}
    for item in content:
        if item.r_multiplier not in keyed_content:
            keyed_content[item.r_multiplier] = {}

        # if item.block_size not in keyed_content[item.r_multiplier]:
        #     keyed_content[item.r_multiplier][item.block_size] = {}

        if item.size_n not in keyed_content[item.r_multiplier]:
            keyed_content[item.r_multiplier][item.size_n] = item

        if keyed_content[item.r_multiplier][item.size_n].error and not item.error:
            keyed_content[item.r_multiplier][item.size_n] = item

    
    body = []

    for r in sorted(keyed_content.keys()):
        # for bs in sorted(keyed_content[r].keys()):
        row = [str(r)]
        for n in sorted(keyed_content[r].keys()):
            item = keyed_content[r][n] # type: Result
            row += [str(item.time)]
        body += [row]


    return header_row, body
    # res = []
    # ###
    # #                         | > n_size
    # # r_size \/ block_size \/ |
    # for table_content in get_table_content_per_core():
    #     pass
    #     # for item in table_content:

def make_latex_table(header, body, block_size, cores):
    tb = TableBuilder(heading_style=("\cellcolor{black!100}\\textbf{\color{white}{", "}}"),
        zebra_rows=[("\cellcolor{black!10}", "",),("","",)], alignment="|l|r|r|r|r|",
        caption="Blocksize: %s, cores: %s" %( str(block_size), str(cores)), label="tbl:perf:blocksize%s:cores:%s" %(str(block_size), str(cores)))
    tb.set_raw_header(header)
    for row in body:
        tb.add_raw_row(row)

    tbl = tb.get_table()
    # tbl.rows[0].cells = [Cell("test")]

    print(tbl.latex())

for tbl in get_table_content_per_core():
    header, body = make_table(tbl)
    
    make_latex_table(header, body, tbl[0].block_size, tbl[0].cores)

# print()

