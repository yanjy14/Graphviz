import re
import pygraphviz as pgv
class Node:
    def __init__(self,name,key):
        self.name = name
        self.key = key
        self.mom = None
        self.father = None
        self.rank = 1

if __name__ == "__main__":
    file_object = open('out.txt')
    node = []
    rank = 0
    for line in file_object:
        length = len(node)
        m = re.findall(r'(\w*[0-9]+)\w*', line)
        #print m
        if len(m) == 2:
            k1 = int(m[0])
            k2 = int(m[1])
            if k1 == 0 and k2 ==1024:
                node.append(Node('n' + str(len(node)),0))
                mom = node[len(node)-1]
                node.append(Node('n' + str(len(node)), 1024))
                father = node[len(node)-1]
                child_key = (mom.key + father.key) / 2
                node.append(Node('n' + str(len(node)), child_key))
                child = node[len(node)-1]
                child.mom = mom
                child.father = father
                child.rank = father.rank + 1
            if k1 == 0 and k2 != 1024 :
                node.append(Node('n' + str(len(node)), 0))
                mom = node[len(node) - 1]
                for father in node[::-1]:
                    if father.key == k2:
                        break
                child_key = (mom.key + father.key) / 2
                node.append(Node('n' + str(len(node)), child_key))
                child = node[len(node) - 1]
                child.mom = mom
                child.father = father
                child.rank = father.rank + 1
            if k1 !=0 and k2!=0:
                #print ('k1:{0},k2:{1}').format(k1,k2)
                for father in node[::-1]:
                    if father.key == k1:
                        break
                for mom in node[::-1]:
                    if mom.key == k2:
                        break
                child_key = (mom.key + father.key) / 2
                #print 'child_key:{0}'.format(child_key)
                node.append(Node('n' + str(len(node)), child_key))
                child = node[len(node) - 1]
                child.mom = mom
                child.father = father
                if father.rank > mom.rank:
                    child.rank = father.rank + 1
                else:
                    child.rank = mom.rank + 1
    file_object.close()
    dot_flie = open('test.dot','w')
    code = ['digraph test{\n']
    rank =0
    for n in node:
        if n.rank>rank:
            rank = n.rank
        code.append('{self.name}[label = "{self.key}"];\n'.format(self=n))
        if n.mom:
            code.append('{mom.name}->{child.name};\n'.format(mom=n.mom,child=n))
        if n.father:
            code.append('{father.name}->{child.name};\n'.format(father=n.father,child=n))
    for i in range(rank):
        code.append('r{rank}[shape = "plaintext",label = "step{rank}"];\n'.format(rank=i))
    code.append('r0->n0[style = "invis", rank = "same"];\n')
    for i in range(1,rank):
        code.append('r{r1}->r{r2}[style = "invis"];\n'.format(r1=i,r2 = i-1))
    code.append('}\n')

    dot_flie.writelines(code)
    dot_flie.close()
    G = pgv.AGraph("test.dot")
    G.layout('dot')
    G.draw('file.png')


    #text = file_object.read()
