def space(): #To make it look good and have proper demarcations
    print()
    print("**********************************************************")
    print()
    

def bubblesort(List):
    n=len(List)
    for i in range(n):
        for j in range(n-i-1):
            if List[j]<List[j+1]:
                List[j],List[j+1]=List[j+1],List[j]
    print("The sorted list in decending order is",List)
    
def insertionsort(List):
    for i in range(1,len(List)):
        a=List[i]
        j=i-1
        while j>=0 and a<List[j]:
            List[j+1]=List[j]
            j-=1
        else:
            List[j+1]=a
    print("The sorted list in decending order is:",List)
    
choice=0

while choice!=3:
    print("Choose from one of the folowing options")
    print("1)Choose 1 for the bubble sort")
    print("2)Choose 2 for the insertion sort")
    print("3)Choose option 3 to exit the code")
    choice=int(input("enter the choice"))
    
    if choice==1:
        space()
        List=eval(input("Enter the List:"))
        bubblesort(List)
        space()
        
    elif choice==2:
        space()
        List=eval(input("Enter the List:"))
        insertionsort(List)
        space()
