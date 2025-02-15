import json

from flask import make_response
from flask_restful import Resource,reqparse
import model.oracledb.image_model as imagedb
import base64
import werkzeug

import os
#파일 업로드
#https://flask-restful.readthedocs.io/en/latest/reqparse.html?highlight=add_argument#argument-locations

class Upload(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('uploads', location='form')
        # 아래는 공통 파라미터 설정(key=value로 받기)
    # post오버라이딩
    def get(self):
        try:
            args = self.parser.parse_args()
            print(args)
        except:
            return "실패"
    def post(self):
        args = self.parser.parse_args()
        image = args['uploads']
        try:
            num =0;
            if image != None and image != '':
                print('image,dase64', image)
                conn = imagedb.connectDatabase()
                data = imagedb.insert(conn)
                num = data[0]
                str1 = 'C:\\Users\\user\\Upload\\' + str(data[0]) + '.png'
                args['DIET_IMAGE'] = str(data[0])
                with open(str1, "bw") as f:
                    f.write(base64.b64decode(image.encode()))
            return num
            # # 파일업로드 관련 파라미터 추가
            # # 첫번째 인자 'uploads'는 파라미터명
            # # location='files' 디렉토리 경로가 아니다.파일 업로드인 경우 반드시 "files"
            # # <form action="http://파이션 Rest 서버 주소/uploads" method="post" enctype="multipart/form-data">
            # # <input type="file" name="uploads"/>
            # self.parser.add_argument('uploads',location='files',type=werkzeug.datastructures.FileStorage)
            # # 모든 파라미터 받기
            # args = self.parser.parse_args()
            # print(f'파일 업로드 args:{args}')#파일 업로드 args:{'title': '프로젝트 하기', 'name': '가길동', 'uploads': <FileStorage: 'AppleApp.jpg' ('image/jpeg')>}
            # file = args['uploads']#FileStorage객체
            # #FileStorage객체은 JSON으로 응답시 직렬화가 안된다
            # #TypeError: Object of type FileStorage is not JSON serializable
            # #즉 args의 'uploads'키의 값을 FileStorage에서 업로드한 파일명으로 변경하자
            # args['uploads']=file.filename
            # # 파일 업로드
            # file.save(os.path.join(self.upload_path,file.filename))
        except:
            return make_response(json.dumps({'failure':'최대 파일 업로드 용량 초과'},ensure_ascii=False),413)

        return make_response(json.dumps(args,ensure_ascii=False), 200)
