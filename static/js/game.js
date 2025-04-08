document.addEventListener('DOMContentLoaded', () => {
    // Game state
    const gameState = {
        player1: {
            name: '',
            score: 0,
            currentCard: null
        },
        player2: {
            name: '',
            score: 0,
            currentCard: null
        },
        currentRound: 0,
        totalRounds: 50,
        currentPlayer: 'player1',
        gameStarted: false,
        attributeSelected: false,
        cardsFlipped: false,
        selectedAttribute: '',
        gameOver: false
    };

    // Cache DOM elements
    const elements = {
        nextRoundBtn: document.getElementById('nextRoundBtn'),
        player1Card: document.getElementById('player1Card'),
        player2Card: document.getElementById('player2Card'),
        player1Score: document.getElementById('player1Score'),
        player2Score: document.getElementById('player2Score'),
        gameStatus: document.getElementById('gameStatus'),
        roundCounter: document.getElementById('roundCounter'),
        player1NameDisplay: document.getElementById('player1NameDisplay'),
        player2NameDisplay: document.getElementById('player2NameDisplay')
    };

    // Initialize event listeners
    function initEventListeners() {
        if (elements.nextRoundBtn) {
            elements.nextRoundBtn.addEventListener('click', nextRound);
        }
    }

    // Helper function to get a placeholder image based on card type
    function getCardImageUrl(card) {
        // Use the card ID directly to get the image
        return `/static/images/placeholder_${card.id}.jpg`;
    }

    // Draw cards for both players
    function drawCards() {
        // Make AJAX request to get cards
        fetch('/draw_cards', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        })
        .then(response => response.json())
        .then(data => {
            gameState.player1.currentCard = data.player1_card;
            gameState.player2.currentCard = data.player2_card;
            
            // Show cards (back side first)
            renderCard('player1', gameState.player1.currentCard, false);
            renderCard('player2', gameState.player2.currentCard, false);
            
            // Wait a moment then flip the cards
            setTimeout(() => {
                flipCards();
                
                updateGameStatus(`Cards drawn! ${gameState[gameState.currentPlayer].name}, please choose an attribute to compare.`);
                
                // Enable attribute selection for current player
                enableAttributeSelection();
            }, 800);
        })
        .catch(error => {
            console.error('Error:', error);
            updateGameStatus('Error drawing cards. Please try again.');
        });
    }

    // Render a card (front or back)
    function renderCard(player, cardData, showFront) {
        const cardElement = player === 'player1' ? elements.player1Card : elements.player2Card;
        
        if (!cardElement) return;

        // Get the appropriate image based on card type
        const cardImageUrl = cardData ? getCardImageUrl(cardData) : '/static/images/card_back.svg';
        
        if (showFront && cardData) {
            // Front side of card with character data
            cardElement.innerHTML = `
                <div class="card ${showFront ? 'flipped' : ''}">
                    <div class="card-back">
                        <img src="/static/images/card_back.svg" alt="Card back" width="100%" height="100%">
                    </div>
                    <div class="card-front">
                        <div class="card-header">
                            <div class="card-name">${cardData.name}</div>
                            <span class="card-type">${cardData.type}</span>
                        </div>
                        <div class="card-image">
                            <img src="${cardImageUrl}" alt="${cardData.name}">
                        </div>
                        <div class="card-attributes">
                            <div class="attribute" data-attribute="hp" ${player === gameState.currentPlayer ? 'onclick="selectAttribute(\'hp\')"' : ''}>
                                <span>HP</span>
                                <span>${gameState.attributeSelected && gameState.selectedAttribute === 'hp' ? cardData.hp : '?'}</span>
                            </div>
                            <div class="attribute" data-attribute="attack" ${player === gameState.currentPlayer ? 'onclick="selectAttribute(\'attack\')"' : ''}>
                                <span>Attack</span>
                                <span>${gameState.attributeSelected && gameState.selectedAttribute === 'attack' ? cardData.attack : '?'}</span>
                            </div>
                            <div class="attribute" data-attribute="defense" ${player === gameState.currentPlayer ? 'onclick="selectAttribute(\'defense\')"' : ''}>
                                <span>Defense</span>
                                <span>${gameState.attributeSelected && gameState.selectedAttribute === 'defense' ? cardData.defense : '?'}</span>
                            </div>
                            <div class="attribute" data-attribute="speed" ${player === gameState.currentPlayer ? 'onclick="selectAttribute(\'speed\')"' : ''}>
                                <span>Speed</span>
                                <span>${gameState.attributeSelected && gameState.selectedAttribute === 'speed' ? cardData.speed : '?'}</span>
                            </div>
                            <div class="attribute" data-attribute="intelligence" ${player === gameState.currentPlayer ? 'onclick="selectAttribute(\'intelligence\')"' : ''}>
                                <span>Intelligence</span>
                                <span>${gameState.attributeSelected && gameState.selectedAttribute === 'intelligence' ? cardData.intelligence : '?'}</span>
                            </div>
                        </div>
                        <div class="card-footer">
                            <span class="card-rank">Rank ${cardData.rank}</span>
                        </div>
                    </div>
                </div>
            `;

            // Add event listeners for attribute selection
            if (player === gameState.currentPlayer) {
                cardElement.querySelectorAll('.attribute').forEach(attr => {
                    attr.addEventListener('click', () => {
                        if (!gameState.attributeSelected) {
                            selectAttribute(attr.dataset.attribute);
                        }
                    });
                });
            }
        } else {
            // Back side of card
            cardElement.innerHTML = `
                <div class="card">
                    <div class="card-back">
                        <img src="/static/images/card_back.svg" alt="Card back" width="100%" height="100%">
                    </div>
                    <div class="card-front">
                        <!-- Card front content would go here -->
                    </div>
                </div>
            `;
        }
    }

    // Flip the cards to reveal
    function flipCards() {
        const player1CardElement = elements.player1Card.querySelector('.card');
        const player2CardElement = elements.player2Card.querySelector('.card');
        
        if (player1CardElement && player2CardElement) {
            player1CardElement.classList.add('flipped');
            player2CardElement.classList.add('flipped');
            gameState.cardsFlipped = true;
        }
        
        // Render card fronts
        renderCard('player1', gameState.player1.currentCard, true);
        renderCard('player2', gameState.player2.currentCard, true);
    }

    // Enable attribute selection for current player
    function enableAttributeSelection() {
        // Update status to indicate which player selects attribute
        updateGameStatus(`${gameState[gameState.currentPlayer].name}, select an attribute on your card to compare.`);
    }

    // Select an attribute for comparison
    function selectAttribute(attribute) {
        if (gameState.attributeSelected) return;
        
        gameState.selectedAttribute = attribute;
        gameState.attributeSelected = true;
        
        // Highlight the selected attribute
        document.querySelectorAll(`.attribute[data-attribute="${attribute}"]`).forEach(attr => {
            attr.classList.add('selected');
        });
        
        updateGameStatus(`${gameState[gameState.currentPlayer].name} selected ${attribute}! Comparing...`);
        
        // Automatically compare after a short delay
        setTimeout(() => {
            compareCards();
        }, 800);
    }

    // Make the selectAttribute function available globally
    window.selectAttribute = selectAttribute;

    // Compare cards based on selected attribute
    function compareCards() {
        if (!gameState.selectedAttribute) return;
        
        // Reveal selected attribute values on both cards
        renderCard('player1', gameState.player1.currentCard, true);
        renderCard('player2', gameState.player2.currentCard, true);
        
        // Compare the selected attribute
        const player1Val = parseInt(gameState.player1.currentCard[gameState.selectedAttribute]);
        const player2Val = parseInt(gameState.player2.currentCard[gameState.selectedAttribute]);
        
        let winner;
        
        if (player1Val > player2Val) {
            winner = 'player1';
        } else if (player2Val > player1Val) {
            winner = 'player2';
        } else {
            // It's a tie
            updateGameStatus("It's a tie! No points awarded.");
            elements.nextRoundBtn.disabled = false;
            return;
        }
        
        // Update score
        gameState[winner].score += 1;
        updateScores();
        
        // Set the winner as the current player for next round
        gameState.currentPlayer = winner;
        
        updateGameStatus(`${gameState[winner].name} wins this round with a higher ${gameState.selectedAttribute}!`);
        
        // Enable next round button
        elements.nextRoundBtn.disabled = false;
    }

    // Move to the next round
    function nextRound() {
        // Reset round state
        gameState.attributeSelected = false;
        gameState.cardsFlipped = false;
        gameState.selectedAttribute = '';
        
        // Reset card highlights
        document.querySelectorAll(`.attribute.selected`).forEach(attr => {
            attr.classList.remove('selected');
        });
        
        // Increment round counter
        gameState.currentRound++;
        updateRoundCounter();
        
        elements.nextRoundBtn.disabled = true;
        
        // Check if game over
        if (gameState.currentRound > gameState.totalRounds) {
            endGame();
            return;
        }
        
        // Automatically draw cards for next round
        drawCards();
    }

    // End the game
    function endGame() {
        gameState.gameOver = true;
        
        // Determine the winner
        let winnerName;
        if (gameState.player1.score > gameState.player2.score) {
            winnerName = gameState.player1.name;
        } else if (gameState.player2.score > gameState.player1.score) {
            winnerName = gameState.player2.name;
        } else {
            winnerName = "It's a tie";
        }
        
        updateGameStatus(`Game Over! ${winnerName} wins with a score of ${Math.max(gameState.player1.score, gameState.player2.score)}!`);
        
        // Redirect to results page
        setTimeout(() => {
            window.location.href = `/results?p1=${encodeURIComponent(gameState.player1.name)}&p1s=${gameState.player1.score}&p2=${encodeURIComponent(gameState.player2.name)}&p2s=${gameState.player2.score}`;
        }, 3000);
    }

    // Update the scores display
    function updateScores() {
        if (elements.player1Score) {
            elements.player1Score.textContent = gameState.player1.score;
        }
        if (elements.player2Score) {
            elements.player2Score.textContent = gameState.player2.score;
        }
    }

    // Update the round counter display
    function updateRoundCounter() {
        if (elements.roundCounter) {
            elements.roundCounter.textContent = `Round ${gameState.currentRound}`;
        }
    }

    // Update game status message
    function updateGameStatus(message) {
        if (elements.gameStatus) {
            elements.gameStatus.textContent = message;
        }
    }

    // Initialize the game
    function initGame() {
        // Get player names from page
        if (elements.player1NameDisplay) {
            gameState.player1.name = elements.player1NameDisplay.textContent || 'Player 1';
        }
        if (elements.player2NameDisplay) {
            gameState.player2.name = elements.player2NameDisplay.textContent || 'Player 2';
        }

        // Initialize event listeners
        initEventListeners();
        
        // Set initial round
        gameState.currentRound = 1;
        updateRoundCounter();
        
        // Start by drawing cards
        drawCards();
    }

    // Start the game
    initGame();
});