# 2024.11.06 - itbetyar.hu - Python | main

import streamlit as st
from PIL import Image
from ultralytics import YOLO
import pathlib

def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load the external CSS
css_path = pathlib.Path("mystyles.css")
load_css(css_path)

model = YOLO('best_tumor_detection_model_120.pt')

def myaction1():
      st.session_state.reset_counter += 1
      st.session_state.imageactive = "imgs/out_test01.jpg"
def myaction2():
      st.session_state.reset_counter += 1
      st.session_state.imageactive = "imgs/out_test02.jpg"
def myaction3():
      st.session_state.reset_counter += 1
      st.session_state.imageactive = "imgs/out_test03.jpg"
def myaction4():
      st.session_state.reset_counter += 1
      st.session_state.imageactive = "imgs/out_test04.jpg"
def myaction5():
      st.session_state.reset_counter += 1
      st.session_state.imageactive = "imgs/out_test06.jpg"
def myaction6():
      st.session_state.reset_counter += 1
      st.session_state.imageactive = "imgs/out_test07.jpg"

def inferenc(image):
    st.session_state.reset_counter += 1
    if isinstance(image, str): # Check if the image is a path (string) or an actual Image object
        image = Image.open(image)  # Open the image if it's a path

    results = model(image) # Perform inference using the YOLO model
    detection_result = results[0]
    annotated_img = detection_result.plot() #Get the annotated image+b.boxes from t results
    # Save the annotated image to session state (replace the imageactive)
    st.session_state.imageactive = annotated_img
    # Optionally, store the results in session state for further use
    st.session_state.detection_results = detection_result

    # Check if there are any detected boxes (i.e., tumors)
    if detection_result.boxes:
        # If there are detected boxes, process the results
        for box in detection_result.boxes:
            confidence = box.conf[0].item()  # Confidence score
            class_name = detection_result.names[int(box.cls[0].item())]  # Class name

            # Save the variables (confidence, class_name) if needed or just print them
            st.session_state.confidence = confidence
            st.session_state.class_name = class_name

            # Display detection details
            oszi2.markdown(f'<div class="detect-text">Detektálás: <b>{class_name}</b>⚠️ <br> Bizonyosság: <b>{confidence * 100:.0f} %</b> <br> Detektálások száma: <b>{len(detection_result.boxes)}</b></div>', unsafe_allow_html=True)
    else:
        # If no boxes are detected (no tumor detected)
        oszi2.markdown('<div class="detect-text-negativ">Nem detektáltunk tumort.✅</div>')

# * #########################################################################

if "imageactive" not in st.session_state:
    st.session_state.imageactive = "imgs/minta.jpg" # ha nincs kép, mintát tölt
if 'reset_counter' not in st.session_state:
     st.session_state.reset_counter = 0 # resetcnt legyen nulla

# * #########################################################################

st.markdown("### itbetyar.hu")
st.title("Braintumor object detection")
st.markdown("---")
st.markdown("Tölts be egy mintát az alábbi gombokra kattinva, vagy tölts fel egy saját képet!")

col1, col2,col3,col4,col5,col6 = st.columns([1,1,1,1,1,1])

col1.image("imgs/out_test01.jpg", width=100)
col1.button("Minta 1", on_click=myaction1, key="kisgomb1")
col2.image("imgs/out_test02.jpg", width=100)
col2.button("Minta 2", on_click=myaction2, key="kisgomb2")
col3.image("imgs/out_test03.jpg", width=100)
col3.button("Minta 3", on_click=myaction3, key="kisgomb3")
col4.image("imgs/out_test04.jpg", width=100)
col4.button("Minta 4", on_click=myaction4, key="kisgomb4")
col5.image("imgs/out_test06.jpg", width=100)
col5.button("Minta 5", on_click=myaction5, key="kisgombn5")
col6.image("imgs/out_test07.jpg", width=100)
col6.button("Minta 6", on_click=myaction6, key="kisgombn6")

st.divider()

# * #########################################################################

oszi1, oszi2 = st.columns([1,1])

uploaded_file = oszi1.file_uploader("Fel is tölthetsz képet!", 
                                    type=["jpg", "jpeg", "png"],
                                    key=f'uploader_{st.session_state.reset_counter}')

oszi1.markdown("2. Ha a képbetöltés megvan, kattints a \"Detektálás indítása\" gombra")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.session_state.imageactive = image
    oszi2.image(st.session_state.imageactive, width=300)
else:
    # Check if the active image is a path or an Image object
    if isinstance(st.session_state.imageactive, str):
        image = Image.open(st.session_state.imageactive)  # Open from path
    else:
        image = st.session_state.imageactive  # Use the Image object directly
    oszi2.image(image, width=300)


oszi2.button("Detektálás indítása", on_click=lambda:inferenc(image), key="nagygomb")

st.divider()

st.markdown('### Leírás', unsafe_allow_html=True)

st.markdown('<div class="custom-text">Fenti minta egy <b>"proof of concept"</b> jellegű bemutató. Nem alkalmas diagnózis felállítására.</div>', unsafe_allow_html=True)

st.markdown('<div class="custom-text2">Az alkalmazott tumor detektáló modell, nyilvános minta adathalmazon lett betanítva, azaz <b>~1000 darab agyi mri</b> felvétel alapján tanult, hatékonysága így <b>80%-os</b>. Produkciós azaz valódi orvosi diagnosztikára is alkamassá tehető magasabb számú oktatókép segítségével.</div>', unsafe_allow_html=True)


