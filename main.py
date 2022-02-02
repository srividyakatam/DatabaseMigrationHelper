from ReadConfig import program_config
from Table_Analysis import table_analysis
from Procedure_Analysis import procedure_analysis
from Views_Analysis import views_analysis
from Function_Analysis import function_analysis
from Write_To_Excel import write_to_excel


if __name__ == '__main__':
    table_information = []
    procedure_information = []
    views_information = []
    function_information = []
    if program_config["runTableAnalysis"] == 1:
        table_information = table_analysis()
    if program_config["runProcedureAnalysis"] == 1:
        procedure_information = procedure_analysis()
    if program_config["runViewsAnalysis"] == 1:
        views_information = views_analysis()
    if program_config["runFunctionAnalysis"] == 1:
        function_information = function_analysis()
    # print(len(table_information), len(procedure_information), len(views_information), len(function_information))
    write_to_excel(table_information, procedure_information,views_information,function_information)
