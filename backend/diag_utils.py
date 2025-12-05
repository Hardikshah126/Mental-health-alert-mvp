import inspect, importlib, traceback
try:
    m = importlib.import_module('app.utils')
    print('app.utils file ->', inspect.getfile(m))
    print('exported names ->', sorted(n for n in dir(m) if not n.startswith('__')))
except Exception:
    traceback.print_exc()
