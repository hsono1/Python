import re
def get_matching_words(regex):
	words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
	matches = []
	for word in words:
		if re.search(regex,word):
			matches.append(word)
	return matches



#All words that contain a "v"

regex = r'v+'

print get_matching_words(regex)

#All words that contain a "ss"

regex = r'ss'
print "\n"
print get_matching_words(regex)

# All words that end with an "e"

regex = r'e$'
print "\n"
print get_matching_words(regex)

# All words that contain an b, any character, then another b

regex = r'b.b'
print "\n"
print get_matching_words(regex)


# All words that contain an "b", any number of characters (including zero), then another "b"

regex = r'b\w*b'
print "\n"
print get_matching_words(regex)




# All words that include all five vowels in order
regex = r'.*a.*e.*i.*o.*u.*'
print "\n"
print get_matching_words(regex)



# All words that only use the letters in regular expression (each letter can appear any number of times)

regex = r'\b[regular expression]+\b'
print "\n"
print get_matching_words(regex)



# All words that contain a double letter

regex = r'.*(.)\1.*'
print "\n"
print get_matching_words(regex)















