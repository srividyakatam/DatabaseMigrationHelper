import glob
from ReadConfig import program_config


def table_analysis():
    table_files = program_config["rootFolder"] + "\\" + program_config["tablesFolder"] + "\\*.sql"
    files = []
    for file in glob.glob(table_files):
        files.append(file)

    import re
    result_set = []
    for file in files:
        table1 = (open(file)).read()
        search_table_name = "CREATE TABLE (.+?) "
        search_constraints = " CONSTRAINT (.+?)"
        search_foreign_key = " FOREIGN KEY (.+?)"
        search_indexes = " INDEX (.+?)"
        search_primary_key = " PRIMARY KEY (.+?)"
        table_name = ""
        has_constraint = 0
        has_foreign_key_reference = 0
        has_primary_key = 0
        has_index = 0
        if re.search(search_table_name, table1):
            table_name = re.search(search_table_name, table1).group(1)
        if re.search(search_constraints, table1):
            has_constraint = 1
        if re.search(search_foreign_key, table1):
            has_foreign_key_reference = 1
        if re.search(search_indexes, table1):
            has_index = 1
        if re.search(search_primary_key, table1):
            has_primary_key = 1
        result1 = {"TableName": table_name, "HasPrimaryKey": has_primary_key, "HasForeignKeyReference": has_foreign_key_reference, "HasIndex": has_index, "HasConstraint": has_constraint}
        result_set.append(result1)

    # print(len(result_set))
    return result_set


if __name__ == '__main__':
    table_analysis()
