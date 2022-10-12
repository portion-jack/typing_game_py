## ASAC_python_hw2
```
.
├── README.md
├── __game__.py     # game_file : function of typing game
├── __main__.py     # main_file : runs game  
├── __scoredb__.py  # scoredb_file : save and load score in game to show top contender
├── __words__.py    # words_file : crawls google trend and make it to typing game question 
├── source          # source_directory
│   ├── finally_did.MP3    # runs when player goes top 3
│   ├── finally_failed.MP3 # runs when player failed the game
│   ├── my_en_word.txt     # words_crawled in daily_google_trend US
│   ├── my_kr_word.txt     # words_crawled in daily_google_trend US
│   ├── score.db           # score_db for ranking
│   ├── success.MP3        # runs when player commits right answer
│   └── wrong.MP3          # runs when player commits wrong answer
└── versions.txt           # version of python and libraries
```
### typing_game
- kr version
- en version 
-   - both uses words in google_trend
-   - [google_trend](https://trends.google.com/trends/)
#### Rules
- 11 stages if you take over 7 : success
- score_ranking will be saved in score.db
- after game it prints top 3 players
- 1. based on accuracy
- 2. based on time
- 3. based on name


Need to install below libaries
>### Libraries
>- playsound
>- requests
>- beautifulsoup4
>- lxml
