import random
from providers.file.fileprov import FileProvider


class OCR:
    def __init__(self):
        self.file_provider = FileProvider()
        self.folder_path = ''

    def transform_number(self, trhee_lines_number) -> list:
        first_line = trhee_lines_number[0]
        second_line = trhee_lines_number[1]
        thirt_line = trhee_lines_number[2]
        if first_line == '   ':
            #first_line = ' _ '#1,4
            if second_line != '|_|' and second_line != '  |':
                second_line = random.choice(['|_|', '  |'])
            thirt_line = '  |'
        elif first_line == ' _ ':
            #first_line == '   '# 0,2,3,5,6,7,8,9
            if second_line == '  |':
                thirt_line = '  |'
            elif second_line == '| |':
                thirt_line = '|_|'
            elif second_line == ' _|':
                thirt_line = random.choice(['|_ ', ' _|'])
            elif second_line == '|_|' or second_line == '|_ ':
                thirt_line = random.choice(['|_|', ' _|'])
            else:
                second_line = random.choice(['  |', ' _|', '|_|', '|_ ', '| |'])
                self.transform_number([first_line, second_line, thirt_line])
        else:
            first_line = random.choice(['   ', ' _ '])
            self.transform_number([first_line, second_line, thirt_line])
            #second_line = random.choice(['  |', ' _|', '|_|', '|_ '])
            #thirt_line = random.choice(['  |', ' _|', '|_|'])

        return [first_line, second_line, thirt_line]
        
    def ocr_entry_questionmark(self, number, entry) -> str:
        copy_number = ''
        if number == '?':
            number_ = self.transform_number(entry)
            number_ = self.read_number(number_)
            if number_ in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                copy_number = number_
        else:
            copy_number = number
        return copy_number

    def ocr_entry(self, entry) -> str:
        array_entries = self.get_entry_array(entry)
        array_numbers = self.get_entry_numbers(entry)
        copy_array_numbers = set()
        new_array_numbers = ''
        if '?' in array_numbers:
            for index, number in enumerate(array_numbers):
                number_ = self.ocr_entry_questionmark(number, array_entries[index])
                new_array_numbers += number_
            copy_array_numbers.add(new_array_numbers)
        else:
            copy_array_numbers.add(array_numbers)

        if self.check_sum(array_numbers) != 0:
            for index, entry2 in enumerate(entry):
                entry3 = self.change_one_character(entry2, index)
                # process again
                copy_array_numbers.add(entry3)
            pass
        else:
            copy_array_numbers.add(array_numbers)

        return copy_array_numbers

        #else:
        #    valid_check_sum = self.ocr.check_sum(array_numbers)
        #    if valid_check_sum != 0:
        #        ocr = True
        #    else:
        #        return array_numbers
        #if '?' in array_numbers:
        #        array_numbers += ' ILL'
        #    elif self.check_sum(array_numbers) != 0:
        #        array_numbers += ' ERR'
#
        #string_return = ''
        #lines = entry.split('\n')
        #from_line = 0
        #to_line = 3
        #while to_line <= 27:
        #    number_array = []
        #    number_char = ''
        #    for line in lines:
        #        number_array.append(line[from_line:to_line])
#
        #    number_char = self.read_number(number_array)
        #    if ocr:
        #        for index, x in enumerate(number_array):
        #            if number_char == '?':
        #                number_array = self.change_one_character(
        #                    number_array,
        #                    index)
        #                number_char = self.read_number(number_array)
        #            else:
        #                break
        #    string_return += number_char
        #    to_line += 3
        #    from_line += 3
#
        #return string_return

    def read_numbers(self, file_name: str) -> list:
        self.file_provider.folder_path = self.folder_path
        return self.file_provider.read(file_name)

    def write_numbers(self, source_list: list, file_name) -> None:
        number_list = []
        for source in source_list:
            number = self.get_entry_numbers(source)
            if '?' in number:
                number += ' ILL'
            elif self.check_sum(number) != 0:
                number += ' ERR'
            number_list.append(number)

        self.file_provider.folder_path = self.folder_path
        self.file_provider.write(number_list, file_name)

    def get_entry_numbers(self, entry) -> str:
        string_return = ''
        array_return = self.get_entry_array(entry)
        for array_entry in array_return:
            string_return += self.read_number(array_entry)

        return string_return

    def read_number(self, number_array) -> int:
        first_line = number_array[0]
        second_line = number_array[1]
        thirt_line = number_array[2]
        result = '?'
        if first_line == '   ':
            result = self._if_line(second_line, '  |', '1', '4')
        elif(first_line == ' _ '):
            match second_line:
                case second_line if second_line == '  |':
                    result = '7'
                case second_line if second_line == ' _|':
                    result = self._if_line(thirt_line, '|_ ', '2', '3')
                case second_line if second_line == '|_ ':
                    result = self._if_line(thirt_line, ' _|', '5', '6')
                case second_line if second_line == '| |':
                    result = '0'
                case second_line if second_line == '|_|':
                    result = self._if_line(
                        thirt_line,
                        '|_|', '8', '?', ' _|', '9')
                case _:
                    result = '?'
        else:
            result = '?'

        return result

    def get_entry_array(self, entry) -> list:
        array_return = []
        lines = entry.split('\n')
        from_line = 0
        to_line = 3
        while to_line <= 27:
            number_array = []
            for line in lines:
                number_array.append(line[from_line:to_line])

            array_return.append(number_array)
            to_line += 3
            from_line += 3

        return array_return

    def check_sum(self, number_string):
        if len(number_string) < 9:
            return None
        result = 0
        position = 9
        for d in number_string:
            result += int(d)*position
            position -= 1

        return result % 11

    def change_character(self, number_char):
        char_result = number_char
        match number_char:
            case number_char if number_char == ' ':
                char_result = random.choice(['|', '_'])
            case number_char if number_char == '_':
                char_result = random.choice(['|', ' '])
            case number_char if number_char == '|':
                char_result = random.choice([' ', '_'])
        return char_result

    def change_one_character(self, number_array, index):
        result = number_array
        if index < len(number_array):
            char_index = number_array[index]
            result = '{}{}{}'.format(
                number_array[:index],
                self.change_character(char_index),
                number_array[index + 1:])
        return result

    def _if_line(
            self,
            line,
            line_if,
            number_if,
            number_else,
            line_elif='x',
            number_elif='x'):
        result = number_else
        if line == line_if:
            result = number_if
        elif line == line_elif:
            result = number_elif

        return result

    def is_invalid_entry_number(sn): 'ERR' in sn or 'ILL' in sn or '?' in sn
