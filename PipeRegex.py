import re

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batcopter lost a wheel')

print(mo.group(1))