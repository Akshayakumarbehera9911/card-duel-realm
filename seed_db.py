from app import app, db
from models import Card, get_card_data

def seed_database():
    with app.app_context():
        try:
            # Check if cards already exist
            existing_count = Card.query.count()
            print(f"Found {existing_count} existing cards")
            
            # Only seed if no cards exist or count is wrong
            if existing_count != 100:
                # Delete existing cards if any
                if existing_count > 0:
                    print(f"Deleting {existing_count} existing cards...")
                    Card.query.delete()
                    db.session.commit()
                
                # Add all 100 cards
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
                new_count = Card.query.count()
                print(f"Database seeded with {new_count} cards.")
                
                # Verify a few random cards
                sample_cards = Card.query.filter(Card.id.in_([1, 50, 100])).all()
                for card in sample_cards:
                    print(f"Card {card.id}: {card.name} ({card.type}) - Rank {card.rank}")
            else:
                print("Database already contains all 100 cards. No seeding required.")
                
        except Exception as e:
            db.session.rollback()
            print(f"Error seeding database: {str(e)}")

if __name__ == "__main__":
    seed_database()