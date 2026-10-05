import re

def parse_procedures(code: str):
    procs = []
    for m in re.finditer(
        r'Процедура\s+(\w+)\s*\(([^)]*)\)(.*?)КонецПроцедуры',
        code, re.DOTALL):
        procs.append({
            'name': m.group(1),
            'params': [p.strip() for p in m.group(2).split(',') if p.strip()],
            'body': m.group(3)})
    return procs
