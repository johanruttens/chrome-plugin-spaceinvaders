#!/usr/bin/env python3
"""Generate placeholder icons for Space Invaders Chrome Extension"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(size, filename):
    """Create a Space Invaders themed icon"""
    # Create black background
    img = Image.new('RGB', (size, size), color='black')
    draw = ImageDraw.Draw(img)

    # Draw a simple alien shape (Space Invaders style)
    scale = size / 128  # Scale based on 128x128 reference

    # Alien body (simplified pixel art style)
    alien_color = '#00FF00'  # Green like the player ship

    if size >= 48:
        # Draw alien body
        body_width = int(size * 0.6)
        body_height = int(size * 0.4)
        body_x = (size - body_width) // 2
        body_y = int(size * 0.3)

        draw.rectangle([body_x, body_y, body_x + body_width, body_y + body_height],
                      fill=alien_color)

        # Draw alien eyes
        eye_size = int(size * 0.08)
        eye_y = body_y + int(body_height * 0.3)
        left_eye_x = body_x + int(body_width * 0.25)
        right_eye_x = body_x + int(body_width * 0.65)

        draw.rectangle([left_eye_x, eye_y, left_eye_x + eye_size, eye_y + eye_size],
                      fill='black')
        draw.rectangle([right_eye_x, eye_y, right_eye_x + eye_size, eye_y + eye_size],
                      fill='black')

        # Draw alien antennae
        antenna_width = int(size * 0.06)
        antenna_height = int(size * 0.15)
        left_antenna_x = body_x + int(body_width * 0.2)
        right_antenna_x = body_x + int(body_width * 0.7)
        antenna_y = body_y - antenna_height

        draw.rectangle([left_antenna_x, antenna_y, left_antenna_x + antenna_width, body_y],
                      fill=alien_color)
        draw.rectangle([right_antenna_x, antenna_y, right_antenna_x + antenna_width, body_y],
                      fill=alien_color)

        # Draw alien legs
        leg_width = int(size * 0.06)
        leg_height = int(size * 0.2)
        leg_y = body_y + body_height

        for i in range(3):
            leg_x = body_x + int(body_width * (0.2 + i * 0.3))
            draw.rectangle([leg_x, leg_y, leg_x + leg_width, leg_y + leg_height],
                          fill=alien_color)
    else:
        # Simplified alien for 16x16
        alien_size = int(size * 0.7)
        alien_x = (size - alien_size) // 2
        alien_y = (size - alien_size) // 2

        draw.rectangle([alien_x, alien_y, alien_x + alien_size, alien_y + alien_size],
                      fill=alien_color)

        # Simple eyes
        eye_size = int(size * 0.15)
        eye_y = alien_y + int(alien_size * 0.3)
        draw.rectangle([alien_x + 2, eye_y, alien_x + 2 + eye_size, eye_y + eye_size],
                      fill='black')
        draw.rectangle([alien_x + alien_size - eye_size - 2, eye_y,
                       alien_x + alien_size - 2, eye_y + eye_size],
                      fill='black')

    # Save the image
    img.save(filename, 'PNG')
    print(f"Created {filename} ({size}x{size})")

def main():
    """Generate all required icons"""
    icons_dir = 'icons'

    # Ensure icons directory exists
    os.makedirs(icons_dir, exist_ok=True)

    # Generate icons in required sizes
    sizes = [16, 48, 128]

    for size in sizes:
        filename = os.path.join(icons_dir, f'icon{size}.png')
        create_icon(size, filename)

    print("\nAll icons generated successfully!")
    print("Icons are Space Invaders themed with green alien design.")

if __name__ == '__main__':
    main()
