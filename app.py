import streamlit as st

st.markdown("""
    <style>
    body {
        background: linear-gradient(to bottom right, #F6F94D, #FFFFFF);
    }
    .stApp {
        background: linear-gradient(to bottom right, #F6F94D, #FFFFFF);
    }
    </style>
""", unsafe_allow_html=True)


from yelp_api import search_restaurants
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


st.markdown("<h1 style='text-align: center;'>YelpMate</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Restaurant Recommender</h4>", unsafe_allow_html=True)

city = st.text_input("Enter a city:")
food_type = st.text_input("What kind of food do you want? (e.g. sushi, pizza)")
price_level = st.selectbox("Select price level:", ["Cheap ($)", "Moderate ($$)", "Expensive ($$$)", "Very Expensive ($$$$)"])

price_map = {
    "Cheap ($)": "1",
    "Moderate ($$)": "2",
    "Expensive ($$$)": "3",
    "Very Expensive ($$$$)": "4"
}

if st.button("Find Restaurants"):
    if city and food_type:
        st.write(" Searching for", food_type, "in", city)
        try:
            results = search_restaurants(city, food_type, price=price_map[price_level])
            if results:
                for r in results:
                    st.markdown("----")  
                    st.image(r["image_url"], width=350)

                    st.markdown(f"### [{r['name']}]({r['url']})")
                    st.write(f"⭐ {r['rating']}  |  📍 {r['location']['address1']}, {r['location']['city']}")
   
                    summary = f"{r['name']} is a {r['categories'][0]['title'].lower()} restaurant in {r['location']['city']}. It has a rating of {r['rating']} stars based on {r['review_count']} reviews."
                    st.write(summary)

                    st.write("📞", r.get("display_phone", "No phone listed"))
            else:
                st.warning("No results found.")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter both city and food type.")



