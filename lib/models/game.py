from colorama import Fore, Style
from models.__init__ import CURSOR, CONN

class Game:

    def __init__(self):
        self.create_table()
        
    # create genre table
    def create_table(self):
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS games (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                console_id INTEGER,
                genre_id INTEGER
            )
        ''')
        CONN.commit()

    @classmethod
    def from_db(cls, row):
        return cls(id=row[0], name=row[1], console_id=row[2], genre_id=row[3])

    # Adds a game to games table
    @classmethod
    def add_game(self, name, console_id, genre_id):
        name_new = name.lower()
        CURSOR.execute("SELECT id FROM games WHERE name = ?", (name_new,))
        existing_id = CURSOR.fetchone()

        if existing_id:
            print(f'A game with the name "{name}" already exists.')
        else:
            CURSOR.execute("INSERT INTO games (name, console_id, genre_id) VALUES (?, ?, ?)", (name, console_id, genre_id))
            CONN.commit()

    # Delete game from games by game_id
    @classmethod
    def delete_by_id(self, game_id):
        CURSOR.execute("SELECT name FROM games WHERE id = ?", (game_id,))
        existing_game = CURSOR.fetchone()

        if existing_game:
            print(f"Deleting {existing_game} (id: {game_id})...")
            CURSOR.execute("DELETE FROM games WHERE id = ?", (game_id,)) 
            CONN.commit()
        else:
            print(f'A game with the name "{existing_game}" does not exist.')
    
    # delete game from games by name
    @classmethod
    def delete_by_name(self, name):
        name_search = name.lower()
        CURSOR.execute("SELECT id FROM games WHERE name = ?", (name_search))
        existing_id = CURSOR.fetchone()

        if existing_id:
            print(f"Deleting {name} (id: {existing_id})...")
            CURSOR.execute("DELETE FROM gamess WHERE id = ?", (existing_id)) 
            CONN.commit()
        else:
            print(f'A game with the name "{name}" does not exist.')
    
    # find games by id
    def find_by_id(self, game_id):
        CURSOR.execute("SELECT * FROM games WHERE id = ?", (game_id))
        existing_game = CURSOR.fetchone()

        if existing_game:
            name = existing_game[1]
            print(f"{Fore.GREEN}Name: {name}{Style.RESET_ALL}")
        else: 
            print(f'{Fore.RED}A game with the id "{game_id}" does not exist.{Style.RESET_ALL}')

    # find games by name
    @classmethod
    def find_by_name(self, name):
        name_search = name.lower()
        CURSOR.execute("SELECT * FROM games WHERE name = ?", (name_search))
        existing_game = CURSOR.fetchone()

        if existing_game:
            name = existing_game[1]
            print(f"{Fore.GREEN}Name: {name}{Style.RESET_ALL}")
        else: 
            print(f'A game with the name "{name}" does not exist.')

    # get all games
    @classmethod
    def get_all_games(self):
        CURSOR.execute("SELECT * FROM games")
        all_games = CURSOR.fetchall()

        if all_games:
            for games in all_games:
                id, name, console_id, genre_id = games
                print(f"{Fore.GREEN}ID: {id} \nName: {name}\n{Style.RESET_ALL}")
        else: 
            print(f"{Fore.GREEN}There are no genres currently. Use the menu to add a genre.{Style.RESET_ALL}")
    

    def __repr__(self):
        return f"{self.name}"