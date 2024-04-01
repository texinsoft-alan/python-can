# SLCAN-CHANGELOG

## 20240401

* SLCAN :

  * 添加输入参数 data_bitrate ：用于指定数据域传输波特率，完善初始化指令下发，并间接判定 self.bitrate_switch = True ；

  * 添加输入参数 protocol ：用于明确通讯协议设定，并存放至 self._can_protocol ；

  * 记录 self.channel_info 便于外部读取；

  * 完善 _recv_internal 函数与 send 函数对 CANFD 帧的处理逻辑；

  * send 函数添加 数据填充 功能：当 dlc 大于 data 数组长度时，自动添加指定值对数组进行补全。

* 添加 ‘test_demo’ ‘test_isotp_demo’ 使用示例。

