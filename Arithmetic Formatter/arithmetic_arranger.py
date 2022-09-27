def arithmetic_arranger(problems, solv=False):
    #Validating if the problem list has more than five elemens
    if len(problems)>5:
        return "Error: Too many problems"

    #declaring the list which contain the elements of each operation
    first_amount=[]
    second_amount=[]
    operator=[]

    #bucle for appendding the element that corresponds to each list from the problem list
    for problem in problems:
        string=problem.split()
        first_amount.append(string[0])
        operator.append(string[1])
        second_amount.append(string[2])

    #bucle for validatting each element in each list complies the rules
    for i in range(len(first_amount)):
        if operator[i]!="+" and operator[i]!="-":
            return "Error: Operator must be '+' or '-'."

        if first_amount[i].isdigit()!=True or second_amount[i].isdigit()!=True:
            return "Error: Numbers must only contain digits."

        if len(first_amount[i])>4 or len(second_amount[i])>4:
            return "Error: Numbers cannot be more than four digits."

    #declarin the lists of each line
    first_line=[]
    second_line=[]
    dash_line=[]
    result_line=[]

    #bucle for adding the space for the first line to ajust it to second line 
    for i in range(len(first_amount)):
        if len(first_amount[i])>len(second_amount[i]):
            first_line.append(" "*2 + first_amount[i])
        else:
            first_line.append(" "*(len(second_amount[i]) - len(first_amount[i]) + 2) + first_amount[i])

    #bucle for adding the operator and the space for the second line to ajust it to first line
    for i in range(len(second_amount)):
        if len(second_amount[i])>len(first_amount[i]):
            second_line.append(operator[i]+" "+second_amount[i])
        else:
            second_line.append(operator[i]+" "*(len(first_amount[i]) - len(second_amount[i]) + 1) + second_amount[i])

    #bucle for adding the dash line according to the longest line between the first line and the second line
    for i in range(len(problems)):
        dash_line.append("-"*max(len(first_line[i]), len(second_line[i])))

    #bucle for resolve each problem and add them with the space to the fourth line
    for i in range(len(first_amount)):
        if operator[i]=="+":
            res=str(int(first_amount[i])+int(second_amount[i]))
        else:
            res=str(int(first_amount[i])+int(second_amount[i]))
        
        if len(res)>max(len(first_amount[i]), len(second_amount[i])):
            result_line.append(" "+ res)
        else:
            result_line.append(" "*(max(len(first_amount[i]), len(second_amount[i])) - len(res) + 2) + res)

    #if Solve is True we going to add the fourth line to the arranged_formatter
    if solv==True:
        arranged_formatter="    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(dash_line) + "\n" + "    ".join(result_line)
    else: 
        arranged_formatter="    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(dash_line)
    
    return arranged_formatter
