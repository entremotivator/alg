import streamlit as st

st.title("Holistic Health Checklist (ALG GIE Framework)")

st.markdown("Use this checklist to evaluate your current health and wellness balance.")

sections = {
    "A - Activity": [
        "I engage in physical activity at least 3 times per week.",
        "I maintain good posture during the day.",
        "I stretch or do mobility exercises regularly.",
        "I feel energized after movement."
    ],
    "L - Lifestyle": [
        "I get 7–8 hours of quality sleep each night.",
        "I have a consistent daily routine.",
        "I manage stress with healthy coping methods.",
        "I spend time in nature or outdoors weekly."
    ],
    "G - Gut Health": [
        "I eat a balanced diet with fruits, vegetables, and fiber.",
        "I have regular and comfortable digestion.",
        "I drink enough water throughout the day.",
        "I minimize processed foods and sugars."
    ],
    "GIE - General Internal & External Balance": [
        "I practice mindfulness, meditation, or reflection.",
        "My environment supports my well-being.",
        "I nurture healthy relationships.",
        "I feel emotionally balanced most days."
    ]
}

total_checked = 0
total_items = 0

for section, items in sections.items():
    st.subheader(section)
    for item in items:
        checked = st.checkbox(item, key=item)
        total_checked += int(checked)
        total_items += 1

st.markdown("---")
st.subheader("Your Summary")

percentage = (total_checked / total_items) * 100
st.write(f"You checked **{total_checked} out of {total_items}** items. ({percentage:.0f}%)")

if percentage >= 80:
    st.success("Excellent! You’re maintaining a great holistic balance.")
elif percentage >= 60:
    st.info("Good! But there are a few areas you might want to pay attention to.")
elif percentage >= 40:
    st.warning("Some important areas might need attention.")
else:
    st.error("It might be time to focus more on your overall health and habits.")

