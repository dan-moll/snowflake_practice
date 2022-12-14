
import streamlit
import pandas

streamlit.title("Parents new healthy dinner")


streamlit.header('Breakfast Favorites')
streamlit.text('Omega 3 & Blueberry Oatmeal π₯£')
streamlit.text('Kale, Spinach & Rocket Smoothie π₯')
streamlit.text('Hard-Boiled Free-Range Egg π')
streamlit.text('Avocado Toastπ₯π')
streamlit.header('ππ₯­ Build Your Own Fruit Smoothie π₯π')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

# Let's put a pick list here so they can pick the fruit they want to include 


# Display the table on the page.

