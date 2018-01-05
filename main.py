from random import randint
die=['Draw without lifiting your chalk','Draw with your eyes closed','Draw with your non-dominent hand']
cate1=open('cat_1.txt','r+')
cate2=open('cat_2.txt','r+')
cate3=open('cat_3.txt','r+')
cate4=open('cat_4.txt','r+')
cat_1=[]
cat_2=[]
cat_3=[]
cat_4=[]
junk1=cate1.read().splitlines()
junk2=cate2.read().splitlines()
junk3=cate3.read().splitlines()
junk4=cate4.read().splitlines()
for temp1 in junk1:
    cat_1.append(temp1.split('.')[1])
for temp2 in junk2:
    cat_2.append(temp2.split('.')[1])
for temp3 in junk3:
    cat_3.append(temp3.split('.')[1])
for temp4 in junk4:
    cat_4.append(temp1.split('.')[1])
def draw(cat):
    temp=randint(1,len(cat)-1)
    temp2=cat[temp]
    cat.remove(cat[temp])
    return temp2
def throw_dice(lis_t):
    return lis_t[randint(0,len(lis_t)-1)]

