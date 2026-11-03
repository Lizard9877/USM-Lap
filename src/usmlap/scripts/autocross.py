"""
This script simulates the autocross event.
"""

from usmlap.competition.events import Autocross
from usmlap.plot import plot_apexes, plot_gg, plot_ggv, plot_velocity_acceleration, plot_map
from usmlap.simulation import SimulationSettings
from usmlap.simulation.settings import QualityPresets
from usmlap.vehicle import Vehicle
from usmlap.track import Mesh

#autocross = Autocross(track_file="FS AutoX Germany 2012")
autocross = Autocross(track_file="FS Endurance Michigan 2014")

vehicle = Vehicle.from_json("WRE5")

simulation_settings = QualityPresets.FAST

solution = autocross.simulate_event(vehicle, simulation_settings)
plot_gg({'WRE5': solution})
plot_ggv({'WRE5': solution})
plot_apexes(solution)
plot_velocity_acceleration(solution)
