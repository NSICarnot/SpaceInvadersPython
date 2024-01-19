import requests
import hashlib

"""
Wrapper pour l'API disponible sur ce repo :
https://git.hulkhogan6262.fr/NSICarnot/SpaceInvadersAPIPython
"""

url = "http://192.168.1.115:80"

class OnlinePlayer:
    def __init__(self, pseudo: str):
        self.pseudo = pseudo
        self.md5 = hashlib.md5(self.pseudo.encode('utf-8')).hexdigest()
    
    def get_best_score(self) -> int:
        """
        Return the best score of the player
        :return: The best score of the player
        """
        params = {
            "player": self.pseudo
        }
        return requests.get(f"{url}/player-score", params=params).json()["score"]
    
    def register_new_score(self, score: int) -> None:
        """
        Register a new score for the player
        :param score: The score to register
        :return: None
        """
        if not score < self.get_best_score():
            params = {
                "player": self.pseudo,
                "score": score,
                "hash": self.md5
            }
            requests.post(f"{url}/register-score", params=params)
        
def get_top(limit: int) -> list:
    """
    Return the best scores
    :param limit: The number of scores to return
    :return: The best scores
    """
    params = {
        "limit": limit
    }
    return requests.get(f"{url}/top", params=params).json()

def get_average() -> float:
    """
    Return the average score
    :return: The average score
    """
    return requests.get(f"{url}/average").json()

def get_entries() -> int:
    """
    Return the number of entries
    :return: The number of entries
    """
    return requests.get(f"{url}/entries").json()