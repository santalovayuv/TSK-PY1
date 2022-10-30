def get_count_char(str_):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_
    count_char_ = {}
    for sumbol in str_.lower():
        if sumbol.isalpha():
            if sumbol in count_char_:
                count_char_[sumbol] += 1
            else:
                count_char_[sumbol] = 1
    return count_char_


def percent_char(count_char_):
    i = 0
    percent_ = {}
    for char in count_char_:
        i += count_char_.get(char)
    for char in count_char_:
        percent_[char] = round((count_char_.get(char)/1)*100, 2)
        check = 0
    for char in percent_:
        check += percent_.get(char)
        return percent_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
