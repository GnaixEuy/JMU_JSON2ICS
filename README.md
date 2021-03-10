# 官方已修复问题，本临时解决方案项目结束，当然如果你无聊想折腾看看也是可以>_<
<hr>
~~通过python手工导入集美大学/诚毅学院JSON转换成ICS文件导入日历软件中~~
~~### 手动解析课程表导入日历~~

~~访问--------------来获取修改后的python脚本（该脚本原先为自动输入获取版本由LGiki编写与GitHub上开源，由于学校网络安全规划导致脚本失效本次将其修改为我们直接提供json的版本）注意使用pip安装requirement.txt中的依赖（终端输入 pip install -r requirement.txt）~~

~~使用电脑通过webvpn访问课程表应用（以openjmu提供方法即可访问）打开导入界面，目前可见问题是一直在加载第一天选择界面，打开你浏览器的检查器，chrome按F12，接下来以Safari为例~~
![1](/READEME.assets/1.png)

~~，点击开发启动检查器，我们可以看到其中有几个错误~~

![2](/READEME.assets/2.png)，应该是某个东西无法通过webvpn来访问（不管了反正我只是要个json文件而已），里面报错的一个刚好点进去就是json文件，记录了你的课程信息

![3](/READEME.assets/3.png)

~~，复制他的内容到一个文本里备用（记得删除图中所圈的这些文字，并且由于体育课是不显示场地允许到null的时候会报错，所以我们把null改为例如“篮球场”），打开python脚本，将你修改后json填入yourjson后面~~

![4](/READEME.assets/clip_image004.png)

~~，通过终端运行脚本，即可得到ics文件，手机或有日历软件的设备打开ics文件即可导入日历~~

![5](/READEME.assets/clip_image005.png)

 
