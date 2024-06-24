import re

def write_employees_to_file(employee_list, path): 
    with open(path, "w") as fh:
        for sub_list in employee_list:
            for employee in sub_list:
                new_emp = re.sub(r'[0-9,]', '', employee) 
                fh.write(new_emp + "\n")
                
    print(employee_list)
    

employee_list = [['Robert,28', 'Alex Denver,30'], 
                 ['Drake Mikelsson,77']]
path = "data.txt" 
write_employees_to_file(employee_list, path)
