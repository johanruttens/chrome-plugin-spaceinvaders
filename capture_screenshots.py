#!/usr/bin/env python3
"""Capture screenshots of the Space Invaders Chrome Extension for Chrome Web Store"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_screenshots_manual():
    """Create screenshots manually using HTML canvas"""
    from PIL import Image, ImageDraw, ImageFont

    # Create screenshots directory
    os.makedirs('screenshots', exist_ok=True)

    # Screenshot 1: Start screen (1280x800)
    print("Creating Screenshot 1: Start screen...")
    img1 = Image.new('RGB', (1280, 800), color='black')
    draw1 = ImageDraw.Draw(img1)

    # Scale up the game canvas (480x640) to fit in 1280x800
    # We'll center it and add black bars on sides
    canvas_scale = 800 / 640  # Scale based on height
    scaled_width = int(480 * canvas_scale)
    scaled_height = 800
    offset_x = (1280 - scaled_width) // 2

    # Draw game area background
    draw1.rectangle([offset_x, 0, offset_x + scaled_width, scaled_height], fill='black')

    # Draw title
    try:
        font_title = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 80)
        font_subtitle = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 48)
        font_text = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 36)
    except:
        font_title = ImageFont.load_default()
        font_subtitle = ImageFont.load_default()
        font_text = ImageFont.load_default()

    # Title
    title_text = "SPACE INVADERS"
    title_bbox = draw1.textbbox((0, 0), title_text, font=font_title)
    title_width = title_bbox[2] - title_bbox[0]
    draw1.text((640 - title_width // 2, 100), title_text, fill='#00FF00', font=font_title)

    # Difficulty selection text
    subtitle_text = "SELECT DIFFICULTY"
    subtitle_bbox = draw1.textbbox((0, 0), subtitle_text, font=font_subtitle)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    draw1.text((640 - subtitle_width // 2, 250), subtitle_text, fill='white', font=font_subtitle)

    # Difficulty options
    easy_text = "EASY"
    medium_text = "> MEDIUM <"
    hard_text = "HARD"

    easy_bbox = draw1.textbbox((0, 0), easy_text, font=font_subtitle)
    easy_width = easy_bbox[2] - easy_bbox[0]
    medium_bbox = draw1.textbbox((0, 0), medium_text, font=font_subtitle)
    medium_width = medium_bbox[2] - medium_bbox[0]
    hard_bbox = draw1.textbbox((0, 0), hard_text, font=font_subtitle)
    hard_width = hard_bbox[2] - hard_bbox[0]

    draw1.text((640 - easy_width // 2, 350), easy_text, fill='#888888', font=font_subtitle)
    draw1.text((640 - medium_width // 2, 430), medium_text, fill='#FFFF00', font=font_subtitle)
    draw1.text((640 - hard_width // 2, 510), hard_text, fill='#888888', font=font_subtitle)

    # Instructions
    inst1_text = "Arrow Up/Down to Select"
    inst2_text = "Press SPACE to Start"
    inst3_text = "Arrow Keys to Move | Space to Shoot"

    inst1_bbox = draw1.textbbox((0, 0), inst1_text, font=font_text)
    inst1_width = inst1_bbox[2] - inst1_bbox[0]
    inst2_bbox = draw1.textbbox((0, 0), inst2_text, font=font_text)
    inst2_width = inst2_bbox[2] - inst2_bbox[0]
    inst3_bbox = draw1.textbbox((0, 0), inst3_text, font=font_text)
    inst3_width = inst3_bbox[2] - inst3_bbox[0]

    draw1.text((640 - inst1_width // 2, 620), inst1_text, fill='white', font=font_text)
    draw1.text((640 - inst2_width // 2, 670), inst2_text, fill='white', font=font_text)
    draw1.text((640 - inst3_width // 2, 720), inst3_text, fill='white', font=font_text)

    img1.save('screenshots/screenshot1_1280x800.png', 'PNG')
    print("✓ Created screenshots/screenshot1_1280x800.png (Start screen)")

    # Screenshot 2: Gameplay (1280x800)
    print("\nCreating Screenshot 2: Active gameplay...")
    img2 = Image.new('RGB', (1280, 800), color='black')
    draw2 = ImageDraw.Draw(img2)

    # Draw game area
    draw2.rectangle([offset_x, 0, offset_x + scaled_width, scaled_height], fill='black')

    # Scale factors for positioning
    def scale_x(x):
        return offset_x + int(x * canvas_scale)

    def scale_y(y):
        return int(y * canvas_scale)

    def scale_dim(dim):
        return int(dim * canvas_scale)

    # Draw UI (Score and Lives)
    ui_font = font_text
    draw2.text((scale_x(10), scale_y(20)), "Score: 450", fill='white', font=ui_font)
    draw2.text((scale_x(350), scale_y(20)), "Lives: 3", fill='white', font=ui_font)

    # Difficulty indicator
    try:
        diff_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 28)
    except:
        diff_font = ImageFont.load_default()
    draw2.text((scale_x(10), scale_y(50)), "Difficulty: MEDIUM", fill='#FFFF00', font=diff_font)

    # Draw aliens (grid)
    alien_rows = 5
    alien_cols = 11
    alien_width = scale_dim(30)
    alien_height = scale_dim(20)
    alien_padding = scale_dim(10)
    alien_offset_top = scale_y(80)
    alien_offset_left = scale_x(30)

    for row in range(alien_rows):
        for col in range(alien_cols):
            # Skip some aliens to show they've been destroyed
            if (row == 4 and col > 7) or (row == 3 and col > 9):
                continue

            ax = alien_offset_left + col * (alien_width + alien_padding)
            ay = alien_offset_top + row * (alien_height + alien_padding)

            # Different colors for different rows
            if row < 2:
                alien_color = '#FF0000'  # Red
            elif row < 4:
                alien_color = '#FF00FF'  # Magenta
            else:
                alien_color = '#FFFF00'  # Yellow

            # Draw alien body
            draw2.rectangle([ax, ay, ax + alien_width, ay + alien_height], fill=alien_color)

            # Draw eyes
            eye_size = scale_dim(4)
            draw2.rectangle([ax + scale_dim(8), ay + scale_dim(5),
                           ax + scale_dim(8) + eye_size, ay + scale_dim(5) + eye_size], fill='black')
            draw2.rectangle([ax + scale_dim(18), ay + scale_dim(5),
                           ax + scale_dim(18) + eye_size, ay + scale_dim(5) + eye_size], fill='black')

    # Draw shields
    shield_y = scale_y(490)
    shield_width = scale_dim(60)
    shield_height = scale_dim(40)
    shield_count = 4
    spacing = (scaled_width - (shield_count * shield_width)) // (shield_count + 1)

    for i in range(shield_count):
        sx = offset_x + spacing + i * (shield_width + spacing)
        # Draw shield with some damage (irregular blocks)
        block_size = scale_dim(5)
        for by in range(0, shield_height, block_size):
            for bx in range(0, shield_width, block_size):
                # Randomly skip some blocks to show damage
                if (i == 1 and bx > shield_width * 0.4 and bx < shield_width * 0.6 and by > shield_height * 0.5):
                    continue
                if (i == 2 and bx < shield_width * 0.3 and by < shield_height * 0.4):
                    continue

                rel_x = bx / shield_width
                rel_y = by / shield_height
                if rel_y < 0.7 or (rel_x > 0.3 and rel_x < 0.7):
                    draw2.rectangle([sx + bx, shield_y + by,
                                   sx + bx + block_size, shield_y + by + block_size],
                                  fill='#00FFFF')

    # Draw player ship
    player_x = scale_x(200)
    player_y = scale_y(580)
    player_width = scale_dim(40)
    player_height = scale_dim(30)

    draw2.rectangle([player_x, player_y, player_x + player_width, player_y + player_height],
                   fill='#00FF00')

    # Draw ship triangle on top
    draw2.polygon([
        (player_x + player_width // 2, player_y - scale_dim(5)),
        (player_x, player_y),
        (player_x + player_width, player_y)
    ], fill='#00FF00')

    # Draw player bullets
    bullet_width = scale_dim(3)
    bullet_height = scale_dim(15)

    bullets = [
        (scale_x(150), scale_y(300)),
        (scale_x(220), scale_y(200)),
        (scale_x(320), scale_y(250))
    ]

    for bx, by in bullets:
        draw2.rectangle([bx, by, bx + bullet_width, by + bullet_height], fill='white')

    # Draw alien bullets
    alien_bullets = [
        (scale_x(100), scale_y(400)),
        (scale_x(280), scale_y(450)),
        (scale_x(380), scale_y(350))
    ]

    for bx, by in alien_bullets:
        draw2.rectangle([bx, by, bx + bullet_width, by + bullet_height], fill='#FF0000')

    img2.save('screenshots/screenshot2_1280x800.png', 'PNG')
    print("✓ Created screenshots/screenshot2_1280x800.png (Active gameplay)")

    # Also create 640x400 versions
    print("\nCreating 640x400 versions...")

    img1_small = img1.resize((640, 400), Image.Resampling.LANCZOS)
    img1_small.save('screenshots/screenshot1_640x400.png', 'PNG')
    print("✓ Created screenshots/screenshot1_640x400.png")

    img2_small = img2.resize((640, 400), Image.Resampling.LANCZOS)
    img2_small.save('screenshots/screenshot2_640x400.png', 'PNG')
    print("✓ Created screenshots/screenshot2_640x400.png")

    print("\n" + "="*60)
    print("✅ All screenshots created successfully!")
    print("="*60)
    print("\nGenerated files:")
    print("  - screenshots/screenshot1_1280x800.png (Start screen)")
    print("  - screenshots/screenshot2_1280x800.png (Gameplay)")
    print("  - screenshots/screenshot1_640x400.png (Start screen, smaller)")
    print("  - screenshots/screenshot2_640x400.png (Gameplay, smaller)")
    print("\nFormat: 24-bit PNG (no alpha channel)")
    print("Ready for Chrome Web Store upload!")

def main():
    """Main function"""
    print("Space Invaders Chrome Extension Screenshot Generator")
    print("="*60)

    # Create screenshots manually using PIL
    create_screenshots_manual()

if __name__ == '__main__':
    main()
