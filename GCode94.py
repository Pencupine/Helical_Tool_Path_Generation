
# =============PARAMETER INITIALISATION=========================
di = 15 			# inner diamter in mm units 
do = 25 			# outer diameter in mm units
ri = di/2			# inner radius in mm units
ro = do/2			# outer radius in mm units
h = 0.5				# in mm units
p = 0.5				# in mm units	
planes = 94			# number of vertical planes to cut the helical intersection
# ======================END=====================================



in_points = list()
out_points = list()
seq_points = list()
inc_points = list()

# =============CODE TO GENERATE THE POINTS======================
import math
PI = math.pi

theta = 0				#angular distance between filaments in radians
z=0

dh = p/planes			# vertical climb between two filaments
dth = (2*PI)/planes		# angular distance between two filaments	

n = int(planes*(h/p))	# Number of filaments to be printed = Number of intersection of Helix and vertical planes
for i in range(n):
	
	theta = theta + dth
	z = z + dh

	xin = ri * math.sin(theta)
	yin = ri * math.cos(theta)
	zin = z
	in_points.append([xin, yin, zin])

	xout = ro * math.sin(theta)
	yout = ro * math.cos(theta)
	zout = z
	out_points.append([xout,yout,zout])

### print (out_points)

# Storing the points sequentiall===================================
dir = 0;
for i in range(n):
	if(dir == 0):
		seq_points.append(in_points[i])
		seq_points.append(out_points[i])
		dir = 1
	else:
		seq_points.append(out_points[i])
		seq_points.append(in_points[i])
		dir = 0

x = 0
y = 0
z = 0

# Storing incremental points data===================================
#inc_points = [[]]
for point in seq_points:
	inc_points.append([round((point[0] - x),3), round((point[1] - y),3), round((point[2] - z),3)])

	x = point[0]
	y = point[1]
	z = point[2]


# ===========Exporting and Generating CSV File======================

import csv

with open('inner_points_file.csv', mode='w') as points_file:
    points_writer = csv.writer(points_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)

    for point in in_points:
    	points_writer.writerow(point);

with open('outer_points_file.csv', mode='w') as points_file:
    points_writer = csv.writer(points_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)

    for point in out_points:
    	points_writer.writerow(point);

with open('sequential_points_file.csv', mode='w') as points_file:
    points_writer = csv.writer(points_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)

    for point in seq_points:
    	points_writer.writerow(point);

with open('incremetal_points_file.csv', mode='w') as points_file:
    points_writer = csv.writer(points_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)

    for point in inc_points:
    	points_writer.writerow(point);

# Saving G Code and M Code data to txt file====================================

file1 = open("myfile.txt","w") 
for point in inc_points:
	print(point)
	s = "X" + str(point[0]) + " Y" + str(point[1]) + " Z" + str(point[2]) + "\n"
	file1.write(s); 