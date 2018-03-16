
def read_input_data():
    with open('input.txt', encoding='utf-8') as input_file:
        input_string = input_file.readline().rstrip()
        template_length = int(input_file.readline())
    return input_string, template_length

def write_output_data(output_string):
    with open('output.txt', 'w') as output_file:
        output_file.write(output_string)

def find_most_freq(string='', length=1):
    templates = {}
    max_count = 1
    for i in range (0, len(string) + 1 - length):
        sequence = string[i:i+length]
        if sequence in templates:
            templates[sequence] += 1
            count = templates[sequence]
            max_count = count if count>max_count else max_count
        else:
            templates[sequence] = 1

    result_templates = []
    for template in templates:
        if templates[template] == max_count:
            result_templates.append(template)

    return result_templates

if __name__ == '__main__': 
    string, length = read_input_data()
    result = find_most_freq(string, length)
    write_output_data(' '.join(result))