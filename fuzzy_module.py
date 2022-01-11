import random

from simpful import *

import util
import global_params


class FuzzyModule(object):
    def __init__(self):
        self.fuzzy_sets = fuzzify_all_variables()
        self.fuzzy_rules = load_rules()
        self.contracting_fs = FuzzySystem()
        # self.quality_fs = FuzzySystem()
        # self.supplying_fs = FuzzySystem()
        # self.communication_fs = FuzzySystem()
        # self.finance_and_assets_fs = FuzzySystem()
        # self.compliance_fs = FuzzySystem()
        # self.EHS_fs = FuzzySystem()
        self.main_fuzzy_system = FuzzySystem()
        for name, var in self.fuzzy_sets.items():
            self.main_fuzzy_system.add_linguistic_variable(name, var)

        self.contract_price = 0.0
        self.contract_type = 0.0
        self.experience = 0.0
        self.overall_quality = 0.0
        self.delayed_deliveries = 0.0
        self.average_delay_delivery = 0.0
        self.information_share = 0.0
        self.overall_communications = 0.0
        self.financial_sustainability = 0.0
        self.overall_compliance = 0.0
        self.has_necessary_certification = 0.0
        self.court_history = 0.0
        self.environment_safety = 0.0
        self.work_safety = 0.0

        self.contracting_fs.add_linguistic_variable('contract_price', self.fuzzy_sets.get('contract_price'))
        self.contracting_fs.add_linguistic_variable('contract_type', self.fuzzy_sets.get('contract_type'))
        self.contracting_fs.add_linguistic_variable('financial_sustainability',
                                                    self.fuzzy_sets.get('financial_sustainability'))
        self.contracting_fs.add_linguistic_variable('contract_risk', self.fuzzy_sets.get('contract_risk'))
        self.contracting_fs.add_rules(self.fuzzy_rules.get('Contracting'))

        # self.supplying_fs.add_linguistic_variable('delayed_deliveries', self.fuzzy_sets.get('delayed_deliveries'))
        # self.supplying_fs.add_linguistic_variable('delayed_deliveries', self.fuzzy_sets.get('delayed_deliveries'))
        # self.supplying_fs.add_linguistic_variable('average_delay_delivery',
        #                                           self.fuzzy_sets.get('average_delay_delivery'))
        self.main_fuzzy_system.add_linguistic_variable('Supplying', get_uniform_four_set())
        self.main_fuzzy_system.add_linguistic_variable('Quality_as_BP', get_uniform_four_set())
        self.main_fuzzy_system.add_linguistic_variable('Communications', get_uniform_four_set())
        self.main_fuzzy_system.add_linguistic_variable('Legal_and_Compliance', get_uniform_four_set())
        self.main_fuzzy_system.add_linguistic_variable('EHS', get_uniform_four_set())
        self.main_fuzzy_system.add_rules(self.fuzzy_rules.get('Main'))

        # self.main_fuzzy_system.set_variable('delayed_deliveries', 5)
        # self.main_fuzzy_system.set_variable('contract_type', 0)
        # self.main_fuzzy_system.set_variable('financial_sustainability', 10)
        # self.main_fuzzy_system.set_variable('contract_price', 500000)
        # self.main_fuzzy_system.set_variable("average_delay_delivery", 0.5)
        # self.main_fuzzy_system.set_variable('overall_quality', 9)

    def set_variables_val_in_module(self, variables_values):
        ch = random.uniform(0,3)
        print(ch)
        self.main_fuzzy_system.set_variable('court_history', ch)
        for k, v in variables_values.items():
            if k not in global_params.COURT_VARIABLES_NAMES:
                self.main_fuzzy_system.set_variable(k, v)

    def fire_main_fuzzy_system(self, version=0):
        firing_result = self.main_fuzzy_system.inference()
        weights = util.load_score_weights(version)

        weighted_final_scores = []
        for k, v in firing_result.items():
            rescale_weight = util.load_score_weights('RESULT_WEIGHT_FACTOR')
            print(rescale_weight)
            rescaled_score = rescale_weight*(abs(5 - v)/4)
            firing_result[k] = rescaled_score
            weight = weights.get(k, False)
            if weight:
                weighted_final_scores.append(v*rescaled_score)
            else:
                weighted_final_scores.append(rescaled_score)

        weighted_avg = sum(weighted_final_scores)/len(weighted_final_scores)
        return firing_result, weighted_final_scores, weighted_avg

def fuzzify_all_variables():
    fuzzy_sets = {}
    fuzzy_values = util.load_fuzzy_variables()
    for name, variable in fuzzy_values.items():
        fuzzy_sets[name] = fuzzify_linguistic_variable(variable)
    return fuzzy_sets


def fuzzify_linguistic_variable(fuzzy_variable):
    fz_set = []
    if fuzzy_variable.get('fuzzy_type') == 'fuzzy':
        for k, val in fuzzy_variable.get('values').items():
            fz_set.append(FuzzySet(function=Trapezoidal_MF(a=val[0], b=val[1], c=val[2], d=val[3]), term=k))
    else:
        for k, val in fuzzy_variable.get('values').items():
            fz_set.append(CrispSet(val[0], val[1], term=k))
    ling_val = LinguisticVariable(fz_set, concept=fuzzy_variable.get('nice_name'),
                                  universe_of_discourse=fuzzy_variable.get('universe_of_discourse'))
    return ling_val


def load_rules():
    clusters = {}
    rules = []
    cluster = ''
    with open(global_params.RULES_FILE, 'r') as file:
        file_lines = file.readlines()
        file_lines[0].replace('\n', '')
        cluster = file_lines[0].replace('\n', '').split(':')[1]
        for line in file_lines[1:]:
            line = line.replace('\n', '')
            if 'Rule_Cluster' in line:
                clusters[cluster] = rules.copy()
                rules = []
                cluster = line.split(':')[1]
            elif line.split(' ')[0] == 'IF':
                rules.append(line)
        clusters[cluster] = rules.copy()
    return clusters


def is_undefined_result(fuzzy_system):
    result_list = [bool(i) for i in fuzzy_system.get_firing_strengths()]
    return True not in result_list


def get_uniform_four_set():
    return AutoTriangle(n_sets=4, terms=['bad', 'acceptable', 'good', 'best'],
                        universe_of_discourse=[0, 10], verbose=False)


