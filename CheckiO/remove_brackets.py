# https://py.checkio.org/mission/remove-brackets


# def brakets_to_del(line, initial_dict={}):
#     print('line 1: ', line)
#     brack_dict = {}
#     opposite_bracket = {')': '(', ']': '[', '}': '{'}
#     closing_brackets = ')}]'
#
#     if not initial_dict:
#         for i in range(len(line)):
#             initial_dict[i] = line[i]
#             brack_dict[i] = line[i]
#     else:
#         brack_dict = initial_dict.copy()
#
#     print('*', brack_dict)
#     print('**', initial_dict)
#
#     for i in brack_dict:
#         print(i)
#         if brack_dict[i] in closing_brackets:
#             j = i - 1
#             while j != -1:
#                 if brack_dict[j] == opposite_bracket[brack_dict[i]]:
#                     del brack_dict[j]
#                     del brack_dict[i]
#                     break
#                 else:
#                     j -= 1
#             else:
#                 continue
#             break
#
#     clear_line = ''.join(brack_dict.values())
#     print('line 2: ', clear_line)
#     if line == clear_line:
#         return brack_dict
#     elif line == '':
#         return ''
#     else:
#         return brakets_to_del(clear_line, initial_dict)


def brakets_to_del(brack_str):
    print('input *:', brack_str)
    opposite_bracket = {')': '(', ']': '[', '}': '{'}
    closing_brackets = ')}]'
    brack_list = [(i, brack_str[i]) for i in range(len(brack_str))]
    deleted_indexes = []
    print(brack_list)

    for i in range(len(brack_list)):
        if brack_list[i][1] in closing_brackets:
            j = i - 1
            while j != -1:
                if brack_list[j][1] == opposite_bracket[brack_list[i][1]]:
                    deleted_indexes.append(i)
                    deleted_indexes.append(j)
                    brack_list.pop(i)
                    brack_list.pop(j)
                    break
                else:
                    j -= 1
            else:
                continue
            break
    remade_line = ''
    for pare in brack_list:
        remade_line += pare[1]
    print(remade_line)
    print('output *: ', brack_list)
    if remade_line == brack_str:
        return remade_line
    else:
        return brakets_to_del(remade_line)


print(brakets_to_del('([])()]]'))


def remove_brackets(line):

        return brakets_to_del(line)


# print(remove_brackets('()]()]'))
# print(remove_brackets(']()]'))
# print(remove_brackets('()]'))



# def indexes_to_del(line):
#     opposite_bracket = {')': '(', ']': '[', '}': '{'}
#     closing_brackets = ')}]'
#
#     indexes = list(range(len(line)))
#
#     for i in range(len(line)):
#         if line[i] in closing_brackets:
#             j = i - 1
#             while j != -1:
#                 if line[j] == opposite_bracket[line[i]]:
#                     indexes.pop(i)
#                     indexes.pop(j)
#                     break
#                 else:
#                     j -= 1
#             else:
#                 continue
#             break
#
#     print(indexes)
#     line_list = list(line)
#
#     for index in indexes[::-1]:
#         del line_list[index]
#
#     clear_line = ''.join(line_list)
#     print(clear_line)
#
#     if line == clear_line:
#         return line
#     elif line == '':
#         return ''
#     else:
#         return indexes_to_del(clear_line)


# print(remove_brackets('(()()'))
# print(remove_brackets('(([))'))
# print(remove_brackets('[[(}]]'))
# print(remove_brackets('[[{}()]]'))
# print(remove_brackets('[[[[[['))
# print(remove_brackets(''))
# print(remove_brackets('[(])'))


# assert remove_brackets('(()()') == '()()'
# assert remove_brackets('[][[[') == '[]'
# assert remove_brackets('[[(}]]') == '[[]]'
# assert remove_brackets('[[{}()]]') == '[[{}()]]'
# assert remove_brackets('[[[[[[') == ''
# assert remove_brackets('[[[[}') == ''
# assert remove_brackets('') == ''
# assert remove_brackets('[(])') == '()'
