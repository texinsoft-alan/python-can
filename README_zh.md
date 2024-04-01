# python-can - slcan

为 slcan 接口添加canable 2.0 工具支持。

English description please [click here](./README.md).

## [CHANGELOG](./SLCAN-CHANGELOG.md)

## slcan 语法参考

```
C\rS6\rO\r
C\rS6\rY2\rO\r
A0\rb123F11121314151617182122232425262728313233343536373841424344454647485152535455565758616263646566676871727374757677788182838485868788\r
V\r
```

## 同步

使用如下命令同步所有分支、标签：

```
git remote set-url origin https://github.com/hardbyte/python-can.git && \
git fetch --all && \
for b in `git branch -r | grep -v -- HEAD`; do git branch --track ${b##origin/} $b; done && \
git pull --all && \
git remote set-url origin https://github.com/texinsoft-alan/python-can.git && \
git push --all origin && \
git push --tags origin
```

## 相关仓库

[normaldotcom / canable-fw](https://github.com/normaldotcom/canable-fw)

[normaldotcom / canable2-fw](https://github.com/normaldotcom/canable2-fw)

[HubertD / cangaroo](https://github.com/HubertD/cangaroo)

## 链接

[SLCAN 和 CAN-FD - 跟进 ·问题 #410 ·linux-can/can-utils (github.com)](https://github.com/linux-can/can-utils/issues/410)

[发送超过 8 个字节时 CAN-FD 消息截断问题 ·问题 #1701 ·hardbyte/python-can (github.com)](https://github.com/hardbyte/python-can/issues/1701)

[CAN FD - 串口线？ ·问题 #1305 ·hardbyte/python-can (github.com)](https://github.com/hardbyte/python-can/issues/1305)
