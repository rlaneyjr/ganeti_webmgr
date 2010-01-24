from core.plugins.plugin import Plugin
from core.plugins.model_support import ModelView

from models import Closet, Device, Location, NetworkCard, Rack


class Devices(Plugin):
    description = 'Provides models and views for tracking.'
    objects = (
        Device,
        NetworkCard,
        #ModelView(Device)
    )


class Inventory(Plugin):
    description = 'Provides models and views for tracking inventory of a server room.'
    depends = Devices
    objects = (
        Location,
        Rack,
        #ModelView(Rack),
        Closet
    )