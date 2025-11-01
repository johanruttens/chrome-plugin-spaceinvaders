#!/usr/bin/env python3
"""Generate an improved, professional-looking Space Invaders icon"""

from PIL import Image, ImageDraw
import os

def create_professional_icon(size, filename):
    """Create a professional Space Invaders themed icon with retro arcade aesthetic"""
    # Create dark space background with slight gradient effect
    img = Image.new('RGB', (size, size), color='#000000')
    draw = ImageDraw.Draw(img)

    # Add subtle dark blue gradient for space feel
    for y in range(size):
        gradient_color = int(20 * (1 - y / size))
        draw.line([(0, y), (size, y)], fill=(0, 0, gradient_color))

    scale = size / 128

    # Draw a stylized classic Space Invaders alien (iconic squid-like alien)
    alien_color = '#00FF00'  # Bright retro green
    highlight_color = '#66FF66'  # Lighter green for highlights
    shadow_color = '#008800'  # Darker green for depth

    # Main alien body proportions
    center_x = size // 2
    center_y = int(size * 0.48)

    # Alien body dimensions
    body_width = int(size * 0.5)
    body_height = int(size * 0.32)
    body_left = center_x - body_width // 2
    body_top = center_y - body_height // 2

    # Draw alien body with rounded top
    draw.rectangle([body_left, body_top + 8, body_left + body_width, body_top + body_height],
                   fill=alien_color)
    draw.ellipse([body_left, body_top, body_left + body_width, body_top + 20],
                 fill=alien_color)

    # Add depth/shadow effect
    draw.rectangle([body_left + 2, body_top + 10, body_left + body_width - 2, body_top + body_height - 2],
                   fill=shadow_color)

    # Draw antenna/horns at the top
    antenna_width = int(size * 0.08)
    antenna_height = int(size * 0.15)

    # Left antenna
    left_antenna_x = body_left + int(body_width * 0.15)
    antenna_y = body_top - antenna_height + 8
    draw.rectangle([left_antenna_x, antenna_y, left_antenna_x + antenna_width, body_top + 8],
                   fill=alien_color)
    draw.ellipse([left_antenna_x - 3, antenna_y - 6, left_antenna_x + antenna_width + 3, antenna_y + 6],
                 fill=highlight_color)

    # Right antenna
    right_antenna_x = body_left + int(body_width * 0.77)
    draw.rectangle([right_antenna_x, antenna_y, right_antenna_x + antenna_width, body_top + 8],
                   fill=alien_color)
    draw.ellipse([right_antenna_x - 3, antenna_y - 6, right_antenna_x + antenna_width + 3, antenna_y + 6],
                 fill=highlight_color)

    # Draw large eyes (iconic feature)
    eye_width = int(size * 0.12)
    eye_height = int(size * 0.16)
    eye_y = body_top + int(body_height * 0.25)

    # Left eye
    left_eye_x = body_left + int(body_width * 0.22)
    draw.ellipse([left_eye_x, eye_y, left_eye_x + eye_width, eye_y + eye_height],
                 fill='#000000')
    # Eye highlight
    draw.ellipse([left_eye_x + 2, eye_y + 2, left_eye_x + eye_width - 4, eye_y + eye_height - 4],
                 fill='#0a0a0a')
    draw.ellipse([left_eye_x + eye_width - 8, eye_y + 3, left_eye_x + eye_width - 3, eye_y + 8],
                 fill='#1a1a1a')

    # Right eye
    right_eye_x = body_left + int(body_width * 0.66)
    draw.ellipse([right_eye_x, eye_y, right_eye_x + eye_width, eye_y + eye_height],
                 fill='#000000')
    draw.ellipse([right_eye_x + 2, eye_y + 2, right_eye_x + eye_width - 4, eye_y + eye_height - 4],
                 fill='#0a0a0a')
    draw.ellipse([right_eye_x + eye_width - 8, eye_y + 3, right_eye_x + eye_width - 3, eye_y + 8],
                 fill='#1a1a1a')

    # Draw claw-like arms/tentacles
    arm_width = int(size * 0.09)
    arm_length = int(size * 0.18)
    arm_y = body_top + int(body_height * 0.6)

    # Left arm
    left_arm_x = body_left - int(arm_width * 0.3)
    draw.polygon([
        (left_arm_x, arm_y),
        (left_arm_x + arm_width, arm_y),
        (left_arm_x + arm_width - 4, arm_y + arm_length),
        (left_arm_x + 4, arm_y + arm_length)
    ], fill=alien_color)

    # Right arm
    right_arm_x = body_left + body_width - int(arm_width * 0.7)
    draw.polygon([
        (right_arm_x, arm_y),
        (right_arm_x + arm_width, arm_y),
        (right_arm_x + arm_width - 4, arm_y + arm_length),
        (right_arm_x + 4, arm_y + arm_length)
    ], fill=alien_color)

    # Draw legs (iconic zigzag pattern)
    leg_width = int(size * 0.08)
    leg_height = int(size * 0.16)
    leg_y = body_top + body_height

    # Four legs
    for i in range(4):
        leg_x = body_left + int(body_width * (0.12 + i * 0.24))

        # Zigzag leg pattern
        if i % 2 == 0:
            # Leg going left
            draw.polygon([
                (leg_x + leg_width, leg_y),
                (leg_x + leg_width, leg_y + leg_height // 2),
                (leg_x, leg_y + leg_height // 2),
                (leg_x, leg_y + leg_height),
                (leg_x - 4, leg_y + leg_height),
                (leg_x - 4, leg_y + leg_height // 2 - 4),
                (leg_x + leg_width - 4, leg_y + leg_height // 2 - 4),
                (leg_x + leg_width - 4, leg_y)
            ], fill=alien_color)
        else:
            # Leg going right
            draw.polygon([
                (leg_x, leg_y),
                (leg_x, leg_y + leg_height // 2),
                (leg_x + leg_width, leg_y + leg_height // 2),
                (leg_x + leg_width, leg_y + leg_height),
                (leg_x + leg_width + 4, leg_y + leg_height),
                (leg_x + leg_width + 4, leg_y + leg_height // 2 - 4),
                (leg_x + 4, leg_y + leg_height // 2 - 4),
                (leg_x + 4, leg_y)
            ], fill=alien_color)

    # Add pixel-art style highlights on top of alien head for retro look
    highlight_size = int(size * 0.04)
    draw.rectangle([body_left + int(body_width * 0.3), body_top + 2,
                   body_left + int(body_width * 0.3) + highlight_size, body_top + 2 + highlight_size],
                   fill=highlight_color)
    draw.rectangle([body_left + int(body_width * 0.6), body_top + 4,
                   body_left + int(body_width * 0.6) + highlight_size, body_top + 4 + highlight_size],
                   fill=highlight_color)

    # Add some stars in the background for space theme
    star_positions = [
        (int(size * 0.15), int(size * 0.15)),
        (int(size * 0.85), int(size * 0.20)),
        (int(size * 0.10), int(size * 0.80)),
        (int(size * 0.90), int(size * 0.85)),
        (int(size * 0.25), int(size * 0.90)),
        (int(size * 0.75), int(size * 0.10))
    ]

    for star_x, star_y in star_positions:
        # Draw a small cross-shaped star
        draw.rectangle([star_x - 1, star_y - 2, star_x + 1, star_y + 2], fill='#FFFFFF')
        draw.rectangle([star_x - 2, star_y - 1, star_x + 2, star_y + 1], fill='#FFFFFF')

    # Save with high quality
    img.save(filename, 'PNG', optimize=True)
    print(f"✓ Created improved {filename} ({size}x{size})")

def create_scaled_icon(source_size, target_size, source_img, filename):
    """Create a scaled down version with high quality"""
    # Use high-quality resampling
    scaled_img = source_img.resize((target_size, target_size), Image.Resampling.LANCZOS)
    scaled_img.save(filename, 'PNG', optimize=True)
    print(f"✓ Created {filename} ({target_size}x{target_size})")

def main():
    """Generate all improved icons"""
    icons_dir = 'icons'
    os.makedirs(icons_dir, exist_ok=True)

    print("🎮 Generating improved Space Invaders icons...")
    print()

    # Generate the main 128x128 icon
    icon_128_path = os.path.join(icons_dir, 'icon128.png')
    create_professional_icon(128, icon_128_path)

    # Load the 128x128 version and scale down for other sizes
    base_img = Image.open(icon_128_path)

    # Generate 48x48
    icon_48_path = os.path.join(icons_dir, 'icon48.png')
    create_scaled_icon(128, 48, base_img, icon_48_path)

    # Generate 16x16
    icon_16_path = os.path.join(icons_dir, 'icon16.png')
    create_scaled_icon(128, 16, base_img, icon_16_path)

    print()
    print("✅ All icons generated successfully!")
    print("📁 Icons saved in:", os.path.abspath(icons_dir))
    print()
    print("Icon features:")
    print("  • Professional Space Invaders alien design")
    print("  • Retro arcade green color scheme")
    print("  • Space-themed dark background with stars")
    print("  • Optimized for Chrome Web Store")

if __name__ == '__main__':
    main()
