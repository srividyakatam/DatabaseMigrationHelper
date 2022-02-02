import glob
from ReadConfig import program_config


def views_analysis():
    view_files = program_config["rootFolder"] + "\\" + program_config["viewsFolder"] + "\\*.sql"
    files = []
    for file in glob.glob(view_files):
        files.append(file)

    import re
    import os
    result_set = []
    for file in files:
        view1 = (open(file)).read()
        head, tail = os.path.split(file)
        search_joins = "(\s.+)?JOIN "
        search_schema_binding = "(\s.+)?WITH SCHEMABINDING"
        view_name = tail[:-4]
        has_joins = 0
        has_schema_binding = 0
        if re.search(search_joins, view1.upper()):
            has_joins = 1
        if re.search(search_schema_binding, view1.upper()):
            has_schema_binding = 1

        result1 = {"ViewName": view_name, "HasJOINS": has_joins, "HasSchemaBinding": has_schema_binding}
        result_set.append(result1)

    return result_set


if __name__ == '__main__':
    views_analysis()
    # print(views_analysis())
