APP_NAME="TestApp"

# xcodebuild -project HelloWorld.xcodeproj -target ${APP_NAME} -sdk iphoneos -configuration Debug CODE_SIGN_IDENTITY="iPhone Developer: 金花 陈 (WYM2ZZDM2X)"
xcodebuild -target ${APP_NAME} -sdk iphoneos -configuration Debug CODE_SIGN_IDENTITY="iPhone Developer: 金花 陈 (WYM2ZZDM2X)"

xcrun -sdk iphoneos PackageApplication -v build/Debug-iphoneos/${APP_NAME}.app -o 'pwd'/build/Debug-iphoneos/${APP_NAME}.ipa

