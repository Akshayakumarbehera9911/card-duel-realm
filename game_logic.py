import random
from models import Card, GameHistory

class Game:
    def __init__(self):
        self.cards = []
        self.player1_deck = []
        self.player2_deck = []
        self.player1_score = 0
        self.player2_score = 0
        self.round = 0
        self.max_rounds = 50
        self.player1_name = "Player 1"
        self.player2_name = "Player 2"
        
    def load_cards(self):
        """Load all cards from the database"""
        self.cards = Card.get_all_cards()
        return self.cards
        
    def start_new_game(self, player1_name=None, player2_name=None):
        """Start a new game by preparing decks for both players"""
        self.player1_score = 0
        self.player2_score = 0
        self.round = 0
        
        # Set player names if provided
        if player1_name:
            self.player1_name = player1_name
        if player2_name:
            self.player2_name = player2_name
            
        # Make sure all cards are loaded
        if not self.cards:
            self.load_cards()
            
        # Create a copy of all cards
        all_cards = self.cards.copy()
        
        # Shuffle the cards
        random.shuffle(all_cards)
        
        # Split cards between players
        half = len(all_cards) // 2
        self.player1_deck = all_cards[:half]
        self.player2_deck = all_cards[half:half*2]  # Ensure equal number of cards
        
        return {
            'player1_deck_size': len(self.player1_deck),
            'player2_deck_size': len(self.player2_deck),
            'max_rounds': self.max_rounds
        }
        
    def draw_cards(self):
        """Draw one card for each player"""
        if not self.player1_deck or not self.player2_deck or self.round >= self.max_rounds:
            return None, None
            
        player1_card = self.player1_deck.pop(0)
        player2_card = self.player2_deck.pop(0)
        self.round += 1
        
        return player1_card, player2_card
        
    def compare_cards(self, player1_card, player2_card, attribute):
        """Compare cards based on the selected attribute"""
        if not player1_card or not player2_card:
            return None
            
        # Get attribute values
        attr_map = {
            'hp': 'hp',
            'attack': 'attack',
            'defense': 'defense',
            'speed': 'speed',
            'intelligence': 'intelligence'
        }
        
        attr_key = attr_map.get(attribute.lower(), 'hp')
        
        player1_value = getattr(player1_card, attr_key)
        player2_value = getattr(player2_card, attr_key)
        
        # Determine winner
        if player1_value > player2_value:
            self.player1_score += 1
            return 'player1'
        elif player2_value > player1_value:
            self.player2_score += 1
            return 'player2'
        else:
            return 'tie'
            
    def get_game_state(self):
        """Get current game state"""
        return {
            'player1_name': self.player1_name,
            'player2_name': self.player2_name,
            'player1_score': self.player1_score,
            'player2_score': self.player2_score,
            'round': self.round,
            'player1_deck_size': len(self.player1_deck),
            'player2_deck_size': len(self.player2_deck),
            'max_rounds': self.max_rounds,
            'is_game_over': self.is_game_over()
        }
        
    def is_game_over(self):
        """Check if the game is over"""
        return (
            self.round >= self.max_rounds or 
            len(self.player1_deck) == 0 or 
            len(self.player2_deck) == 0
        )
        
    def get_winner(self):
        """Get the winner of the game"""
        if self.player1_score > self.player2_score:
            return 'player1'
        elif self.player2_score > self.player1_score:
            return 'player2'
        else:
            return 'tie'
            
    def save_game_history(self, db_session):
        """Save game history to database"""
        if not self.is_game_over():
            return None
            
        winner = self.get_winner()
        winner_name = None
        
        if winner == 'player1':
            winner_name = self.player1_name
        elif winner == 'player2':
            winner_name = self.player2_name
        
        # Create new game history record
        game_history = GameHistory(
            player1_name=self.player1_name,
            player2_name=self.player2_name,
            player1_score=self.player1_score,
            player2_score=self.player2_score,
            winner=winner_name,
            rounds_played=self.round
        )
        
        # Save to database
        db_session.add(game_history)
        db_session.commit()
        
        return game_history.to_dict()

# Create a global game instance
game_instance = Game()