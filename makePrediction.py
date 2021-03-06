

from modules.handleData.filterPrediction import filterPrediction
import sys
from modules.db.savePrediction import savePrediction
from modules.handleModel.makeModel import make
from modules.handleModel.predict import *


# initial_dataset.csv를 통해 훈련된 모델
model = make()


# - 결과 리스트: [ {age: 10, gender: 0, item: '1600', action: 0.22}, ... ]
predictResult = predictAction()





## 필터링
savingList = []
if len(sys.argv) > 1: # 필터 모드 파라미터가 있을 시 각 모드에 맞는 필터를 적용하여 저장
    filterMode = sys.argv[1] # item | user | top
    savingList = filterPrediction(filterMode, predictResult)
else: # 필터 모드 파라미터가 없을 시 확률 0.2 이하를 제외하고 저장
    savingList = filterPrediction('user', predictResult)
    

## DB에 저장
savePrediction(savingList)

## 예측 결과 출력

