from PIL import Image, ImageDraw, ImageFont
import random
import string
import sys

def generate_random_string(length):
    digits = random.choice(string.digits)
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    special_characters = random.choice("!#%:,.;*()[]{}<>/?@&-=+")

    remaining_chars = random.choices(
        string.ascii_letters + string.digits + "!#%:,.;*()[]{}<>/?@&-=+", k=length - 4
    )

    result_list = list(digits + uppercase + lowercase + special_characters + "".join(remaining_chars))
    random.shuffle(result_list)

    return "".join(result_list)

def create_image_with_text(text, width=720, height=360):
    image = Image.new('RGB', (width, height), "white")
    draw = ImageDraw.Draw(image)

    for _ in range(100000):
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        draw.point((x, y), fill=(0, random.randint(150, 255), 0))

    draw.line((0, height, width, 0), fill="yellow", width=1)

    font_size = min(max(4, (width // len(text)) // 2 * 2), 24)
    try:
        font = ImageFont.truetype("times.ttf", font_size)
    except OSError:
        font = ImageFont.load_default()

    text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:]

    if text_width > width or text_height > height:
        raise ValueError("Ошибка! Текст не помещается в изображение. Уменьшите длину строки.")

    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2
    draw.text((text_x, text_y), text, font=font, fill="red")

    image.save("output.jpg")
    return image


try:
    user_input = input()
    length = int(user_input)
except ValueError:
    print("Ошибка! Длина должна быть целым числом.")
    sys.exit(1)

if length < 4:
    print("Ошибка! Длина должна быть минимум 4 символа.")
    sys.exit(1)

try:
    rand_str = generate_random_string(length)
except Exception as e:
    print(e)
    sys.exit(1)

try:
    img = create_image_with_text(rand_str)
    img.show()
except Exception as e:
    print(e)
    sys.exit(1)