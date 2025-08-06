from collections import deque

def load_data(input):
    with open(input, 'r') as file:
        raw_def, raw_eq = file.read().split('\n\n')
        raw_def = raw_def.splitlines()
        raw_eq = raw_eq.splitlines()
        
        definitions = {}
        for definition in raw_def:
            definition = definition.split(': ')
            definitions[definition[0]] = int(definition[1])
        
        equations = []
        for equation in raw_eq:
            equations.append(equation.replace('-> ', '').split(' '))

    return definitions, equations

def parse_command(variables, commands: deque):
    command = commands.popleft()
    var1, operator, var2, result = command
    if var1 in variables and var2 in variables:
        var1, var2 = variables[var1], variables[var2]
        if operator == 'AND':
            variables[result] = int(var1 and var2)
        elif operator == 'OR':
            variables[result] = int(var1 or var2)
        elif operator == 'XOR':
            variables[result] = int(var1 ^ var2)
    else:
        commands.append(command)

if __name__ == '__main__':
    variables, equations = load_data('input.txt')
    equations = deque(equations)
    while equations:
        parse_command(variables, equations)

    answer = []
    for i in range(100):
        var = f'z{i:02}'
        if var in variables:
            answer.insert(0, str(variables[var]))
        else:
            break
    answer = ''.join(answer)

    print(int(answer, 2))