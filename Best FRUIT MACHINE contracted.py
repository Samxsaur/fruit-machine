x=1
import time
import random
w=0
u=0
p=0
q=0
n=0
z=0
t=[]
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
money=1.00
f=input ("Lets play, yes for Yes, no for No...")
if f==("yes"):
    while x==1:
        t==0
        list1==0
        list2==0
        list3==0
        list4==0
        list5==0
        t.clear()
        list1.clear()
        list2.clear()
        list3.clear()
        list4.clear()
        list5.clear()
        print ("You have £",money,"in your account")
        print ("You spent 20p on turn")
        money=money-0.2
        b=random.randint(1,6)
        c=random.randint(1,6)
        d=random.randint(1,6)
        if b==1:
            print ("   ")
            time.sleep(0.5)
            print ("           Cherry")
            w=(w+1)
            t.append(w)
        elif b==2:
            print ("   ")
            time.sleep(0.5)
            print ("           Bell")
            u=(u+1)
            (list1).append(u)
        elif b==3:
            print ("   ")
            time.sleep(0.5)
            print ("           Lemon")
            p=(p+1)
            (list2).append(p)
        elif b==4:
            print ("   ")
            time.sleep(0.5)
            print ("           Orange")
            q=(q+1)
            (list3).append(q)
        elif b==5:
            print ("   ")
            time.sleep(0.5)
            print ("           Star")
            n=n+1
            (list4).append(n)
        elif b==6:
            print ("   ")
            time.sleep(0.5)
            print ("           Skull")
            z=z+1
            (list5).append(z) 
        if c==1:
            print ("   ")
            time.sleep(0.5)
            print ("           Cherry")
            w=w+1
            t.append(w)    
        elif c==2:
            print ("   ")
            time.sleep(0.5)
            print ("           Bell")
            u=u+1
            (list1).append(u)
        elif c==3:
            print ("   ")
            time.sleep(0.5)
            print ("           Lemon")
            p=p+1
            (list2).append(p)
        elif c==4:
            print ("   ")
            time.sleep(0.5)
            print ("           Orange")
            q=q+1
            (list3).append(q) 
        elif c==5:
            print ("   ")
            time.sleep(0.5)
            print ("           Star")
            n=n+1
            (list4).append(n)
        elif c==6:
            print ("   ")
            time.sleep(0.5)
            print ("           Skull")
            z=z+1
            (list5).append(z)
        if d==1:
            print ("   ")
            time.sleep(0.5)
            print ("           Cherry")
            w=w+1
            t.append(w) 
        elif d==2:
            print ("   ")
            time.sleep(0.5)
            print ("           Bell")
            u=u+1
            (list1).append(u)
        elif d==3:
            print ("   ")
            time.sleep(0.5)
            print ("           Lemon")
            p=p+1
            (list2).append(p)
        elif d==4:
            print ("   ")
            time.sleep(0.5)
            print ("           Orange")
            q=q+1
            (list3).append(q)
        elif d==5:
            print ("   ")
            time.sleep(0.5)
            print ("           Star")
            n=n+1
            (list4).append(n)
        elif d==6:
            print ("   ")
            time.sleep(0.5)
            print ("           Skull")
            z=z+1
            (list5).append(z)
        if (len(t))==2:
            money=money+0.5
        if (len(t))==3:
            money=money+1
        if (len(list1))==2:
            money=money+0.5
        if (len(list1))==3:
            money=money+5
        if (len(list2))==2:
            money=money+0.5
        if (len(list2))==3:
            money=money+1
        if (len(list3))==2:
            money=money+0.5
        if (len(list3))==3:
            money=money+1
        if (len(list4))==2:
            money=money+0.5
        if (len(list4))==3:
            money=money+1
        if (len(list5))==2:
            money=money/2 
        if (len(list5))==3:
            print ("Awww")
            money=money-money
        money = (round(money, 1))
        if money==0.0:
            print ("You ran out of money :(")
            x=2
        elif money<0.0:
            print ("You ran out of money :(")
            x=2
        else:
            print ("   ")
            inpu=input ("Play again?...")
            if inpu==("yes"):
                list1==list1*0
                list2==list2*0
                list3==list3*0
                list4==list4*0
                list5==list5*0
                x=1
            elif inpu==("no"):
                print ("You have £",money,"'s left in your account")
                money=money*0
                t.clear()
                list1.clear()
                list2.clear()
                list3.clear()
                list4.clear()
                list5.clear()
                x=2
else:
        x=2
