# Space Invaders Popup - Chrome Extension

A fully playable, classic Space Invaders game that runs directly in your Chrome browser toolbar popup. No need to open a new tab—just click the extension icon and start playing!

## 🎮 Features

- **Classic Gameplay**: Authentic Space Invaders experience with familiar mechanics
- **Three Difficulty Levels**: Choose between Easy, Medium, and Hard modes
  - **Easy**: Slower aliens, more lives (5), more bullets (5), less aggressive shooting
  - **Medium**: Balanced gameplay with 3 lives and 3 bullets
  - **Hard**: Fast aliens, fewer lives (2), limited bullets (2), aggressive alien fire
- **Player Ship**: Move left/right with arrow keys and shoot with spacebar
- **Alien Grid**: Multiple rows of invaders that move side-to-side and drop down
- **Alien Attacks**: Aliens shoot back at random intervals
- **Protective Shields**: Destructible barriers that protect your ship
- **Score System**: Track your performance as you destroy invaders
- **Lives System**: Lives vary by difficulty level (2-5 lives)
- **Progressive Difficulty**: New waves of faster aliens when you clear the screen
- **Game States**: Start screen with difficulty selection, active gameplay, and game over screens
- **Compact Design**: Fits perfectly in a 480x640px popup window

## 📦 Installation

### Option 1: Install from Chrome Web Store (Coming Soon)
Once published, you'll be able to install directly from the Chrome Web Store.

### Option 2: Install as Unpacked Extension (For Development)

1. **Clone or download this repository**:
   ```bash
   git clone https://github.com/yourusername/chrome-plugin-spaceinvaders.git
   ```

2. **Load the extension in Chrome**:
   - Note: Icon files are already included in the `icons/` directory
   - Open Chrome and navigate to `chrome://extensions/`
   - Enable "Developer mode" (toggle in top-right corner)
   - Click "Load unpacked"
   - Select the project's root directory
   - The Space Invaders icon should appear in your toolbar

## 🕹️ How to Play

1. **Start the Game**: Click the extension icon in your Chrome toolbar
2. **Select Difficulty**: 
   - Use **Arrow Up** / **Arrow Down** to cycle through difficulty levels (Easy, Medium, Hard)
   - Each difficulty level is color-coded (Easy = Green, Medium = Yellow, Hard = Red)
   - Press **Spacebar** to start the game with your selected difficulty
3. **Game Controls**:
   - **Arrow Left** / **Arrow Right**: Move your ship horizontally
   - **Spacebar**: Fire laser (bullet limit varies by difficulty)
4. **Objective**: Destroy all aliens before they reach the bottom of the screen
5. **Scoring**: Earn points for each alien destroyed (varies by alien type)
6. **Lives**: Number of lives depends on your selected difficulty (Easy: 5, Medium: 3, Hard: 2)

## 🛠️ Technical Details

### Technology Stack
- **Manifest Version**: 3 (Chrome Extension Manifest V3)
- **Frontend**: Vanilla JavaScript (ES6+)
- **Graphics**: HTML5 Canvas API
- **Styling**: Pure CSS3

### Project Structure
```
chrome-plugin-spaceinvaders/
├── manifest.json          # Chrome extension configuration
├── popup.html            # Game container HTML
├── popup.css             # Popup styling (480x640px canvas)
├── popup.js              # Complete game logic with difficulty levels (608 lines)
├── icons/                # Extension icons (16x16, 48x48, 128x128)
│   ├── icon16.png
│   ├── icon48.png
│   └── icon128.png
├── docs/                 # Project documentation
│   ├── intent-integrity-chain.md
│   └── requirements.md
├── LICENSE               # MIT License
└── README.md            # This file
```

### Key Implementation Details
- **Game Loop**: Uses `requestAnimationFrame` for smooth 60 FPS rendering
- **Collision Detection**: Pixel-perfect collision detection for all projectiles
- **Entity Management**: Efficient handling of player, aliens, shields, and projectiles
- **State Management**: Clean separation between game states (start, playing, game over)
- **No External Dependencies**: Pure vanilla JavaScript—no libraries required

## 📋 Chrome Web Store Compliance

This extension is built to comply with Chrome Web Store policies:
- ✅ Uses Manifest V3
- ✅ No remote code execution
- ✅ No external dependencies or CDN resources
- ✅ All code is contained within the extension
- ✅ Minimal permissions required (none beyond popup display)
- ✅ Clear, descriptive metadata
- ✅ Appropriate content rating (suitable for all ages)

## 🔧 Development

### Prerequisites
- Google Chrome (latest version recommended)
- Basic understanding of Chrome Extension development

### Building for Production

**Note**: The Chrome Web Store accepts **.zip files** for submission, NOT .crx files. Chrome automatically packages the .zip into a .crx during the review process.

A production-ready `space-invaders-extension.zip` file is already included in this repository.

To create your own distribution package:
1. Test the extension thoroughly in unpacked mode
2. Create a ZIP file of the project root (excluding development files):
   ```bash
   zip -r space-invaders-extension.zip . -x "*.git*" "*.DS_Store" "docs/*" "prompts/*" "generate_icons.py"
   ```
3. Upload the ZIP file to the [Chrome Web Store Developer Dashboard](https://chrome.google.com/webstore/devconsole)

### Testing
- Load the unpacked extension and click the icon to launch
- Test all controls (arrow keys, spacebar)
- Verify collision detection works correctly
- Confirm game states transition properly
- Check that the popup displays correctly without scrollbars

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2025 Baruch Sadogursky

## 🙏 Acknowledgments

- Inspired by the classic Space Invaders arcade game by Tomohiro Nishikado (1978)
- Built as a demonstration of Chrome Extension development with vanilla JavaScript
- Created following the Intent Integrity Chain (IIC) methodology

## 🐛 Known Issues

- No sound effects or background music (keeping it lightweight)
- No high score persistence (scores reset when popup closes)
- Icons are placeholder graphics (Space Invaders themed green aliens)

## 🚀 Future Enhancements (Ideas)

- Add sound effects and retro music
- Implement local high score tracking using Chrome Storage API
- Include power-ups and bonus rounds
- Add keyboard customization options
- Implement touch controls for mobile debugging
- Add leaderboard functionality

---

**Enjoy the game! May your aim be true and your reflexes swift! 👾**
