import gmplot 
import geocoder 
import test_data


def get_map():
    ipadress=geocoder.ip('me')
    #print(ipadress.latlng)
    lst = ipadress.latlng

    personal_lat =lst[0]
    personal_long = lst[-1]
    
    
    lat = [lst[0], 43.64589] 
    lang = [lst[-1], -79.75385]


    gmapOne = gmplot.GoogleMapPlotter(43.64608, -79.75399, 15)


    gmapOne.scatter(lat, lang, '#ff000', size=50, marker=False)
    gmapOne.plot(lat,lang,'blue', edge_width=2.5)
    gmapOne.draw("map.html")



test = get_map()


