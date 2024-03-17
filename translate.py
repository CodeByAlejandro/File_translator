import readline
from pathlib import Path
from deep_translator import GoogleTranslator

# Enable tab completion with input() function
readline.parse_and_bind('tab: complete')

# Get input file to translate
file_to_translate = Path()
valid_input = False
while not valid_input:
    file_to_translate = Path(input('Provide file to translate: '))
    if not file_to_translate.is_file():
        print('> Error: Please provide an existing file\n')
    else:
        valid_input = True

# Retrieve available languages
translator = GoogleTranslator(source='auto')
supp_languages_dict = GoogleTranslator.get_supported_languages(
    translator,
    as_dict=True
)

# Make sure linting tools realize supp_languages_dict is most definitely a dict
if not isinstance(supp_languages_dict, dict):
    supp_languages_dict = {}

# Determine max language tuple length
max_lang_length = max(
    len(str(language)) for language in supp_languages_dict.items()
)

# Print available languages as tuples in columns
print('The following languages are supported:')
columns = 3
column_width = max_lang_length + 2
languages_acc = []
for language in supp_languages_dict.items():
    languages_acc.append(language)
    if len(languages_acc) == columns:
        line = '\t'
        for index, language_tuple in enumerate(languages_acc):
            if index != len(languages_acc) - 1:
                line += f'{str(language_tuple):<{column_width}}'
            else:
                line += f'{str(language_tuple):<{max_lang_length}}'
        print(line)
        languages_acc.clear()
    else:
        continue

# Get language to translate to
lang_selected = str()
valid_input = False
while not valid_input:
    lang_selected = input('Pick a language from the list (long or short form): ')
    if lang_selected not in supp_languages_dict.keys() \
    and lang_selected not in supp_languages_dict.values():
        print('> Please pick a supported language from the list')
    else:
        valid_input = True

# Translate file
print('Translating your file ...')
output_file = file_to_translate.with_name('translated.txt')
translator.target = lang_selected
try:
    with open(output_file, mode='w') as output:
        output.write(translator.translate_file(str(file_to_translate.absolute())))
except Exception as err:
    print('> Error occurred while trying to write output file:', err)
else:
    print(f'You can find your translation here: {output_file.absolute()}')
