from media import Movie
import fresh_tomatos as FT


# Initialize some movies here, respect the constructor order: Title, youtube_url, storyline, movie_photo_link

harry_potter_1 = Movie("Harry Potter and the Philosopher's Stone",
                       "https://www.youtube.com/watch?v=VyHV0BRtdxo",
                        "Rescued from the outrageous neglect of his aunt and uncle,"
                        "a young boy with a great destiny proves his worth while attending "
                        "Hogwarts School of Witchcraft and Wizardry.",
                        "https://vignette.wikia.nocookie.net/harrypotter/images/0/0e/Philostone.jpg/revision/latest/scale-to-width-down/338?cb=20170824190451")


harry_potter_2 = Movie("Harry Potter and the Chamber of Secrets",
                       "https://www.youtube.com/watch?v=1bq0qff4iF8",
                       "Harry ignores warnings not to return to Hogwarts,"
                       " only to find the school plagued by a series of "
                       "mysterious attacks and a strange voice haunting him.",
                       "https://i.jeded.com/i/harry-potter-and-the-chamber-of-secrets.12466.jpg")

harry_potter_3 = Movie("Harry Potter and the Prisoner of Azkaban",
                       "https://www.youtube.com/watch?v=lAxgztbYDbs",
                       "It's Harry's third year at Hogwarts; not only does"
                       " he have a new \"Defense Against the Dark Arts\" teacher,"
                       " but there is also trouble brewing. Convicted murderer Sirius Black has escaped "
                       "the Wizards' Prison and is coming after Harry.",
                       "http://vignette1.wikia.nocookie.net/harrypotter/images/c/c4/7VTALkqjG40vby3uVIsp03d7yXy.jpg/revision/latest?cb=20130803163319")

harry_potter_4 = Movie("Harry Potter and the Goblet of Fire",
                       "https://www.youtube.com/watch?v=BNcW1JLJ660",
                       "A young wizard finds himself competing"
                       " in a hazardous tournament between rival"
                       " schools of magic, but he is distracted by"
                       " recurring nightmares.",
                       "https://vignette.wikia.nocookie.net/harrypotter/images/2/2c/Goblet_of_Fire_Film_Poster.jpg/revision/latest/scale-to-width-down/333?cb=20140817011104")

movie_list = [harry_potter_1,harry_potter_2,harry_potter_3,harry_potter_4]
start_page = FT.open_movies_page(movie_list)