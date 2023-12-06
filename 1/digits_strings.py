import re

# Opening and reading a text file line by line
file_path = '../data/1.txt'


############## 1 ################

def extract_only_numbers(string):
    """
    Extracts only numbers from a string
    :param string: String to extract numbers from
    :return: String containing only numbers
    """
    return ''.join([char for char in string if char.isdigit()])

def get_calibration_score_q1(file_path):
    with open(file_path, 'r') as file:
    
        rolling_sum = 0
        for line in file:
            # Process each line as needed
            output = line.strip()  # Example: Stripping newline characters and saving it to output
            digits_only = extract_only_numbers(output)
            if len(digits_only) == 1:
                double_diget = digits_only*2
            elif len(digits_only) > 1:
                double_diget = digits_only[0] + digits_only[-1]
            else:
                print('No digits found in string')
            rolling_sum += int(double_diget)
        return rolling_sum


############## 2 ################

def convert_words_to_numbers(string):
    """
    Converts words to numbers
    :param string: String to convert
    :return: String with words converted to numbers
    """
    if 'one' in string:
        string = string.replace('one', 'o1e')
    elif 'two' in string:
        string = string.replace('two', 't2o')
    elif 'three' in string:
        string = string.replace('three', 't3e')
    elif 'four' in string:
        string = string.replace('four', 'f4r')
    elif 'five' in string:
        string = string.replace('five', 'f5e')
    elif 'six' in string:
        string = string.replace('six', 's6x')
    elif 'seven' in string:
        string = string.replace('seven', 's7n')
    elif 'eight' in string:
        string = string.replace('eight', 'e8t')
    elif 'nine' in string:
        string = string.replace('nine', 'n9e')
    return string
    

def get_calibration_score_q2(file_path):

    with open(file_path, 'r') as file:
    
        rolling_sum = 0
        checkstring = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        for line in file:
            # Process each line as needed
            output = line.strip()  # Example: Stripping newline characters and saving it to output

            for string in checkstring:
                if string in output:
                    output = convert_words_to_numbers(output)

            # print('string_digits_letters=', output)
            digits_only = extract_only_numbers(output)
            # print('digits_only=', digits_only)
            if len(digits_only) == 1:
                double_diget = digits_only+digits_only
            elif len(digits_only) > 1:
                double_diget = digits_only[0] + digits_only[-1]
            else:
                print('No digits found in string')
            rolling_sum += int(double_diget)
        return rolling_sum




def main():
    pass
    print('q1:', get_calibration_score_q1(file_path))
    print('q2:', get_calibration_score_q2(file_path))

if __name__ == '__main__':
    main()
        



    
