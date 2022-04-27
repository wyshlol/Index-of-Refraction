from error_calc import Rules
import math

def radians(degrees:list):
	radians = []
	for degree in degrees:
		radians.append(math.radians(degree))
	return radians

def degrees(radians:list):
	degrees = []
	for radian in radians:
		degrees.append(math.degrees(radian))
	return degrees

def index_of_refraction(theta_i:list, theta_r:list, n:float):
	refractive_index = []
	for i in range(len(theta_i)):
		refractive_index.append((n * math.sin(math.radians(theta_i[i]))) / math.sin(math.radians(theta_r[i])))
	return refractive_index

def average(list_to_avg:list):
	return sum(list_to_avg) / len(list_to_avg)

def sine_of(list_to_sine:list):
	return_list = []
	for i in list_to_sine:
		return_list.append(math.sin(i))
	return return_list


if __name__ == '__main__':
	print('------------ INDEX OF REFRACTION -------------\n')
	theta_i = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
	theta_r = [193, 196, 200, 202, 206, 210, 212, 217, 220, 222]

# get θ from the normal
	theta_r_revised = []
	for theta in theta_r:
		theta_r_revised.append(theta - 180)

	print(f'θ_i: {theta_i}°')
	print(f'θ_r: {theta_r_revised}°')

# convert degrees into radians
	rad_theta_i = radians(theta_i)
	rad_theta_r_revised = radians(theta_r_revised)

	#print(sine_of(rad_theta_i))
	#print(sine_of(rad_theta_r_revised))

# index of refractions
	index_of_refraction_air = 1.0003
	index_of_refraction_water = index_of_refraction(theta_i, theta_r_revised, index_of_refraction_air)

	print(f' Refractive Index of Water (n): {average(index_of_refraction_water):13f}')
	print('----------------------------------------------\n')

	print('--------------- ERROR ANALYSIS ---------------\n')
	error_theta = 0.5 #degrees

# δsinθ
	error_rad_theta_i = []
	for theta in rad_theta_i:
		error_rad_theta_i.append(math.sin(theta + math.radians(error_theta)) - math.sin(theta))

	error_rad_theta_r = []
	for theta in rad_theta_r_revised:
		error_rad_theta_r.append(math.sin(theta + math.radians(error_theta)) - math.sin(theta))

	error_index_of_refraction_water = Rules.rule4([math.sin(average(rad_theta_i)), math.sin(average(rad_theta_r_revised))], [average(error_rad_theta_i), average(error_rad_theta_r)], [1, -1], average(index_of_refraction_water))
	print(f' δn: {error_index_of_refraction_water:40f}')

	print('----------------------------------------------\n')