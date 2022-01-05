import csv
import json
import globals

fuzzy_variable_template = {
    'internal_name' : "internal_name_2",
    'nice_name' : "Nice Name",
    'universe_of_discourse' : [0.0, 50.0],
    'fuzzy_type' : 'fuzzy',
    'function_types' : {
        'foo' : 'Endpoint',
        'bar' : 'Trapezoidal',
        'nuar' : 'Trapezoidal'
    },
    'values' : {
        'foo' : [0, 0.0, 5.0, 10.0],
        'bar' : [4.0, 12.0, 20.0, 25.0],
        'nuar' : [19.0, 25.0, 50.0, 50.0]
    }
}

crisp_variable_template = {
    'internal_name' : "crispy",
    'nice_name' : "Nice Lol",
    'universe_of_discourse' : [0, 2],
    'fuzzy_type' : 'crisp',
    'function_types' : {
        'boo' : 'Endpoint',
        'far' : 'Trapezoidal',
    },
    'values' : {
        'bar' : [0, 1],
        'foo' : [1, 2],
    }
}


def save_fuzzy_variables(fuzzy_variables, overwrite=False):
    dumped_dict = {}

    if overwrite:
        for var in fuzzy_variables:
            dumped_dict[var.get('internal_name')] = var
    else:
        current_settings = load_fuzzy_variables()

        for var in fuzzy_variables:
            current_settings[var.get('internal_name')] = var
        dumped_dict = current_settings.copy()
    json_file = open(globals.FUZZY_VARIABLES_FILE, 'w')
    json_file.write(json.dumps(dumped_dict, indent=4))
    json_file.close()


def load_fuzzy_variables():
    json_file = open(globals.FUZZY_VARIABLES_FILE, "r")
    fuzzy_variables = json.loads(json_file.read())
    json_file.close()
    return fuzzy_variables


def gen_init_fuzzy_values(values_names):
    result = {}
    for name in values_names:
        result[name] = [0.0, 0.0, 0.0, 0.0]
    return result


def gen_init_crisp_values(values_names):
    result = {}
    i = 1.0
    for name in values_names:
        result[name] = [i-1, i].copy()
        i += 1
    return result


def init_fuzzy_file():
    linguistic_variables = []

    with open(globals.LINGUISTIC_VALUES_FILE, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in list(reader)[1:]:
            row = list(filter(lambda item: item, row))
            new_fuzzy_var = fuzzy_variable_template.copy()
            new_fuzzy_var['internal_name'] = row[0]
            new_fuzzy_var['nice_name'] = row[1]
            if row[2] == 'fuzzy':
                new_fuzzy_var['fuzzy_type'] = 'fuzzy'
                new_fuzzy_var['values'] = gen_init_fuzzy_values(row[3:])
                new_fuzzy_var['universe_of_discourse'] = [0.0, 1.0]
            elif row[2] == 'crisp':
                new_fuzzy_var['fuzzy_type'] = 'crisp'
                new_fuzzy_var['values'] = gen_init_crisp_values(row[3:])
                new_fuzzy_var['universe_of_discourse'] = [0.0, float(len(row[3:]))]
            linguistic_variables.append(new_fuzzy_var)

    save_fuzzy_variables(linguistic_variables, True)