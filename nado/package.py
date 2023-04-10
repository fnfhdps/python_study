# import travel.thailand
# # import 맨 뒤는 모듈이나 패키지만 가능
# #import travel.thailand.ThailandPackage 사용 안됨
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

from travel import *
# # 그냥 쓰면 안되고 개발자가 원하는 공간을 설정 해야함
# # __init__파일에 __all__ list를 추가한다
# #trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()

import inspect
import random
print(inspect.getfile(random)) # 모듈의 경로를 알려줌
print(inspect.getfile(thailand))