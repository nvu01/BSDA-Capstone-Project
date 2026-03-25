import json
import pandas as pd

def get_metadata (json_file):
    with open (json_file, 'r') as file:
        metadata = json.load(file)
    variables = metadata['variables']
    variables = pd.DataFrame(variables).transpose().reset_index()
    variables.rename(columns={'index':'var_code'}, inplace=True)
    return variables

def input_prompt():
    '''Prompt user to input table ID and label's components'''
    table_id = input('Table ID:')
    parent_col = input('Parent column:')
    child_col = input('Child column:')
    parent_label = input('Parent label:')
    child_label_1 = input('Child label 1:')
    child_label_2 = input('Child label 2:')
    child_label_3 = input('Child label 3:')

    # A list of label's components
    label_components = [child_col, parent_col, parent_label, child_label_1, child_label_2, child_label_3]

    return table_id, label_components


def get_var_label(label_components):
    ''' Return variable's label by assembling user's inputs'''
    label = []
    for i in label_components:
        # Filter out empty elements
        if i != '':
            label.append(i.strip())

    if len(label) <= 1:  # A label should have at least 2 components
        var_label = None
    else:
        var_label = '!!'.join(label)  # Components are assembled and separated by "!!"

    return var_label


def get_var_id(table_id, label_components):
    '''Call get_var_label function to retrieve variable label.
        Validate the format of table ID and variable label.
        If the table ID and variable label are valid, look up variable code based on table ID and variable label.'''

    var_label = get_var_label(label_components)
    b_var = get_metadata('b_variables.json')
    s_var = get_metadata('s_variables.json')
    dp_var = get_metadata('dp_variables.json')

    result = pd.DataFrame()

    if not table_id or not table_id.lower().startswith(('b', 's', 'dp')) or var_label is None:
        raise ValueError('Invalid inputs!')
    else:
        if table_id.lower().startswith('b'):
            result = b_var.loc[
                (b_var['group'].str.contains(table_id, case=False)) & (b_var['label'].str.lower() == var_label.lower())]
        elif table_id.lower().startswith('s'):
            result = s_var.loc[
                (s_var['group'].str.contains(table_id, case=False)) & (s_var['label'].str.lower() == var_label.lower())]
        elif table_id.lower().startswith('dp'):
            result = dp_var.loc[
                (dp_var['group'].str.contains(table_id, case=False)) & (dp_var['label'].str.lower() == var_label.lower())]

        print(f'Table: {result["group"].values[0]}')
        print(f'Variable label: {result["label"].values[0]}')
        print(f'Variable code: {result["var_code"].values[0]}')


if __name__ == '__main__':
    try:
        table, components = input_prompt()
        get_var_id(table, components)
    except ValueError as excpt:
        print(excpt)
    except Exception as excpt:
        print(f'Variable not found! No matching table or label. ({excpt})')