import importlib, traceback
try:
    m = importlib.import_module('app.main')
    print('Imported app.main OK; attributes:', [n for n in dir(m) if not n.startswith('__')][:40])
except Exception:
    traceback.print_exc()
