# -*- coding: utf-8 -*-
"""BigData-Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wzA69UpyRVHiiRxgoF9hNWdYD1nTiw88
"""

# 단계 1: 폰트 설치
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm

!apt-get -qq -y install fonts-nanum > /dev/null


# 단계 2: 런타임 재시작
import os
os.kill(os.getpid(), 9)

# 마이너스 표시 문제
mpl.rcParams['axes.unicode_minus'] = False

# 한글 폰트 설정
fe = fm.FontEntry(
    fname=r'/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf', # ttf 파일이 저장되어 있는 경로
    name='NanumGothic')                        # 이 폰트의 원하는 이름 설정
fm.fontManager.ttflist.insert(0, fe)              # Matplotlib에 폰트 추가
plt.rcParams.update({'font.size': 18, 'font.family': 'NanumGothic'}) # 폰트 설정

<<<<<<< HEAD
=======
# 필요한 라이브러리 임포트
>>>>>>> 1d5c6fb (code update)
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import seaborn as sns
import matplotlib.pyplot as plt

<<<<<<< HEAD

# 데이터를 DataFrame으로 읽기
df = pd.read_excel('/content/시군별_논벼_생산량.xlsx')

# 첫 두 행을 확인하여 올바른 데이터 구조 파악
print("Initial columns:", df.columns.tolist())
print("First row:", df.iloc[0].tolist())

# 실제 데이터 구조에 맞게 처리
# 두 번째 행을 새로운 열 이름으로 사용
new_columns = []
for col in df.iloc[1]:
    if pd.isna(col):
        new_columns.append('temp')  # 임시 이름 부여
    else:
        new_columns.append(str(col))
df.columns = new_columns

# 첫 두 행 제거 (이미 열 이름으로 사용했으므로)
df = df.iloc[2:].reset_index(drop=True)

# 빈 리스트 생성
processed_data = []

# 각 행정구역별로 데이터 처리
for idx, row in df.iterrows():
    region = row.iloc[0]  # 첫 번째 열이 행정구역

    # 열 이름을 순회하면서 데이터 추출
    for i in range(0, len(row)-1, 2):  # 2칸씩 건너뛰며 처리
        if i+1 < len(row):  # 인덱스 범위 확인
            year = 2008 + (i//2)  # 연도 계산
            area = row.iloc[i]
            production = row.iloc[i+1]

            # 데이터 추가 (문자열 '-' 처리 포함)
            try:
                area_value = float(area) if pd.notnull(area) and str(area) != '-' else 0
                production_value = float(production) if pd.notnull(production) and str(production) != '-' else 0

                processed_data.append({
                    '행정구역': region,
=======
def process_rice_data(file_path, target_regions=None, output_path=None):
    """
    쌀 생산량 데이터를 한번에 처리하는 통합 함수

    Args:
        file_path (str): 쌀 생산량 엑셀 파일 경로
        target_regions (list): 필터링할 지역 리스트 (None이면 전체 지역)
        output_path (str): 결과를 저장할 파일 경로 (None이면 저장하지 않음)
    Returns:
        pd.DataFrame: 처리된 쌀 생산량 데이터프레임
    """
    # 원본 데이터 읽기
    raw_data = pd.read_excel(file_path)

    # 첫 번째 행에서 연도 정보 추출
    years = [int(col) for col in raw_data.columns[1:] if str(col).isdigit()]
    unique_years = sorted(list(set(years)))  # 중복 제거하고 정렬

    # 두 번째 행의 컬럼 정보 가져오기 (재배면적/생산량 구분)
    column_info = raw_data.iloc[1]

    # 데이터 재구조화를 위한 리스트
    restructured_data = []

    # 실제 데이터는 3번째 행부터 시작
    for idx, row in raw_data.iloc[2:].iterrows():
        region_name = row.iloc[0]  # 지역명

        # 각 연도별로 데이터 추출
        for i, year in enumerate(unique_years):
            area_idx = i * 2 + 1  # 재배면적 열 인덱스
            prod_idx = i * 2 + 2  # 생산량 열 인덱스

            try:
                area = row.iloc[area_idx]
                production = row.iloc[prod_idx]

                # 결측치와 '-' 처리
                area_value = float(area) if pd.notnull(area) and str(area) != '-' else 0
                production_value = float(production) if pd.notnull(production) and str(production) != '-' else 0

                restructured_data.append({
                    '행정구역': region_name,
>>>>>>> 1d5c6fb (code update)
                    '연도': year,
                    '재배면적(ha)': area_value,
                    '생산량(톤)': production_value
                })
            except ValueError:
<<<<<<< HEAD
                continue  # 숫자로 변환할 수 없는 경우 건너뛰기

# 새로운 DataFrame 생성
result_df = pd.DataFrame(processed_data)

# 데이터 정렬
result_df = result_df.sort_values(['행정구역', '연도']).reset_index(drop=True)

# 엑셀로 저장
result_df.to_excel('processed_rice_production.xlsx', index=False)

df1 = pd.read_excel('/content/processed_rice_production.xlsx')
print(df1.head(20))

# 데이터를 DataFrame으로 읽기
df2 = pd.read_csv('/content/연간기후전체지역.csv', encoding='euc-kr')
print(df2.head(20))
# 데이터를 DataFrame으로 읽기
df3 = pd.read_csv('/content/월별기후전체지역.csv', encoding='euc-kr')
print(df3.head(20))

##processed_rice_production 데이터에서 지역 필터링##

import pandas as pd

# 데이터 읽기
df = pd.read_excel('/content/processed_rice_production.xlsx')

# 원하는 지역 필터링
target_regions = ['전라남도', '충청남도', '전라북도', '경상북도']
filtered_df = df[df['행정구역'].isin(target_regions)]

# 결과 저장
filtered_df.to_excel('filtered_rice_production.xlsx', index=False)

# 결과 확인
print(filtered_df)

##연간기후전체 지역 필터링 코드##

# 데이터 불러오기
import pandas as pd

# 각 도시별 행정구역 정보를 담은 딕셔너리 생성
region_dict = {
    # 전라남도
    '목포': '전라남도', '여수': '전라남도', '순천': '전라남도',
    '완도': '전라남도', '진도(첨찰산)': '전라남도', '진도군': '전라남도',
    '해남': '전라남도', '고흥': '전라남도', '광양시': '전라남도',
    '보성군': '전라남도', '강진군': '전라남도', '장흥': '전라남도',

    # 충청남도
    '서산': '충청남도', '천안': '충청남도', '보령': '충청남도',
    '부여': '충청남도', '홍성': '충청남도',

    # 전라북도
    '전주': '전라북도', '군산': '전라북도', '부안': '전라북도',
    '임실': '전라북도', '정읍': '전라북도', '남원': '전라북도',
    '장수': '전라북도', '고창군': '전라북도', '순창군': '전라북도',

    # 경상북도
    '포항': '경상북도', '안동': '경상북도', '상주': '경상북도',
    '울진': '경상북도', '봉화': '경상북도', '영주': '경상북도',
    '문경': '경상북도', '청송군': '경상북도', '영덕': '경상북도',
    '의성': '경상북도', '구미': '경상북도', '영천': '경상북도',
    '경주시': '경상북도'
}

# 지역 정보 추가
df2['행정구역'] = df2['지점명'].map(region_dict)

# 원하는 지역만 필터링
target_regions = ['전라남도', '충청남도', '전라북도', '경상북도']
filtered_df = df2[df2['행정구역'].isin(target_regions)]

# 결과 출력
print(filtered_df.head())

# 필터링된 데이터 확인
print("\n각 도별 도시 수:")
print(filtered_df['행정구역'].value_counts())

##월별기후전체 지역 필터링 코드##

# 데이터 불러오기
import pandas as pd

# 각 도시별 행정구역 정보를 담은 딕셔너리 생성
region_dict = {
    # 전라남도
    '목포': '전라남도', '여수': '전라남도', '순천': '전라남도',
    '완도': '전라남도', '진도(첨찰산)': '전라남도', '진도군': '전라남도',
    '해남': '전라남도', '고흥': '전라남도', '광양시': '전라남도',
    '보성군': '전라남도', '강진군': '전라남도', '장흥': '전라남도',

    # 충청남도
    '서산': '충청남도', '천안': '충청남도', '보령': '충청남도',
    '부여': '충청남도', '홍성': '충청남도',

    # 전라북도
    '전주': '전라북도', '군산': '전라북도', '부안': '전라북도',
    '임실': '전라북도', '정읍': '전라북도', '남원': '전라북도',
    '장수': '전라북도', '고창군': '전라북도', '순창군': '전라북도',

    # 경상북도
    '포항': '경상북도', '안동': '경상북도', '상주': '경상북도',
    '울진': '경상북도', '봉화': '경상북도', '영주': '경상북도',
    '문경': '경상북도', '청송군': '경상북도', '영덕': '경상북도',
    '의성': '경상북도', '구미': '경상북도', '영천': '경상북도',
    '경주시': '경상북도'
}

# 지역 정보 추가
df2['행정구역'] = df2['지점명'].map(region_dict)
df3['행정구역'] = df3['지점명'].map(region_dict)

# 원하는 지역만 필터링
target_regions = ['전라남도', '충청남도', '전라북도', '경상북도']
filtered_df = df2[df2['행정구역'].isin(target_regions)]
filtered_df_monthly = df3[df3['행정구역'].isin(target_regions)]

# 결과 출력
print(filtered_df.head())

# 필터링된 데이터 확인
print("\n각 도별 도시 수:")
print(filtered_df['행정구역'].value_counts())

# 필터링된 데이터를 CSV 파일로 저장
filtered_df.to_csv('filtered_climate_data.csv', index=False, encoding='utf-8-sig')
filtered_df_monthly.to_csv('filtered_climate_monthly_data.csv', index=False, encoding='utf-8-sig')

print("파일이 성공적으로 저장되었습니다.")
=======
                continue
            except IndexError:
                continue

    # 데이터프레임 생성 및 정렬
    processed_df = pd.DataFrame(restructured_data)
    processed_df = processed_df.sort_values(['행정구역', '연도']).reset_index(drop=True)

    # 특정 지역 필터링
    if target_regions:
        processed_df = processed_df[processed_df['행정구역'].isin(target_regions)]

    # 결과 저장
    if output_path:
        processed_df.to_excel(output_path, index=False)
        print(f"데이터가 {output_path}에 저장되었습니다.")

    return processed_df

def filter_climate_data(annual_climate_path, monthly_climate_path):
    """
    연간 및 월별 기후 데이터를 필터링하는 함수

    Args:
        annual_climate_path (str): 연간 기후 데이터 CSV 파일 경로
        monthly_climate_path (str): 월별 기후 데이터 CSV 파일 경로
    Returns:
        tuple: (필터링된 연간 기후 데이터, 필터링된 월별 기후 데이터)
    """
    # 지역별 행정구역 매핑 정보
    region_mapping = {
        # 전라남도 지역
        '목포': '전라남도', '여수': '전라남도', '순천': '전라남도',
        '완도': '전라남도', '진도(첨찰산)': '전라남도', '진도군': '전라남도',
        '해남': '전라남도', '고흥': '전라남도', '광양시': '전라남도',
        '보성군': '전라남도', '강진군': '전라남도', '장흥': '전라남도',

        # 충청남도 지역
        '서산': '충청남도', '천안': '충청남도', '보령': '충청남도',
        '부여': '충청남도', '홍성': '충청남도',

        # 전라북도 지역
        '전주': '전라북도', '군산': '전라북도', '부안': '전라북도',
        '임실': '전라북도', '정읍': '전라북도', '남원': '전라북도',
        '장수': '전라북도', '고창군': '전라북도', '순창군': '전라북도',

        # 경상북도 지역
        '포항': '경상북도', '안동': '경상북도', '상주': '경상북도',
        '울진': '경상북도', '봉화': '경상북도', '영주': '경상북도',
        '문경': '경상북도', '청송군': '경상북도', '영덕': '경상북도',
        '의성': '경상북도', '구미': '경상북도', '영천': '경상북도',
        '경주시': '경상북도'
    }

    # 기후 데이터 읽기
    annual_climate = pd.read_csv(annual_climate_path, encoding='euc-kr')
    monthly_climate = pd.read_csv(monthly_climate_path, encoding='euc-kr')

    # 행정구역 정보 추가
    annual_climate['행정구역'] = annual_climate['지점명'].map(region_mapping)
    monthly_climate['행정구역'] = monthly_climate['지점명'].map(region_mapping)

    # 분석 대상 지역 설정
    target_regions = ['전라남도', '충청남도', '전라북도', '경상북도']

    # 대상 지역 데이터만 필터링
    filtered_annual = annual_climate[annual_climate['행정구역'].isin(target_regions)]
    filtered_monthly = monthly_climate[monthly_climate['행정구역'].isin(target_regions)]

    return filtered_annual, filtered_monthly

# 메인 실행 코드
if __name__ == "__main__":
    # 파일 경로 설정
    rice_file = '/content/시군별_논벼_생산량.xlsx'
    annual_climate_file = '/content/연간기후전체지역.csv'
    monthly_climate_file = '/content/월별기후전체지역.csv'

    # 타겟 지역 설정
    target_regions = ['전라남도', '충청남도', '전라북도', '경상북도']

    # 1. 쌀 생산량 데이터 처리
    rice_data = process_rice_data(
        file_path=rice_file,
        target_regions=target_regions,
        output_path='filtered_rice_production.xlsx'
    )

    # 2. 기후 데이터 처리
    filtered_annual, filtered_monthly = filter_climate_data(
        annual_climate_file,
        monthly_climate_file
    )

    # 처리된 기후 데이터 저장
    filtered_annual.to_csv('filtered_climate_annual_data.csv', index=False, encoding='utf-8-sig')
    filtered_monthly.to_csv('filtered_climate_monthly_data.csv', index=False, encoding='utf-8-sig')

    print("모든 데이터 처리가 완료되었습니다.")
>>>>>>> 1d5c6fb (code update)
