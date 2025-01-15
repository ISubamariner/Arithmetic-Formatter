def arithmetic_arranger(problems, show_answers=False):
    top_string=[]
    bot_string=[]
    bar_string=[]
    solution_string=[]
    if len(problems)>5:
        return ('Error: Too many problems.')

    for operand in problems:
        char_num=len(operand)
        
        for i in operand:   
            if i.isalpha():
                return ('Error: Numbers must only contain digits.')

            if i=="/" or i=="*":
                return ("Error: Operator must be '+' or '-'.")

        for i in operand:
            if i=="+":

                string_split= operand.split(sep="+")
                operation="+"
                total= str(int(string_split[0])+int(string_split[1]))

            elif i=="-":

                string_split= operand.split(sep="-")
                operation="-"
                total= str(int(string_split[0])-int(string_split[1]))

            

        if len(string_split)>2:
            return("Error: Too much operations")

        string_split=[string_split[0].strip(),string_split[1].strip()]

        if len(string_split[0]) >= 5 or len(string_split[1]) >= 5 :
            return ('Error: Numbers cannot be more than four digits.')
        
        space_count= lambda a:len(a[1])-len(a[0]) if len(a[1]) > len(a[0]) else len(a[0])-len(a[1])
        space_add= lambda a:f'{space_count(a)*" "}{a[0]}' if len(a[1]) > len(a[0]) else f'{space_count(a)*" "}{a[1]}' 

        if len(string_split[1]) > len(string_split[0]):
            string_split=[space_add(string_split),string_split[1]]
        elif len(string_split[1]) < len(string_split[0]):
            string_split=[string_split[0],space_add(string_split)]


        top_string+= 2*" " +string_split[0]+ 4*" "

        bot_string+= operation + " "+string_split[1]+ 4*" " 

        bar_string+= ((len(string_split[1])+2)*'-')+4*" " 

        solution_string+= (" "*((len(string_split[1])+2)-len(total)))+str(total)+ 4*" "
        
        #print(total,space_add(string_split),bar_string)
        

    
    top_string="".join(top_string)
    top_string=top_string[:-4]
    bot_string="".join(bot_string)
    bot_string=bot_string[:-4]
    bar_string="".join(bar_string)
    bar_string=bar_string[:-4]
    solution_string="".join(solution_string)
    solution_string=solution_string[:-4]

    if show_answers== True:
        problems= top_string +'\n'+ bot_string+'\n'+ bar_string+'\n'+ solution_string
    else:
        problems= top_string +'\n'+ bot_string+'\n'+ bar_string
        
    return problems
  
  print(f'10. \n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')
