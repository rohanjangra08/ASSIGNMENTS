#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
print("WELCOME TO BATTLEFIELD GAME ")
print()
print('''RULES: Just find where ships are hiding.
       You have to find 4 ships.
       You have 10 chances to do that.''')
print()
level=input("select a level (EASY or MEDIUM or HARD)")
if level=="EASY"or level=='easy'or level=='Easy' :
    level1=32
elif level=="MEDIUM"or level=='medium'or level=='Medium' :
    level1=16
else :
    level1=10
def alp(a1) :
    if a1=="A" or a1=="a":
        return 0
    elif a1=="B" or a1=='b':
        return 1
    elif a1=="C" or a1=='c' :
        return 2
    elif a1=="D" or a1=='d':
        return 3
    elif a1=="E" or a1=='e':
        return 4
    elif a1=="F" or a1=='f':
        return 5
    elif a1=="G" or a1=='g':
        return 6
    elif a1=="H" or a1=='h':
        return 7
def print1(l) :
    print(" ",end=" ")
    for i in range(1,9,1) :
        print(i,end="  ")
    print()
    a="A"
    for i1 in l :
        print(a,end="")
        a=chr(ord(a)+1)
        for j in i1 :
            print(j,end="")
        print()
l1=[["| |","| |","| |","| |","| |","| |","| |","| |"],["| |","| |","| |","| |","| |","| |","| |","| |"],["| |","| |","| |","| |","| |","| |","| |","| |"],["| |","| |","| |","| |","| |","| |","| |","| |"],["| |","| |","| |","| |","| |","| |","| |","| |"],["| |","| |","| |","| |","| |","| |","| |","| |"],["| |","| |","| |","| |","| |","| |","| |","| |"],["| |","| |","| |","| |","| |","| |","| |","| |"]]
l10=[["| |","| |","| |","| |","| |","| |","| |","| |"],["| |","| |","| |","| |","| |","| |","| |","| |"],["| |","| |","| |","| |","| |","| |","| |","| |"],["| |","| |","| |","| |","| |","| |","| |","| |"],["| |","| |","| |","| |","| |","| |","| |","| |"],["| |","| |","| |","| |","| |","| |","| |","| |"],["| |","| |","| |","| |","| |","| |","| |","| |"],["| |","| |","| |","| |","| |","| |","| |","| |"]]
i=1
l2=[]
l8=[]
while i<=level1 :
    a=random.randrange(0,8,1)
    b=random.randrange(0,8,1)
    l2.append(a)
    l2.append(b)
    c=str(a)+str(b)
    l8.append(c)
    i+=1
for i in range(0,level1*2,2):
    l1[l2[i]][l2[i+1]]="|#|"
    

print1(l10)
m=9
print()
print()
l9=[]
count1=0

for i in range(10) :
    print("{} Chance :".format(i+1))
    b=input("Select row by entering any alp from A-H :")
    a=int(input("Select coloumn by entering any no from 1-8 :"))
    b=alp(b)
    c=str(b)+str(a-1)
    print()
    if l1[b][a-1]=="|#|":
        if c not in l9 :
            print("WOW BATTLESHIP FOUND 👏👏 ")
            c=str(b)+str(a-1)
            l9.append(c)
            count1+=1
            l10[b][a-1]="|#|"  
        else :
            print("YOU ALREADY FOUND IT 😥😥")
    else :
        l10[b][a-1]="|-|"
        print("OH TRY AGAIN ☹☹")
    print()
    print1(l10)
    count=0
    for i in l8 :
        if i in l9 :
            count+=1
    if count1>=4 :
        print()
        print("🎉🎉🎉YOU WON THE GAME🎉🎉🎉")
        break
    print()
    print("*"*30)
    print("-->Chances left : {}".format(m))
    print("-->Battleship found {}/4".format(count1))
    print("*"*30)
    m-=1
else :
    print()
    print("😭😭😭 YOU LOST 😭😭😭")
print("You got",count1/10*100,"% 👍👍")


# In[ ]:




