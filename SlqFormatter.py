class SqlFormatter(object):
    input_path = ""
    output_path = ""
    line = ""
    commonReplacement = {'\n': ' ', r'\t': ' ', ' ,': ','}
    wordsToFind = {'select ': 'select\n\t', ', ': ',\n\t', ',': ',\n\t', ' then ': '\n\t\tthen ', ' else ': '\n\t\telse ', 'end': '\n\tend', 'from': '\nfrom', 'inner': '\ninner', 'left': '\nleft', 'rigth': '\nrigth', 'join': '\njoin', ' on ': '\n\ton ', ' on(': '\n\ton(', ' and ': '\n\tand ', ' where ': '\nwhere ', ' order ': '\norder ', '\n\t\n\t': '\n\t', '\n\n': '\n' } 
    lastClean = {'left \njoin': 'left join', 'rigth \njoin': 'rigth join', 'inner \njoin': 'inner join', 'outer \njoin': 'outer join'}

    def __init__(self, input_path, output_path):
        self.input_path = input_path
        
        self.output_path = output_path

    def format(self):
        with open(self.input_path, 'r') as f:
            lines = f.readlines()

            for line in lines:
                with open(self.output_path, 'a') as f:
                    f.write(self.replace(line) + f'\n---------------------------------------------------------------\n')
                
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

formatter = SqlFormatter("test.txt", "output.txt")
formatter.format()