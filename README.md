# python-can - slcan

Add canable 2.0 tool support to the slcan interface.

中文说明请[点击此处](./README_zh.md)。

## [CHANGELOG](./SLCAN-CHANGELOG.md)

## SLCAN Syntax Reference

```
C\rS6\rO\r
C\rS6\rY2\rO\r
A0\rb123F11121314151617182122232425262728313233343536373841424344454647485152535455565758616263646566676871727374757677788182838485868788\r
V\r
```

## Sync

Use the following command to synchronize all branches and labels:

```
git remote set-url origin https://github.com/hardbyte/python-can.git && \
git fetch --all && \
for b in `git branch -r | grep -v -- HEAD`; do git branch --track ${b##origin/} $b; done && \
git pull --all && \
git remote set-url origin https://github.com/texinsoft-alan/python-can.git && \
git push --all origin && \
git push --tags origin
```

## Related Repositories

[normaldotcom / canable-fw](https://github.com/normaldotcom/canable-fw)

[normaldotcom / canable2-fw](https://github.com/normaldotcom/canable2-fw)

[HubertD / cangaroo](https://github.com/HubertD/cangaroo)

## Related Links

[SLCAN and CAN-FD - Follow up · Issue #410 · linux-can/can-utils (github.com)](https://github.com/linux-can/can-utils/issues/410)

[CAN-FD Message Truncation Issue When Sending More Than 8 Bytes · Issue #1701 · hardbyte/python-can (github.com)](https://github.com/hardbyte/python-can/issues/1701)

[CAN FD - serial line? · Issue #1305 · hardbyte/python-can (github.com)](https://github.com/hardbyte/python-can/issues/1305)
