import re

class SqlFormatter(object):
    input_path = ""
    report_name = ""
    line = ""
    database = ""
    commonReplacement = {}
    wordsToFind = {}
    lastClean = {}

    def __init__(self, input_path, report_name, database):
        self.input_path = input_path
        self.report_name = report_name
        self.database = database
        self.commonReplacement = {'spark.sql("': '', '");': ';', '" + database + "': f'{self.database}', r'\n': ' ', r'\t': ' ', ' ,': ',', }
        self.wordsToFind = {'select ': 'select\n\t', ', ': ',\n\t', ',': ',\n\t', ' then ': '\n\t\tthen ', ' else ': '\n\t\telse ', 'end': '\n\tend', 'from': '\nfrom', 'inner': '\ninner', 'left': '\nleft', 'rigth': '\nrigth', 'join': '\njoin', ' on ': '\n\ton ', ' on(': '\n\ton(', ' and ': '\n\tand ', ' where ': '\nwhere ', ' order ': '\norder ', '\n\t\n\t': '\n\t', '\n\n': '\n' } 
        self.lastClean = {'left \njoin': 'left join', 'rigth \njoin': 'rigth join', 'inner \njoin': 'inner join', 'outer \njoin': 'outer join'}

    def format(self):
        sql_file_name = f'{self.report_name}.sql'
        with open(self.input_path, 'r') as f:
            lines = f.readlines()

            for line in lines:
                with open(sql_file_name, 'a') as o:
                    o.write(self.replace(line) + f'\n---------------------------------------------------------------\n')
        
        self.printTables(sql_file_name, self.report_name)
                
    def replace(self, line):
        line = line.lower()

        #Common replacement for cleaning tabs, doble spaces and lines breaks
        for x, y in self.commonReplacement.items():
            line = line.replace(x, y)

        while line.count('  ') :
            line = line.replace('  ', ' ')

        for x, y in self.wordsToFind.items():
            line = line.replace(x, y)

        for x, y in self.lastClean.items():
            line = line.replace(x, y)

        return line

    def printTables(self, input_file, output_file):
        tables = []
        with open(input_file, 'r') as f:
            lines = f.readlines()

            for line in lines:
                line =  line.lower()
                table = re.search(r"(from|join) (\w+.\w+)", line)
                
                if(table):
                    tables.append(table.group(2))
        
        tables.sort()
        tables = list(dict.fromkeys(tables))

        with open(f'{output_file}-tables.txt', 'a') as f:
            for x in tables:
                f.write(f'{x}\n')

formatter = SqlFormatter("input.txt", "caratula_per", "zdm_ssso")
formatter.format()