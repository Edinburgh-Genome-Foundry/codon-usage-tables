import os


_this_dir = os.path.dirname(os.path.realpath(__file__))
_tables_dir = os.path.join(_this_dir, '..', "data", "tables")

available_tables = [filename[:-4] for filename in os.listdir(_tables_dir)]

def get_table(table_name):
    result = {}
    with open(os.path.join(_tables_dir, table_name + '.csv'), 'r') as f:
        for line in f.read().split("\n")[1:]:
            aa, codon, freq = line.split(',')
            if aa not in result:
                result[aa] = {}
            result[aa][codon] = float(freq)
    return result

def get_all_tables():
    return {
        table_name: get_table(table_name)
        for table_name in available_tables
    }
