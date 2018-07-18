import mysql.connector
from random import randint
import time

a = time.time()

mydb = mysql.connector.connect(
  host="27.253.99.29",
  port="3307",
  user="python",
  passwd="realcoolpassword",
  database="game"
)

b = time.time()
mycursor = mydb.cursor()
c = time.time()
mycursor.execute("SELECT * FROM info")
d = time.time()
info = [x for x in mycursor]
e = time.time()

for p in info[-10:]:
    print(p)

f = time.time()
numPlayers = len(info)
currentX = randint(0, 99)
currentY = randint(0, 99)
values = "({}, {}, {})".format(numPlayers, currentX, currentY)

g = time.time()
mycursor.execute("INSERT INTO info (PlayerID, x, y) VALUES {}".format(values))
h = time.time()
mycursor.execute("SELECT * FROM info")
i = time.time()
info = [x for x in mycursor]
j = time.time()

for p in info[-10:]:
    print(p)

print("a->b: {:.2f}s".format(b-a))
print("b->c: {:.2f}s".format(c-b))
print("c->d: {:.2f}s".format(d-c))
print("d->e: {:.2f}s".format(e-d))

print("f->g: {:.2f}s".format(b-a))
print("g->h: {:.2f}s".format(c-b))
print("h->i: {:.2f}s".format(d-c))
print("i->j: {:.2f}s".format(e-d))

input()
