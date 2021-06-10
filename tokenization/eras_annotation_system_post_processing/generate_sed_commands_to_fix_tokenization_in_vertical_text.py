# -*- coding: utf-8 -*-
import sys


def usage(script_filename):
    print("Usage: %s contractions_filename sed_commands_output_filename" % script_filename)
    print("       Contractions file must be in the format: derived_word1 + derived_word2 = original_word")
    exit(1)


def get_contractions_dict(contractions_filename):
    contractions_dict = {}
    
    with open(contractions_filename, "r") as file:
        for line in file:
            words = line.split("=")
            assert len(words) == 2
            
            original_word = words[1].strip()
            
            derived_words = words[0].split("+")
            
            assert len(derived_words) == 2
            
            derived_word1 = derived_words[0].strip()
            derived_word2 = derived_words[1].strip()
            
            contractions_dict[original_word] = [derived_word1, derived_word2]
    
    return contractions_dict


def generate_sed_commands(contractions_dict):
    sed_command_list = []
    sed_command_stub = 's/^{}\\(\\t.*\\)$/{}\\1\\n{}\\1/Ig'
    
    # Commands to treat expressions like 'faz-se' and 'manter-se-ia', breaking into
    # multiple lines
    hyphen_command_list = [
        's/^\\([^-\\t]*\\)-\\([^-\\t]*\\)\\(\\t.*$\\)/\\1\\3\\n-\\3\\n\\2\\3/g',
        's/^\\([^-\\t]*\\)-\\([^-\\t]*\\)-\\([^-\\t]*\\)\\(\\t.*$\\)/\\1\\4\\n-\\4\\n\\2\\4\\n-\\4\\n\\3\\4/g',
    ]
    
    sed_command_list.extend(hyphen_command_list)
    
    # Quotation marks to default tokens
    quotation_marks_regex_from_to = [
        ['^["”"“”]', '"'],
        ["^´", "'"],
        ['^[\–\-\–]', '-'],
        ]
    for from_to in quotation_marks_regex_from_to:
        sed_command = 's/%s/%s/g' % (from_to[0], from_to[1])
        
        sed_command_list.append(sed_command)
    
    # Command to treat monetary values like 'R$3.000,00', breaking in two lines, one with 'R$' and
    # the other with '3.000,00'
    sed_command_list.append('s/^\\(R\\$\\)\\([^\\t]*\\)\\(\\t.*\\)$/\\1\\3\\n\\2\\3/g')
    
    # Command to treat Brazilian monetary currency, wrongly broken in two lines, first 'R' and the
    # second '$', joining into one single line 'R$'
    sed_command_list.append('/^R\\t.*$/{N; s/R\\(\\t[^\\n]*\\)\\n\\$[^\\n]*/R$\\1/ }')
   
    for key in contractions_dict.keys():
        vals = contractions_dict[key]
        
        sed_command = sed_command_stub.format(key, *vals)
        
        sed_command_list.append(sed_command)
    
    return sed_command_list


if __name__ == '__main__':
    if (len(sys.argv) < 3):
        usage(sys.argv[0])
    
    contractions_filename = sys.argv[1]
    sed_commands_output_filename = sys.argv[2]
    
    contractions_dict = get_contractions_dict(contractions_filename)
    
    sed_command_list = generate_sed_commands(contractions_dict)
    
    with open(sed_commands_output_filename, "w") as file:
        for sed_command in sed_command_list:
            file.write(sed_command)
            file.write('\n')
