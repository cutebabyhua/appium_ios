var target = UIATarget.localTarget();
target.setDeviceOrientation(UIA_DEVICE_ORIENTATION_PORTRAIT);

UIALogger.logStart("用例开始")

var mWindow = target.frontMostApp().mainWindow();
var keyboard = target.frontMostApp().keyboard();

mWindow.textFields()["IntegerA"].tap();
target.delay(3);
keyboard.typeString("7");
target.delay(3);
mWindow.textFields()["TextField2"].textFields()["IntegerB"].tap();
target.delay(3);
keyboard.typeString("8");
target.delay(3);
mWindow.buttons()["ComputeSumButton"].staticTexts()["求和"].tap();

var answer = mWindow.staticTexts()["Answer"];

if (answer.value() == "15"){
	UIALogger.logPass("加法运算测试通过");
}
else {
	UIALogger.logFail("加法运算测试失败");
}
