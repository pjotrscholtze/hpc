import read_slurms
from typing import List
from read_slurms import Result


def get_table_content_per_core() -> List[List[Result]]:
    tables = {} 
    for result in read_slurms.get_results():
        result = result # type: Result
        if result.cores not in tables:
            tables[result.cores] = []

        tables[result.cores] += [result]

    res = []
    for k in tables:
        res.append(tables[k])
    return res

def make_table(content: List[Result]):
    header_row = ["R", "Blocksize"]

    raw_header_items = []
    for item in content:
        if item.size_n not in raw_header_items:
            raw_header_items.append(item.size_n)

    raw_header_items = sorted(raw_header_items)
    header_row += [str(item) for item in raw_header_items]

    keyed_content = {}
    for item in content:
        if item.r_multiplier not in keyed_content:
            keyed_content[item.r_multiplier] = {}

        if item.block_size not in keyed_content[item.r_multiplier]:
            keyed_content[item.r_multiplier][item.block_size] = {}

        keyed_content[item.r_multiplier][item.block_size][item.size_n] = item
    
    body = []

    for r in sorted(keyed_content.keys()):
        for bs in sorted(keyed_content[r].keys()):
            row = [str(r), str(bs)]
            for n in sorted(keyed_content[r][bs].keys()):
                item = keyed_content[r][bs][n] # type: Result
                row += [str(item.time)]
            body += [row]


    return body
    # res = []
    # ###
    # #                         | > n_size
    # # r_size \/ block_size \/ |
    # for table_content in get_table_content_per_core():
    #     pass
    #     # for item in table_content:

print(make_table(get_table_content_per_core()[0]))
# print()


