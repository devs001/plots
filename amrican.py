from pygal.maps.world import World
import requests
WM=World()
WM.title='north America'
WM.add('dorth america',['ca','mx','us'])
WM.add('Central America',['bz','cr','gt','hn','ni','pa','sv'])
WM.add('South America',['ar','bo','br','cl','co','ec','gf','gf','gy','pe','py',
                        'sr','uy','ve'])
WM.render_to_file('america1.svg')