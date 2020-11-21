from tkinter import * #IMPORT TKINTER

#VAR'S
def findLen(str):
    counter = 0    
    for i in str:
        counter += 1
    return counter

def generate_code(event):           #GENERATE CODE
    d=ent.get()
    lenth = Label(root, text=findLen(d))   #
    lenth.after(2000, lenth.destroy)       #  LENTH OF LINE
    lenth.pack()                           #
    data=list(d)
    data.reverse()
    c,ch,j,r,h=0,0,0,0,[]
 
    while ((len(d)+r+1)>(pow(2,r))):
        r=r+1
 
    for i in range(0,(r+len(data))):
        p=(2**c)
 
        if(p==(i+1)):
            h.append(0)
            c=c+1
 
        else:
            h.append(int(data[j]))
            j=j+1
 
    for parity in range(0,(len(h))):
        ph=(2**ch)
        if(ph==(parity+1)):
            startIndex=ph-1
            i=startIndex
            toXor=[]
 
            while(i<len(h)):
                block=h[i:i+ph]
                toXor.extend(block)
                i+=2*ph
 
            for z in range(1,len(toXor)):
                h[startIndex]=h[startIndex]^toXor[z]
            ch+=1
 
    h.reverse()
    lab['text'] = ''.join(map(str, h))
############
def find_error(event):                                           # FIND PROBLEMS
    d=ent.get()
    lenth1 = Label(root, text=findLen(d))   #
    lenth1.after(2000, lenth1.destroy)      # LENTH OF LINE
    lenth1.pack()                           #
    data=list(d)
    data.reverse()
    c,ch,j,r,error,h,parity_list,h_copy=0,0,0,0,0,[],[],[]
 
    for k in range(0,len(data)):
        p=(2**c)
        h.append(int(data[k]))
        h_copy.append(data[k])
        if(p==(k+1)):
            c=c+1
            
    for parity in range(0,(len(h))):
        ph=(2**ch)
        if(ph==(parity+1)):
 
            startIndex=ph-1
            i=startIndex
            toXor=[]
 
            while(i<len(h)):
                block=h[i:i+ph]
                toXor.extend(block)
                i+=2*ph
 
            for z in range(1,len(toXor)):
                h[startIndex]=h[startIndex]^toXor[z]
            parity_list.append(h[parity])
            ch+=1
    parity_list.reverse()
    error=sum(int(parity_list) * (2 ** i) for i, parity_list in enumerate(parity_list[::-1]))
    
    if((error)==0):
        lab['bg'] = 'lime'
        lab['text'] = "There is no errors"
 
    elif((error)>=len(h_copy)):
        lab['bg'] = 'yellow'
        lab['text'] = 'Error cannot be detected'
 
    else:
        lab['bg'] = 'red'
        lab['text'] = 'Error is in', error, 'bit'
 
        if(h_copy[error-1]=='0'):
            h_copy[error-1]='1'
 
        elif(h_copy[error-1]=='1'):
            h_copy[error-1]='0'
            h_copy.reverse()
            Label(text = map(str, h_copy)).pack()

#HEAD
root = Tk()
root.minsize(300, 300)
#BODY
ent = Entry(width=30)
but = Button(text="Generate Hamming code")
but1 = Button(text="Finding error in hamming code")
lab = Label()

but.bind('<Button-1>', generate_code)
but1.bind('<Button-1>', find_error)

ent.pack()
but.pack()
but1.pack()
lab.pack()
#ENDL
root.mainloop()
