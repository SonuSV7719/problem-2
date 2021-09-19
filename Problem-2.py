# Coded by : Sonu Shriram vishwakarma

# Problem statement:

"""

In second year computer engineering class, group A student's paly criket, group B students play badminton and group C students play football

write a Python program using functions to compute following:

       a) List of students who play both criket and badminton

       b) List of students who play either cricket or badminton but not both

       c) Number of students who play neither cricket nor badminton

       d) Number of students who play cricket and football but not badminton

"""



# Function to check any perticular element is in the list or not. If in list then true will be return otherwise false will be return



def In(element, list1):

    flag =0

    for i in range(len(list1)):

        if element == list1[i]:

            flag = 1

    if flag == 1:

        return True

    else:

        return False 



# Function to check similar elements in any one list if similar elements are in list then neglect that element



def noSimilarEle(list1):

    flag =0 

    noSimilarEle =[]

    for i in range(len(list1)):

        for j in range(len(list1)):

        

            if list1[i]==list1[j]:

                continue

            else:

                if In(list1[i], noSimilarEle):

                    flag =1

                    break

                if flag == 0:

                    noSimilarEle.append(list1[i])

                    break

        flag = 0

    if In(list1[0], noSimilarEle):

        pass

    else:    

        noSimilarEle.append(list1[0])

    

    return noSimilarEle





# Function for to check union of two lists---------------------------->>



def myUnion(list1, list2):

    add = list1+list2

    union = noSimilarEle(add)

    return union



# Function to find intersection of two list



def intersection(list1, list2):

    intersection = []

    for i in range(len(list1)):

        for j in range(len(list2)):

            if list1[i]!=list2[j]:

                continue

            else:

                if In(list1[i], intersection):

                    pass

                else:

                    intersection.append(list1[i])

                    break

    return intersection



# Function to subtract list from list



def listSub(list1, list2):

    sub = []

    for i in range(len(list1)):

        if In(list1[i], list2):

            continue

        else:

            sub.append(list1[i])

    return sub



# Function to create list by taking values from user 



def create_set(set, num):

    for i in range(num):

        number = i+1

        element = input(f"Enter element number {number} : ")

        set.append(element)

    return set



listOfAllStudent = []

n = int(input("Enter total no of elements of list of all student: "))

create_set(listOfAllStudent, n)

badminton = []

n1 = int(input("Enter total no of elements of student who play badminton: "))

create_set(badminton, n1)

cricket = []

n2 = int(input("Enter total no of elements of student who play criket: "))

create_set(cricket, n2)

football = []

n3 = int(input("Enter total no of elements of student who play football: "))

create_set(football, n3)





print(f"List of students who play both criket and badminton,\n{cricket} intersection {badminton} is: ",intersection(cricket, badminton))



print(f"List of students who play either cricket or badminton but not both\n{cricket} union {badminton} is: ",myUnion(cricket, badminton))



unionCriBad = myUnion(cricket, badminton)

print(f"list of students who play neither cricket nor badminton,\n{listOfAllStudent}-({cricket} union {badminton}) is: ", listSub(listOfAllStudent, unionCriBad))



print("Number of students who play neither cricket nor badminton is: ", len(listSub(listOfAllStudent, unionCriBad)))



print(f"List of students who play both criket and football,\n{cricket} intersection {football} is: ",intersection(cricket, football))



print(f"Number of students who play both criket and football but nor badminton is: ", len(intersection(cricket, football)))



