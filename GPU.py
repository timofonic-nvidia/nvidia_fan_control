"""
GPU class module
"""

class GPU(object):

    """
    A graphic processing unit (GPU) class

    Attributes:
        slot (int): GPU's slot.
        model (str): GPU's model/name.

    """

    def __init__(self, slot, model):

        """
        Creates a GPU object

        Args:
            slot (int): GPU's slot on system.
            model (str): GPU's name/model.
        """

        self.slot = slot
        self.model = model

    @property
    def fanspeed(self):
        """GPU fan speed in percentage"""

        return self.fanspeed

    @fanspeed.setter
    def fanspeed(self, speed):
        self.fanspeed = speed

    @property
    def temperature(self):
        """GPU's core temperature in Celcius"""

        return self.temperature

    @temperature.setter
    def temperatue(self, temperature):
        self.temperatue = temperature

    def __str__(self):
        """ String representation of the class"""

        summary = "Slot: %d Model: %s " % (self.slot, self.model)

        return summary
