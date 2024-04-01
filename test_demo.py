#!/usr/bin/env python

"""
Tests for CANable 2.0 interfaces
"""
import can
import time

def test_main():
    print('wait init...')
    # this uses the default configuration (for example from the config file)
    # see https://python-can.readthedocs.io/en/stable/configuration.html
    # Using specific buses works similar:
    # bus = can.Bus(interface='socketcan', channel='vcan0', bitrate=250000)
    # bus = can.Bus(interface='pcan', channel='PCAN_USBBUS1', bitrate=500000)
    # bus = can.Bus(interface='ixxat', channel=0, bitrate=250000)
    # bus = can.Bus(interface='vector', app_name='CANalyzer', channel=0, bitrate=250000)
    # ...
    # bus1 = can.interface.Bus(bustype='slcan', channel='COM13', bitrate=500000, data_bitrate=2000000)
    bus1 = can.Bus(channel='COM13',
                    interface="slcan",
                    bitrate=500000,
                    data_bitrate=2000000,
                    protocol=can.CanProtocol.CAN_FD)
    # bus2 = can.Bus(channel='COM15', interface="slcan", bitrate=500000, data_bitrate=2000000)
    print('init succeed!')

    msg1 = can.Message(arbitration_id = 0x601,
                        data = [1, 25, 0, 1, 3, 1, 4, 1, 4, 1],
                        dlc = 48,
                        is_extended_id = False,
                        is_fd = True)
    msg2 = can.Message(arbitration_id = 0x602,
                        data = [1, 25, 0, 1, 3, 1, 4, 1, 4, 1],
                        dlc = 8,
                        is_extended_id = False,
                        is_fd = False)

    try:
        bus1.send(msg1)
        print("Message1 sent on {}".format(bus1.channel_info))
        time.sleep(0.2)
        bus1.send(msg2)
        print("Message2 sent on {}".format(bus1.channel_info))
    except can.CanError:
        print("Message NOT sent")

    # bus1.shutdown()

    for msg in bus1:
    # for msg in bus2:
        print(f"0x{msg.arbitration_id:X}: {msg.data.hex(' ')}, can_fd: {msg.is_fd} dlc: {msg.dlc}")

    bus1.shutdown()

if __name__ == "__main__":
    test_main()
