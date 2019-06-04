import ast
import sys

def analyse_block(codestring):
    numForLoops = 0
    numRangeLoops = 0
    tree = ast.parse(codestring)
    for node in ast.walk(tree):
        if isinstance(node, (ast.For)):
            # print('for loop on line %d' % (node.lineno))
            numForLoops += 1
            if isinstance(node.iter, (ast.Call)):
                call = node.iter
                if isinstance(call.func, (ast.Name)):
                    if call.func.id == 'range':
                        # print('for loop iter is fn call: %s' % call.func.id)
                        numRangeLoops += 1
                        
    print('for loops %d\nrange %d\n' % (numForLoops, numRangeLoops))


def main():
    if len(sys.argv) < 2:
        print('usage: parser.py file_to_analyse')
        sys.exit(-1)
    filename = sys.argv[1]
    with open(filename) as f:
        if filename.endswith(".py"):
            # it's a Python source code file
            analyse_block(f.read())
        ###elif filename.endswith(".ipynb"):
            # it's a Jupyter notebook file
            # open notebook with JSON
            # iterate over blocks, looking for code blocks
            # for each code block, run analyse_block and
            # sum results for counts

main()

