import ast, sys
p = r'.\\app\\utils.py'
src = open(p, 'r', encoding='utf8').read()
tree = ast.parse(src, filename=p)
funcs = [n.name for n in tree.body if isinstance(n, ast.FunctionDef)]
classes = [n.name for n in tree.body if isinstance(n, ast.ClassDef)]
assigns = [n.targets[0].id for n in tree.body if isinstance(n, ast.Assign) and hasattr(n.targets[0],'id')]
print('functions:', funcs)
print('classes:', classes)
print('assigns:', assigns)
