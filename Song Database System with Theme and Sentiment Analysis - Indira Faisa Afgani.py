
from tabulate import tabulate # Import database nya
from datetime import datetime

themes = [
    'Love',
    'Life',
    'Friendship',
    'Self Growth',
    'Escapism',
    'Mental Health', 
    'Family',
    'Social Issues',
    'Other'
    ]

song_data = [   

    {'song_id' : '1',
     'song_title' : 'Count on Me',
     'artist' : 'Bruno Mars',
     'year' : 2011,
     'theme' : 'Friendship',
     'sentiment_score' : 2,
     'sentiment_descriptions' : 'Expressing loyalty, emotional support, and reliability in friendship.',
     'lyrics_excerpt' : "You'll always have my shoulder when you cry"
     },

    {'song_id' : '2', 
     'song_title' : 'Put Your Records On',
     'artist' : 'Corinne Bailey Rae',
     'year' : 2006,
     'theme' : 'Self Growth',
     'sentiment_score' : 2,
     'sentiment_descriptions' : 'Promoting self-acceptance, inner peace, and emotional resilience.',
     'lyrics_excerpt' : "You're gonna find yourself somewhere, somehow."
    },
    
    {'song_id' : '3', 
     'song_title' : 'Listen Before I Go',
     'artist' : 'Billie Eilish',
     'year' : 2019,
     'theme' : 'Mental Health',
     'sentiment_score' : -2,
     'sentiment_descriptions' : 'Expressing distress, loneliness, and despair.',
     'lyrics_excerpt' : 'I wanna see the world when I stop breathing.'
    },
    
    {'song_id' : '4', 
     'song_title' : 'Pocket Locket',
     'artist' : 'Alaina Castillo',
     'year' : 2021,
     'theme' : 'Love',
     'sentiment_score' : -1,
     'sentiment_descriptions' : 'Expressing emotional vulnerability and attachment within a romantic relationship',
     'lyrics_excerpt' : "I don't see my love as weakness, I know in the end you'll be the one."
    },

    {'song_id' : '5', 
     'song_title' : 'Valentine',
     'artist' : 'Laufey',
     'year' : 2022,
     'theme' : 'Love',
     'sentiment_score' : 2,
     'sentiment_descriptions' : 'Portraying affection and romantic longing in a gentle and sincere manner.',
     'lyrics_excerpt' : "'Cause I think I've fallen in love this time"
    },
    
    {'song_id' : '6', 
     'song_title' : 'Criminal',
     'artist' : 'Britney Spears',
     'year' : 2011,
     'theme' : 'Love',
     'sentiment_score' : -2,
     'sentiment_descriptions' : "Portraying romantic attraction toward a socially disapproved or 'dangerous' partner",
     'lyrics_excerpt' : "He lies, he bluffs, he's unreliable."
    },
    
    {'song_id' : '7', 
     'song_title' : 'Nightcrawlers',
     'artist' : 'Niki',
     'year' : 2020,
     'theme' : 'Life',
     'sentiment_score' : -2,
     'sentiment_descriptions' : 'Enjoying life without thinking of the consequences',
     'lyrics_excerpt' : "We don't really think about the after, we just run like hell 'til we're cadavers"
    },
    
    {'song_id' : '8',
     'song_title' : "That's Life",
     'artist' : 'Frank Sinatra',
     'year' : 1966,
     'theme' : 'Life',
     'sentiment_score' : 1,
     'sentiment_descriptions' : 'Portraying failure, disappointment, and the cyclical nature of success and struggle',
     'lyrics_excerpt' : "I've been a puppet, a pauper, a pirate, a poet, a pawn and a king."
    },
    
    {'song_id' : '9', 
     'song_title' : '1-800-273-8255',
     'artist' : 'Logic',
     'year' : 2017,
     'theme' : 'Mental Health',
     'sentiment_score' : -1,
     'sentiment_descriptions' : 'Begins with intense emotional distress, but gradually shifts toward seeking help and choosing to stay alive',
     'lyrics_excerpt' : "I don't wanna be alive, I just wanna die today"
    },
    
    {'song_id' : '10', 
     'song_title' : 'Where Is The Love?',
     'artist' : 'The Black Eyed Peas',
     'year' : 2003,
     'theme' : 'Social Issues',
     'sentiment_score' : -1,
     'sentiment_descriptions' : 'The song criticizes violence, discrimination, terrorism, and social injustice, questioning the moral direction of society.',
     'lyrics_excerpt' : "What's going on with the world, momma?"
    }

]

songs = song_data

def show_table(songs):
    table = []

    for song in songs:
        
        desc = song['sentiment_descriptions']
        lyrics = song['lyrics_excerpt']

        if len(desc) > 25:
            desc = desc[0:25] + "..."

        if len(lyrics) > 25:
            lyrics = lyrics[0:25] + "..."

        table.append([
            song['song_id'],
            song['song_title'],
            song['artist'],
            song['year'],
            song['theme'],
            song['sentiment_score'],
            desc,
            lyrics
        ]) 

    print(tabulate(table, headers=['ID', 'Song Title', 'Artist', 'Year', 'Theme', 'Sentiment Score', 'Sentiment Descriptions', 'Lyrics Excerpt'], tablefmt='heavy_outline'))

def read_menu(songs): 
    
    while True:
        print('''
The Songs' Database:
1. Show all the database
2. Show data by ID
3. Search data
4. Back to main menu
        ''')

        read_choice = input("Please enter the option's number here: ").strip()
        
        if read_choice == '1': 
            print ('Here is the current database:')
            show_table(songs)
        
        elif read_choice =='2': 
            data_found = False 
            search_id = input('Enter the ID :').strip()

            for song in songs: 
                if song['song_id'] == search_id:
                    print_search_song (song)
                    data_found = True
                    break
            
            if not data_found:
                print("The song ID does not exist in the database!")

        elif read_choice =='3': 
            search_song (songs)

        elif read_choice =='4':
            break

        else:
            print("\n The number you just input is invalid! Please refer to The Song's Database Menu for the number.")

def search_song(songs):
    
    while True:
        print('''
DISCLAIMER! You may search the database by:
    1. Song Title
    2. Artist
    3. Year
    4. Theme
    5. Sentiment Score
        ''')

        search_data = input('Please enter the number of your options here: ').lower().strip()

        # SEARCH DARI JUDUL
        if search_data =='1':
            data_found = False
            search_song_title = input ('Enter the song title: ').strip()

            for song in songs:
                if song['song_title'].lower() == search_song_title.lower():
                    print_search_song (song)
                    data_found = True
                
            if not data_found:
                print('The song does not exist in the database!')
        
            break
        
        # SEARCH NAMA ARTIST
        elif search_data == '2':
            data_found = False
            search_artist = input ('Enter the name of the artist: ').strip()

            for song in songs:
                if song['artist'].lower() == search_artist.lower():
                    print_search_song (song)
                    data_found = True
                
            if not data_found:
                print('The artist does not exist in the database!')
            
            break

        # SEARCH TAHUN
        elif search_data == '3':
            data_found = False
            search_year = input ('Enter the year of the song: ').strip()

            if search_year.isdigit():
                search_year = int(search_year)

                for song in songs:
                    if song['year'] == search_year:
                        print_search_song (song)
                        data_found = True
                    
                if not data_found:
                    print('The year does not exist in the database!')
            
            else:
                print('The year is invalid!')     

            break               

        # SEARCH THEME
        elif search_data == '4':
            data_found = False
            search_theme = input ('Enter the theme of the song: ').strip()

            for song in songs:
                if song['theme'].lower() == search_theme.lower():
                    print_search_song (song)
                    data_found = True
            
            if not data_found:
                print('The theme does not exist in the database!')
            
            break
        
        # SEARCH SENTIMENT SCORE
        elif search_data == '5':
            data_found = False

            while True:
                try:
                    search_sentiment_score = int(input('Enter the sentiment score: ').strip())

                    if search_sentiment_score not in [-2, -1, 1, 2]:
                        print('The score does not exist in the database!')
                        break # KENAPA INI PERLU 2 BREAK?

                    else:
                        for song in songs: 
                            if song['sentiment_score'] == search_sentiment_score:
                                print_search_song (song)
                                data_found = True     
                        
                    break
                
                except ValueError:
                    print('The score is invalid! Please enter a valid number.')
            
            break

        else:
                print("Invalid option! Please try again.")
    
def print_search_song (song):
    print(f'''\n
Here is the data you are looking for: 
    ID:{song['song_id']}
    Song Title: {song['song_title']}
    Artist: {song['artist']}
    Year: {song['year']}
    Theme: {song['theme']}
    Sentiment Score: {song['sentiment_score']}
    Sentiment Descriptions: {song['sentiment_descriptions']}
    Lyrics Excerpt: {song['lyrics_excerpt']}
        ''')

def add_song(songs):

    while True:
        print('''
Add Songs to Database:
1. Add songs and datas
2. Back to main menu
        ''')

        add_choice = input("Please enter the option's number here: ").strip()
        
        if add_choice == '1': 
            # AUTO GENERATE ID
            existing_id = [int(song['song_id']) for song in songs]
            new_id = str(max(existing_id, default=0)+1)

            print(f'The new song ID (Auto-generated) is {new_id}')

            new_song = {}
            new_song['song_id'] = new_id 

            # ADD SONG 
            while True: 
                add_song_title = input('Enter the title of the song: ').strip()

                if add_song_title == '':
                    print('The title of the song is empty. Please enter the name of the song.')
                else: 
                    break

            # ADD ARTIST
            while True:
                add_artist = input('Enter the name of the artist: ').title().strip()

                if add_artist =='':
                    print("The artist's name is empty! Please enter the name of the artist.")
                else:
                    break
            
            if duplicate_song(songs, add_song_title, add_artist):
                print("This song already exists in the database!")
                continue
                
            # ADD YEAR
            while True: 
                add_year = input('Enter the year the song was released (1800 - 2026): ').strip()
                current_year = datetime.now().year

                if not add_year.isdigit():
                    print('The year you just input is invalid! Please put numbers only.')
                    continue

                add_year = int(add_year)
                
                if add_year == 0:
                    print('The year cannot be 0! Please refer to the database and enter a positive number only for the ID.')
                    continue

                if 1800 <= add_year <= current_year:
                    break
                else:
                    print('The year you input is invalid! Please input the valid year of the song.')

            # ADD THEME
            print('''
Please enter the theme based on the option below:
    1. Love 
    2. Life 
    3. Friendship
    4. Self Growth
    5. Escapism 
    6. Mental Health
    7. Family
    8. Social Issues
    9. Other (Please put the description in the score descriptions.)
            ''')

            while True:

                add_theme = input('Please enter the number of the theme here: ').strip()
                
                if add_theme.isdigit():
                    add_theme = int(add_theme)

                    if 1 <= add_theme <= len(themes):
                        new_song['theme'] = themes[add_theme - 1]                        
                        break
                    else:
                        print("Invalid number!")
                else: 
                    print('The theme is invalid! Please enter the theme based on the options above')

            # ADD SENTIMENT SCORE
            print('''
Before adding the sentiment score, please review the guidelines below!

Sentiment Score Guideline: 
-2 : Very Negative
-1 : Negative
 1 : Positive
 2 : Very Positive
            ''')

            while True: 
                try:

                    add_sentiment = int(input('Enter the sentiment score (-2 to 2): ').strip())
                    
                    if add_sentiment in [-2, -1, 1, 2]:
                        break

                    else:
                        print('The score is invalid! Please refer to the guidelines for the scoring.')
                        continue
                
                except ValueError:
                    print('The score is invalid! Please enter a valid number.')
                
            # ADD SENTIMENT DESCRIPTIONS
            while True:
                add_sentiment_descriptions = input("Enter the sentiment score's descriptions :").capitalize().strip()

                if add_sentiment_descriptions =='':
                    print('The descriptions is empty! Please enter the description of the song.')
                else:
                    break

            # ADD LYRICS
            while True:
                add_lyrics = input('Enter the excerpt of the lyrics: ').capitalize().strip()

                if add_lyrics =='':
                    print('The lyrics excerpt is empty! Please insert the excerpt.')
                else:
                    break

            while True:
                confirm = input("Are you sure you want to save this song? (Yes/No): ").lower().strip()
                
                if confirm == 'yes':
                    songs.append({'song_id':new_id, 'song_title':add_song_title, 'artist':add_artist, 'year': add_year, 'theme' : themes[add_theme - 1], 'sentiment_score' : add_sentiment, 'sentiment_descriptions' : add_sentiment_descriptions, 'lyrics_excerpt' : add_lyrics})
                    print('Song Database: \n')
                    show_table(songs)

                    print(f"Congratulations! {add_song_title.title()} by {add_artist.title()} has been added to the database!")

                    break

                elif confirm == 'no':
                    print("Song was not saved!")
                    
                    break

                else:
                    print("Invalid input! Please type 'yes' or 'no'.")
        
        elif add_choice == '2':
            break

        else:
            print("\n The number you just input is invalid! Please refer to the Add Songs to Database menu.")

def duplicate_song(songs, song_title, artist): # To check duplicate songs and artists
    song_title = song_title.strip().lower()
    artist = artist.strip().lower()

    for song in songs:
        if (song['song_title'].strip().lower() == song_title.lower() and song['artist'].strip().lower() == artist.lower()):
            return True
    return False

def update_song (songs):
    
    while True: 
        print('''
Update songs from the Database:
1. Update songs and datas
2. Back to main menu
        ''')

        update_choice = input("Please enter the option's number here: ").strip()

        if update_choice == '1':

            input_song_id = input("\n Please enter the song's ID that you want to update :").strip()

            song_to_update = False 
            for song in songs: 
                if song['song_id'] == input_song_id:
                    song_to_update = song
                    break
            
            if song_to_update is False: 
                print('The ID does not exist! Please refer to the database for the ID Numbers and the songs.')
                continue

            print(f'''
\n This is the song that you want to update :
    ID:{song_to_update['song_id']}
    Song Title: {song_to_update['song_title']}
    Artist: {song_to_update['artist']}
    Year: {song_to_update['year']}
    Theme: {song_to_update['theme']}
    Sentiment Score: {song_to_update['sentiment_score']}
    Sentiment Descriptions: {song_to_update['sentiment_descriptions']}
    Lyrics Excerpt: {song_to_update['lyrics_excerpt']}
            ''') 

            checker_update = False

            while True:
                checker = input("Are you sure you want to update the data (Yes/No): ").lower().strip()

                if checker == 'yes':                     
                        
                    while True:
                        print('''
Update options:
    1. Theme
    2. Sentiment Score
    3. Sentiment Description
    4. Lyrics
    5. Finish Update
                        ''')
                        
                        update_options = input('Choose the numbers you want to update: ').strip()

                        # UPDATE THEME
                        if update_options == '1':

                            print('''
Please enter the theme based on the option below:
1. Love 
2. Life 
3. Friendship
4. Self Growth
5. Escapism 
6. Mental Health
7. Family
8. Social Issues
9. Other
                            ''')

                            while True:

                                update_theme = input('Please enter the number of the new theme here: ').strip()
                                
                                if update_theme.isdigit():
                                    update_theme = int(update_theme)

                                    if 1 <= update_theme <= len(themes):
                                        old_value = song_to_update['theme']
                                        new_value = themes[update_theme - 1]

                                        if confirm_update('Theme', old_value, new_value):
                                            song_to_update['theme'] = new_value
                                            print("Theme is updated successfully!")
                                        else:
                                            print("Update cancelled.")
                                    
                                    break

                                else:
                                    print("Invalid number! Please choose between 1-8.")
                            else: 
                                print('The theme is invalid! Please enter the number based on the options above')
                            
                        # UPDATE SENTIMENT SCORE
                        elif update_options == '2':

                            print('''
Before adding the sentiment score, please review the guidelines below!

Sentiment Score Guideline: 
-2 : Very Negative
-1 : Negative
 1 : Positive
 2 : Very Positive
                            ''')
                            
                            while True: 
                                try:
                                    update_sentiment_score = int(input('Please enter the new sentiment score: ').strip())

                                    if update_sentiment_score not in [-2, -1, 1, 2]:
                                        print('The score is invalid! Please refer to the sentiment score guideline for the scoring.')
                                        continue

                                    else:
                                       old_value = song_to_update['sentiment_score']
                                       new_value =update_sentiment_score

                                    if confirm_update('Sentiment Score', old_value, new_value):
                                            song_to_update['sentiment_score'] = new_value
                                            print("Sentiment score is updated successfully!")
                                    else:
                                        print("Update cancelled.")

                                    break
                                    
                                except ValueError:
                                    print('The score is invalid! Please enter a valid number.')
                                
                        # UPDATE SENTIMENT DESCRIPTIONS
                        elif update_options == '3':
                            while True: 
                                update_sentiment_descriptions = input('Please enter the new sentiment descriptions :').strip()

                                if update_sentiment_descriptions == '':
                                    print('The descriptions cannot be empty! Please enter something.')
                                    continue
                                
                                else:
                                    old_value = song_to_update['sentiment_descriptions']
                                    new_value = update_sentiment_descriptions
                                    
                                if confirm_update('Sentiment Descriptions', old_value, new_value):
                                    song_to_update['sentiment_descriptions'] = update_sentiment_descriptions
                                    print("Sentiment descriptions updated successfully!")
                                
                                else:
                                    print("Update cancelled.")
                                
                                break
                        
                        # UPDATE LYRICS
                        elif update_options == '4':
                            while True: 
                                update_lyrics = input('Please enter the new lyrics excerpt: ').strip()
                                
                                if update_lyrics =='':
                                    print('The lyrics cannot be empty! Please enter something.')
                                    continue

                                else:
                                    old_value = song_to_update['lyrics_excerpt']
                                    new_value = update_lyrics

                                if confirm_update('Lyrics Excerpt', old_value, new_value):
                                    song_to_update['lyrics_excerpt'] = update_lyrics
                                    print("Lyrics updated successfully!")
                                
                                else:
                                    print("Update cancelled.")
                                
                                break
            
                        # FINISH UPDATE
                        elif update_options == '5':
                            print("Update finished!")
                            break

                        else:
                            print("Invalid option!")
                    
                    break
                    
                elif checker == 'no':
                    print("Update cancelled.")
                    checker_update = True
                    break

                else:
                    print("Invalid input! Please type 'Yes' or 'No'.")
            
        elif update_choice == '2':
            break

        else:
            print("\n The number you just input is invalid! Please refer to the Update Songs from the Database menu.")

def confirm_update(field_name, old_value, new_value):
    while True:
        confirm = input(
            f"\nAre you sure you want to change the {field_name} "
            f"\nfrom '{old_value}' \nto '{new_value}'? (Yes/No): "
        ).lower().strip()

        if confirm == 'yes':
            return True
        elif confirm == 'no':
            return False
        else:
            print("Invalid input! Please type 'yes' or 'no'.")

def delete_song (songs):
    while True: 

        print('''
Delete Songs from Database:
1. Delete songs and datas
2. Back to main menu
        ''')

        delete_choice = input("Please enter the option's number here: ").strip()

        if delete_choice == '1':
            while True:
                delete_id = input('\nEnter the Song ID you would like to remove: ').strip()
                
                delete_song = False
                for song in songs:
                    if song ['song_id'] == delete_id:
                        delete_song = song
                        break
                
                if delete_song is False:
                    print("ID not found in database!")
                    break

                print(f'''
\n This is the song that you want to delete :
        ID:{delete_song['song_id']}
        Song Title: {delete_song['song_title']}
        Artist: {delete_song['artist']}
        Year: {delete_song['year']}
        Theme: {delete_song['theme']}
        Sentiment Score: {delete_song['sentiment_score']}
        Sentiment Descriptions: {delete_song['sentiment_descriptions']}
        Lyrics Excerpt: {delete_song['lyrics_excerpt']}
                ''') 

                # Pilihan ya atau tidak 
                while True:
                    checker=input("Are you sure you want to delete the data (Yes/No) :").lower().strip()

                    if checker == 'yes':
                        songs.remove (delete_song)
                        print('\n Song Database: \n')
                        show_table(songs)
                        print(f"\n{delete_song['song_title']} by {delete_song['artist']} has been deleted.")
                        break
                
                    elif checker == 'no':
                        print('Delete cancelled!')
                        break
                    
                    else: 
                        continue
                
                break
        
        elif delete_choice == '2':
            break

        else:
            print("\n The number you just input is invalid! Please refer to the Delete Songs from Database menu.")

def main_menu(songs): 

    while True:
        main_menu = input('''
Welcome to InDiSongAnalysis!

Main Menu:
1. The songs' database
2. Add a new song
3. Update the song entry 
4. Delete the existing song entry 
5. Exit the program

Please type your number here: ''').strip()

        if main_menu =='1': # Buat menu Read
            read_menu(songs)

        elif main_menu == '2': # Buat add new song
            add_song(songs)

        elif main_menu =='3': # Untuk Update existing song
            update_song(songs)

        elif main_menu == '4': # Untuk delete data
            delete_song(songs)

        elif main_menu == '5': # Untuk exit program
            print ('\n Thank you for accessing InDiSongAnalysis. May you have a great day ahead!')
            break
        
        else: # Untuk kalo ada yang masukin diluar 1 - 6
            print ('Your choice is invalid! Please refer to the Main Menu for the options.')


main_menu(songs)





