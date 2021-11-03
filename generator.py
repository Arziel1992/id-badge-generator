# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import qrcode.image.svg
from PIL import Image, ImageDraw, ImageFont
from cairosvg import svg2png


# %%
# read and display imported data
df = pd.read_csv("funcionarios.csv", keep_default_na=False)
# print(df)

# define template to use
template = Image.open("templates/390x600.png")
width, heigth = template.size

# define qr parameters
factory = qrcode.image.svg.SvgPathImage


# %%
# convert to a dictionary of records
records = df.to_dict('records')

# select a font family to write with
lato = ImageFont.truetype("fonts/Lato/Lato-Regular.ttf", size=24)
montserrat = ImageFont.truetype("fonts/Montserrat/Montserrat-Bold.ttf", size=24)


# %%
# defines the drawing parameters on the card
def generate_card(data, p_run, card, x):

    # take a clear copy of the template
    clear = card.copy()

    # import pohoto and paste on card
    pic = Image.open(f"photos/{p_run}.jpg").resize((150, 150), Image.ANTIALIAS)
    clear.paste(pic, (120, 50))

    # start drawing on card
    draw = ImageDraw.Draw(clear)

    # draw ID text
    draw.text((157, 380), str(data['run']), font=lato, fill='#7D909B')

    # draw text with PIL text anchors MA, with image x = width/2 and y = distance from top to center text horizontally
    draw.text((x/2, 238), data['nombre'], font=montserrat, fill='#0F5D89', anchor='ma')
    draw.text((x/2, 276), data['departamento'], font=lato, fill='#7D909B', anchor='ma')
    draw.text((x/2, 313), data['cargo'], font=lato, fill='#7D909B', anchor='ma')

    # create QR, from record data and save as temp svg
    svg = qrcode.make(data, image_factory=factory)
    svg.save('temp/temp.svg')

    # convert temp svg to temp png
    svg2png(url="temp/temp.svg", write_to="temp/temp.png")

    # import temp png and paste onto card as a mask to avoid transparency overwriting the card
    temp = Image.open(f"temp/temp.png").resize((110, 110), Image.ANTIALIAS)
    clear.paste(temp, (265, 475), temp)

    # TO-DO find a method to create the svg and paste/draw it directly, avoiding conversions and saving/re-saving entirely

    return clear


# %%
# loops each record to be drawn
for record in records:
    p_run = record['run'].replace('.','').replace('-','')
    card_done = generate_card(record, p_run, template, width)
    card_done.save(f"cards/{p_run}.png")


