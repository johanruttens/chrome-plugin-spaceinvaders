// Space Invaders Game
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

// Set canvas dimensions
canvas.width = 480;
canvas.height = 640;

// Game states
const GAME_STATE = {
  START: 'start',
  PLAYING: 'playing',
  GAME_OVER: 'gameOver'
};

// Difficulty levels
const DIFFICULTY = {
  EASY: 'easy',
  MEDIUM: 'medium',
  HARD: 'hard'
};

// Difficulty settings
const DIFFICULTY_SETTINGS = {
  easy: {
    alienSpeed: 0.5,
    alienShootChance: 0.0003,
    alienBulletSpeed: 2,
    alienDropDistance: 15,
    maxPlayerBullets: 5,
    lives: 5
  },
  medium: {
    alienSpeed: 1,
    alienShootChance: 0.0005,
    alienBulletSpeed: 3,
    alienDropDistance: 20,
    maxPlayerBullets: 3,
    lives: 3
  },
  hard: {
    alienSpeed: 1.5,
    alienShootChance: 0.0008,
    alienBulletSpeed: 4,
    alienDropDistance: 25,
    maxPlayerBullets: 2,
    lives: 2
  }
};

// Game variables
let gameState = GAME_STATE.START;
let selectedDifficulty = DIFFICULTY.MEDIUM;
let currentDifficultySettings = DIFFICULTY_SETTINGS.medium;
let score = 0;
let lives = 3;
let animationId;

// Player
const player = {
  x: canvas.width / 2 - 20,
  y: canvas.height - 60,
  width: 40,
  height: 30,
  speed: 5,
  moveLeft: false,
  moveRight: false
};

// Bullets
let playerBullets = [];
const BULLET_SPEED = 7;
const BULLET_WIDTH = 3;
const BULLET_HEIGHT = 15;

// Aliens
let aliens = [];
const ALIEN_ROWS = 5;
const ALIEN_COLS = 11;
const ALIEN_WIDTH = 30;
const ALIEN_HEIGHT = 20;
const ALIEN_PADDING = 10;
const ALIEN_OFFSET_TOP = 80;
const ALIEN_OFFSET_LEFT = 30;
let alienDirection = 1;
let alienSpeed = 1;
let alienDropDistance = 20;

// Alien bullets
let alienBullets = [];
let alienBulletSpeed = 3;
let alienShootChance = 0.0005;

// Shields
let shields = [];
const SHIELD_WIDTH = 60;
const SHIELD_HEIGHT = 40;
const SHIELD_Y = canvas.height - 150;

// Keyboard controls
const keys = {};

// Initialize game
function init() {
  createAliens();
  createShields();
  gameState = GAME_STATE.START;
  drawStartScreen();
}

// Create alien grid
function createAliens() {
  aliens = [];
  for (let row = 0; row < ALIEN_ROWS; row++) {
    for (let col = 0; col < ALIEN_COLS; col++) {
      aliens.push({
        x: ALIEN_OFFSET_LEFT + col * (ALIEN_WIDTH + ALIEN_PADDING),
        y: ALIEN_OFFSET_TOP + row * (ALIEN_HEIGHT + ALIEN_PADDING),
        width: ALIEN_WIDTH,
        height: ALIEN_HEIGHT,
        alive: true,
        type: row < 2 ? 3 : row < 4 ? 2 : 1
      });
    }
  }
}

// Create shields
function createShields() {
  shields = [];
  const shieldCount = 4;
  const spacing = (canvas.width - (shieldCount * SHIELD_WIDTH)) / (shieldCount + 1);

  for (let i = 0; i < shieldCount; i++) {
    const shield = {
      x: spacing + i * (SHIELD_WIDTH + spacing),
      y: SHIELD_Y,
      width: SHIELD_WIDTH,
      height: SHIELD_HEIGHT,
      blocks: []
    };

    // Create shield blocks (simplified grid)
    const blockSize = 5;
    for (let by = 0; by < SHIELD_HEIGHT; by += blockSize) {
      for (let bx = 0; bx < SHIELD_WIDTH; bx += blockSize) {
        // Create shield shape (arch-like)
        const relX = bx / SHIELD_WIDTH;
        const relY = by / SHIELD_HEIGHT;
        const isShieldShape = relY < 0.7 || (relX > 0.3 && relX < 0.7);

        if (isShieldShape) {
          shield.blocks.push({
            x: shield.x + bx,
            y: shield.y + by,
            width: blockSize,
            height: blockSize,
            alive: true
          });
        }
      }
    }
    shields.push(shield);
  }
}

// Draw player ship
function drawPlayer() {
  ctx.fillStyle = '#00FF00';
  ctx.fillRect(player.x, player.y, player.width, player.height);

  // Draw ship details
  ctx.fillStyle = '#00FF00';
  ctx.beginPath();
  ctx.moveTo(player.x + player.width / 2, player.y - 5);
  ctx.lineTo(player.x, player.y);
  ctx.lineTo(player.x + player.width, player.y);
  ctx.closePath();
  ctx.fill();
}

// Draw aliens
function drawAliens() {
  aliens.forEach(alien => {
    if (alien.alive) {
      // Different colors for different alien types
      if (alien.type === 3) {
        ctx.fillStyle = '#FF0000';
      } else if (alien.type === 2) {
        ctx.fillStyle = '#FF00FF';
      } else {
        ctx.fillStyle = '#FFFF00';
      }

      ctx.fillRect(alien.x, alien.y, alien.width, alien.height);

      // Draw alien eyes
      ctx.fillStyle = '#000000';
      ctx.fillRect(alien.x + 8, alien.y + 5, 4, 4);
      ctx.fillRect(alien.x + 18, alien.y + 5, 4, 4);
    }
  });
}

// Draw bullets
function drawBullets() {
  ctx.fillStyle = '#FFFFFF';
  playerBullets.forEach(bullet => {
    ctx.fillRect(bullet.x, bullet.y, BULLET_WIDTH, BULLET_HEIGHT);
  });

  ctx.fillStyle = '#FF0000';
  alienBullets.forEach(bullet => {
    ctx.fillRect(bullet.x, bullet.y, BULLET_WIDTH, BULLET_HEIGHT);
  });
}

// Draw shields
function drawShields() {
  ctx.fillStyle = '#00FFFF';
  shields.forEach(shield => {
    shield.blocks.forEach(block => {
      if (block.alive) {
        ctx.fillRect(block.x, block.y, block.width, block.height);
      }
    });
  });
}

// Draw UI
function drawUI() {
  ctx.fillStyle = '#FFFFFF';
  ctx.font = '20px Arial';
  ctx.fillText(`Score: ${score}`, 10, 30);
  ctx.fillText(`Lives: ${lives}`, canvas.width - 100, 30);

  // Display current difficulty
  ctx.font = '16px Arial';
  ctx.fillStyle = selectedDifficulty === DIFFICULTY.EASY ? '#00FF00' :
                  selectedDifficulty === DIFFICULTY.HARD ? '#FF0000' : '#FFFF00';
  ctx.fillText(`Difficulty: ${selectedDifficulty.toUpperCase()}`, 10, 55);
}

// Draw start screen
function drawStartScreen() {
  ctx.fillStyle = '#000000';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  ctx.fillStyle = '#00FF00';
  ctx.font = '40px Arial';
  ctx.textAlign = 'center';
  ctx.fillText('SPACE INVADERS', canvas.width / 2, 100);

  // Difficulty selection
  ctx.fillStyle = '#FFFFFF';
  ctx.font = '24px Arial';
  ctx.fillText('SELECT DIFFICULTY', canvas.width / 2, 200);

  const difficultyY = 250;
  const difficultySpacing = 60;

  // Draw difficulty options
  // Easy
  ctx.font = '20px Arial';
  if (selectedDifficulty === DIFFICULTY.EASY) {
    ctx.fillStyle = '#00FF00';
    ctx.fillText('> EASY <', canvas.width / 2, difficultyY);
  } else {
    ctx.fillStyle = '#888888';
    ctx.fillText('EASY', canvas.width / 2, difficultyY);
  }

  // Medium
  if (selectedDifficulty === DIFFICULTY.MEDIUM) {
    ctx.fillStyle = '#FFFF00';
    ctx.fillText('> MEDIUM <', canvas.width / 2, difficultyY + difficultySpacing);
  } else {
    ctx.fillStyle = '#888888';
    ctx.fillText('MEDIUM', canvas.width / 2, difficultyY + difficultySpacing);
  }

  // Hard
  if (selectedDifficulty === DIFFICULTY.HARD) {
    ctx.fillStyle = '#FF0000';
    ctx.fillText('> HARD <', canvas.width / 2, difficultyY + difficultySpacing * 2);
  } else {
    ctx.fillStyle = '#888888';
    ctx.fillText('HARD', canvas.width / 2, difficultyY + difficultySpacing * 2);
  }

  // Instructions
  ctx.fillStyle = '#FFFFFF';
  ctx.font = '18px Arial';
  ctx.fillText('Arrow Up/Down to Select', canvas.width / 2, 450);
  ctx.fillText('Press SPACE to Start', canvas.width / 2, 480);
  ctx.fillText('Arrow Keys to Move | Space to Shoot', canvas.width / 2, 520);

  ctx.textAlign = 'left';
}

// Draw game over screen
function drawGameOverScreen() {
  ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  ctx.fillStyle = '#FF0000';
  ctx.font = '50px Arial';
  ctx.textAlign = 'center';
  ctx.fillText('GAME OVER', canvas.width / 2, canvas.height / 2 - 40);

  ctx.fillStyle = '#FFFFFF';
  ctx.font = '25px Arial';
  ctx.fillText(`Final Score: ${score}`, canvas.width / 2, canvas.height / 2 + 20);
  ctx.fillText('Press SPACE to Restart', canvas.width / 2, canvas.height / 2 + 60);

  ctx.textAlign = 'left';
}

// Update player
function updatePlayer() {
  if (player.moveLeft && player.x > 0) {
    player.x -= player.speed;
  }
  if (player.moveRight && player.x < canvas.width - player.width) {
    player.x += player.speed;
  }
}

// Update bullets
function updateBullets() {
  // Update player bullets
  playerBullets = playerBullets.filter(bullet => {
    bullet.y -= BULLET_SPEED;
    return bullet.y > 0;
  });

  // Update alien bullets
  alienBullets = alienBullets.filter(bullet => {
    bullet.y += alienBulletSpeed;
    return bullet.y < canvas.height;
  });
}

// Update aliens
function updateAliens() {
  let shouldMoveDown = false;

  // Check if aliens hit edge
  aliens.forEach(alien => {
    if (alien.alive) {
      if ((alien.x <= 0 && alienDirection < 0) ||
          (alien.x + alien.width >= canvas.width && alienDirection > 0)) {
        shouldMoveDown = true;
      }
    }
  });

  if (shouldMoveDown) {
    alienDirection *= -1;
    aliens.forEach(alien => {
      if (alien.alive) {
        alien.y += alienDropDistance;
      }
    });
  }

  // Move aliens
  aliens.forEach(alien => {
    if (alien.alive) {
      alien.x += alienSpeed * alienDirection;

      // Alien shooting
      if (Math.random() < alienShootChance) {
        alienBullets.push({
          x: alien.x + alien.width / 2,
          y: alien.y + alien.height,
          width: BULLET_WIDTH,
          height: BULLET_HEIGHT
        });
      }

      // Check if aliens reached player
      if (alien.y + alien.height >= player.y) {
        lives = 0;
      }
    }
  });
}

// Check collisions
function checkCollisions() {
  // Player bullets vs aliens
  playerBullets = playerBullets.filter(bullet => {
    let bulletActive = true;

    aliens.forEach(alien => {
      if (alien.alive &&
          bullet.x < alien.x + alien.width &&
          bullet.x + bullet.width > alien.x &&
          bullet.y < alien.y + alien.height &&
          bullet.y + bullet.height > alien.y) {
        alien.alive = false;
        bulletActive = false;
        score += alien.type * 10;
      }
    });

    return bulletActive;
  });

  // Player bullets vs shields
  playerBullets = playerBullets.filter(bullet => {
    let bulletActive = true;

    shields.forEach(shield => {
      shield.blocks.forEach(block => {
        if (block.alive &&
            bullet.x < block.x + block.width &&
            bullet.x + bullet.width > block.x &&
            bullet.y < block.y + block.height &&
            bullet.y + bullet.height > block.y) {
          block.alive = false;
          bulletActive = false;
        }
      });
    });

    return bulletActive;
  });

  // Alien bullets vs player
  alienBullets = alienBullets.filter(bullet => {
    if (bullet.x < player.x + player.width &&
        bullet.x + bullet.width > player.x &&
        bullet.y < player.y + player.height &&
        bullet.y + bullet.height > player.y) {
      lives--;
      return false;
    }
    return true;
  });

  // Alien bullets vs shields
  alienBullets = alienBullets.filter(bullet => {
    let bulletActive = true;

    shields.forEach(shield => {
      shield.blocks.forEach(block => {
        if (block.alive &&
            bullet.x < block.x + block.width &&
            bullet.x + bullet.width > block.x &&
            bullet.y < block.y + block.height &&
            bullet.y + bullet.height > block.y) {
          block.alive = false;
          bulletActive = false;
        }
      });
    });

    return bulletActive;
  });
}

// Shoot player bullet
function shootBullet() {
  if (playerBullets.length < currentDifficultySettings.maxPlayerBullets) {
    playerBullets.push({
      x: player.x + player.width / 2 - BULLET_WIDTH / 2,
      y: player.y,
      width: BULLET_WIDTH,
      height: BULLET_HEIGHT
    });
  }
}

// Check win condition
function checkWinCondition() {
  const allDead = aliens.every(alien => !alien.alive);
  if (allDead) {
    // Respawn aliens with increased difficulty
    createAliens();
    alienSpeed += 0.5;
    score += 100;
  }
}

// Game loop
function gameLoop() {
  if (gameState === GAME_STATE.PLAYING) {
    // Clear canvas
    ctx.fillStyle = '#000000';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Update
    updatePlayer();
    updateBullets();
    updateAliens();
    checkCollisions();
    checkWinCondition();

    // Draw
    drawShields();
    drawPlayer();
    drawAliens();
    drawBullets();
    drawUI();

    // Check game over
    if (lives <= 0) {
      gameState = GAME_STATE.GAME_OVER;
      drawGameOverScreen();
    }
  } else if (gameState === GAME_STATE.GAME_OVER) {
    drawGameOverScreen();
  }

  animationId = requestAnimationFrame(gameLoop);
}

// Apply difficulty settings
function applyDifficulty() {
  const settings = currentDifficultySettings;
  alienSpeed = settings.alienSpeed;
  alienShootChance = settings.alienShootChance;
  alienBulletSpeed = settings.alienBulletSpeed;
  alienDropDistance = settings.alienDropDistance;
  lives = settings.lives;
}

// Reset game
function resetGame() {
  score = 0;
  playerBullets = [];
  alienBullets = [];
  alienDirection = 1;
  player.x = canvas.width / 2 - 20;
  applyDifficulty();
  createAliens();
  createShields();
}

// Keyboard event listeners
document.addEventListener('keydown', (e) => {
  if (e.code === 'ArrowLeft') {
    if (gameState === GAME_STATE.PLAYING) {
      player.moveLeft = true;
    }
    e.preventDefault();
  }
  if (e.code === 'ArrowRight') {
    if (gameState === GAME_STATE.PLAYING) {
      player.moveRight = true;
    }
    e.preventDefault();
  }
  if (e.code === 'ArrowUp' && gameState === GAME_STATE.START) {
    e.preventDefault();
    // Cycle difficulty up: Easy -> Medium -> Hard -> Easy
    if (selectedDifficulty === DIFFICULTY.HARD) {
      selectedDifficulty = DIFFICULTY.MEDIUM;
    } else if (selectedDifficulty === DIFFICULTY.MEDIUM) {
      selectedDifficulty = DIFFICULTY.EASY;
    } else {
      selectedDifficulty = DIFFICULTY.HARD;
    }
    currentDifficultySettings = DIFFICULTY_SETTINGS[selectedDifficulty];
    drawStartScreen();
  }
  if (e.code === 'ArrowDown' && gameState === GAME_STATE.START) {
    e.preventDefault();
    // Cycle difficulty down: Easy -> Medium -> Hard -> Easy
    if (selectedDifficulty === DIFFICULTY.EASY) {
      selectedDifficulty = DIFFICULTY.MEDIUM;
    } else if (selectedDifficulty === DIFFICULTY.MEDIUM) {
      selectedDifficulty = DIFFICULTY.HARD;
    } else {
      selectedDifficulty = DIFFICULTY.EASY;
    }
    currentDifficultySettings = DIFFICULTY_SETTINGS[selectedDifficulty];
    drawStartScreen();
  }
  if (e.code === 'Space') {
    e.preventDefault();
    if (gameState === GAME_STATE.START) {
      resetGame();
      gameState = GAME_STATE.PLAYING;
    } else if (gameState === GAME_STATE.PLAYING) {
      shootBullet();
    } else if (gameState === GAME_STATE.GAME_OVER) {
      resetGame();
      gameState = GAME_STATE.PLAYING;
    }
  }
});

document.addEventListener('keyup', (e) => {
  if (e.code === 'ArrowLeft') {
    player.moveLeft = false;
  }
  if (e.code === 'ArrowRight') {
    player.moveRight = false;
  }
});

// Start game
init();
gameLoop();
