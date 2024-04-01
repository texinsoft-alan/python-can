#!/usr/bin/env python

"""
Tests for CANable 2.0 interfaces
"""
# In this example, we transmit a payload using a blocking send()
import isotp
# import logging
import time

from can.interfaces.slcan import slcanBus, CanProtocol

# def my_error_handler(error):
#     # Called from a different thread, needs to be thread safe
#     logging.warning('IsoTp error happened : %s - %s' % (error.__class__.__name__, str(error)))


def test_tp_main(stack_params):
    print('wait init...')
    bus = slcanBus(channel='COM13',
                    interface="slcan",
                    bitrate=500000,
                    data_bitrate=2000000,
                    protocol=CanProtocol.CAN_FD)
    print('init succeed!')
    addr = isotp.Address(isotp.AddressingMode.Normal_11bits, rxid=0x718, txid=0x708)
    addr2 = isotp.Address(isotp.AddressingMode.Normal_11bits, rxid=0x708, txid=0x718)

    # stack = isotp.CanStack(bus, address=addr, error_handler=my_error_handler, params={"tx_padding":0})
    stack = isotp.CanStack(bus, address=addr, params={"tx_padding":0xCC})

    senddata = [0x10, 0x03]
    print("test begin...")
    stack.send(senddata)    # Non-blocking send, does not raise exception.

    while stack.transmitting():
        # time.sleep(0.005)
        time.sleep(stack.sleep_time())
        stack.process()
    print("Payload transmission done.")

    rec = None
    # while(rec == None):
    stack.process()
    rec = stack.recv()
    try:
        print(rec.hex(' '))
    except Exception as e:
        print(repr(e))

    bus.shutdown()

if __name__ == "__main__":
    STACK_PARAMS = {
        'stmin': 2,
        'blocksize': 8,
        'override_receiver_stmin': None,
        'rx_flowcontrol_timeout': 1000,
        'rx_consecutive_frame_timeout': 1000,
        'wftmax': 0,
        'tx_data_length': 8,
        'tx_padding': None,
        'rx_flowcontrol_timeout': 1000,
        'rx_consecutive_frame_timeout': 1000,
        'can_fd': False,
        'max_frame_size': 65536,
        'bitrate_switch': False,
        'rate_limit_enable': False,
        'listen_mode': False,
        'blocking_send': False
    }
    test_tp_main(STACK_PARAMS)
