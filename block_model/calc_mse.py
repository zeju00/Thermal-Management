import pandas as pd
import numpy as np

# 파일 경로 설정
file_path1 = 'outputs/gcc.ttrace'
file_path2 = '../example1/outputs/gcc.ttrace'

# 데이터 읽기
data1 = pd.read_csv(file_path1, sep='\t')
data2 = pd.read_csv(file_path2, sep='\t')

# 데이터 구조 확인
print("Data1 Head:")
print(data1.head())
print("\nData2 Head:")
print(data2.head())

# 각 part의 열 이름 추출 (두 파일의 열 이름이 동일하다고 가정)
parts = data1.columns

# MSE 계산 함수
def calculate_mse(series1, series2):
    return np.mean((series1 - series2) ** 2)

# MSE 계산
mse_results = {}

# 각 part에 대해 MSE 계산
for part in parts:
    mse = calculate_mse(data1[part], data2[part])
    mse_results[part] = mse

# MSE 결과를 데이터프레임으로 변환
mse_df = pd.DataFrame(list(mse_results.items()), columns=['Part', 'MSE'])

# MSE 결과 출력
print(mse_df)

# MSE 결과를 CSV 파일로 저장
output_file_path = 'mse_results.csv'
mse_df.to_csv(output_file_path, index=False)
