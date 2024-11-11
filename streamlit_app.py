################################################################
################################################################
#     2024.11 - itbetyar.hu - Braintumor object detection
################################################################

import streamlit as st
from PIL import Image
from ultralytics import YOLO
import pathlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import io

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
    if isinstance(image, str):  # Check if the image is a path (string) or an actual Image object
        image = Image.open(image)  # Open the image if it's a path

    results = model(image)  # Perform inference using the YOLO model
    detection_result = results[0]
    
    # Create a matplotlib figure to draw custom bounding boxes
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.imshow(image)  # Display the original image
    
    # Hide axes and remove borders
    ax.axis('off')  # Turn off the axes
    
    # If there are bounding boxes detected, draw them
    if detection_result.boxes:
        for box in detection_result.boxes:
            # Extract coordinates and confidence
            x_min, y_min, x_max, y_max = box.xyxy[0].tolist()  # Get bounding box coordinates
            confidence = box.conf[0].item()  # Confidence score
            class_name = detection_result.names[int(box.cls[0].item())]  # Class name

            # Draw the bounding box with custom color and style
            ax.add_patch(patches.Rectangle(
                (x_min, y_min), x_max - x_min, y_max - y_min,
                linewidth=3, edgecolor='cyan', facecolor='none'))  # Draw the bounding box
            ax.text(x_min, y_min - 10, f'{class_name} {confidence:.2f}',
                    fontsize=12, color='cyan', weight='bold',
                    bbox=dict(facecolor='black', alpha=0.5, edgecolor='none', boxstyle='round,pad=0.3'))
            
            oszi1.markdown(f'<div class="detect-text">Detektálás: <b>{class_name}</b>⚠️ <br> Bizonyosság: <b>{confidence * 100:.0f} %</b> <br> Detektálások száma: <b>{len(detection_result.boxes)}</b></div>', unsafe_allow_html=True)

        # Adjust layout to remove any extra whitespace around the image
        plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

        # Save the figure to a BytesIO object (in-memory file)
        img_buf = io.BytesIO()
        fig.savefig(img_buf, format='png', bbox_inches='tight', pad_inches=0)  # Save without padding
        img_buf.seek(0)  # Rewind to the beginning of the file

        # Convert the image to a PIL Image
        img = Image.open(img_buf)

        # Save the annotated image in session state
        st.session_state.imageactive = img  # Store the annotated PIL image
        # Optionally, store the results in session state for further use
        st.session_state.detection_results = detection_result
    else:
        st.session_state.imageactive = image  # No detections, keep the original image
        # Show message if no detections are found
        oszi1.markdown('<div class="detect-text-negativ">Nem detektáltunk tumort.✅ </div>', unsafe_allow_html=True)

# * #########################################################################

if "imageactive" not in st.session_state:
    st.session_state.imageactive = "imgs/minta.jpg"  # If there's no image, load a default one
if 'reset_counter' not in st.session_state:
    st.session_state.reset_counter = 0  # Reset counter starts at 0

# * #########################################################################
# * ####################### Frontend starts here ##########################

bev1, bev2, bev3, bev4 = st.columns([0.6, 3, 3, 3])
bev1.image("imgs/itb_logo.webp", width=38)
bev2.markdown('<div class="mylink"><a href="https://itbetyar.hu" target="_blank">itbetyar.hu</a></div>', unsafe_allow_html=True)

bev21, bev22 = st.columns([3, 2])
bev21.title("Braintumor object detection")
bev22.image("imgs/mri.webp", width=100)
st.subheader("A.I. alapon működő agytumor detektálás")
st.markdown('<div class="mylink">Alábbi applikáció az itbetyar.hu <a href="https://itbetyar.hu/mesterseges-intelligencia-fejleszto-tanfolyam/" target="_blank">A.I. Developer tanfolyamának</a> minta anyaga</div>', unsafe_allow_html=True)

st.markdown("---")

st.markdown('<div class="custom-text3">1. Tölts be egy mintát az alábbi gombokra kattintva, vagy tölts fel egy saját képet!</div>', unsafe_allow_html=True)
col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])
col1.image("imgs/out_test01.jpg", width=100)
col1.button("Minta 1", on_click=myaction1, key="kisgomb1")
col2.image("imgs/out_test02.jpg", width=100)
col2.button("Minta 2", on_click=myaction2, key="kisgomb2")
col3.image("imgs/out_test03.jpg", width=100)
col3.button("Minta 3", on_click=myaction3, key="kisgomb3")
col4.image("imgs/out_test04.jpg", width=100)
col4.button("Minta 4", on_click=myaction4, key="kisgomb4")
col5.image("imgs/out_test06.jpg", width=100)
col5.button("Minta 5", on_click=myaction5, key="kisgombn5", help="Negatív, tumor mentes minta")
col6.image("imgs/out_test07.jpg", width=100)
col6.button("Minta 6", on_click=myaction6, key="kisgombn6", help="Negatív, tumor mentes minta")

st.markdown('<div class="custom-text3">2. Ha a képbetöltés megvan, kattints a <b>"Detektálás indítása"</b> gombra</div>', unsafe_allow_html=True)
st.divider()

# * #########################################################################

oszi1, oszi2 = st.columns([1, 1])

uploaded_file = oszi1.file_uploader("Fel is tölthetsz képet!",
                                    type=["jpg", "jpeg", "png"],
                                    key=f'uploader_{st.session_state.reset_counter}')

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

oszi2.button("Detektálás indítása", on_click=lambda: inferenc(image), key="nagygomb")




# * #########################################################################
# * #########################################################################

st.divider()

also1,also2,also3,also4 = st.columns([1,2,2,1])
also2.image("imgs/aidev.webp", width=200)
also3.markdown('<div class="mylink">Ha szeretnél hasonló applikációkat készíteni várunk <a href="https://itbetyar.hu/mesterseges-intelligencia-fejleszto-tanfolyam/" target="_blank">A.I. Developer tanfolyamainkon</a></div>', unsafe_allow_html=True)


st.markdown('### Leírás:', unsafe_allow_html=True)
st.markdown('<div class="custom-text">Fenti minta egy <b>"proof of concept"</b> jellegű bemutató. Nem alkalmas diagnózis felállítására.</div>', unsafe_allow_html=True)

foot1,foot2,foot3,foot4 = st.columns([3,0.6,1,3])
foot2.image("imgs/itb_logo.webp", width=38)
foot3.markdown('<div class="mylink"><a href="https://itbetyar.hu" target="_blank">itbetyar.hu</a></div>', unsafe_allow_html=True)


st.markdown('<div class="custom-text2">Az alkalmazott tumor detektáló modell, nyilvános minta adathalmazon lett betanítva, azaz <b>~1000 darab agyi mri</b> felvétel alapján tanult, hatékonysága így <b>80%-os</b>. Produkciós azaz valódi orvosi diagnosztikára is alkamassá tehető magasabb számú oktatókép segítségével.</div>', unsafe_allow_html=True)
