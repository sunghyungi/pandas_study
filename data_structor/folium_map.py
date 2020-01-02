import folium

seoul_map = folium.Map(location=[37.55, 126.98], zoom_start=12)

seoul_map.save('./seoul.html')


seoul_map2 = folium.Map(location=[37.55, 126.98], titles='Stamen Terrain', zoom_start=12)
seoul_map3 = folium.Map(location=[37.55, 126.98], titles='Stamen Toner', zoom_start=15)

seoul_map2.save('./seoul2.html')
seoul_map3.save('./seoul3.html')