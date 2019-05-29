import ast
import sys

def main():
    if len(sys.argv) < 2:
        print('usage: parser.py file_to_analyse')
        sys.exit(-1)
    filename = sys.argv[1]
    with open(filename) as f:
        tree = ast.parse(f.read())
    for node in ast.walk(tree):
        if isinstance(node, (ast.For)):
            print('for loop on line %d' % (node.lineno))
            if isinstance(node.iter, (ast.Call)):
                call = node.iter
                if isinstance(call.func, (ast.Name)):
                    print('for loop iter is fn call: %s' % call.func.id)
    

main()

