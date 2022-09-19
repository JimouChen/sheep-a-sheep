import os

# 以下参数根据自己的需要进行修改：
SYS_CONFIG = {
    # 参数 header_t 和 target_uid 二选一，建议使用header_t模式，若实在不会再使用target_uid模式，使用target_uid模式会耗时，建议获取一次后就替换成header_t模式，自行分辨
    # 说明:
    # 1、 header_t: 就是直接使用自己获取的t值，header_t优先级填写则为最高,
    # ios stream 抓取t值
    "header_t": 'xxx',
    # target_uid: 目标uid，就是你要闯关帐号的uid，若使用header_t模式请填0
    "target_uid": 0,
    # 获取到的header中的user-agent值
    "header_user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.28(0x18001c29) NetType/4G Language/zh_CN",
    # 设定的完成耗时，单位s，默认-1随机表示随机生成1s~1h之内的随机数，设置为正数则为固定
    "cost_time": -1,
    # 需要通关的次数，最大支持10，默认1
    "cycle_count": 2,
    # 闯关羊群开关: 1开启/0关闭 ，默认打开
    "sheep_type": 1,
    # 闯关话题开关: 1开启/0关闭 ，默认开启
    "topic_type": 1
}


def get(key: str):
    value = os.getenv(key)
    if value is None:
        if key in SYS_CONFIG:
            value = SYS_CONFIG[key]
    return value
