from pygal.maps.world import World
wmap=World()

wmap.title='world with data'
wmap.add("north america",{'ca':10,'us':100121,'mx':123123424})
wmap.render_to_file('na_population_data_color_darkness1.svg')



