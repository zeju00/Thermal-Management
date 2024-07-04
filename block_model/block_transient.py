import pandas as pd
import matplotlib.pyplot as plt

# 파일 경로
file_path = 'outputs/gcc.ttrace'

# 데이터 읽기
data = pd.read_csv(file_path, sep='\t')

# 데이터 구조 확인
print(data.head())

# part 열들을 추출
parts = data.columns

# 선 그래프 그리기
plt.figure(figsize=(14, 8))

for part in parts:
    plt.plot(data.index, data[part], label=part)

# 그래프 제목과 축 레이블 설정
plt.title('Time Series Temperature for Each Part')
plt.xlabel('Time')
plt.ylabel('Temperature')

# 범례 추가
plt.legend()

# 그래프를 PNG 파일로 저장
output_file_path = 'block_transient.png'
plt.savefig(output_file_path)

# 그래프 표시
#plt.show()
