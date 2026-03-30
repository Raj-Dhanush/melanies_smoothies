import requests

if ingredients_list:
    ingredients_string = ''

    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '

    # Insert logic (unchanged)
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients, name_on_order)
                        values ('""" + ingredients_string + """','""" + name_on_order + """')"""

    time_to_insert = st.button('Submit Order')

    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered, ' + name_on_order + '!', icon="✅")

    # 🔥 NEW PART (nutrition display)
    for fruit_chosen in ingredients_list:
        st.subheader(fruit_chosen + ' Nutrition Information')

        fruit_name = fruit_chosen.lower().rstrip('s')

        smoothiefroot_response = requests.get(
            "https://my.smoothiefroot.com/api/fruit/" + fruit_name
        )

        st.dataframe(
            data=smoothiefroot_response.json(),
            use_container_width=True
        )
