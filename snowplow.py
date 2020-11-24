import random
# Ask for customized road grid size
print("Precondition: Row/column should be greater than 2")
x=(int)(input("How many columns?"))
y=(int)(input("How many rows?"))
# If the dimension of the grid is less than 2, then one of the method won't work, exit
if (x<=2 or y<=2):
	exit()
#Here you get to choose 3 methods
#Method 1 covers the grid square by square in order, starts from bottom left of the map and finishes at the top right
#Method 2 finishes all the rows first then finish all the columns
#Method 3 will just bump around the map randomly until all the roads are cleared
choice=(int)(input("Which method would you like to choose? 1 or 2 or 3? (Just choose a number)"))

#Node is the point connecting the road in 4 directions, each node represents the road number in each direction [East,South,West,North], and the x-y coordinate of the node is the same as the index in the 2D list.
def createNode():
	global node
	node=[]
	for i in range (x):
		node.append([])
		for j in range (y):
			node[i].append([0,0,0,0])

#Create the appropriate amount of roads in the grid, each road/edge will have a unique number
def createRoad():
	global road
	road=[]
	for i in range (2*x*y-x-y):
		road.append(i+1)

#Calling this function will generate a map with customized size and all labeled roads
def createMap():
	global node, x, y, road,timer, moveX,moveY
	createRoad()
	createNode()
	timer=0
	moveX=0
	moveY=0
	# All the inner roads will be labeled in this chunck
	for i in range (1,x-1):
		for j in range (1,y-1):
			for check in range (4):
				if (node[i][j][0]==0):
					node[i+1][j][2]=road[0]
					node[i][j][0]=road[0]
					road.pop(0)
				if(node[i][j][1]==0):
					node[i][j-1][3]=road[0]
					node[i][j][1]=road[0]
					road.pop(0)
				if(node[i][j][2]==0):
					node[i-1][j][0]=road[0]
					node[i][j][2]=road[0]
					road.pop(0)
				if(node[i][j][3]==0):
					node[i][j+1][1]=road[0]
					node[i][j][3]=road[0]
					road.pop(0)

	#All the outter roads will be labeled in this chunck
	for i in range (x-1):
		node[i][0][0]=road[0]
		node[i+1][0][2]=road[0]
		road.pop(0)
	for j in range (y-1):
		node[x-1][j][3]=road[0]
		node[x-1][j+1][1]=road[0]
		road.pop(0)
	for i in range (x-1,0,-1):
		node[i][y-1][2]=road[0]
		node[i-1][y-1][0]=road[0]
		road.pop(0)
	for j in range (y-1,0,-1):
		node[0][j][1]=road[0]
		node[0][j-1][3]=road[0]
		road.pop(0)

#createMap()
#for k in node:
#	print(k)

#Helper function that uses global variables to move the robot, each time the robot moves, it updates its location, count the time, and marks its path as cleared
def move(direction):
	global timer,moveX,moveY,road,node
	if(direction=="left"):
		print("(",moveX,",",moveY,") to (",moveX-1,",",moveY,")")
		road.append(node[moveX][moveY][2])
		node[moveX][moveY][2]=0
		node[moveX-1][moveY][0]=0
		moveX-=1
	elif(direction=="right"):
		print("(",moveX,",",moveY,") to (",moveX+1,",",moveY,")")
		road.append(node[moveX][moveY][0])
		node[moveX][moveY][0]=0
		node[moveX+1][moveY][2]=0
		moveX+=1
	elif(direction=="up"):
		print("(",moveX,",",moveY,") to (",moveX,",",moveY+1,")")
		road.append(node[moveX][moveY][3])
		node[moveX][moveY][3]=0
		node[moveX][moveY+1][1]=0
		moveY+=1
	elif(direction=="down"):
		print("(",moveX,",",moveY,") to (",moveX,",",moveY-1,")")
		road.append(node[moveX][moveY][1])
		node[moveX][moveY][1]=0
		node[moveX][moveY-1][3]=0
		moveY-=1
	timer+=1

#This is used for method 1 to move the robot to the lower right of the map
def goRight():
	global timer,moveX,moveY,road,node
	while(moveX!=x-1 and moveY!=0):
		move("right")
		move("down")

#This is used for method 1 to move the robot to the upper left of the map
def goUp():
	global timer,moveX,moveY,road,node
	while(moveX!=0 and moveY!=y-1):
		move("up")
		move("left")

createMap()
if (choice==1):
	move("right")
	goUp()
	while(True):
		if(moveX==0):
			if(node[moveX][moveY][1]!=0 and node[moveX][moveY][3]!=0):
				move("down")
				move("up")
				move("up")
				goRight()
			else:
				move("down")
				move("up")
				print("(",moveX,",",moveY,") to (",moveX+1,",",moveY,")")
				print("(",moveX+1,",",moveY,") to (",moveX+2,",",moveY,")")
				moveX+=2
				timer+=2
		elif(moveX==x-1 and moveY==y-1):
			move("left")
			move("right")
			move("down")
			break
		elif(moveY==0):
			if(node[moveX][moveY][0]!=0 and node[moveX][moveY][2]!=0):
				move("left")
				move("right")
				move("right")
				goUp()
			else:
				move("left")
				move("right")
				print("(",moveX,",",moveY,") to (",moveX,",",moveY+1,")")
				print("(",moveX,",",moveY+1,") to (",moveX,",",moveY+2,")")
				moveY+=2
				timer+=2
		elif(moveY==y-1):
			if(node[moveX][moveY][0]!=0 and node[moveX][moveY][2]!=0):
				move("left")
				goRight()
			else:
				print("(",moveX,",",moveY,") to (",moveX+1,",",moveY,")")
				print("(",moveX+1,",",moveY,") to (",moveX+2,",",moveY,")")
				moveX+=2
				timer+=2
		elif(moveX==x-1 and moveY==y-1):
			move("left")
			move("right")
			move("down")
		elif(moveX==x-1):
			if (node[moveX][moveY][1]!=0 and node[moveX][moveY][3]!=0):
				move("down")
				goUp()
			else:
				print("(",moveX,",",moveY,") to (",moveX,",",moveY+1,")")
				print("(",moveX,",",moveY+1,") to (",moveX,",",moveY+2,")")
				moveY+=2
				timer+=2
elif (choice==2):
	while(True):
		for i in range (x-1):
			move("right")
		if(moveY!=y-1):
			move("up")
		for i in range (x-1):
			move("left")
		if(moveY!=y-1):
			move("up")
		else:
			break
	if(moveX==0):
		while(True):
			for j in range(y-1):
				move("down")
			if(moveX!=x-1):
				move("right")
			for j in range(y-1):
				move("up")
			if (moveX!=x-1):
				move("right")
			else:
				break
	elif(moveX==x-1):
		while(True):
			for j in range(y-1):
				move("down")
			if(moveX!=0):
				move("left")
			for j in range(y-1):
				move("up")
			if (moveX!=0):
				move("left")
			else:
				break
elif(choice==3):
	trials=[]
	#Do 50 trials
	for tri in range (50):
		print("Trial ",tri+1)
		createMap()
		while(True):
			countStop=0
			for i in range(x):
				for j in range (y):
					if(node[i][j]==[0,0,0,0]):
						countStop+=1
			if(countStop==x*y):
				break
			if (node[moveX][moveY]==[0,0,0,0]):
				pick=random.randint(0,3)
				if(pick==0 and moveX!=x-1):
					move("right")
				elif(pick==1 and moveY!=0):
					move("down")
				elif(pick==2 and moveX!=0):
					move("left")
				elif(pick==3 and moveY!=y-1):
					move("up")
			else:
				pick=random.randint(0,3)
				if (pick==0 and node[moveX][moveY][pick]!=0):
					move("right")
				elif(pick==1 and node[moveX][moveY][pick]!=0):
					move("down")
				elif(pick==2 and node[moveX][moveY][pick]!=0):
					move("left")
				elif(pick==3 and node[moveX][moveY][pick]!=0):
					move("up")
		#Record the time used in each trial
		trials.append(timer)
	#Set get the fastest time
	timer=min(trials)
	#Prints the trial with the fastest time
	print("Trial", trials.index(timer)+1," took the least time")
#Indicates the total/best time used in specific case.
print("Took ",timer," minutes to clear.")
#This should show a list of lists of lists of 0, which means all the roads are cleared
for k in node:
	print(k)
