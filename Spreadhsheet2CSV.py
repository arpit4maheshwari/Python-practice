import re

fname = 'data/spreadsheet.csv'

dict_alpha = {'A': 'list_array_modified[0]',            # Making a dictionary to map Alphabets to row number
                'B': 'list_array_modified[1]',
                'C': 'list_array_modified[2]',
                'D': 'list_array_modified[3]',
                'E': 'list_array_modified[4]',
                'F': 'list_array_modified[5]',
                'G': 'list_array_modified[6]',
                'H': 'list_array_modified[7]',
                'I': 'list_array_modified[8]',
                'J': 'list_array_modified[9]'
              }

rows = 0
list_array_raw = []
list_array_modified = []


def operator_covert(expression):
    str_exp_modified = []
    exp_operators = re.split("[-| / | * | + ]", expression)
    # str_exp = re.search("[-| / | * | + ]", row[i])
    for operator in exp_operators:
        if operator == "":
            break
        try:
            operator = int(operator)
        except:
            str_exp_num_list = re.findall("\d", operator)  # str_exp_num is a list of size 1, containing number
            str_exp_char = re.sub("\d", "", operator)  # operator = A0, str_exp_char = A
            match = str_exp_num_list[0]  # Match contains the number, example A0 as operator will give 0
            operator_mod = str_exp_char + "[" + match + "]"  # operator_mod = A[0]
            operator_mod = operator_mod.replace(str(str_exp_char), dict_alpha[str(str_exp_char)])
            expression = expression.replace(operator, operator_mod)  # replacing A0 with list_array_modified[0][0]
            str_exp_modified.append(operator_mod)
    return expression



with open(fname,'r') as f:
    for line in f:
        element = line.split(",")       # Creates the list of row delimited by ','
        for i in range(len(element)):   # Looping over total number of records in the row
             element[i] = element[i].rstrip()       # This is to remove \n from the last element.
        print element
        list_array_raw.append(element)      # Appends the list named row to the List
        rows += 1                   # Iterates the number of rows

print ("Total number of lines / rows are : " + str(rows))
# print ("Value of list_array_raw is -----> "+ str(list_array_raw))
print ("The value of spreadsheet.csv is below:")



for row in list_array_raw:
    column_val = 0
    for i in range(len(row)):
        try:
            row[i] = int(row[i])
        except ValueError:
            row[i] = row[i].replace('=','')
            original_row_i = row[i]
            bracket_expression_row = ""
            bracket_expression = ""
            updated_bracket_expression = ""
            if (re.findall("[()]",row[i])):
                bracket_expression = row[i][row[i].find("(")+len("("):row[i].rfind(")")]
                updated_bracket_expression = operator_covert(bracket_expression)
                row[i] = row[i].replace(bracket_expression,updated_bracket_expression)
            operation_expression = original_row_i.replace(bracket_expression,"").replace("(","").replace(")","")
            updated_expression = operator_covert(operation_expression)
            row[i] = original_row_i.replace(bracket_expression,updated_bracket_expression).replace(operation_expression,updated_expression)
        column_val += 1
    print row
    list_array_modified.append(row)

# column = 0
column_val = 0
row_val = 0
multi_list = [[0 for col in range(row)] for row in range(rows)]
# multi_list = []

# print ("Array_list modified is+++++++++++++++++++++++++++++++")
# print list_array_modified


for row in list_array_modified:
    column_val = 0
    for column in range(len(row)):
        # print ("Value of row_val is: "), row_val
        # print ("Value of column_val is: "), column_val
        # print ("Value of list array value is ",list_array_modified[row_val][column_val])
        try:
            row[column] = int(list_array_modified[row_val][column_val])
        except ValueError:
            # print ("Value of eval is: "),eval((list_array_modified[row_val][column_val]))
            row[column] = eval(list_array_modified[row_val][column_val])
        column_val += 1
    print row
    multi_list.append(row)
    row_val +=1









