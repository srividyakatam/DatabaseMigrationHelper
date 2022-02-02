import glob
from ReadConfig import program_config


def function_analysis():
    func_files = program_config["rootFolder"] + "\\" + program_config["functionsFolder"] + "\\*.sql"
    files = []
    for file in glob.glob(func_files):
        files.append(file)

    import re
    import os
    result_set = []
    for file in files:
        func1 = (open(file)).read()
        head, tail = os.path.split(file)
        search_joins = "(\s.+)?JOIN "
        search_return_type = "(\s.+)?RETURNS TABLE"
        func_name = tail[:-4]
        has_joins = 0
        returns_table = 0
        if re.search(search_joins, func1.upper()):
            has_joins = 1
        if re.search(search_return_type, func1.upper()):
            returns_table = 1

        result1 = {"FunctionName": func_name, "HasJOINS": has_joins, "TableValuedFunction": returns_table}
        result_set.append(result1)

    return result_set


if __name__ == '__main__':
    function_analysis()
    # print(function_analysis())
