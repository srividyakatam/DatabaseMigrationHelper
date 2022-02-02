import pandas as pd
from ReadConfig import program_config


def write_to_excel(table_info=None, procedure_info=None, views_info=None,function_info=None):
    tab_info = pd.DataFrame()
    prc_info = pd.DataFrame()
    v_info = pd.DataFrame()
    func_info = pd.DataFrame()
    if table_info is not None:
        tab_info = pd.DataFrame(data=table_info)
    if procedure_info is not None:
        prc_info = pd.DataFrame(data=procedure_info)
    if views_info is not None:
        v_info = pd.DataFrame(data=views_info)
    if function_info is not None:
        func_info = pd.DataFrame(data=function_info)
    with pd.ExcelWriter(program_config["outputFileName"]) as writer:
        tab_info.to_excel(writer, sheet_name='tables', index=False)
        prc_info.to_excel(writer, sheet_name='procedures', index=False)
        v_info.to_excel(writer, sheet_name='views', index=False)
        func_info.to_excel(writer, sheet_name='functions', index=False)


if __name__ == '__main__':
    sample_info = [{"TableName": 'sample_table'
                       , "HasPrimaryKey": 1
                       , "HasForeignKeyReference": 0
                       , "HasIndex": 1, "HasConstraint": 1
                    }]
    write_to_excel(sample_info)
