import streamlit as st, random
from PIL import Image, ImageDraw, ImageFont

SUITS="♠♥♣♦"; RANKS="23456789TJQKA"
FONT = ImageFont.load_default()

def card_img(r,s):
    img=Image.new("RGB",(90,130),"white")
    d=ImageDraw.Draw(img); d.rectangle([(0,0),(89,129)],outline="black")
    d.multiline_text((5,5),f"{r}\n{s}",font=FONT,fill="black",spacing=2)
    return img

if "hand" not in st.session_state:
    deck=[(r,s) for s in SUITS for r in RANKS]+[("JK",""),("MK","")]
    random.shuffle(deck); st.session_state.hand=deck[:9]

strip=Image.new("RGB",(90*9,130),"white")
for i,c in enumerate(st.session_state.hand): strip.paste(card_img(*c),(i*90,0))

st.title("بنت السبيت – نسخة ويب")
st.image(strip)
if st.button("يد جديدة"): st.session_state.clear()
