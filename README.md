# Autowork
python3+selenium3自动化框架


<<<<<<< HEAD
环境介绍：
python3.6.1 版本
selenium3.4.1 版本
chrome61版本
chromedriver.exe  2.32版本
=======
环境介绍： 
>>>>>>> 02aa86c3a08bfa7d6899e011c4c3c8fcbc55c1ae

  python3.6.1 版本  
  selenium3.4.1 版本  
  chrome61版本 
  chromedriver.exe  2.32版本
  
一.环境安装  
环境安装请自行百度

二.框架执行介绍  
1.下载本框架完成后，需要在 src/xuliemail.py 中配置邮件（配置发件人，收件人，邮箱服务器）  
2.执行case时需要在 runcase/test_sina/test_Weibologin.py 中配置微博账户  
3.配置驱动文件到环境变量，如已设置忽略该步  

三.功能介绍  
1.该框架用最新的python，selenium，以及最新的chrome版本进行测试。方便大家了解版本特性，新手可以更快的上手  
2.测试报告模板美化（最初的测试报告生成比较low，这个是借鉴大神（Findyou）的。感谢大神对测试报告美化做出的贡献）  
3.上传文件更加方便，我在runlib里面放置了脚本文件（xulie3.au3）和上传工具（xulie3.exe）。方便大家在执行的时候可以更便捷的修改上传参数  
4.其他优化

四.框架介绍  
-driver 文件夹放置执行时浏览器的驱动文件夹（我这里用的是chrome，所以配置的是chromedriver.exe）  
-imgs   该文件夹为程序执行时出现错误的截图文件夹  
-log    改文件夹为程序执行时的log  
-page   用例模板  
- --sina  sina相关用例模板  
-report 放置程序生成的测试报告  
-runcase  
- --test_sina  sina用例执行模块  
-runlib  放置程序所执行时的一些执行库（HTMLTestRunner.py为测试报告生成模板，xulie3.au3为Autoit上传工具的脚本，可以根据这个修改上传文件参数                  xulie3.exe为上传文件工具，通过python调用该工具实现文件上传到浏览器）  
-src  程序执行服务文件夹（service简写，文件夹包括浏览器配置，邮件配置，log配置，测试报告生成配置，简化脚本程序）
