class Item():
    def __init__(self,value,weight):
        self.value=value
        self.weight=weight
W=50

def Knap(W,arr):
    arr.sort(key=lambda x:(x.value/x.weight),reverse=True)
    finalvalue=0
    for item in arr:
        if item.weight<=W:
            finalvalue=finalvalue+item.value
            W=W-item.weight
        else:
            finalvalue=finalvalue+item.value*W/item.weight
            break
    print(finalvalue)


arr=[Item(60,10),Item(100,20),Item(120,30)]
Knap(50,arr)