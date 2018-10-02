import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])


map = folium.Map(location=[28.58, -99.09], zoom_start = 6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name ="My Map")


def color_changer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


for lt, ln, el, nm in zip(lat, lon, elev, name):
    fg.add_child(folium.Marker(location=[lt, ln],
    popup=folium.Popup(str(el) + " m", parse_html=True),
    icon = folium.Icon(color = color_changer(el))))


map.add_child(fg)
map.save("Map1.html")
