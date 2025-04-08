from flask import render_template, request, jsonify, session, redirect, url_for
import logging
from game_logic import game_instance
from app import db, app

def get_card_image_number(card_id):
    """Get image number based on card ID"""
    # Simply use the card ID directly (assuming IDs go from 1 to 100)
    # This ensures each card always gets the same image
    return card_id

def register_routes(app):
    @app.route('/')
    def index():
        """Render the home page"""
        # Home page with simple player inputs
        return render_template('index.html')
        
    @app.route('/start_game', methods=['POST', 'GET'])
    def start_game():
        """Start a new game with player names"""
        if request.method == 'POST':
            player1_name = request.form.get('player1_name', 'Player 1')
            player2_name = request.form.get('player2_name', 'Player 2')
            
            # Reset game state for a new game with player names
            game_state = game_instance.start_new_game(player1_name, player2_name)
            max_rounds = game_state['max_rounds']
            
            # Render the main game page directly
            return render_template('game.html', 
                                  player1_name=player1_name, 
                                  player2_name=player2_name,
                                  max_rounds=max_rounds)
        else:
            # If accessed directly with GET, redirect to home page
            return redirect(url_for('index'))
        
    @app.route('/cards')
    def cards():
        """Render the cards collection page"""
        all_cards = game_instance.load_cards()
        return render_template('cards.html', cards=all_cards, get_card_image_number=get_card_image_number)
        
    @app.route('/results')
    def results():
        """Render the game results page"""
        player1 = request.args.get('p1', 'Player 1')
        player1_score = int(request.args.get('p1s', 0))
        player2 = request.args.get('p2', 'Player 2')
        player2_score = int(request.args.get('p2s', 0))
        
        winner = None
        if player1_score > player2_score:
            winner = player1
        elif player2_score > player1_score:
            winner = player2
        
        return render_template('results.html', 
                              player1=player1, 
                              player1_score=player1_score,
                              player2=player2,
                              player2_score=player2_score,
                              winner=winner)
        
    @app.route('/draw_cards', methods=['POST'])
    def draw_cards():
        """API endpoint to draw cards for both players"""
        player1_card, player2_card = game_instance.draw_cards()
        
        if not player1_card or not player2_card:
            return jsonify({'error': 'No more cards to draw'}), 400
            
        return jsonify({
            'player1_card': player1_card.to_dict(),
            'player2_card': player2_card.to_dict()
        })
        
    @app.route('/compare_cards', methods=['POST'])
    def compare_cards():
        """API endpoint to compare cards based on selected attribute"""
        data = request.json
        attribute = data.get('attribute')
        player1_card_data = data.get('player1_card')
        player2_card_data = data.get('player2_card')
        
        # This would ideally come from the server-side game state
        # but for this implementation we'll use the client data
        from models import Card
        
        # Create temporary card objects for comparison
        player1_card = Card()
        player1_card.id = player1_card_data['id']
        player1_card.name = player1_card_data['name']
        player1_card.type = player1_card_data['type']
        player1_card.rank = player1_card_data['rank']
        player1_card.hp = player1_card_data['hp']
        player1_card.attack = player1_card_data['attack']
        player1_card.defense = player1_card_data['defense']
        player1_card.speed = player1_card_data['speed']
        player1_card.intelligence = player1_card_data['intelligence']
        
        player2_card = Card()
        player2_card.id = player2_card_data['id']
        player2_card.name = player2_card_data['name']
        player2_card.type = player2_card_data['type']
        player2_card.rank = player2_card_data['rank']
        player2_card.hp = player2_card_data['hp']
        player2_card.attack = player2_card_data['attack']
        player2_card.defense = player2_card_data['defense']
        player2_card.speed = player2_card_data['speed']
        player2_card.intelligence = player2_card_data['intelligence']
        
        winner = game_instance.compare_cards(player1_card, player2_card, attribute)
        
        return jsonify({
            'winner': winner,
            'game_state': game_instance.get_game_state()
        })
        
    @app.route('/game_state')
    def game_state():
        """API endpoint to get current game state"""
        return jsonify(game_instance.get_game_state())
        
    @app.route('/reseed_database')
    def reseed_database():
        """Force reseed the database with all cards"""
        from models import Card, get_card_data
        
        try:
            # First delete all existing cards
            print("Deleting existing cards...")
            Card.query.delete()
            db.session.commit()
            
            # Now add all 100 cards
            card_data = get_card_data()
            print(f"Adding {len(card_data)} cards to database...")
            
            for idx, card_dict in enumerate(card_data):
                card = Card(
                    id=idx + 1,
                    name=card_dict["name"],
                    type=card_dict["type"],
                    rank=card_dict["rank"],
                    hp=card_dict["hp"],
                    attack=card_dict["attack"],
                    defense=card_dict["defense"],
                    speed=card_dict["speed"],
                    intelligence=card_dict["intelligence"]
                )
                db.session.add(card)
            
            db.session.commit()
            card_count = Card.query.count()
            
            return f"Database reseeded with {card_count} cards. <a href='/cards'>View Cards</a>"
        except Exception as e:
            db.session.rollback()
            return f"Error reseeding database: {str(e)}"