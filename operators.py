# logic operatoins examples

'''
  Truth table for objects
  1 or 2 
  None or 2
  1 or None
  None or 2

  1 and 2 
  None and 2
  1 and None
  None and 2
'''
'''
F F 
F T 
T F
T T
'''


OrTests = [
    'None or 0',
    'None or 2',
    '1 or None',
    '3 or 2'
]

OrTests2 = [
    'False or 0',
    'False or 2',
    '1 or False',
    '3 or 2'
]

AndTests = [
    '1 and 2', 
    'None and 2',
    '1 and None',
    'None and 2'
]
AndTests2 = [
    'False and None', 
    'False and 1',
    'True and None',
    'True and 2'
]

print('----Or Tests---')
for item in OrTests:
    print(item, '=',eval(item))
for item in OrTests2:
    print(item, '=',eval(item))
print('----And Tests---')
for item in AndTests:
    print(item, '=',eval(item))
for item in AndTests2:
    print(item, '=',eval(item))
