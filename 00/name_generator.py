#!/usr/bin/python3
import random

names = [ 'Ada', 'Edith', 'Grace', 'Evelyn', 'Mary', 'Susan', 'Carol', 'Janese','Radia'] 

surnames = ['Lovelace', 'Clarke', 'Hopper', 'Granville', 'Keller', 'Kare', 'Shaw', 'Swanson', 'Perlman' ]


descriptions = {'Ada Lovelace' : "At 26, encouraged by her husband, Lovelace returned to assisting her friend and mentor Charles Babbage, known as the father of the computer, on a project called \"The Analytical Engine.\" During this time, she was asked to translate Italian engineer Luigi Meneabrea’s lecture notes from French to English. She found many errors and expanded on the original in her footnotes.",
'Edith Clarke' : "Edith Clarke created and patented The Clarke Calculator, a graphical device that solved equations used to send power through electrical transmission lines longer than 250 meters. Her massive contribution to transcontinental telephone communication silenced skeptics; in 1922, at 38, Edith Clarke became the first professional female electrical engineer.",
'Grace Hopper' : "Grace Hopper was a computer scientist, Yale Ph.D, and United States Navy Rear Admiral who also—on top of everything else—helped pioneer computer programming. “Humans are allergic to change,” she once said. \“They love to say, ‘We’ve always done it this way.’ I try to fight that. That’s why I have a clock on my wall that runs counter-clockwise.\”",
'Evelyn Granville' : "arinnched pennies, financial aid, and academic scholarship made her continued education possible. Granville attended Smith College and then Yale for her Ph.D, becoming just the second African American women to receive a mathematics doctorate at any American University.",
'Mary Keller' : "The first woman to receive a Ph.D in Computer Science was a nun: Mary Kenneth Keller entered the “Sister of Charity” in 1932, professing her vows in 1940.",
'Carol Shaw' : "Shaw programmed one of the Atari’s best-known shooter games, River Raid. For the first time, gamers could experience an inordinate amount of non-random, repeating terrain despite constrictive memory limits. River Raid was the first game that allowed the shooter to accelerate and slow down all over the screen.",
'Radia Perlman' : "Perlman created the algorithm behind the Spanning Tree Protocol (STP), which is an essential part of the Internet’s underlying foundation." }

def generate_name():
	name = random.choice(names)
	surname = random.choice(surnames)
	return " ".join([name, surname])

if __name__=="__main__":
	result = generate_name()
	print(result)
	if result in descriptions:
		print(descriptions[result])
