import streamlit as st
import pandas as pd

# Load product data
@st.cache_data
def load_data():
    return pd.DataFrame([
        {"Product Name": "Luxury Lipstick", "Price": "$25", "Description": "Matte finish with long-lasting effect.", 
         "Image URL": "https://i.imgur.com/I0aVkiW.jpg", "Category": "Makeup", 
         "WhatsApp Link": "https://wa.me/p/1234567890123456/94784727313"},
        
        {"Product Name": "Hydrating Face Cream", "Price": "$40", "Description": "Moisturizing cream with natural extracts.", 
         "Image URL": "photos/Photoroom-20241128_235342.jpg", "Category": "Skincare",
         "WhatsApp Link": "https://wa.me/p/8827644900615978/94784727313"},
        
        {"Product Name": "Eyeliner Pen", "Price": "$15", "Description": "Waterproof and smudge-proof eyeliner.", 
         "Image URL": "https://i.imgur.com/2nQbhwm.jpg", "Category": "Makeup",
         "WhatsApp Link": "https://wa.me/p/3456789012345678/94784727313"},
        
        {"Product Name": "Luxury Perfume", "Price": "$80", "Description": "Elegant fragrance with floral notes.", 
         "Image URL": "https://i.imgur.com/tp7W6Qj.jpg", "Category": "Fragrance",
         "WhatsApp Link": "https://wa.me/p/4567890123456789/94784727313"},
        
        {"Product Name": "Silky Hair Serum", "Price": "$30", "Description": "Repairs damaged hair and adds shine.", 
         "Image URL": "https://i.imgur.com/TtfU8wG.jpg", "Category": "Haircare",
         "WhatsApp Link": "https://wa.me/p/5678901234567890/94784727313"},
        
        {"Product Name": "BB Cream", "Price": "$35", "Description": "All-in-one skin foundation and moisturizer.", 
         "Image URL": "photos/Photoroom-20241128_032528.jpg", "Category": "Makeup",
         "WhatsApp Link": "https://wa.me/p/6789012345678901/94784727313"},
    ])

data = load_data()

# --- Page Setup ---
st.set_page_config(page_title="Trendy Product Catalog", page_icon="🛍️", layout="wide")

# --- Sidebar ---
st.sidebar.image("https://i.imgur.com/k1yUoEX.png", width=250)  # Placeholder Logo
st.sidebar.title("📞 Contact Us")
st.sidebar.write("📱 **WhatsApp:** +94XXXXXXXXX")
st.sidebar.write("📧 **Email:** shop4me@gmail.com")
st.sidebar.write("🌍 **Follow us:** [Instagram](https://instagram.com) | [Facebook](https://facebook.com)")

# --- Search & Filter ---
st.title("🛍️ Trending Product Catalog")
category_filter = st.sidebar.selectbox("🎯 Filter by Category:", ["All"] + list(data["Category"].unique()))
search_query = st.sidebar.text_input("🔎 Search Products...")

# Filter logic
filtered_data = data
if category_filter != "All":
    filtered_data = filtered_data[filtered_data["Category"] == category_filter]
if search_query:
    filtered_data = filtered_data[filtered_data["Product Name"].str.contains(search_query, case=False, na=False)]

# --- Display Products ---
st.markdown("### ✨ Featured Products ✨")
cols = st.columns(3)  # Creates 3-column layout

for index, row in filtered_data.iterrows():
    with cols[index % 3]:  # Arranges items in a grid
        st.image(row["Image URL"], width=200)
        st.subheader(row["Product Name"])
        st.write(f"💰 **Price:** {row['Price']}")
        st.write(f"📌 {row['Description']}")

        # Dynamic WhatsApp Order Link
        whatsapp_link = row["WhatsApp Link"]
        st.markdown(f'<a href="{whatsapp_link}" target="_blank"><button style="background-color:#25D366;color:white;padding:10px;border-radius:5px;border:none;">🛒 Order Now</button></a>', unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.markdown("💖 **Thank you for visiting our catalog!** Stay tuned for exciting offers.")
