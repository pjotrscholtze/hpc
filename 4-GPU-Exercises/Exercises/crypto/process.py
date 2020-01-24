

import json
from typing import Dict
skipable_files = "original2.data"

class Result:
    def __init__(self, filename: str, key: str, keysize: str, results: Dict[str, str], error: bool):
        self.filename = filename
        self.key = key
        self.keysize = keysize
        self.results = results
        self.error = error

    @property
    def encryption_sequential(self):
        return self.results["Encryption (sequential)"]
    
    @property
    def encrypt_kernel(self):
        return self.results["Encrypt (kernel)"]
    
    @property
    def encrypt_memory(self):
        return self.results["Encrypt (memory)"]
    
    @property
    def decryption_sequential(self):
        return self.results["Decryption (sequential)"]
    
    @property
    def decrypt_kernel(self):
        return self.results["Decrypt (kernel)"]
    
    @property
    def decrypt_memory(self):
        return self.results["Decrypt (memory)"]

clean_data = {}
sizes = []

with open("result.json", "r") as f:
    data = json.loads("".join(f.readlines()))

    for file_name in data:
        if file_name in skipable_files: continue
        clean_data[file_name] = {}
        for size in data[file_name]:
            key = data[file_name][size]['key']
            result = data[file_name][size]['result']
            parsed_results = {}
            error = False
            try:
                for line in result.split("\n"):
                    if ":" in line:
                        parts = line.split(":")
                        name = parts[0]
                        duration = parts[1].strip().split()[0]
                        parsed_results[name] = duration
                if size not in sizes:
                    sizes.append(size)
            except:
                parsed_results = line
                error = True
            clean_data[file_name][int(size)] = (Result(file_name, key, size, parsed_results, error))

def make_header(sizes, file_name):
    sorted_sizes = sorted([int(a) for a in sizes])
    sorted_sizes = [str(a) for a in sorted_sizes]

    t = """
            \\begin{table}[ht!]
                \caption{\\textit{3.4 results, filename %s }}
                \label{tbl:3_4_results_%s}
                \\begin{tabularx}{463.5pt}{|l|%s}
                    \hline
                    \cellcolor{black!100}\\textbf{\color{white}{Key size:}} & %s \\\\
    """ % (file_name,file_name, "r|" * (len(sizes) + 1), " ".join(["                    \cellcolor{black!100}\\textbf{\color{white}{%s}} &\n" % size for size in sorted_sizes])[:-3])
    return t
def make_footer():
    return """
            \hline
        \end{tabularx}
    \end{table}"""

tables = []


for file_name in clean_data:
    table_results = {
        "decryption_sequential": [],
        "decrypt_kernel": [],
        "decrypt_memory": [],
        "encryption_sequential": [],
        "encrypt_kernel": [],
        "encrypt_memory": [],
    }
    table_name_mapping = {
        "decryption_sequential": "dec. seq.",
        "decrypt_kernel": "dec. krnl",
        "decrypt_memory": "dec. mem",
        "encryption_sequential": "enc. seq.",
        "encrypt_kernel": "enc. krnl",
        "encrypt_memory": "enc. mem",
    }

    t = sorted(clean_data[file_name])

    keys = {}

    for size in t:
        item = clean_data[file_name][size]
        if item.error: continue
        item = item # type: Result
        item_res = {
            "decryption_sequential": item.decryption_sequential,
            "decrypt_kernel": item.decrypt_kernel,
            "decrypt_memory": item.decrypt_memory,
            "encryption_sequential": item.encryption_sequential,
            "encrypt_kernel": item.encrypt_kernel,
            "encrypt_memory": item.encrypt_memory,
        }
        keys[item.keysize] = item.key

        for field in item_res: 
            table_results[field].append(item_res[field])

    rows = []
    for i, row_name in enumerate(table_results):
        prepending = ["", "\cellcolor{black!10}"][i % 2]
        rows.append(" &\n".join(
            ["                    %s%s" % (prepending, cell) for cell in [table_name_mapping[row_name]]+table_results[row_name]]))

    key_list = """\\begin{itemize}
    %s
\\end{itemize}""" % ("\n".join(["    \item For key length '%s' used key '%s'" % (k, keys[k]) for k in keys]))
    tables.append(
        make_header(sizes, item.filename) + "\\\\\n\n".join(rows) + "\\\\\n" + make_footer() + key_list
    )

with open("table.latex", "w") as f:
    f.writelines(tables)

# print("\n".join(tables))
# print()
    