import streamlit as st

st.set_page_config(page_title="Excellence Coaching for Leaders", page_icon="🌟")

st.title("🌟 Excellence Coaching for Leaders")
st.subheader("Assess your leadership and set goals for growth")

st.markdown("### 🧭 Leadership Self-Assessment")

areas = {
    "Vision & Strategic Thinking": "I regularly communicate a clear vision and make strategic decisions.",
    "Communication": "I listen actively and communicate clearly with my team.",
    "Emotional Intelligence": "I manage my emotions and respond with empathy.",
    "Accountability": "I take ownership and hold others accountable with fairness.",
    "Adaptability": "I embrace change and guide others through it.",
    "Decision-Making": "I make timely, informed decisions even under pressure.",
    "Team Empowerment": "I support and empower others to grow and succeed.",
}

total_score = 0

for area, description in areas.items():
    st.markdown(f"**{area}**")
    st.caption(description)
    rating = st.slider(f"How strong are you in {area.lower()}?", 1, 10, 5, key=area)
    total_score += rating

st.markdown("---")
average_score = total_score / len(areas)
st.subheader(f"🧮 Your Leadership Score: **{average_score:.1f}/10**")

# Feedback
if average_score >= 8:
    st.success("Excellent leadership performance! Keep nurturing your strengths.")
elif average_score >= 6:
    st.info("Solid foundation. Identify areas for consistent growth.")
else:
    st.warning("Consider focused coaching in key areas to enhance your leadership impact.")

st.markdown("### 🎯 Set a Leadership Growth Goal")

goal = st.text_area("What is one leadership goal you'd like to focus on this month?")
if goal:
    st.success(f"🎯 Goal set: *{goal}*")

st.markdown("---")
st.markdown("💬 **Coaching Prompt:**")
st.write(
    "👉 *What would excellence in leadership look like for you in 3 months?* "
    "Describe it in 3 sentences."
)

reflection = st.text_area("Write your reflection here...")

st.markdown("---")
st.caption("Developed with 💡 for leaders aiming to grow with purpose.")
