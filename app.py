import streamlit as st

st.set_page_config(page_title="Plant Matching Game", page_icon="🌿")

st.title("🌿 Plant Matching Game")
st.subheader("Can you match the plant names to their pictures?")

# Sample plant data
plants = [
    {
        "name": "Cactus",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Echinocactus_grusonii_01.jpg/220px-Echinocactus_grusonii_01.jpg",
        "options": ["Cactus", "Fern", "Rose"]
    },
    {
        "name": "Fern",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Nephrolepis_exaltata_02.jpg/220px-Nephrolepis_exaltata_02.jpg",
        "options": ["Basil", "Fern", "Sunflower"]
    },
    {
        "name": "Rose",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Rose_flower_in_garden.jpg/220px-Rose_flower_in_garden.jpg",
        "options": ["Tulip", "Rose", "Aloe Vera"]
    }
]

score = 0

for idx, plant in enumerate(plants):
    st.image(plant["image"], width=200)
    answer = st.radio(f"Which plant is this? 🌱 (Plant #{idx + 1})", plant["options"], key=idx)
    
    if answer == plant["name"]:
        st.success("✅ Correct!")
        score += 1
    else:
        st.error(f"❌ Oops! It's a {plant['name']}.")

st.markdown("---")
st.subheader(f"🌟 Final Score: {score} / {len(plants)}")

if score == len(plants):
    st.balloons()
    st.success("Perfect match! You're a plant expert! 🥇")
elif score >= 2:
    st.success("Great job! You're learning fast 🌼")
else:
    st.info("Keep trying! You'll get better with practice 🌱")

st.markdown("🌻 Tip: Try playing again to improve your score!")
