import logging
from app import app, db
from models import Card, get_card_data, DATABASE_VERSION, DatabaseVersion

# Set up logger
logger = logging.getLogger(__name__)

# Always force reseed to ensure cards are updated on each deployment to Render
should_reseed = True
logger.info("Forcing database reseed for Render deployment")

def seed_database(force=False):
    """
    Seeds the database with card data
    
    Args:
        force (bool): If True, will reseed database even if cards already exist
                     Default is False which only seeds if cards are missing or count is wrong
    """
    with app.app_context():
        try:
            # Check if cards already exist
            existing_count = Card.query.count()
            logger.info(f"Found {existing_count} existing cards")
            
            # Check database version
            current_version = DatabaseVersion.query.first()
            # Always force reseed to ensure cards are updated on each deployment to Render
            should_reseed = True
            logger.info("Forcing database reseed for Render deployment")
            
            if current_version:
                logger.info(f"Database version: {current_version.version}, Latest version: {DATABASE_VERSION}")
            else:
                logger.info("No database version found. Will create version record.")
            
            # Reseed if forced, count is wrong, or version mismatch
            if should_reseed:
                logger.info("Reseeding database...")
                
                # Start a transaction
                try:
                    # Delete existing cards if any
                    if existing_count > 0:
                        logger.info(f"Deleting {existing_count} existing cards...")
                        Card.query.delete()
                        db.session.commit()
                    
                    # Add all cards
                    card_data = get_card_data()
                    logger.info(f"Adding {len(card_data)} cards to database...")
                    
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
                    
                    # Update or create version record
                    if current_version:
                        current_version.version = DATABASE_VERSION
                    else:
                        db.session.add(DatabaseVersion(version=DATABASE_VERSION))
                    
                    db.session.commit()
                    
                    # Log success
                    new_count = Card.query.count()
                    logger.info(f"Database seeded with {new_count} cards.")
                    
                    # Verify a few random cards
                    sample_cards = Card.query.filter(Card.id.in_([1, 50, 100])).all()
                    for card in sample_cards:
                        logger.info(f"Card {card.id}: {card.name} ({card.type}) - Rank {card.rank}")
                
                except Exception as e:
                    db.session.rollback()
                    logger.error(f"Error during database transaction: {str(e)}")
                    raise
            else:
                logger.info("Database already contains all cards with correct version. No seeding required.")
                
        except Exception as e:
            db.session.rollback()
            logger.error(f"Error seeding database: {str(e)}")
            raise

if __name__ == "__main__":
    seed_database(force=True)