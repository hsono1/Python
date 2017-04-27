# Assignment created by
# Andrew Song
# Hans Sono

def draw_star(arr):
	for idx in arr:
		print "*" * idx





draw_star([3,4, 1, 5, 7])	

print "\n"

def draw_star1(arr):
	for idx in arr:
		if isinstance(idx,int):
			print "*" * idx
		else:
			print idx[0].lower() * len(idx)



draw_star1([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])


			    
