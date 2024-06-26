import numpy as np

'''
흥부부대찌개 신주쿠점의 흥행에 성공한 영훈이는 여세를 몰아 LA에도 가맹점을 하나 냈습니다.

이제 아버지께 매출을 보고하기 위한 프로세스가 조금 복잡해졌습니다. 각 지점의 매출을 원화로 변환시키고 더해야 하죠.
1엔에 10.08원, 1달러에 1138원이라고 가정하세요. 그리고 두 지점의 매출의 합이 원화로 담긴 numpy array를 만들어 출력해주세요.

반복문은 사용하면 안 됩니다!
'''

revenue_in_yen = [
    300000, 340000, 320000, 360000, 
    440000, 140000, 180000, 340000, 
    330000, 290000, 280000, 380000, 
    170000, 140000, 230000, 390000, 
    400000, 350000, 380000, 150000, 
    110000, 240000, 380000, 380000, 
    340000, 420000, 150000, 130000, 
    360000, 320000, 250000
]

revenue_in_dollar = [
    1200, 1600, 1400, 1300, 
    2100, 1400, 1500, 2100, 
    1500, 1500, 2300, 2100, 
    2800, 2600, 1700, 1400, 
    2100, 2300, 1600, 1800, 
    2200, 2400, 2100, 2800, 
    1900, 2100, 1800, 2200, 
    2100, 1600, 1800
]

# 여기에 코드를 작성하세요
yen_array = np.array(revenue_in_yen)
dollar_array = np.array(revenue_in_dollar)
won_array = yen_array*10.08 + dollar_array*1138
# 테스트 코드
won_array