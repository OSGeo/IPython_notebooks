ax = protected_areas_utm.plot(figsize=(10, 10), color='green')
data_utm.plot(ax=ax, markersize=5, alpha=0.5, column='mineral1', legend=True)
ax.set_axis_off()