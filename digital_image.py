import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Digital Image", layout="centered")

st.title("🖼️ Digital Image Viewer (Drawn Using NumPy)")

# Image dimensions
height = 200
width = 300

# Create black image
image = np.zeros((height, width, 3), dtype=np.uint8)

# Red rectangle
image[50:150, 50:150] = [255, 0, 0]

# Green rectangle
image[50:150, 160:260] = [0, 255, 0]

# Blue bottom stripe
image[180:200, :] = [0, 0, 255]

# Show image using matplotlib
fig, ax = plt.subplots()
ax.imshow(image)
ax.set_title("Digital Image")
ax.axis('off')

st.pyplot(fig)
