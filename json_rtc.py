import json
import re

file_to_fix = 'loc_en.data'

def fix_json_formatting(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json_file.read()

    regex = r',(?!\s*?[\{\[\"\'\w])'
    data_fixed = re.sub(regex, '', data)

    data_parsed = json.loads(data_fixed)

    json_string = json.dumps(data_parsed, ensure_ascii=False, indent=2)

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json_string)

    print(f'JSON: {json_file_path}')

fix_json_formatting(file_to_fix)

