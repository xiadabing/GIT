#1、记录的信息不全面，并没有把执行时间等相关信息执行出来，日志等级，日志详细信息
#2、文件信息混乱不清，不方便使用脚本统计
#3、当日志大的时候，没有自动进行日志轮转功能


#使用专业的日志器，可以解决以上问题
#使用做菜的例子进行类比学习

#1、菜 --》 日志信息
#装菜的容器（盘子、汤碗、饭盒、木桶） --》日志收集器（Logger），用来装日志器的

#2、装菜的容器对装菜种类的限制 --》类似于日志收集器的日志等级(NOTET(0)、DEBUG(10)
# INFO(20),WARNING(30),ERROR(40),CRITICAL(50))
#NOTET(0)  表示不限制类型，所有日志都接收
#DEBUG(10) 除了日志等级为NOTET(0)的不收集，其它的都收集
#INFO(20)  不能收集NOTET和DEBUG的日志，其余日志等级比它高的都可以收集
#日志等级比当前设置等级高的都可以收集，比它低的都不可以收集

#3、装好的菜，放置的地方(餐桌、茶几、凳子)  -->日志输出渠道(console终端、文件、smtp、http) (Handlers)

#4、放置菜的对方对菜种类的限制 --> 日志输出渠道的日志等级 日志等级比当前设置等级高的都可以输出，比它低的都不可以输出

#5、菜的摆盘方式 --> 日志显示格式(Formatter)


import logging  #python系统自带的

#1、定义日志收集器
#logging.root()  默认的root根收集器，使用日志等级为WARNING，只能输出等级大于warning的日志，不满足我们的需求，不推荐使用

#返回Logger对象
case_logger = logging.getLogger("case") #如果不传name参数，那么默认使用root根收集器

#2、指定日志收集器的日志等级
case_logger.setLevel(logging.DEBUG)

#3、定义日志输出渠道(可以指定多个渠道)
#输出到console控制台
console_handle = logging.StreamHandler()
#输出到文件中
file_handle = logging.FileHandler("case.log",encoding="utf-8")

#4、指定日志输出渠道的日志等级
#console_handle.setLevel(logging.ERROR)
console_handle.setLevel("ERROR")  #如果不能够被日志收集器收集的日志，一定没办法输出到渠道中
file_handle.setLevel(logging.INFO)

#5、定义日志显示的格式
#%(asctime)s  定义日志显示当前时间，系统固定写法
#%(levelname)s  日志等级名称
#%(message)s    日志信息
simple_formatter = logging.Formatter("%(asctime)s - [%(levelname)s] - [日志信息]:%(message)s") #简单的日志格式
verbose_formatter = logging.Formatter("%(asctime)s - [%(levelname)s] - %(module)s -%(name)s -%(lineno)d- [日志信息]:%(message)s") #复杂的日志格式

console_handle.setFormatter(simple_formatter) #设置终端的日志为简单格式
file_handle.setFormatter(verbose_formatter)   #设置终端的日志为复杂格式

#6、对接，将日志收集器与输出渠道进行对接
case_logger.addHandler(console_handle)
case_logger.addHandler(file_handle)


if __name__ == '__main__':
    case_logger.debug("这是debug日志")
    case_logger.info("这是nfo日志")
    case_logger.warning("这是warning日志")
    case_logger.error("这是error日志")
    case_logger.critical("这是critical日志")
