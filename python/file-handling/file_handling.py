"""
File Handling in python refers to a process of performing operations on a file such as
creating , reading, writing and closing the file 
"""

f = open('example.txt', 'r')
content = f.read()
print(content)
f.close()

c = open("example.txt", 'w')
c.write("Hey Their! This is Prathyush Varrey\n")
c.write("Currently I'm woring in Wipro and By 2027 I'll be an AI Engineer in a Top Product based Company or Unicorn")
c.write("\nAlso I'l build my own company and sell it to become a Billionaire")

c.close()

c = open("example.txt", 'r')
rewritten_content = c.read()
print(rewritten_content)
c.close()


with open("example.txt", 'w') as text:
    text.write("Hello My Name is Prathyush\n")
    text.write("I'm a AI FDE by 2027")

with open("example.txt", 'r') as text:
    content=text.read()
    print(content)