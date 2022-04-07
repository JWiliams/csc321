import graph, socket
"""
this code creates a dictionary with the domain as keys
and a result of the getfqdn function on their ipAddress(es)
"""

dic = graph.gg
new_dic = dict()
p = []
for k,v in dic.items():
    #new_dic[k] = socket.getfqdn(v)
    for i in v:
        p.append(socket.getfqdn(i))
    new_dic[k] = p
    p = []

print(new_dic)

with open('Digraph.txt', 'w') as d:
    d.write('digraph {')
    d.write('\n')
    for k,v in new_dic.items():
        for i in v:
            d.write('    ')
            d.write(f'"{k}" -> "{i}";')
            d.write('\n')
    d.write('}')

