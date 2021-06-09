# Python-Android
Run python script on the top of Android application.

## Environment preparation
1. Install Android Studio
2. Install Python (3.6 or 3.7 or 3.8 or 3.9)

## Prepare source code
1. Generate a Python-based Android app with cookiecutter
```
$ python3 -m pip install --user cookiecutter
$ cookiecutter https://github.com/beeware/briefcase-android-gradle-template --checkout 3.8
You've downloaded C:\Users\name\.cookiecutters\briefcase-android-gradle-templat
e before. Is it okay to delete and re-download it? [yes]: yes
formal_name [App Name]: VRIT
app_name [vrit]:
module_name [vrit]:
bundle [com.example]:
package_name [com.example]:
splash_background_color [#FFFFFF]:
version [1.0]:
version_code [10000]:
```
2. Download Python Android Support zip (`Python-3.8-Android-support.b3.zip`)

[Python-Android-support](https://github.com/beeware/Python-Android-support)
```
https://briefcase-support.org/python?platform=android&version=3.8
```
Copy and paste under `Python-Android\app` directory
```
├───include
│   └───python3.8
│       ├───cpython
│       └───internal
├───libs
│   ├───arm64-v8a
│   ├───armeabi-v7a
│   ├───x86
│   └───x86_64
└───src
    └───main
        └───assets
            └───stdlib
```

3. Get source code of [beeware/rubicon-java](https://github.com/beeware/rubicon-java/tree/7fb59c7a21b68b5a863170981f5df784b20d14f9)
```
$ git clone https://github.com/beeware/rubicon-java.git
$ cd rubicon-java
$ cp rubicon ../app/src/main/assets/python/app_packages
```

Finally, open project via Android Studio and run project.
