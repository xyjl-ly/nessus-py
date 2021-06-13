#!/bin/bash
echo '
第一次使用


toch README.md  //这个貌似必须有，我第一次因为这个上传出错
git init   // 初始化
git add.  // .代表添加文件夹下所有文件 
git commit -m "first commit"   // 把添加的文件提交到版本库，并填写提交备注
git remote add origin git@10.180.30.18:test/your_file_name.git //建立远程链接，git@10.180.30.18:test/your_file_name.git 为你的远程仓库地址，其中有两个链接，一个http，一个ssh，我自己用http链接上传失败，改用ssh就可以了。
git push -u origin master // 将代码上传
'

echo '
以后

git add.  // .代表添加文件夹下所有文件     
git commit -m "change ** file"   // 把添加的文件提交到版本库，并填写提交备注
git push -u origin master // 将代码上传
'

echo '
每次输入密码解决
	git config --global credential.helper store
	git pull

'
