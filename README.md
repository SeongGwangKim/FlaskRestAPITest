# FlaskRestAPI
<br>
![업로드된원본](https://user-images.githubusercontent.com/78336335/148682864-51b41514-cf92-42c0-9de6-286d3bb0be81.png)

<br>
1. json으로 이미지 파일의 이름을 보낸다.<br>
![json1](https://user-images.githubusercontent.com/78336335/148682855-9379f0c4-54a6-4de6-bdb7-ce5007c16ad1.png)
<br>
4. json으로 받은 이미지의 이름으로 s3에서 찾아 임시저장소에 다운로드한다.<br>
![업로드된원본](https://user-images.githubusercontent.com/78336335/148682864-51b41514-cf92-42c0-9de6-286d3bb0be81.png)
<br>
6. 임시 저장한 이미지를 변환한 후에 이미지를 잠시 로컬에 저장한다.<br>
7. 변환된 이미지를 s3에 업로드한다.<br>
![변환된이미지업로드](https://user-images.githubusercontent.com/78336335/148682861-22e23ae6-ccb9-41f4-92e4-55d39b6b07a3.png)
<br>
8. 업로드 후 변환된 이미지를 삭제한다.<br>
9. 변환된 이미지의 이름을 json으로 보낸다.<br>
![json2](https://user-images.githubusercontent.com/78336335/148682859-cf74e473-70f4-40b5-89e5-903cc11478cf.png)
<br>
# 결과
![변환전후](https://user-images.githubusercontent.com/78336335/148682862-9387c06b-b856-4e17-9858-53b57312252a.png)

