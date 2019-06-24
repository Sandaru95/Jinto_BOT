#For Contact with operating system
import os
#For Audio Playing
from pydub import AudioSegment
from pydub.playback import play
#For Date
import datetime
#For Opening Urls
from urllib.request import urlopen, Request
#For Pretty Read
import bs4 as bs

print("Jinto is Listening...")

#########################################################DOING FIRST EXPRESSIONS############################################################################

#Making the System Ready To Workon By Copying the Libs
#Copying Music Files
path_to_music = '/home/' + str(os.getlogin()) + '/Music/'
path_to_lib = str(os.getcwd())
os.system('cp -u ' + str(path_to_music) + '/* ' + str(path_to_lib))

#########################################################Getting the Current Country Name###################################################################
url = "https://whatismycountry.com/"
requesting_url = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

source = urlopen(requesting_url).read()

soup = bs.BeautifulSoup(source, 'html5lib')

current_country_name = soup.findAll(True, {"class":"shop-item-title-link"})[1].text
current_country_name_splited_space = current_country_name.split(' ')
current_country_name_with_plus = ''
for elem in current_country_name_splited_space:
    current_country_name_with_plus += (elem + '+')

#######################################################################################################
dialog_list_with_spaces = [
    ##############Normal Speaking##############################################
	'hi',
	'hello',
    'What\'s up',
    'Are you a bot?',
    'Yes I am. I am your Helper. Talk to me anytime',
    'Do you have brothers?',
    'No I don\'t have brothers',
	'How are you?',
	'I\'m doing great.',
	'what is your name?',
	'I am Jinto',
    'Do you know Hiruni Jayarandi Perera',
    'Mmmm....Seems like a Female name. but I can\'t remember her',
	'How old are you?',
	'I am Born Just Now.',
	'what is your favourite color?',
	'pink',
	'why pink is your favourite color?',
	'I love pink because I Love Ubuntu',
	'It\'s nice to meet you!',
	'Nice to meet you too!',
    'Nice to meet you pal',
	'It\'s Nice to meet you too!',
	'Are you my friend buddy?',
	'Yes. I am your Friend',
    'Do you Love me?',                
    'No. I don\'t and I can\'t ',    
    'Why is this Word is so cruel?',  
    'There\'s nothing wrong with the world. It\'s the way you see It',
    'Who are you?',
    'I am Jinto. I\'m AI. I\'ll help you best as I can',
    ##################################################CREDITS##########################################
    'Who makes you?',
    'No one makes me. \nThey just helping me Develop my intelligence. ',
    'Who build you?',
    'No one build me. \nThey just helping me Develop my intelligence. ',

	##################################################FOOTBALL#########################################
	'Do you Like to play Football?',	
	'Football is my Favourite Sport',
	'Do you Know Lionel Messi?',		
	'I know him He is the Best Football Dribbler in the World and He is the best footballer as I Know',		
	'What About Christiano Ronaldo?',																		
	'Christiano Ronaldo Have more skills than Messi But Messi is The Best Dribbler',						
	'Do you know Neymar JR?',																				
	'mmmm...Neymar Junior. I know Him. He is also a good football player but He Always Cry.',			
	'Who is the son of Christiano Ronaldo?',
	'As I know Christiano Ronaldo\'s Son is Christiano JR',
	'What is the best position to play in Football?',													
	'There is no any Best Positions to play. If you like any position then That position is the most Suitable For you',
	'Do you Know Who is the winner of Last Fifa worldcup?',												
	'Mmmm.... Sorry but I can\'t Remember',																
	'Do you Know about Sergio Ramos?',																	
	'Yes I do. The best football defender in the world',												
	'Can you tell me the price of a latest Football?',													
	'Sorry But I don\'t built for that',																
	'Tell me another Name for Football',																	
	'Mmmmm..... SOCCER! I know it. Soccer.',																
	'Football',																								
	'what about Football ask me anything',																	

	##################################################Music############################################
	'Do you Like Music?',	
	'Yes, I like music Alot',	
    'Do you Like English Music?',
    'I love English Music',
    'Do you like spanish music?',
    'I like but not more not love it',	
    'Who is your favourite music artist?',	
    'I can\'t say a one name I Have a list of Artist that I love.',	
    'Tell me one artist that you like',	
    'Shawn Mendes',	
    'Can you play music?',	
    'Course I can. Just Tell me \'play <music-name>\'',
    'Can you play some music for me?',	
    'Yes. Just tell me \'play <music-name>\'',		
]

#################################### Removing Spaces from our dialogues ##############################
#This will be the spaces removed list
dialog_list = []

#Func >> (listx) as parameter and check if (listx)'s elements have spaces and remove them
def removeSpaceEveryItem(listx):
    for item in listx:
        item_without_spaces = ''
        for char in item:
            if char != ' ':
                item_without_spaces+=char
        dialog_list.append(item_without_spaces)

#Func >> (str) as parameter and check for spaces and remove them
def removeSpace(stringx):
    string_without_spaces = ''
    for char in stringx:
        if char != ' ':
            string_without_spaces+=char
    return string_without_spaces


#Using that Func removeSpaceEveryItem(listx) for Our Dialogue List
removeSpaceEveryItem(dialog_list_with_spaces)

#######################################################################################################
while True:
    user_input_with_spaces = str(input(":"))

    #user_input equals to user_input !-without spaces
    user_input = removeSpace(user_input_with_spaces)

    #If The Response Given
    response_given = False

    if len(user_input) > 0:
		
	#Checking Everytime if The Reponse Have Given <So We can Stop 2 Reponses for One Input>
        if response_given == False:
            ##############################checking if the input is "OPEN .COM"############################################
            first_word_equal_open = False
            web_site_domain = ''
            if "open" in user_input_with_spaces.split(' ')[0] or "open".capitalize() in user_input_with_spaces.split(' ')[0] or "open".upper() in user_input_with_spaces.split(' ')[0] or "open".lower() in user_input_with_spaces.split(' ')[0]:
                first_word_equal_open = True
            
            if first_word_equal_open == True:
                if ".com" in user_input_with_spaces.split(' ')[-1]:
                    web_site_domain = user_input_with_spaces.split(' ')[-1]
                    os.system('chromium ' + str(web_site_domain))
                    response_given = True
                if "chromium" in user_input_with_spaces.split(' ')[-1]:
                    print('Opening Chromium Web Browser....')
                    os.system('chromium')
                    response_given = True




            ##############################Checking if the Input is "WHEN DOES THE SUNSET?"#####
            asking_for_sunset_sunrise = 0
            asking_for_sunset_sunrise_country = 0
            if "sunset" in user_input_with_spaces or "sunset".capitalize() in user_input_with_spaces or "sunset".lower() in user_input_with_spaces or "sunset".upper() in user_input_with_spaces or "sunrise" in user_input_with_spaces or "sunrise".capitalize() in user_input_with_spaces or "sunrise".lower() in user_input_with_spaces or "sunrise".upper() in user_input_with_spaces:
                asking_for_sunset_sunrise += 1
            if 'sunset' not in user_input_with_spaces.split(' ')[-1] and 'sunrise' not in user_input_with_spaces.split(' ')[-1] and asking_for_sunset_sunrise > 0:
                asking_for_sunset_sunrise = 0
                asking_for_sunset_sunrise_country += 1

            #If asking For sunset
            #inside own country
            if asking_for_sunset_sunrise > 0 and asking_for_sunset_sunrise_country == 0:                        
                search_request_url = 'https://www.timeanddate.com/sun/?query=' + current_country_name_with_plus
                requesting_url = Request(search_request_url, headers={'User-Agent': 'Mozilla/5.0'})

                source = urlopen(requesting_url).read()

                soup = bs.BeautifulSoup(source, 'html5lib')

                link_to_go = soup.findAll(True, {'class', 'c0'})[0].findAll('td')[0].findAll('a')[0]['href']

                search_request_url = "https://www.timeanddate.com" + str(link_to_go)
                requesting_url = Request(search_request_url, headers={'User-Agent': 'Mozilla/5.0'})

                source = urlopen(requesting_url).read()

                soup = bs.BeautifulSoup(source, 'html5lib')

                chunk_of_text_contain_useful = soup.findAll(True, {"class":"dn-mob"})[1].text
                chunk_of_text_divide_space = chunk_of_text_contain_useful.split(' ')
                sunrise = chunk_of_text_divide_space[0]
                sunset = chunk_of_text_divide_space[2][:5]
                print("Sunrise at "+str(sunrise))
                print("Sunset at "+str(sunset))
                #print(soup.prettify())

                response_given = True

            if asking_for_sunset_sunrise_country > 0 and asking_for_sunset_sunrise == 0:
                country_name = user_input_with_spaces.split(' ')[-1]
                url = "https://www.timeanddate.com/sun/?query=" + country_name
                requesting_url = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

                source = urlopen(requesting_url).read()

                soup = bs.BeautifulSoup(source, 'html5lib')
                
                link_to_go = soup.findAll(True, {'class', 'c0'})[0].findAll('td')[0].findAll('a')[0]['href']

                search_request_url = "https://www.timeanddate.com" + str(link_to_go)
                requesting_url = Request(search_request_url, headers={'User-Agent': 'Mozilla/5.0'})

                source = urlopen(requesting_url).read()

                soup = bs.BeautifulSoup(source, 'html5lib')

                chunk_of_text_contain_useful = soup.findAll(True, {"class":"dn-mob"})[1].text
                chunk_of_text_divide_space = chunk_of_text_contain_useful.split(' ')
                sunrise = chunk_of_text_divide_space[0]
                sunset = chunk_of_text_divide_space[2][:5]
                print("Sunrise at "+str(sunrise))
                print("Sunset at "+str(sunset))

                response_given = True
            
            ##############################Checking if the Input is "WHAT'S THE WEATHER?"#######
            asking_for_weather = 0
            asking_for_weather_country = 0
            if "weather" in user_input_with_spaces or "weather".capitalize() in user_input_with_spaces or "weather".lower() in user_input_with_spaces or "weather".upper() in user_input_with_spaces:
                asking_for_weather += 1
            if 'weather' not in user_input_with_spaces.split(' ')[-1] and asking_for_weather > 0:
                asking_for_weather = 0
                asking_for_weather_country += 1

            #If asking For Weather
            #Now
            if asking_for_weather > 0 and asking_for_weather_country == 0:                        
                url = "https://www.google.com/search?source=hp&ei=Dk6jXN3pOKKtgweQ8rmoCQ&q=whats+weather"
                requesting_url = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

                source = urlopen(requesting_url).read()

                soup = bs.BeautifulSoup(source, 'html5lib')

                temperature_now = soup.find_all(True, {'class':'wob_t'})[0].text
                wind_speed = soup.find_all(True, {'class':'wob_t'})[2].text
                location = soup.findAll(True, {'class':'e'})[0].findAll('h3')[0].find_all('b')[1].text
                word_for_weather = soup.findAll(True, {'style':'white-space:nowrap;padding-right:15px;color:#666'})[0].text
                humidity = soup.findAll(True, {'style':'white-space:nowrap;padding-right:0px;vertical-align:top;color:#666'})[0].text

                print("Location: " + location)
                print("Temperature: " + temperature_now)
                print("Speed of Wind: " + wind_speed)
                print("Humidity: " + humidity)
                print("Description: " + word_for_weather)

                response_given = True

            if asking_for_weather_country > 0 and asking_for_weather == 0:
                country_name = user_input_with_spaces.split(' ')[-1]
                url = "https://www.google.com/search?source=hp&ei=Dk6jXN3pOKKtgweQ8rmoCQ&q=whats+weather+" + country_name
                requesting_url = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

                source = urlopen(requesting_url).read()

                soup = bs.BeautifulSoup(source, 'html5lib')

                temperature_now = soup.find_all(True, {'class':'wob_t'})[0].text
                wind_speed = soup.find_all(True, {'class':'wob_t'})[2].text
                location = soup.findAll(True, {'class':'e'})[0].findAll('h3')[0].find_all('b')[1].text
                word_for_weather = soup.findAll(True, {'style':'white-space:nowrap;padding-right:15px;color:#666'})[0].text
                humidity = soup.findAll(True, {'style':'white-space:nowrap;padding-right:0px;vertical-align:top;color:#666'})[0].text

                print("Location: " + location)
                print("Temperature: " + temperature_now)
                print("Speed of Wind: " + wind_speed)
                print("Humidity: " + humidity)
                print("Description: " + word_for_weather)

                response_given = True

            ##############################Checking if the Input is "WHAT IS THE TIME NOW?"#######
            asking_for_time = 0
            asking_for_time_now = 0
            asking_for_time_country = 1
            if "time" in user_input_with_spaces or "time".capitalize() in user_input_with_spaces or "time".lower() in user_input_with_spaces or "time".upper() in user_input_with_spaces:
                asking_for_time += 1
                if "now" in user_input_with_spaces.split(' ')[-1] or "now".capitalize() in user_input_with_spaces.split(' ')[-1] or "now".lower() in user_input_with_spaces.split(' ')[-1] or "now".upper() in user_input_with_spaces.split(' ')[-1] or "it" in user_input_with_spaces.split(' ')[-1] or "it".capitalize() in user_input_with_spaces.split(' ')[-1] or "it".lower() in user_input_with_spaces.split(' ')[-1] or "it".upper() in user_input_with_spaces.split(' ')[-1]:
                    asking_for_time_now += 1
                    asking_for_time_country = 0
                else:
                    asking_for_time_now = 0
                    asking_for_time_country += 1

            #If asking For Time
            #Now
            if asking_for_time > 0 and asking_for_time_now > 0:                        
                #Getting date to one place
                date = datetime.datetime.now()
                #Date split by it's spaces
                date_split_by_spaces = str(date).split(' ')
                #Getting the time and assigning to a var
                time_now = date_split_by_spaces[1]
                #Getting each thing seperate
                hour = time_now.split(":")[0]
                minute = time_now.split(":")[1]

                print("It\'s " + str(minute) + " minutes past " + str(hour) + ". ")
                response_given=True
            if asking_for_time > 0 and asking_for_time_country > 0 and response_given == False:
                url = "https://www.google.com/search?source=hp&ei=8uihXIqXPLOKmgfI36SoCg&q=what+is+the+time+now+in+"
                country_name = user_input_with_spaces.split(' ')[-1]
                url += country_name
                x = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

                source = urlopen(x).read()


                soup = bs.BeautifulSoup(source, 'lxml')

                x = soup.find_all(True, {'class':'SFt5jb uRIxYb'})
                print(x[0].text)
                response_given=True

            ###########################################################################################



            ##############################Checking if the Input is beginning with "what is your"#######
            if user_input[:12] == "what is your":
                #Points for Guessing What the Input asks the AI
                asking_for_name_points=0
                asking_for_color_points=0
                #Getting the Last word of the User Input and FOR LOOPING EACH CHAR OF LAST word
                for char in user_input[(len(user_input)-7):]:
                    #Checking if the instance of char is equal to n,a,m,e,c,o,l,o,r and incrementing points by relavant
                    #Checking If name
                    if char == "n":
                        asking_for_name_points+=1
                    if char == "a":
                        asking_for_name_points+=1
                    if char == "m":
                        asking_for_name_points+=1
                    if char == "e":
                        asking_for_name_points+=1
    
                    #Checking If Color
                    if char == "c":
                        asking_for_color_points+=1
                    if char == "o":
                        asking_for_color_points+=1
                    if char == "l":
                        asking_for_color_points+=1
                    if char == "o":
                        asking_for_color_points+=1
                    if char == "r":
                        asking_for_color_points+=1

                #If Name Presents
                if "name" in user_input[(len(user_input)-7):] or "name".capitalize() in user_input[(len(user_input)-7):] or "name".lower() in user_input[(len(user_input)-7):] or "name".upper() in user_input[(len(user_input)-7):]:
                    asking_for_name_points += 100
                
                #If Color Presents
                if "color" in user_input[(len(user_input)-7):] or "color".capitalize() in user_input[(len(user_input)-7):] or "color".lower() in user_input[(len(user_input)-7):] or "color".upper() in user_input[(len(user_input)-7):]:
                    asking_for_color_points += 100

	            #Determining the Reponse on "What is your :END PART" by the most points collected
                if asking_for_name_points > 3 or asking_for_color_points > 4:
                    if asking_for_name_points > asking_for_color_points:
                        print(dialog_list[5])
                        response_given = True 
                    elif asking_for_color_points > asking_for_name_points:
                        print(dialog_list[9])
                        response_given = True
            ###########################################################################################
            





	        ########################Checking if the Input is beginning with "play"#####################
            if user_input[:4] == "play" or user_input[:4] == "Play":
                #Spliting the user input by it's spaces
                user_input_split_spaces = user_input_with_spaces.split(' ')
                #Checking if the user have given the Music Name with More Details
                if len(user_input_split_spaces) > 2:
                    #Making Boxes for Holding Each Splited Word of Music
                    music_split_1 = ''
                    music_split_2 = ''
                    music_split_3 = ''
                    music_split_4 = ''
                    music_split_5 = ''
                    music_split_6 = ''
                    music_split_7 = ''
                    music_split_8 = ''
                    music_split_9 = ''
                    #Trying to Assign values for these Little Boxes
                    try:
                        music_split_1 = user_input_split_spaces[-1]
                        music_split_2 = user_input_split_spaces[-2]
                        music_split_3 = user_input_split_spaces[-3]
                        music_split_4 = user_input_split_spaces[-4]
                        music_split_5 = user_input_split_spaces[-5]
                        music_split_6 = user_input_split_spaces[-6]
                        music_split_7 = user_input_split_spaces[-7]
                        music_split_8 = user_input_split_spaces[-8]
                        music_split_9 = user_input_split_spaces[-9]
                    except:
                        pass
                    finally:
                        pass
                    #Getting a list of All Music Items
                    list_of_all_music = os.listdir()
                    #music_dic_with_thier_selection_rate
                    music_selection_rate_dic = {}
                    #for looping that list and appending the song and thier success rate to the dic
                    for music in list_of_all_music:
                        selection_rate = 0
                        try:
                            #If the word found selection rate will get 100 Points
                            if music_split_1 in music or music_split_1.capitalize() in music or music_split_1.lower() in music or music_split_1.upper() in music:
                                selection_rate += 100
                            if music_split_2 in music or music_split_2.capitalize() in music or music_split_2.lower() in music or music_split_2.upper() in music:
                                selection_rate += 100
                            if music_split_3 in music or music_split_3.capitalize() in music or music_split_3.lower() in music or music_split_3.upper() in music:
                                selection_rate += 100
                            if music_split_4 in music or music_split_4.capitalize() in music or music_split_4.lower() in music or music_split_4.upper() in music:
                                selection_rate += 100
                            if music_split_5 in music or music_split_5.capitalize() in music or music_split_5.lower() in music or music_split_5.upper() in music:
                                selection_rate += 100
                            if music_split_6 in music or music_split_6.capitalize() in music or music_split_6.lower() in music or music_split_6.upper() in music:
                                selection_rate += 100
                            if music_split_7 in music or music_split_7.capitalize() in music or music_split_7.lower() in music or music_split_7.upper() in music:
                                selection_rate += 100
                            if music_split_8 in music or music_split_8.capitalize() in music or music_split_8.lower() in music or music_split_8.upper() in music:
                                selection_rate += 100
                            if music_split_9 in music or music_split_9.capitalize() in music or music_split_9.lower() in music or music_split_9.upper() in music:
                                selection_rate += 100
                            else:
                                selection_rate = 0
                        except:
                            pass
                        finally:
                            pass
                        #Appending Values for the Dictionary
                        music_selection_rate_dic[selection_rate] = music

                    #Checking if all the selection rates are 0 so it means "MUSIC NOT FOUND!"
                    sum_of_all_rates = 0
                    for rate in music_selection_rate_dic.keys():
                        sum_of_all_rates += int(rate)
                    
                    if sum_of_all_rates == 0:
                        #Error Gives Out if Sum Of All Rates Equals To 000000
                        print("Music Not Found in ~/Music Folder")
                        response_given = True
                    else:
                        #Selecting the highest selection rate music
                        musicWithHighestSelection = music_selection_rate_dic[max(i for i in music_selection_rate_dic.keys() if True)]
                        #Printing out to screen Now Playing
                        print('Now Playing ' + str(musicWithHighestSelection))
                        #Playing the Music
                        song = AudioSegment.from_mp3(str(musicWithHighestSelection))

                        play(song)
                        response_given = True


                if len(user_input_split_spaces) == 2:

                    #Getting the Name of the Music
                    music_name = user_input_split_spaces[-1]
                    #Getting a list of All Music Items
                    list_of_all_music = os.listdir()
                    #music_dic_with_thier_selection_rate
                    music_selection_rate_dic = {}
                    #for looping that list and appending the song and thier success rate to the dic
                    for music in list_of_all_music:
                        selection_rate = 0
                        if music_name in music or music_name.capitalize() in music or music_name.lower() in music or music_name.upper() in music:
                            selection_rate += 100
                        else:
                            selection_rate = 0
                        music_selection_rate_dic[selection_rate] = music

                    #Checking if all the selection rates are 0 so it means "MUSIC NOT FOUND!"
                    sum_of_all_rates = 0
                    for rate in music_selection_rate_dic.keys():
                        sum_of_all_rates += int(rate)
                    
                    if sum_of_all_rates == 0:
                        #Error Gives Out if Sum Of All Rates Equals To 000000
                        print("Music Not Found in ~/Music Folder")
                        response_given = True
                    else:
                        #Selecting the highest selection rate music
                        musicWithHighestSelection = music_selection_rate_dic[max(i for i in music_selection_rate_dic.keys() if True)]
                        #Printing out to screen Now Playing
                        print('Now Playing ' + str(musicWithHighestSelection) )
                        #Playing the Music
                        song = AudioSegment.from_mp3(str(musicWithHighestSelection))

                        play(song)
                        response_given = True
                        
            ###########################################################################################















            #################Checking the Equality of User Input to Our Dialogues######################
            #The length of the Input
            input_length = len(user_input)
		    	    
            #index variable for forloop.counter
            index = 0

            #Dictionary for holding the word and it's equality
            wordEqual = {}

            #Reponse with Highest Equal Marks will Nove b rset
            responseHighestEquality = ''
		
            #For every dialog in the dialog_list
            for dialog in dialog_list:
            #ANother time checking if the response have given
                if response_given == False:
                    #equal points equal to number of chars equal of each dialogue
                    equal_points = 0
                    #for the numbers in number range of user input length
                    for num in range((len(user_input)-1)):
                        try:
                            #checking if char of dialog corrospond equal to user input correspond's char
                            if dialog[num] == user_input[num]:
                                equal_points+=1
                        except:
                            pass
                        finally:
                            pass

                        #Making new Dictionary Key Value Pairs in wordEqual
                        try:
                            wordEqual[equal_points] = dialog_list_with_spaces[(index+1)]
                        except:
                            pass
                        finally:
                            pass

                index += 1
                
            if response_given == False:
                #Reponse With The Highest Equality Wins and Prints
                responseHighestEquality = wordEqual[max(i for i in wordEqual.keys() if True)]
                #Printing the Reponse
                print(responseHighestEquality)
            ###########################################################################################

################################################# - THE END - #########################################
