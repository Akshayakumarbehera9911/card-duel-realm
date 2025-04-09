from app import db
from datetime import datetime

class Card(db.Model):
    __tablename__ = 'cards'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    rank = db.Column(db.String(1), nullable=False, key='`rank`') # SQLAlchemy will handle the backticks for MySQL
    hp = db.Column(db.Integer, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    intelligence = db.Column(db.Integer, nullable=False)
    
    @classmethod
    def get_all_cards(cls):
        """Load all cards from the database"""
        # Explicitly get all cards with a limit higher than expected
        return cls.query.limit(150).all()  # Increased limit to ensure all cards are retrieved
    
    def to_dict(self):
        """Convert card to dictionary for JSON serialization"""
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'rank': self.rank,
            'hp': self.hp,
            'attack': self.attack,
            'defense': self.defense,
            'speed': self.speed,
            'intelligence': self.intelligence
        }

class GameHistory(db.Model):
    __tablename__ = 'game_history'
    
    id = db.Column(db.Integer, primary_key=True)
    player1_name = db.Column(db.String(100), nullable=False, default='Player 1')
    player2_name = db.Column(db.String(100), nullable=False, default='Player 2')
    player1_score = db.Column(db.Integer, nullable=False)
    player2_score = db.Column(db.Integer, nullable=False)
    winner = db.Column(db.String(100), nullable=True)
    rounds_played = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        """Convert game history to dictionary for JSON serialization"""
        return {
            'id': self.id,
            'player1_name': self.player1_name,
            'player2_name': self.player2_name,
            'player1_score': self.player1_score,
            'player2_score': self.player2_score,
            'winner': self.winner,
            'rounds_played': self.rounds_played,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

# Card data for initialization
# Card data for initialization
def get_card_data():
    """Get initial card data for database seeding"""
    return [
        {"name": "Mystic Mirage", "type": "Magician", "rank": "B", "hp": 160, "attack": 12, "defense": 230, "speed": 85, "intelligence": 347},
        {"name": "Terra Bloom", "type": "Cultivator", "rank": "B", "hp": 175, "attack": 300, "defense": 25, "speed": 3, "intelligence": 179},
        {"name": "Fauna Whisperer", "type": "Beast Tamer", "rank": "B", "hp": 180, "attack": 42, "defense": 210, "speed": 75, "intelligence": 8},
        {"name": "Mortis Veil", "type": "Necromancer", "rank": "C", "hp": 5, "attack": 280, "defense": 70, "speed": 65, "intelligence": 192},
        {"name": "Gear Tinker", "type": "Mechanic", "rank": "C", "hp": 145, "attack": 2, "defense": 320, "speed": 175, "intelligence": 90},
        {"name": "Blade Honor", "type": "Samurai", "rank": "A", "hp": 170, "attack": 190, "defense": 85, "speed": 90, "intelligence": 55},
        {"name": "Shadow Slip", "type": "Assassin", "rank": "B", "hp": 140, "attack": 90, "defense": 65, "speed": 350, "intelligence": 25},
        {"name": "Umbra Lancer", "type": "Shadow Caster", "rank": "A", "hp": 155, "attack": 295, "defense": 1, "speed": 195, "intelligence": 80},
        {"name": "Soul Wanderer", "type": "Spirit Walker", "rank": "C", "hp": 150, "attack": 75, "defense": 70, "speed": 290, "intelligence": 137},
        {"name": "Elixir Brewer", "type": "Alchemist", "rank": "B", "hp": 145, "attack": 185, "defense": 7, "speed": 180, "intelligence": 295},
        {"name": "Blade Master", "type": "Sword Saint", "rank": "A", "hp": 165, "attack": 400, "defense": 85, "speed": 90, "intelligence": 15},
        {"name": "Aether Guardian", "type": "Divine Sage", "rank": "S", "hp": 380, "attack": 190, "defense": 290, "speed": 2, "intelligence": 310},
        {"name": "Swift Cutter", "type": "Blade Dancer", "rank": "A", "hp": 160, "attack": 195, "defense": 5, "speed": 340, "intelligence": 70},
        {"name": "Hex Weaver", "type": "Curse Master", "rank": "B", "hp": 55, "attack": 290, "defense": 35, "speed": 75, "intelligence": 295},
        {"name": "Beast Caller", "type": "Summoner", "rank": "B", "hp": 150, "attack": 10, "defense": 170, "speed": 75, "intelligence": 395},
        {"name": "Spell Thief", "type": "Arcane Thief", "rank": "C", "hp": 145, "attack": 285, "defense": 1, "speed": 195, "intelligence": 85},
        {"name": "Crimson Healer", "type": "Blood Shaman", "rank": "B", "hp": 365, "attack": 15, "defense": 280, "speed": 75, "intelligence": 190},
        {"name": "Gale Force", "type": "Wind Striker", "rank": "A", "hp": 155, "attack": 90, "defense": 7, "speed": 300, "intelligence": 180},
        {"name": "Chrono Slice", "type": "Time Reaper", "rank": "A", "hp": 60, "attack": 295, "defense": 175, "speed": 195, "intelligence": 185},
        {"name": "Fiend Slayer", "type": "Demon Hunter", "rank": "A", "hp": 270, "attack": 300, "defense": 180, "speed": 9, "intelligence": 175},
        {"name": "Sigil Scribe", "type": "Rune Scribe", "rank": "B", "hp": 155, "attack": 8, "defense": 175, "speed": 285, "intelligence": 195},
        {"name": "Ice Archer", "type": "Frost Archer", "rank": "B", "hp": 50, "attack": 295, "defense": 7, "speed": 195, "intelligence": 180},
        {"name": "Flame Conjurer", "type": "Pyro Wielder", "rank": "B", "hp": 155, "attack": 400, "defense": 2, "speed": 85, "intelligence": 185},
        {"name": "Tempest Mage", "type": "Storm Caller", "rank": "C", "hp": 150, "attack": 290, "defense": 5, "speed": 185, "intelligence": 290},
        {"name": "Vision Prophet", "type": "Seer", "rank": "A", "hp": 60, "attack": 7, "defense": 180, "speed": 75, "intelligence": 400},
        {"name": "Void Disciple", "type": "Dark Acolyte", "rank": "B", "hp": 155, "attack": 290, "defense": 5, "speed": 85, "intelligence": 190},
        {"name": "Star Protector", "type": "Celestial Guard", "rank": "S", "hp": 385, "attack": 185, "defense": 295, "speed": 3, "intelligence": 295},
        {"name": "Spirit Crafter", "type": "Soul Forger", "rank": "B", "hp": 165, "attack": 15, "defense": 385, "speed": 5, "intelligence": 190},
        {"name": "Holy Combatant", "type": "Battle Cleric", "rank": "A", "hp": 370, "attack": 190, "defense": 290, "speed": 2, "intelligence": 185},
        {"name": "Dark Defender", "type": "Void Knight", "rank": "B", "hp": 375, "attack": 195, "defense": 285, "speed": 1, "intelligence": 7},
        {"name": "Force Manipulator", "type": "Gravity Bender", "rank": "A", "hp": 55, "attack": 290, "defense": 280, "speed": 195, "intelligence": 190},
        {"name": "Mirage Weaver", "type": "Illusionist", "rank": "B", "hp": 5, "attack": 80, "defense": 7, "speed": 285, "intelligence": 400},
        {"name": "Wyrm Hunter", "type": "Dragon Slayer", "rank": "A", "hp": 380, "attack": 300, "defense": 3, "speed": 285, "intelligence": 7},
        {"name": "Wandering Sage", "type": "Mystic Nomad", "rank": "B", "hp": 60, "attack": 285, "defense": 8, "speed": 290, "intelligence": 385},
        {"name": "Wild Commander", "type": "Beastmaster", "rank": "B", "hp": 375, "attack": 190, "defense": 285, "speed": 3, "intelligence": 7},
        {"name": "Ghost Striker", "type": "Phantom Rogue", "rank": "B", "hp": 5, "attack": 295, "defense": 7, "speed": 400, "intelligence": 8},
        {"name": "Battle Commander", "type": "Warlord", "rank": "A", "hp": 385, "attack": 300, "defense": 290, "speed": 3, "intelligence": 7},
        {"name": "Celestial Blade", "type": "Heaven's Blade", "rank": "A", "hp": 65, "attack": 395, "defense": 8, "speed": 290, "intelligence": 8},
        {"name": "Ethereal Guide", "type": "Spirit Sage", "rank": "B", "hp": 60, "attack": 8, "defense": 7, "speed": 280, "intelligence": 395},
        {"name": "Storm Caster", "type": "Thunder Mystic", "rank": "B", "hp": 55, "attack": 395, "defense": 7, "speed": 285, "intelligence": 190},
        {"name": "Shield Maiden", "type": "Valkyrie", "rank": "A", "hp": 375, "attack": 190, "defense": 390, "speed": 8, "intelligence": 85},
        {"name": "Glyph Master", "type": "Runic Mystic", "rank": "B", "hp": 60, "attack": 8, "defense": 280, "speed": 7, "intelligence": 395},
        {"name": "Reaper's Grace", "type": "Death Dancer", "rank": "A", "hp": 65, "attack": 400, "defense": 7, "speed": 395, "intelligence": 8},
        {"name": "Abyss Wielder", "type": "Void Caster", "rank": "C", "hp": 5, "attack": 85, "defense": 7, "speed": 8, "intelligence": 400},
        {"name": "Phantasm Edge", "type": "Specter Blade", "rank": "B", "hp": 5, "attack": 395, "defense": 7, "speed": 290, "intelligence": 8},
        {"name": "Spirit Medium", "type": "Ghost Seer", "rank": "B", "hp": 60, "attack": 90, "defense": 7, "speed": 285, "intelligence": 390},
        {"name": "Inner Power", "type": "Chi Adept", "rank": "B", "hp": 365, "attack": 195, "defense": 280, "speed": 2, "intelligence": 285},
        {"name": "Disorder Mage", "type": "Chaos Sorcerer", "rank": "C", "hp": 50, "attack": 190, "defense": 7, "speed": 8, "intelligence": 395},
        {"name": "Steel Knuckle", "type": "Iron Fist", "rank": "B", "hp": 370, "attack": 400, "defense": 285, "speed": 8, "intelligence": 7},
        {"name": "Dusk Fighter", "type": "Night Brawler", "rank": "C", "hp": 5, "attack": 395, "defense": 7, "speed": 395, "intelligence": 7},
        {"name": "Curse Weaver", "type": "Hex Binder", "rank": "B", "hp": 5, "attack": 85, "defense": 7, "speed": 8, "intelligence": 400},
        {"name": "Force Shaper", "type": "Energy Sculptor", "rank": "A", "hp": 60, "attack": 295, "defense": 8, "speed": 285, "intelligence": 390},
        {"name": "Sand Warrior", "type": "Desert Striker", "rank": "B", "hp": 365, "attack": 190, "defense": 385, "speed": 2, "intelligence": 7},
        {"name": "Sacred Defender", "type": "Holy Knight", "rank": "A", "hp": 375, "attack": 90, "defense": 390, "speed": 2, "intelligence": 85},
        {"name": "String Master", "type": "Puppet Master", "rank": "B", "hp": 50, "attack": 8, "defense": 7, "speed": 85, "intelligence": 400},
        {"name": "Essence Drain", "type": "Mana Eater", "rank": "B", "hp": 5, "attack": 290, "defense": 7, "speed": 85, "intelligence": 395},
        {"name": "Stone Fist", "type": "Jade Warrior", "rank": "B", "hp": 360, "attack": 185, "defense": 380, "speed": 1, "intelligence": 90},
        {"name": "Lunar Slicer", "type": "Moonblade", "rank": "A", "hp": 65, "attack": 395, "defense": 8, "speed": 290, "intelligence": 85},
        {"name": "Astral Summoner", "type": "Starcaller", "rank": "B", "hp": 5, "attack": 8, "defense": 7, "speed": 85, "intelligence": 400},
        {"name": "Skeletal Mage", "type": "Bone Binder", "rank": "B", "hp": 60, "attack": 8, "defense": 280, "speed": 7, "intelligence": 395},
        {"name": "Shadow Samurai", "type": "Dark Ronin", "rank": "A", "hp": 370, "attack": 395, "defense": 8, "speed": 290, "intelligence": 7},
        {"name": "Thought Stealer", "type": "Mind Flayer", "rank": "B", "hp": 5, "attack": 8, "defense": 7, "speed": 8, "intelligence": 405},
        {"name": "Night Strider", "type": "Shadow Dancer", "rank": "A", "hp": 60, "attack": 295, "defense": 7, "speed": 400, "intelligence": 7},
        {"name": "Bone Conjurer", "type": "Skull Mage", "rank": "C", "hp": 5, "attack": 290, "defense": 7, "speed": 8, "intelligence": 395},
        {"name": "Enchanted Blade", "type": "Runeblade", "rank": "B", "hp": 65, "attack": 395, "defense": 8, "speed": 85, "intelligence": 85},
        {"name": "Blood Cleric", "type": "Scarlet Priest", "rank": "B", "hp": 360, "attack": 8, "defense": 380, "speed": 2, "intelligence": 390},
        {"name": "Claw Master", "type": "Fang Tamer", "rank": "B", "hp": 65, "attack": 85, "defense": 7, "speed": 385, "intelligence": 90},
        {"name": "Deep Hunter", "type": "Abyss Stalker", "rank": "B", "hp": 370, "attack": 295, "defense": 8, "speed": 280, "intelligence": 8},
        {"name": "Soul Guide", "type": "Spiritual Adept", "rank": "B", "hp": 60, "attack": 8, "defense": 280, "speed": 7, "intelligence": 395},
        {"name": "Granite Knuckle", "type": "Stone Fist", "rank": "B", "hp": 375, "attack": 395, "defense": 290, "speed": 1, "intelligence": 7},
        {"name": "Mystic Scribe", "type": "Ink Scribe", "rank": "C", "hp": 50, "attack": 8, "defense": 7, "speed": 85, "intelligence": 400},
        {"name": "Storm Lord", "type": "Thunder Lord", "rank": "A", "hp": 70, "attack": 400, "defense": 8, "speed": 85, "intelligence": 85},
        {"name": "Nightmare Walker", "type": "Dream Walker", "rank": "B", "hp": 5, "attack": 8, "defense": 7, "speed": 290, "intelligence": 395},
        {"name": "Spirit Bender", "type": "Soul Bender", "rank": "B", "hp": 60, "attack": 8, "defense": 280, "speed": 8, "intelligence": 390},
        {"name": "Flame Dancer", "type": "Fire Dervish", "rank": "B", "hp": 5, "attack": 400, "defense": 7, "speed": 290, "intelligence": 8},
        {"name": "Frost Artist", "type": "Ice Sculptor", "rank": "A", "hp": 65, "attack": 290, "defense": 85, "speed": 8, "intelligence": 390},
        {"name": "Time Weaver", "type": "Chrono Mystic", "rank": "B", "hp": 50, "attack": 8, "defense": 7, "speed": 85, "intelligence": 400},
        {"name": "Feral Caller", "type": "Beast Summoner", "rank": "B", "hp": 370, "attack": 8, "defense": 380, "speed": 2, "intelligence": 390},
        {"name": "Arcane Hunter", "type": "Mystic Hunter", "rank": "A", "hp": 65, "attack": 395, "defense": 8, "speed": 395, "intelligence": 8},
        {"name": "Lance Master", "type": "Spear Saint", "rank": "A", "hp": 370, "attack": 395, "defense": 8, "speed": 290, "intelligence": 8},
        {"name": "Ghost Whisperer", "type": "Spirit Caller", "rank": "B", "hp": 5, "attack": 8, "defense": 7, "speed": 85, "intelligence": 395},
        {"name": "Phantom Master", "type": "Ghost Puppet", "rank": "B", "hp": 50, "attack": 290, "defense": 7, "speed": 85, "intelligence": 390},
        {"name": "Inferno Blade", "type": "Hellflame", "rank": "A", "hp": 65, "attack": 405, "defense": 8, "speed": 85, "intelligence": 8},
        {"name": "Ember Mage", "type": "Flame Mystic", "rank": "B", "hp": 60, "attack": 395, "defense": 8, "speed": 85, "intelligence": 390},
        {"name": "Sigil Guardian", "type": "Rune Guardian", "rank": "B", "hp": 370, "attack": 8, "defense": 390, "speed": 2, "intelligence": 85},
        {"name": "Zephyr Stride", "type": "Wind Walker", "rank": "B", "hp": 5, "attack": 8, "defense": 7, "speed": 400, "intelligence": 85},
        {"name": "Blade Summoner", "type": "Sword Caller", "rank": "B", "hp": 65, "attack": 395, "defense": 8, "speed": 85, "intelligence": 8},
        {"name": "Reflection Mage", "type": "Mirror Mage", "rank": "B", "hp": 5, "attack": 285, "defense": 2, "speed": 385, "intelligence": 395},
        {"name": "Quiet Death", "type": "Silent Blade", "rank": "B", "hp": 50, "attack": 395, "defense": 7, "speed": 400, "intelligence": 6},
        {"name": "Mystic Knight", "type": "Arcane Knight", "rank": "A", "hp": 270, "attack": 390, "defense": 285, "speed": 85, "intelligence": 9},
        {"name": "Scarlet Fist", "type": "Crimson Fist", "rank": "B", "hp": 265, "attack": 400, "defense": 280, "speed": 9, "intelligence": 7},
        {"name": "Phantom Caster", "type": "Spectral Mage", "rank": "C", "hp": 5, "attack": 85, "defense": 5, "speed": 380, "intelligence": 395},
        {"name": "Wraith Summoner", "type": "Phantom Caller", "rank": "B", "hp": 50, "attack": 85, "defense": 7, "speed": 390, "intelligence": 390},
        {"name": "Dusk Sorcerer", "type": "Twilight Mage", "rank": "B", "hp": 55, "attack": 90, "defense": 7, "speed": 285, "intelligence": 395},
        {"name": "Divine Tamer", "type": "Heavenly Tamer", "rank": "A", "hp": 270, "attack": 90, "defense": 385, "speed": 8, "intelligence": 390},
        {"name": "Celestia Angelique", "type": "Sky Guardian", "rank": "B", "hp": 260, "attack": 8, "defense": 390, "speed": 385, "intelligence": 8},
        {"name": "Shadea Nightwalker", "type": "Shadowbrand", "rank": "C", "hp": 50, "attack": 385, "defense": 7, "speed": 395, "intelligence": 8},
        {"name": "Fortis Titanicus", "type": "Stone Protector", "rank": "S", "hp": 400, "attack": 8, "defense": 410, "speed": 1, "intelligence": 75},
        {"name": "Obscura Voidshade", "type": "Void Wanderer", "rank": "S", "hp": 180, "attack": 400, "defense": 9, "speed": 375, "intelligence": 395},
        {"name": "Zenith Stellaris", "type": "Star Forger", "rank": "A", "hp": 170, "attack": 390, "defense": 8, "speed": 280, "intelligence": 395}
    ]