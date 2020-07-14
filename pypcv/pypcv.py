# This file is part of pypcv.
#
# pypcv is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pypcv is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pypcv.  If not, see <https://www.gnu.org/licenses/>.

__all__ = ["PyPCV"]

import usb.core
import usb.util


class PyPCV:
    """Python interface to Power Commander V.
    """

    idVendor = 0x10B6
    idProduct = 0x0502

    read_address = 0x81
    write_address = 0x01

    buffer_size = 64

    device = None

    def connect(self):
        """Connect to USB device.
        """

        self.device = usb.core.find(idVendor=self.idVendor, idProduct=self.idProduct)

        if self.device is None:
            raise RuntimeError(
                "Device not found. Make sure device is connected and try again."
            )

    def write(self, packet):
        """Write to device.

        Parameters
        ----------
        packet : `str`
            Packet to write to device.
        """

        if self.device is None:
            raise RuntimeError(
                "Devide not connected. Call `connect` before trying to write."
            )

        self.device.write(self.write_address, packet)

    def read(self):
        """Read from device.

        Returns
        -------
        packet : `str`
            Packet read from device.
        """

        if self.device is None:
            raise RuntimeError(
                "Devide not connected. Call `connect` before trying to read."
            )

        return self.device.read(self.read_address, size_or_buffer=self.buffer_size)
