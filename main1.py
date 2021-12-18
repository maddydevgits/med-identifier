import streamlit as st
from PIL import Image
import cv2 
import pytesseract
import pyttsx3
engine = pyttsx3.init()
# Adding custom options
k=['Vitam-5G','FERROUS','SERRATIOPEPTIDASE','NEURO','CELIN','Lifestar','beshine','THIOTRES','Mohan']
custom_config = r'--oem 3 --psm 6'
found=None
def load_image(image_file):
    im = Image.open(image_file)
    return im

def main():
    st.title("Med Identifier")
    menu = ["Image"]
    choice = st.sidebar.selectbox("Menu",menu)
    if choice == "Image":
        st.subheader("Image")
        image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])
        if image_file is not None:
            # To See details
            file_details = {"filename":image_file.name, "filetype":image_file.type,
                              "filesize":image_file.size}
            st.write(file_details)
            # To View Uploaded Image
            st.image(load_image(image_file),width=250)
            img=cv2.imread(image_file.name)
            a=(pytesseract.image_to_string(img, config=custom_config))
            #print(a)
            found=-1
            for i in range(len(k)):
                try:
                    print(a.index(k[i]))
                    found=i
                    print(found)
                    pass
                except:
                    pass
            st.text("Expected Result")
            if(found==0):
                st.text("Medicine Identified: Vitam-5G ")
                st.text("It cures: Strength")
                engine.say("Medicine Identified as Vitam-5G, It cures: Strength")
                engine.runAndWait()
            elif(found==1):
                st.text("Medicine Identified: Ferrous Sulphide")
                st.text("It cures: Anemia")
            elif(found==2):
                st.text("Medicine Identified: Serratiopeptisdose")
                st.text("It cures: Muscles Pain")
            elif(found==3):
                st.text("Medicine Identified: Neuro Care")
                st.text("It cures: Pathetic Pain")
            elif(found==4):
                st.text("Medicine Identified: Koye Celin")
                st.text("It cures: Red Blood Cells Increase")
            elif(found==5):
                st.text("Medicine Identified: Zinc")
                st.text("It cures: Immune")
            elif(found==6):
                st.text("Medicine Identified: Berberine Hydrochloride")
                st.text("It cures: Bacterial Infection for Eye")
            elif(found==7):
                st.text("Medicine Identified: L-Glutathione")
                st.text("It cures: Skin Tone Improver")
            elif(found==8):
                st.text("Medicine Identified: Teneligliptin")
                st.text("It cures: High Blood Sugar Levels")




if (__name__=="__main__"):
    main()