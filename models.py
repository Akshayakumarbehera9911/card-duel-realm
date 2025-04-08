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
        {"name": "Mystic Mirage", "type": "Magician", "rank": "B", "hp": 160, "attack": 75, "defense": 70, "speed": 85, "intelligence": 95},
        {"name": "Terra Bloom", "type": "Cultivator", "rank": "B", "hp": 175, "attack": 85, "defense": 80, "speed": 70, "intelligence": 75},
        {"name": "Fauna Whisperer", "type": "Beast Tamer", "rank": "B", "hp": 180, "attack": 80, "defense": 80, "speed": 75, "intelligence": 80},
        {"name": "Mortis Veil", "type": "Necromancer", "rank": "C", "hp": 150, "attack": 90, "defense": 70, "speed": 65, "intelligence": 95},
        {"name": "Gear Tinker", "type": "Mechanic", "rank": "C", "hp": 145, "attack": 80, "defense": 85, "speed": 75, "intelligence": 90},
        {"name": "Blade Honor", "type": "Samurai", "rank": "A", "hp": 170, "attack": 95, "defense": 85, "speed": 90, "intelligence": 75},
        {"name": "Shadow Slip", "type": "Assassin", "rank": "B", "hp": 140, "attack": 90, "defense": 65, "speed": 100, "intelligence": 85},
        {"name": "Umbra Lancer", "type": "Shadow Caster", "rank": "A", "hp": 155, "attack": 95, "defense": 70, "speed": 95, "intelligence": 80},
        {"name": "Soul Wanderer", "type": "Spirit Walker", "rank": "C", "hp": 150, "attack": 75, "defense": 70, "speed": 90, "intelligence": 90},
        {"name": "Elixir Brewer", "type": "Alchemist", "rank": "B", "hp": 145, "attack": 85, "defense": 70, "speed": 80, "intelligence": 95},
        {"name": "Blade Master", "type": "Sword Saint", "rank": "A", "hp": 165, "attack": 100, "defense": 85, "speed": 90, "intelligence": 75},
        {"name": "Aether Guardian", "type": "Divine Monk", "rank": "S", "hp": 180, "attack": 90, "defense": 90, "speed": 80, "intelligence": 100},
        {"name": "Swift Cutter", "type": "Blade Dancer", "rank": "A", "hp": 160, "attack": 95, "defense": 75, "speed": 100, "intelligence": 70},
        {"name": "Hex Weaver", "type": "Curse Master", "rank": "B", "hp": 155, "attack": 90, "defense": 75, "speed": 75, "intelligence": 95},
        {"name": "Beast Caller", "type": "Summoner", "rank": "B", "hp": 150, "attack": 80, "defense": 70, "speed": 75, "intelligence": 95},
        {"name": "Spell Thief", "type": "Arcane Thief", "rank": "C", "hp": 145, "attack": 85, "defense": 70, "speed": 95, "intelligence": 85},
        {"name": "Crimson Healer", "type": "Blood Shaman", "rank": "B", "hp": 165, "attack": 85, "defense": 80, "speed": 75, "intelligence": 90},
        {"name": "Gale Force", "type": "Wind Striker", "rank": "A", "hp": 155, "attack": 90, "defense": 70, "speed": 100, "intelligence": 80},
        {"name": "Chrono Slice", "type": "Time Reaper", "rank": "A", "hp": 160, "attack": 95, "defense": 75, "speed": 95, "intelligence": 85},
        {"name": "Fiend Slayer", "type": "Demon Hunter", "rank": "A", "hp": 170, "attack": 100, "defense": 80, "speed": 90, "intelligence": 75},
        {"name": "Sigil Scribe", "type": "Rune Scribe", "rank": "B", "hp": 155, "attack": 80, "defense": 75, "speed": 85, "intelligence": 95},
        {"name": "Ice Archer", "type": "Frost Archer", "rank": "B", "hp": 150, "attack": 95, "defense": 70, "speed": 95, "intelligence": 80},
        {"name": "Flame Conjurer", "type": "Pyro Wielder", "rank": "B", "hp": 155, "attack": 100, "defense": 70, "speed": 85, "intelligence": 85},
        {"name": "Tempest Mage", "type": "Storm Caller", "rank": "C", "hp": 150, "attack": 90, "defense": 75, "speed": 85, "intelligence": 90},
        {"name": "Vision Prophet", "type": "Seer", "rank": "A", "hp": 160, "attack": 75, "defense": 80, "speed": 75, "intelligence": 100},
        {"name": "Void Disciple", "type": "Dark Acolyte", "rank": "B", "hp": 155, "attack": 90, "defense": 75, "speed": 85, "intelligence": 90},
        {"name": "Star Protector", "type": "Celestial Guard", "rank": "S", "hp": 185, "attack": 85, "defense": 95, "speed": 75, "intelligence": 95},
        {"name": "Spirit Crafter", "type": "Soul Forger", "rank": "B", "hp": 165, "attack": 85, "defense": 85, "speed": 75, "intelligence": 90},
        {"name": "Holy Combatant", "type": "Battle Priest", "rank": "A", "hp": 170, "attack": 90, "defense": 90, "speed": 80, "intelligence": 85},
        {"name": "Dark Defender", "type": "Void Knight", "rank": "B", "hp": 175, "attack": 95, "defense": 85, "speed": 80, "intelligence": 70},
        {"name": "Force Manipulator", "type": "Gravity Bender", "rank": "A", "hp": 155, "attack": 90, "defense": 80, "speed": 95, "intelligence": 90},
        {"name": "Mirage Weaver", "type": "Illusionist", "rank": "B", "hp": 145, "attack": 80, "defense": 75, "speed": 85, "intelligence": 100},
        {"name": "Wyrm Hunter", "type": "Dragon Slayer", "rank": "A", "hp": 180, "attack": 100, "defense": 85, "speed": 85, "intelligence": 75},
        {"name": "Wandering Sage", "type": "Mystic Nomad", "rank": "B", "hp": 160, "attack": 85, "defense": 80, "speed": 90, "intelligence": 85},
        {"name": "Wild Commander", "type": "Beastmaster", "rank": "B", "hp": 175, "attack": 90, "defense": 85, "speed": 80, "intelligence": 75},
        {"name": "Ghost Striker", "type": "Phantom Rogue", "rank": "B", "hp": 150, "attack": 95, "defense": 70, "speed": 100, "intelligence": 80},
        {"name": "Battle Commander", "type": "Warlord", "rank": "A", "hp": 185, "attack": 100, "defense": 90, "speed": 75, "intelligence": 70},
        {"name": "Celestial Blade", "type": "Heaven's Blade", "rank": "A", "hp": 165, "attack": 95, "defense": 85, "speed": 90, "intelligence": 80},
        {"name": "Ethereal Guide", "type": "Spirit Sage", "rank": "B", "hp": 160, "attack": 80, "defense": 75, "speed": 80, "intelligence": 95},
        {"name": "Storm Caster", "type": "Thunder Monk", "rank": "B", "hp": 155, "attack": 95, "defense": 75, "speed": 85, "intelligence": 90},
        {"name": "Shield Maiden", "type": "Valkyrie", "rank": "A", "hp": 175, "attack": 90, "defense": 90, "speed": 85, "intelligence": 85},
        {"name": "Glyph Master", "type": "Runic Monk", "rank": "B", "hp": 160, "attack": 80, "defense": 80, "speed": 75, "intelligence": 95},
        {"name": "Reaper's Grace", "type": "Death Dancer", "rank": "A", "hp": 165, "attack": 100, "defense": 75, "speed": 95, "intelligence": 80},
        {"name": "Abyss Wielder", "type": "Void Caster", "rank": "C", "hp": 145, "attack": 85, "defense": 70, "speed": 80, "intelligence": 100},
        {"name": "Phantasm Edge", "type": "Specter Blade", "rank": "B", "hp": 155, "attack": 95, "defense": 75, "speed": 90, "intelligence": 85},
        {"name": "Spirit Medium", "type": "Ghost Monk", "rank": "B", "hp": 160, "attack": 90, "defense": 75, "speed": 85, "intelligence": 90},
        {"name": "Inner Power", "type": "Chi Wielder", "rank": "B", "hp": 165, "attack": 95, "defense": 80, "speed": 90, "intelligence": 85},
        {"name": "Disorder Mage", "type": "Chaos Monk", "rank": "C", "hp": 150, "attack": 90, "defense": 75, "speed": 80, "intelligence": 95},
        {"name": "Steel Knuckle", "type": "Iron Fist", "rank": "B", "hp": 170, "attack": 100, "defense": 85, "speed": 85, "intelligence": 70},
        {"name": "Dusk Fighter", "type": "Night Brawler", "rank": "C", "hp": 155, "attack": 95, "defense": 75, "speed": 95, "intelligence": 75},
        {"name": "Curse Weaver", "type": "Hex Binder", "rank": "B", "hp": 150, "attack": 85, "defense": 75, "speed": 80, "intelligence": 100},
        {"name": "Force Shaper", "type": "Energy Sculptor", "rank": "A", "hp": 160, "attack": 95, "defense": 85, "speed": 85, "intelligence": 90},
        {"name": "Sand Warrior", "type": "Desert Striker", "rank": "B", "hp": 165, "attack": 90, "defense": 85, "speed": 85, "intelligence": 75},
        {"name": "Sacred Defender", "type": "Holy Knight", "rank": "A", "hp": 175, "attack": 90, "defense": 90, "speed": 80, "intelligence": 85},
        {"name": "String Master", "type": "Puppet Master", "rank": "B", "hp": 150, "attack": 80, "defense": 75, "speed": 85, "intelligence": 100},
        {"name": "Essence Drain", "type": "Mana Eater", "rank": "B", "hp": 155, "attack": 90, "defense": 75, "speed": 85, "intelligence": 95},
        {"name": "Stone Fist", "type": "Jade Monk", "rank": "B", "hp": 160, "attack": 85, "defense": 80, "speed": 90, "intelligence": 90},
        {"name": "Lunar Slicer", "type": "Moonblade", "rank": "A", "hp": 165, "attack": 95, "defense": 80, "speed": 90, "intelligence": 85},
        {"name": "Astral Summoner", "type": "Starcaller", "rank": "B", "hp": 155, "attack": 80, "defense": 75, "speed": 85, "intelligence": 100},
        {"name": "Skeletal Mage", "type": "Bone Binder", "rank": "B", "hp": 160, "attack": 85, "defense": 80, "speed": 75, "intelligence": 95},
        {"name": "Shadow Samurai", "type": "Dark Ronin", "rank": "A", "hp": 170, "attack": 95, "defense": 85, "speed": 90, "intelligence": 75},
        {"name": "Thought Stealer", "type": "Mind Flayer", "rank": "B", "hp": 145, "attack": 85, "defense": 70, "speed": 80, "intelligence": 105},
        {"name": "Night Strider", "type": "Shadow Dancer", "rank": "A", "hp": 160, "attack": 95, "defense": 75, "speed": 100, "intelligence": 75},
        {"name": "Bone Conjurer", "type": "Skull Mage", "rank": "C", "hp": 155, "attack": 90, "defense": 70, "speed": 80, "intelligence": 95},
        {"name": "Enchanted Blade", "type": "Runeblade", "rank": "B", "hp": 165, "attack": 95, "defense": 80, "speed": 85, "intelligence": 85},
        {"name": "Blood Cleric", "type": "Scarlet Priest", "rank": "B", "hp": 160, "attack": 85, "defense": 80, "speed": 80, "intelligence": 90},
        {"name": "Claw Master", "type": "Fang Tamer", "rank": "B", "hp": 165, "attack": 85, "defense": 75, "speed": 85, "intelligence": 90},
        {"name": "Deep Hunter", "type": "Abyss Stalker", "rank": "B", "hp": 170, "attack": 95, "defense": 85, "speed": 80, "intelligence": 80},
        {"name": "Soul Guide", "type": "Spiritual Boxer", "rank": "B", "hp": 160, "attack": 85, "defense": 80, "speed": 75, "intelligence": 95},
        {"name": "Granite Knuckle", "type": "Stone Fist", "rank": "B", "hp": 175, "attack": 95, "defense": 90, "speed": 70, "intelligence": 75},
        {"name": "Mystic Scribe", "type": "Ink Scribe", "rank": "C", "hp": 150, "attack": 80, "defense": 75, "speed": 85, "intelligence": 100},
        {"name": "Storm Lord", "type": "Thunder Lord", "rank": "A", "hp": 170, "attack": 100, "defense": 80, "speed": 85, "intelligence": 85},
        {"name": "Nightmare Walker", "type": "Dream Walker", "rank": "B", "hp": 155, "attack": 80, "defense": 75, "speed": 90, "intelligence": 95},
        {"name": "Spirit Bender", "type": "Soul Bender", "rank": "B", "hp": 160, "attack": 85, "defense": 80, "speed": 85, "intelligence": 90},
        {"name": "Flame Dancer", "type": "Fire Dervish", "rank": "B", "hp": 155, "attack": 100, "defense": 75, "speed": 90, "intelligence": 80},
        {"name": "Frost Artist", "type": "Ice Sculptor", "rank": "A", "hp": 165, "attack": 90, "defense": 85, "speed": 85, "intelligence": 90},
        {"name": "Time Weaver", "type": "Chrono Monk", "rank": "B", "hp": 150, "attack": 80, "defense": 75, "speed": 85, "intelligence": 100},
        {"name": "Feral Caller", "type": "Beast Summoner", "rank": "B", "hp": 170, "attack": 85, "defense": 80, "speed": 80, "intelligence": 90},
        {"name": "Arcane Hunter", "type": "Mystic Hunter", "rank": "A", "hp": 165, "attack": 95, "defense": 80, "speed": 95, "intelligence": 80},
        {"name": "Lance Master", "type": "Spear Saint", "rank": "A", "hp": 170, "attack": 95, "defense": 85, "speed": 90, "intelligence": 80},
        {"name": "Ghost Whisperer", "type": "Spirit Caller", "rank": "B", "hp": 155, "attack": 80, "defense": 75, "speed": 85, "intelligence": 95},
        {"name": "Phantom Master", "type": "Ghost Puppet", "rank": "B", "hp": 150, "attack": 90, "defense": 75, "speed": 85, "intelligence": 90},
        {"name": "Inferno Blade", "type": "Hellflame", "rank": "A", "hp": 165, "attack": 105, "defense": 80, "speed": 85, "intelligence": 80},
        {"name": "Ember Mage", "type": "Flame Monk", "rank": "B", "hp": 160, "attack": 95, "defense": 80, "speed": 85, "intelligence": 90},
        {"name": "Sigil Guardian", "type": "Rune Guardian", "rank": "B", "hp": 170, "attack": 85, "defense": 90, "speed": 75, "intelligence": 85},
        {"name": "Zephyr Stride", "type": "Wind Walker", "rank": "B", "hp": 155, "attack": 80, "defense": 75, "speed": 100, "intelligence": 85},
        {"name": "Blade Summoner", "type": "Sword Caller", "rank": "B", "hp": 165, "attack": 95, "defense": 85, "speed": 85, "intelligence": 80},
        {"name": "Reflection Mage", "type": "Mirror Mage", "rank": "B", "hp": 155, "attack": 85, "defense": 80, "speed": 85, "intelligence": 95},
        {"name": "Quiet Death", "type": "Silent Blade", "rank": "B", "hp": 150, "attack": 95, "defense": 70, "speed": 100, "intelligence": 80},
        {"name": "Mystic Knight", "type": "Arcane Knight", "rank": "A", "hp": 170, "attack": 90, "defense": 85, "speed": 85, "intelligence": 90},
        {"name": "Scarlet Fist", "type": "Crimson Fist", "rank": "B", "hp": 165, "attack": 100, "defense": 80, "speed": 90, "intelligence": 75},
        {"name": "Phantom Caster", "type": "Spectral Monk", "rank": "C", "hp": 155, "attack": 85, "defense": 75, "speed": 80, "intelligence": 95},
        {"name": "Wraith Summoner", "type": "Phantom Caller", "rank": "B", "hp": 150, "attack": 85, "defense": 75, "speed": 90, "intelligence": 90},
        {"name": "Dusk Sorcerer", "type": "Twilight Mage", "rank": "B", "hp": 155, "attack": 90, "defense": 75, "speed": 85, "intelligence": 95},
        {"name": "Divine Tamer", "type": "Heavenly Tamer", "rank": "A", "hp": 170, "attack": 90, "defense": 85, "speed": 85, "intelligence": 90},
        {"name": "Celestia Angelique", "type": "Sky Guardian", "rank": "B", "hp": 160, "attack": 80, "defense": 90, "speed": 85, "intelligence": 80},
        {"name": "Shadea Nightwalker", "type": "Shadowbrand", "rank": "C", "hp": 150, "attack": 85, "defense": 70, "speed": 95, "intelligence": 80},
        {"name": "Fortis Titanicus", "type": "Stone Protector", "rank": "S", "hp": 200, "attack": 80, "defense": 110, "speed": 60, "intelligence": 75},
        {"name": "Obscura Voidshade", "type": "Void Wanderer", "rank": "S", "hp": 180, "attack": 100, "defense": 90, "speed": 75, "intelligence": 95},
        {"name": "Zenith Stellaris", "type": "Star Forger", "rank": "A", "hp": 170, "attack": 90, "defense": 80, "speed": 80, "intelligence": 95}
    ]