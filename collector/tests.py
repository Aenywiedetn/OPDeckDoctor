from .models import Card
import base64
import os


def convert_image_to_base64(image_path):
    with open(image_path, 'rb') as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def fill_images_base64():
    cards = Card.objects.all()  # Retrieve all cards from the database
    img_folder = 'OPDeckDoctor2/static/img/'

    for card in cards:
        image_path = os.path.join(img_folder, f"{card.idx}.png")

        if os.path.exists(image_path):
            base64_image = convert_image_to_base64(image_path)
            card.image = base64_image
            card.save()
            print(f"Base64 image saved for Card {card.idx}")
        else:
            print(f"Image not found for Card {card.idx}")

def card_order_check():
    cards = Card.objects.all()

    for card in cards:
        print(f"Order is: {card.idx}")