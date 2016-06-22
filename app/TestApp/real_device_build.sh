APP_NAME="TestApp"

xcodebuild -target ${APP_NAME} -sdk iphoneos -configuration Debug CODE_SIGN_IDENTITY="iPhone Developer: 3435763748@qq.com (35Y3T43H87)"
xcrun -sdk iphoneos PackageApplication -v build/Debug-iphoneos/${APP_NAME}.app -o `pwd`/build/Debug-iphoneos/${APP_NAME}.ipa
