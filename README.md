ABOUT THE PROJECT :- 

news_finder is a website which gives latest news information if you serarch any keyword.
It will give you your old search records as well as current search results.

GETTING STARTED :- Follow line by line istructions to get your project working in your system

1 > Clone project from github using :- 

        = > git clone "https://github.com/ankita1308/news_finder.git"

2> Open your project and get inside the project(news_finder) using : -
        
        = > cd news_finder

3 > Install virtual environment using :- 

        = > pip install virtualenv

4 > Create virtual environment in your system using : - 

        = > python -m venv myenv

5 > Activate virtual environment using :-

        = > myenv\Scripts\activate

6 > Install project dependencies(required packages) using :- 

        = > pip install -r .\requirements.txt

7 > Login to NewsAPI to generate token your secret key and paste that secret key in utils.py file of searchPage directory. Below are the query where you can set your key in apiKey variable.

    """ 
    parameters = {
        'q': query,  # query phrase
        'pageSize': 20,  # maximum is 100
        'apiKey': ""  # your own API key
    }

    """

8 > Run local server of project using :-

        = > py manage.py runserver

9 > Copy localhost(http://127.0.0.1:8000/) of your system and paste it into chrome to run :-

10 > Register yourself with providing details llike username, password, email

11 > Login yourself 

12 > Search keyword to get results

        
