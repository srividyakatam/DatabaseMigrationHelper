import glob
from ReadConfig import program_config


def procedure_analysis():
    procedure_files = program_config["rootFolder"] + "\\" + program_config["proceduresFolder"] + "\\*.sql"
    files = []
    for file in glob.glob(procedure_files):
        files.append(file)

    import re
    import os
    result_set = []
    for file in files:
        procedure1 = (open(file)).read()
        head, tail = os.path.split(file)
        search_cursors = r'(?<=DECLARE)(\s.+)?CURSOR'
        search_while_loop = r'(?<=WHILE)(\s.+)?BEGIN'
        procedure_name = tail[:-4]
        has_cursor = 0
        has_while_loop = 0
        has_more_code = 0
        if len(re.findall(search_cursors,procedure1.upper(),re.DOTALL)) > 0:
            has_cursor = 1
        if len(re.findall(search_while_loop,procedure1.upper(),re.DOTALL)) > 0:
            has_while_loop = 1
        lines = procedure1.split("\n")
        if len(procedure1) > 400:
            has_more_code = 1

        result1 = {"ProcedureName": procedure_name, "HasCursor": has_cursor, "HasWhileLoop": has_while_loop, "HasMoreThan400Lines": has_more_code}
        result_set.append(result1)

    return result_set


if __name__ == '__main__':
    procedure_analysis()
    # print(procedure_analysis())
