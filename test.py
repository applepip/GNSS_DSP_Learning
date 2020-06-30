import matplotlib.pyplot as plt
from astroplan.plots import plot_sky
from astroplan import FixedTarget
from astroplan import Observer
import numpy as np
from astropy.time import Time
import astropy.units as u
from astropy.coordinates import SkyCoord

subaru = Observer.at_site('subaru')
altair = FixedTarget.from_name('Altair')
vega = FixedTarget.from_name('Vega')

altair_style = {'color': 'r'}
deneb_style = {'color': 'g'}
time = Time('2015-06-16 12:00:00')

coordinates = SkyCoord('20h41m25.9s', '+45d16m49.3s', frame='icrs')
deneb = FixedTarget(name='Deneb', coord=coordinates)

altair_rise = subaru.target_rise_time(time, altair) + 5*u.minute
altair_set = subaru.target_set_time(time, altair) - 5*u.minute

vega_rise = subaru.target_rise_time(time, vega) + 5*u.minute
vega_set = subaru.target_set_time(time, vega) - 5*u.minute

deneb_rise = subaru.target_rise_time(time, deneb) + 5*u.minute
deneb_set = subaru.target_set_time(time, deneb) - 5*u.minute

sunset_tonight = subaru.sun_set_time(time, which='nearest')
all_up_start = np.max([altair_rise, vega_rise, deneb_rise])
start = np.max([sunset_tonight, all_up_start])

plot_sky(altair, subaru, start, style_kwargs=altair_style)
plot_sky(vega, subaru, start)
plot_sky(deneb, subaru, start, style_kwargs=deneb_style)

plt.legend(loc='center left', bbox_to_anchor=(1.25, 0.5))
plt.show()