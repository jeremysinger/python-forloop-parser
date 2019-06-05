import ast
import sys

def analyse_block(codestring):
    '''count how many for loops are present in a code block'''
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

class ForVisitor(ast.NodeVisitor):
    '''specialized ast visitor for for loops, to inspect depth of loop nesting'''
    maxDepth = 0
    currDepth = 0
    def visit_For(self, node):
        ##print(node)
        print('for loop on line %d' % (node.lineno), end=' ... ')
        self.currDepth +=1
        print(' at depth %d' % self.currDepth)
        if self.currDepth > self.maxDepth:
            self.maxDepth = self.currDepth
        self.generic_visit(node)
        self.currDepth -= 1

    
def analyse_loop_depth(codestring):
    '''use visitor to find max depth of for loop in a code block'''
    tree = ast.parse(codestring)
    v = ForVisitor()
    v.visit(tree)
    print('max depth of for loop is %d' % v.maxDepth)
    
    
def main():
    if len(sys.argv) < 2:
        print('usage: parser.py file_to_analyse')
        sys.exit(-1)
    filename = sys.argv[1]
    with open(filename) as f:
        if filename.endswith(".py"):
            # it's a Python source code file
            code = f.read()
            analyse_block(code)
            analyse_loop_depth(code)
        ###elif filename.endswith(".ipynb"):
            # it's a Jupyter notebook file
            # open notebook with JSON
            # iterate over blocks, looking for code blocks
            # for each code block, run analyse_block and
            # sum results for counts

main()

