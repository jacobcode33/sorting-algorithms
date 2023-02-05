from graphics import *
import time
import random
import math
length = 250
pause = 0#.05
bottom = 550

def bubble(List):
    global draw1
    draw1 = GraphWin("Bubble sort", 1000, 600, autoflush = False)
    draw1.setBackground (color_rgb(255, 255, 255))

    List = []
    for i in range (0, length):
        List.append (random.randint(0, 255)) # creates random list
    hold = 0
    change = True
    while change == True:
        change = False
        time.sleep (pause)
        
        for item in draw1.items[:]: # clears drawing
            item.undraw()
        
        for count in range (0, len(List) -1): # resets one run of list
            if List[count] > List[count + 1]:
                change = True
                hold = List[count]
                List.remove(List[count])
                List.insert(count+1, hold)
        
            line = Line (Point (((count*(900/len(List))) + 50), bottom), Point ((count*(900/len(List))+ 50), (bottom - (List[count] * 2)))) # draws a line
            line.setOutline (color_rgb (List[count], List[count], List[count]))
            line.setWidth ((900/len(List))-2)
            line.draw (draw1)
        draw1.update()
    return(List)
            
def insertion(List):
    global draw2
    draw2 = GraphWin("Insertion sort", 1000, 600, autoflush = False)
    draw2.setBackground (color_rgb(255, 255, 255))
    
    hold = 0
    for count in range (0, len(List) - 1):
        if List[count] > List[count + 1]:
            hold = List[count +1]
            List.pop(count +1)
            place = False
            search = 0
            while place == False:
                if List[search] >= hold:
                    List.insert(search, hold)
                    #List.append(hold)                        ### to show an incorrect algorithm
                    place = True                    
                search = search + 1

            time.sleep (pause)
                
            for item in draw2.items[:]: # clears drawing
                item.undraw()

            for draw in range (0, len(List) - 1):
                line = Line (Point (((draw*(900/len(List))) + 50), bottom), Point ((draw*(900/len(List))+ 50), (bottom - (List[draw] * 2)))) # draws a line
                line.setOutline (color_rgb (List[draw], List[draw], List[draw]))
                line.setWidth ((900/len(List)) - 2)
                line.draw (draw2)
            draw2.update()
    return(List)


def bogo(List):
    global draw3
    draw3 = GraphWin("Bogo sort", 1000, 600, autoflush = False)
    draw3.setBackground (color_rgb(255, 255, 255))
    
    ordered = False
    while not ordered:
        random.shuffle(List)
        ordered = True
        count = 0
        last = 0
        while ordered and count < len(List):
            if last > List[count]:
                ordered = False
            last = List[count]
            count += 1

        for item in draw3.items[:]: # clears drawing
                item.undraw()
            
        for draw in range (0, len(List) - 1):
            line = Line (Point (((draw*(900/len(List))) + 50), bottom), Point ((draw*(900/len(List))+ 50), (bottom - (List[draw] * 2)))) # draws a line
            line.setOutline (color_rgb (List[draw], List[draw], List[draw]))
            line.setWidth ((900/len(List)) - 2)
            line.draw (draw3)
        draw3.update()
    print(List)
    return(List)

def merge(List):
    global draw4
    length = len(List) # for drawing at end
    draw4 = GraphWin("Merge sort", 1000, 600, autoflush = False)
    draw4.setBackground (color_rgb(255, 255, 255))
    for i in range(len(List)): # divide up the list
        List[i] = [List[i]]
    while len(List) != 1:
        for i in range(math.floor(len(List)/2)):
            hold1 = List[i]
            hold2 = List[i+1]
            #print (List)
            minimum = 0 # as its sorting a presorted list with hold1 it knows that the next item in the list must be greater than the last
            for o in range(len(hold2)): # in turn inserts one of these into hold1 (insersion sort of these two (presorted) lists)
                u = minimum
                done = False
                while u < len(hold1) and not done:
                    if hold2[0] < hold1[u]:
                        hold1.insert(u, hold2[0])
                        hold2.pop(0)
                        done = True
                    u += 1
                if not done:
                    hold1.insert(u, hold2[0])
                    hold2.pop(0)
                minimum = u
            List.pop(i+1)
            
            for item in draw4.items[:]: # clears drawing
                item.undraw()
            count = 0
            for draw1 in range (len(List)):
                for draw2 in range(len(List[draw1])):
                    line = Line (Point (((count*(900/length)) + 50), bottom), Point ((count*(900/length)+ 50), (bottom - (List[draw1][draw2] * 2)))) # draws a line
                    line.setOutline (color_rgb (List[draw1][draw2], List[draw1][draw2], List[draw1][draw2]))
                    line.setWidth ((900/length) - 2)
                    line.draw (draw4)
                    count += 1
            draw4.update()
            time.sleep(pause)
    return List[0]
                    
def quick(List, canvas):
    global draw5
    #draw5 = GraphWin("Quick sort", 1000, 600, autoflush = False)
    #draw5.setBackground (color_rgb(255, 255, 255))
    placed = []
    # could add a median of three to choose a good pivot.. but not yet
    start = None
    stop = None
    done = False
    for i in range(len(List)): # find the boundaries of the unplaced sublist
        if i not in placed and not done:
            done = True
            start = i
    done = False
    for i in range(start, len(List)):
        if i in placed and not done or i == len(List)-1:
            done = True
            stop = i
    #print (start, stop)
    pivot = 0
    List.append(List[pivot]) # first move the pointer to the end
    List.pop(pivot)
    pivot = stop
    print (List[pivot])

    lp,rp = start,stop
    while lp <= rp: # until the left and right pointers cross
        print (List)
        time.sleep(1)
    
        lp = start
        done = False
        while lp < stop-1 and not done: # leftpointer
            if List[lp] > List[pivot]:
                done = True
                print (List[lp])
            else:
                lp += 1
        print (List[lp])
            
        rp = stop-1
        done = False
        while rp >= start and not done: #rightpointer
            #print (rp)
            if List[rp] < List[pivot]:
                done = True
            else:
                rp -= 1

        List[lp], List[rp] = List[rp], List[lp]
    List[lp], List[pivot] = List[pivot], List[lp]
    print (List[rp], List[lp])
    print (List)
    placed.append(rp)
    

    



def check(List, canvas):
    for draw in range (0, len(List) - 1):
        if List[draw] <= List[draw+1]:
            time.sleep(pause)
            line = Line (Point (((draw*(900/len(List))) + 50), bottom), Point ((draw*(900/len(List))+ 50), (bottom - (List[draw] * 2)))) # draws a line
            line.setOutline (color_rgb (0, List[draw], 0))
            line.setWidth ((900/len(List)) - 2)
            line.draw (canvas)
            canvas.update()
        else:
            time.sleep(pause)
            line = Line (Point (((draw*(900/len(List))) + 50), bottom), Point ((draw*(900/len(List))+ 50), (bottom - (List[draw] * 2)))) # draws a line
            line.setOutline (color_rgb (List[draw], 0, 0))
            line.setWidth ((900/len(List)) - 2)
            line.draw (canvas)
            canvas.update()

def makelist():
    List = []
    for i in range (0, length):
        List.append (random.randint(0, 255)) # creates random list
    return List

#quick(makelist(), None)
check(bubble(makelist()), draw1)
check(insertion(makelist()), draw2)
check(merge(makelist()), draw4)
check(bogo(makelist()), draw3) # joke sorting algorithm, shuffles the numbers at random until they are in order
