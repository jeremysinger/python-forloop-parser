import ast
import json
import sys

def analyse_block(codestring):
    '''count how many for loops are present in a code block'''
    '''return a pair for (number of for loops, number of for loops with range iterator'''
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
                        
    #print('for loops %d\nrange %d\n' % (numForLoops, numRangeLoops))
    return (numForLoops, numRangeLoops)

class ForVisitor(ast.NodeVisitor):
    '''specialized ast visitor for for loops, to inspect depth of loop nesting'''
    maxDepth = 0
    currDepth = 0
    def visit_For(self, node):
        ##print(node)
        ##print('for loop on line %d' % (node.lineno), end=' ... ')
        self.currDepth +=1
        ##print(' at depth %d' % self.currDepth)
        if self.currDepth > self.maxDepth:
            self.maxDepth = self.currDepth
        self.generic_visit(node)
        self.currDepth -= 1

    
def analyse_loop_depth(codestring):
    '''use visitor to find max depth of for loop in a code block'''
    '''returns this max depth int value'''
    tree = ast.parse(codestring)
    v = ForVisitor()
    v.visit(tree)
    #print('max depth of for loop is %d' % v.maxDepth)
    return v.maxDepth
    
    
def main():
    if len(sys.argv) < 2:
        print('usage: parser.py file_to_analyse')
        sys.exit(-1)
    filename = sys.argv[1]

    numLoops = 0
    numRange = 0
    maxDepth = 0
    
    with open(filename) as f:
        if filename.endswith(".py"):
            # it's a Python source code file
            code = f.read()
            (numLoops, numRange) = analyse_block(code)
            maxDepth = analyse_loop_depth(code)
        elif filename.endswith(".ipynb"):
            # it's a Jupyter notebook file
            # open notebook with JSON
            notebook = json.load(f)
            # iterate over blocks, looking for code blocks
            for cell in notebook['cells']:
                if cell['cell_type'] == 'code':
                    # for each code block, run analyse_block and
                    # sum results for counts
                    code = '\n'.join(cell['source'])
                    tmp_pair = analyse_block(code)
                    numLoops += tmp_pair[0]
                    numRange += tmp_pair[1]
                    tmp_int = analyse_loop_depth(code)
                    if tmp_int > maxDepth:
                        maxDepth = tmp_int
    # report result for analysis of file
    print ('%s %d %d %d' % (filename, numLoops, numRange, maxDepth))

main()

