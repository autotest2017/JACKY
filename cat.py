#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coder: JACKY
# version: 1.0

"""
1、函数与方法的区别？JAVA没有函数的概念
2、程序结束时，加上“；”可不可以，会不会对PYTHON业界书写的约定有什么不一样？会不会对编译的过程产生多余的负担？还是仅仅为了美观？
"""


def run(name, action):
    print "%s 正在 %s" % (name, action)

run("JACKY","EAT")

"""
为什么%s一定要在引号里
"""
# def run1(name, action):
#     print %s "正在" %s % (name, action)

##########################################################

class Cat:
    #PYTHON里初始化代表着直接给入场初始化，之所以加个self，是为了代表实例化后的对象自己，类比于JAVA的this，JAVA的方法入参可以不输入，但必须要用this来代表对象自己
    #__new__创建一个对象
    #__init__创建对象后，把对象初始化
    def  __init__(self,name):
        self.name = name
        print "this is init"

    def shout(self):
        #self参数是对象本身，实例化以后的对象调用的函数，这是对象方法
        print self.name + "miao"

    @classmethod
    #这是类方法
    #类方法的作用？？？
    #方法的第一个参数都是类对象，而不是实例对象？？？
    def classmethod(cls):
        print "this is classmethod"

    @staticmethod
    #这是静态方法，静态方法不能用self
    #要在类中使用静态方法，需在类成员函数前面加上@staticmethod标记符，以表示下面的成员函数是静态函数。使用静态方法的好处是，不需要定义实例即可使用这个方法。另外，多个实例共享此静态方法。
    #这是一个辅助函数，与类的关系不大，打印日志，输出一些信息
    def staticmethod():
        print "this is staticmethod"


cat1 = Cat("白猫")
cat2 = Cat("黑猫")

cat1.shout()
cat2.shout()
# Cat.shout()   #对象方法不能直接用类来调用

Cat.classmethod()
cat1.classmethod()

Cat.staticmethod()
cat1.staticmethod()

"""
直接调用类，则会构建一个对象
直接调用函数，则会调用函数里的具体实现
直接调用对象方法，则会调用方法里的具体实现
直接输入对象，则会输出该对象的物理地址  print 对象名
"""

"""
PYTHON中对象方法的定义与其他语言不一样，第一个参数一般都命名为self（相当于其他语言的this），用于传递对象本身，而在调用的时候则不必显性传递，系统会自动传递
"""