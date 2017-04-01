import bs4, urllib

#
# build url to webpage holding qb stats
#

# open text file holding names of all active quarterbacks
qb_file = open('qbs.txt','r')

# store qb names in list
qbs = qb_file.read().split(sep='\n')

# loop thru list of qb's and build each url
for q in qbs:
	name = q.split(sep=' ')
	qb_link = name[1][0]+'/'+name[1][0:4]+name[0][0:2]
	print(qb_link)
	qb_url = 'http://www.pro-football-reference.com/players/'+qb_link+'00.htm'
	print(qb_url)
	#
	# open url for page holding qb stats
	#
	print("Attempting to connect to: ",qb_url)
	try:
	    req = urllib.request.urlopen(qb_url).read()
	    soup = bs4.BeautifulSoup(req,"html.parser")
	    print("Page loaded!")
	except:
	    print("Failed to load page!")

	print(type(soup)) # verify class type (should be bs4.BeautifulSoup)

	#
	# extract passing stats from page
	#

	stats = soup.find_all('table',attrs={'id':'passing'})
	if len(stats)>0:
		print(name[1],"'s stats extracted!")
	else:
		print('Failed to extract ',name[1],"'s stats!")

	#
	# write and save stats to local text file
	#

	print('Writing stats to text file...')

	# build path to text file
	print('Building file path...')
	filepath = 'qb/'+name[0][0].lower()+name[1].lower()
	ext = '.txt'

	# open file, write to file, close file
	print('Writing to: ',filepath+ext,'...')
	file = open(filepath+ext, 'w', encoding = 'utf-8')
	try:
	    file.write(stats[0].get_text())
	    # hopefully done?
	    print("Stats written to file!")
	except:
	    file.write("march sadness :(")
	    print('Failed to write file!')

	file.close()

print("DONE!!!")
