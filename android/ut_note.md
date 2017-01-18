# 单测

结合Android Studio与 JUnit进行单测。

此外可以集成 [Mockito](https://github.com/mockito/mockito) 在本地单元测试中测试 Android API 调用，以及集成 [Espresso](https://developer.android.com/topic/libraries/testing-support-library/index.html#Espresso) 或 [UI Automator](https://developer.android.com/topic/libraries/testing-support-library/index.html#UIAutomator) 在仪器测试中演练用户交互。

可以利用 [Espresso 测试记录器](https://developer.android.com/studio/test/espresso-test-recorder.html)自动生成 Espresso 测试

[官方介绍](https://developer.android.com/training/testing/start/index.html)

## 测试类型和位置

- 本地单元测试

  运行在本地JVM上面。

  只要用于测试工具集这类的类，或者完全Android环境不相关的业务代码。

  位于 `module-name/src/test/java/`

  这部分用JUnit进行，不能放在AndroidTest里

- **Instrumented tests**仪表测试

  运行在设备上。

  有权访问Instrumentation API

## Gradle配置

```
dependencies {
    // Required for local unit tests (JUnit 4 framework)
    testCompile 'junit:junit:4.12'

    // Required for instrumented tests
    androidTestCompile 'com.android.support:support-annotations:24.0.0'
    androidTestCompile 'com.android.support.test:runner:0.5'
}
```



## 测试方法

- 带返回值的函数

  直接使用Asset系列断言

- void类型函数

  使用Mock。

  mockIo框架



## 实施

### 本地

1. ![2764830419-56d8f325753c3](/Users/elbert/Documents/personal/learn/android/Pic/2764830419-56d8f325753c3.png)

   选择Create New Test

2. ![3657506268-56d8f34c260d8_articlex](/Users/elbert/Documents/personal/learn/android/Pic/3657506268-56d8f34c260d8_articlex.png)

   setUp/@Before：表示运行在所有单测case前的方法。可以用来初始化公共属性或其他统一操作等







## 备注

参考[测试的基础逻辑](http://chriszou.com/2016/04/13/android-unit-testing-start-from-what.html)

