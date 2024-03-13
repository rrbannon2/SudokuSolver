import clingo.control
import clingo


clingo_results = [[None for x in range(9)] for y in range(9)]
clingo_result_dict = {}
def on_model(model):
    solution = str(model)
    solution = solution.replace('number','')
    solution = solution.split(' ')
    for num in solution:
        clingo_results[int(num[1])-1][int(num[3])-1] = int(num[-2])
    for row in clingo_results:
        print(row)
    
    for row in range(len(clingo_results)):
        for column in range(len(clingo_results[row])):
            clingo_result_dict[str(row+1)+','+str(column+1)] = str(clingo_results[row][column])
    
def run_python(json_puzzle):
    nums_dict = json_puzzle
    

    asp_code_base = ''
    with open('clingoSudokuSolver/asp_code_base.txt','r') as file:
        asp_code_base += file.read()
        
   
    
    for key in nums_dict.keys():
        num = key + "," + nums_dict[key]
        num_str = "number({}).".format(num)
        asp_code_base += num_str

    asp_code_base += "#show number/3."
    
    max_step = 5

    control = clingo.Control()
    control.configuration.solve.models = 1
    try:
        control.add("base", [], asp_code_base)
    except:
        RuntimeError(asp_code_base)
    parts = []
    parts.append(("base", []))
    control.ground(parts)
    ret, step = None, 1
    while step <= max_step and (step == 1 or not ret.satisfiable):
        
        ret = control.solve(on_model=on_model)
        step += 1

    return clingo_result_dict
    
