# Code
The solution to homework 4 is divided up into two python files, a docker file,
and an svg file. Here I will give a description of all files in repo!


The first python file is graph.py. 
### graph.py
The outcome of graph.py will be
a list of domains used, a forward-DNS dictionary, a reverse-DNS 
dictionary.

Next is graph2.py
### graph2.py
The outcome of graph2.py will be domains linked to 
hostnames that were the result of their IP addresses 
being used in the python function "socket.getfdqn()". Also
graph2.py will create a text document that is in the dot language. 
Using the command "cat Diagram.txt | dot -Tsvg -Kfdp > output.svg" on the text document will create an svg diagram
of the dictionary that was printed out. It will
be called 'output.svg'.

### Diagram.txt
This is written in dot language. It was created when graph2.py was
executed. Run "cat Diagram.txt | dot -Tsvg -Kfdp > output.svg" 

The container, docker-compose.yml.
### docker-compose.yml
This is just responsible for running a Docker container.

The display
### output.svg
This is a diagram of the outcome of graph2.py. This was created 
with a module called Graphviz. 