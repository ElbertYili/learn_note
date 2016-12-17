# [The Clean Architecture](http://blog.csdn.net/elinavampire/article/details/44745923)

- 原文链接:[The Clean Architecture](http://blog.8thlight.com/uncle-bob/2012/08/13/the-clean-architecture.html)


![20150330085022947](/Users/elbert/Documents/personal/learn/android/Pic/20150330085022947.jpg)

## 架构特点

1. 独立框架
2. 可测试
3. 独立于UI

## 依赖规则

- 同心圆代表不同区域，外圈是机制，内圈是策略。
- 源代码*只能*向内依赖。内圈不出现外圈的名字、数据格式

## 架构组成

### Entities

​	封装项目、企业层次内的业务规则。

​	一个Entity可以是一个对象的方法、一组数据结构。

​	当外部发生变化时，这些Entity不应该受影响

### Use Case

​	包含应用程序本身特定的业务规则

​	他封装并实现了所有的系统用例。

​	这些用例编排数据的流入和流出的实体,指示这些实体用它们项目业务规则到达用例的目标。

​	这一层即不应该影响到Entites，也不应该被外置层影响。

### Interface Adapters

​	 数据转换。使Use Case、entites和外层机构都能输入输出最合适的数据结构

​	Wholly contain the MVC architecture of a GUI。The Presenters, Views, and Controllers all belong in here

### Frameworks and Drivers

​	We keep these things on the outside where they can do little harm

### 不只是4个层

​	没有规定你必须使用这四个圆环

​	依赖规则始终适用,源代码始终向内依赖.越往圆圈内侧抽象水平越高,最外面的圆圈为低一级的具体细节.越往圆圈内侧抽象和封装的层次更高,最内侧圆层次最高,最普通.



