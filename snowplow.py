# Ask for customized road grid and start point
print("Precondition: Row/column should be greater than 2")
x=(int)(input("How many columns?"))
y=(int)(input("How many rows?"))
if (x<=2 or y<=2):
	exit()
choice=(int)(input("Which method would you like to choose? 1 or 2? (Just choose a number)"))
#Create the x y coordinates, and the road lists
node=[]
road=[]

#Input values for xy coordinates, which consist of the road number in each direction [East,South,West,North]
for i in range (x):
	node.append([])
	for j in range (y):
		node[i].append([0,0,0,0])
#print(node)

#Number all roads
for i in range (2*x*y-x-y):
	road.append(i+1);
#print(road)
totalRoad=len(road)
print(totalRoad)

#Label the inner block of roads
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

#Fill up the rest of the outter roads
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
#Shows a labeled map
for k in node:
	print(k)

#Essential variables to determine moves and count time
timer=0
moveX=0
moveY=0

#Helper function that uses global variables to move the robot
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

def goRight():
	global timer,moveX,moveY,road,node
	while(moveX!=x-1 and moveY!=0):
		move("right")
		move("down")

def goUp():
	global timer,moveX,moveY,road,node
	while(moveX!=0 and moveY!=y-1):
		move("up")
		move("left")
#Try to cover all the roads
#The 

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
	timer-=1
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

print("Took ",timer," minutes to clear.")
for k in node:
	print(k)
