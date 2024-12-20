# combine.py
#    fixes multiline file 
import sys 

# get filename from cla
filename = sys.argv[1]

lines = []
with open(filename,"r") as f:
   lines = f.readlines()

#i = 1
#for l in lines:
#   print(f"{i}: {l}",end='')
#   i += 1

out_lines = []
i = 0
for l in lines:
  if l.startswith(" "):
     # print(f'DEBUG i: {i} l: {l} len out_lines: {len(out_lines)}')
     out_lines[i-1] = out_lines[i-1].replace('\n','') # remove cr
     out_lines[i-1] += l[1:] # do not include first space
     continue
  else:
     out_lines.append(l)
     i += 1

for l in out_lines:
   print(f"{l}", end='')

