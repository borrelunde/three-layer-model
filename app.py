import matplotlib
from matplotlib import pyplot as plt

# The styles from SciencePlots are used even though PyCharm thinks otherwise.
# noinspection PyUnresolvedReferences
import scienceplots

import formulas
import matter

layer_one = matter.water_sea
layer_two = matter.steel
layer_three = matter.water_sea
layer_two_length = 0.1  # Layer two length in meters.

min_freq = 0  # Minimum frequency in Hertz.
max_freq = 75_000  # Maximum frequency in Hertz.

# Create data ranging from frequency min_freq to max_freq.
data = [formulas.intensity_transmission_coefficient(
    layer_one=layer_one,
    layer_two=layer_two,
    layer_three=layer_three,
    frequency=f,
    L=layer_two_length) for f in range(min_freq, max_freq)]

# Choose style, this configuration relies on SciencePlots.
plt.style.use(['science', 'notebook', 'grid'])

# Figure size in inches along the x-axis and the y-axis.
fig, axes = plt.subplots(figsize=(8, 4))

# Plot data on the axes.
axes.plot(data, label="Intensity transmission coefficient")

# Font used on the title, labels, etc.
font = 'Times New Roman'

# Set the title and axes labels.
axes.set_title(f'Three-layer model: {layer_one.name} - {layer_two.name} - {layer_three.name}', fontname=font)
axes.set_xlabel('Frequency [Hz]', fontname=font)
axes.set_ylabel('Intensity transmission coefficient [-]', fontname=font)

# Change the font of all ticks.
axes.tick_params(axis='both', which='both')
axes.tick_params(axis='both', which='minor')
for tick in axes.get_xticklabels():
    tick.set_fontname(fontname=font)
for tick in axes.get_yticklabels():
    tick.set_fontname(fontname=font)

# Comma as thousands separator.
axes.get_xaxis().set_major_formatter(
    matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

# Limit x-axis and y-axis.
axes.set_xlim(left=min_freq, right=max_freq)
axes.set_ylim(bottom=-0, top=1.05)

# Writing mathematical expressions in Python:
# https://matplotlib.org/stable/tutorials/text/mathtext.html
text = '\n'.join([
    fr'$\mathrm{{\rho_1 = {layer_one.density}\ kg/m^3}}$',
    fr'$\mathrm{{c_1 = {layer_one.velocity}\ m/s}}$',
    fr'$\mathrm{{\rho_2 = {layer_two.density}\ kg/m^3}}$',
    fr'$\mathrm{{c_2 = {layer_two.velocity}\ m/s}}$',
    fr'$\mathrm{{\rho_3 = {layer_three.density}\ kg/m^3}}$',
    fr'$\mathrm{{c_3 = {layer_three.velocity}\ m/s}}$',
    fr'$\mathrm{{L = {layer_two_length}\ m}}$'
])

# Apply the text.
axes.text(0.0375,
          0.925,
          text,
          transform=axes.transAxes,
          fontname=font,
          verticalalignment='top',
          bbox=dict(facecolor='white', edgecolor='black'))

# Save as figure.png in the figures directory.
plt.savefig('figures/figure.png', dpi=200, pad_inches=0.5)
