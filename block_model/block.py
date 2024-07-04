import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# 플로어플랜 데이터
floorplan_data = """
L2_left	0.004900	0.005530	0.000000	0.009800
L2	0.016000	0.009800	0.000000	0.000000
L2_right	0.004900	0.005530	0.011100	0.009800
Icache	0.003100	0.002600	0.004900	0.009800
Dcache	0.003100	0.002600	0.008000	0.009800
Bpred_0	0.001033	0.000700	0.004900	0.012400
Bpred_1	0.001033	0.000700	0.005933	0.012400
Bpred_2	0.001033	0.000700	0.006967	0.012400
DTB_0	0.001033	0.000700	0.008000	0.012400
DTB_1	0.001033	0.000700	0.009033	0.012400
DTB_2	0.001033	0.000700	0.010067	0.012400
FPAdd_0	0.001100	0.000900	0.004900	0.013100
FPAdd_1	0.001100	0.000900	0.006000	0.013100
FPReg_0	0.000550	0.000380	0.004900	0.014000
FPReg_1	0.000550	0.000380	0.005450	0.014000
FPReg_2	0.000550	0.000380	0.006000	0.014000
FPReg_3	0.000550	0.000380	0.006550	0.014000
FPMul_0	0.001100	0.000670	0.002200	0.015330
FPMul_1	0.001600	0.000670	0.003300	0.015330
FPMap_0	0.001100	0.000670	0.000000	0.015330
FPMap_1	0.001100	0.000670	0.001100	0.015330
IntMap	0.000900	0.001514	0.004900	0.014480
IntQ	0.003100	0.000670	0.011100	0.015330
IntReg_0	0.000900	0.000670	0.014200	0.015330
IntReg_1	0.000900	0.000670	0.015100	0.015330
IntExec	0.001800	0.002900	0.009300	0.013100
FPQ	0.000900	0.001550	0.007100	0.013100
LdStQ	0.001300	0.002300	0.008000	0.013700
ITB_0	0.000650	0.000600	0.008000	0.013100
ITB_1	0.000650	0.000600	0.008650	0.013100


"""

# 온도 데이터
temperature_data = """
L2_left	324.52
L2	324.08
L2_right	324.99
Icache	331.22
Dcache	335.57
Bpred_0	333.71
Bpred_1	334.19
Bpred_2	333.84
DTB_0	329.02
DTB_1	328.77
DTB_2	328.35
FPAdd_0	329.88
FPAdd_1	330.15
FPReg_0	330.02
FPReg_1	330.34
FPReg_2	330.50
FPReg_3	330.28
FPMul_0	327.41
FPMul_1	326.88
FPMap_0	323.72
FPMap_1	324.24
IntMap	327.99
IntQ	325.61
IntReg_0	341.95
IntReg_1	342.38
IntExec	332.99
FPQ	328.17
LdStQ	332.19
ITB_0	329.36
ITB_1	329.75
"""

# 데이터를 파싱하여 파츠 정보와 온도 정보를 딕셔너리로 저장
parts = {}
temperatures = {}

for line in floorplan_data.strip().split('\n'):
    tokens = line.split()
    unit_name = tokens[0]
    width = float(tokens[1])
    height = float(tokens[2])
    left_x = float(tokens[3])
    bottom_y = float(tokens[4])
    parts[unit_name] = (width, height, left_x, bottom_y)

for line in temperature_data.strip().split('\n'):
    tokens = line.split()
    unit_name = tokens[0]
    temperature = float(tokens[1])
    temperatures[unit_name] = temperature

# 히트맵 그리기
fig, ax = plt.subplots()

# 컬러맵 설정 (반전된 hot 컬러맵 사용)
cmap = plt.get_cmap('hot_r')
min_temp = min(temperatures.values())
max_temp = max(temperatures.values())
norm = plt.Normalize(vmin=min_temp, vmax=max_temp)

# 각 파츠를 직사각형으로 그리기
for unit_name, (width, height, left_x, bottom_y) in parts.items():
    temperature = temperatures.get(unit_name, min_temp)  # 온도가 없으면 최소값으로 설정
    color = cmap(norm(temperature))
    rect = patches.Rectangle((left_x, bottom_y), width, height, linewidth=1, edgecolor='black', facecolor=color)
    ax.add_patch(rect)
    # 각 파츠에 레이블 추가
    plt.text(left_x + width/2, bottom_y + height/2, unit_name, color='black', ha='center', va='center', fontsize=8)

# 축 설정 및 제목 추가
ax.set_xlim(0, max([p[2] + p[0] for p in parts.values()]))
ax.set_ylim(0, max([p[3] + p[1] for p in parts.values()]))
ax.set_title('Heatmap of Floorplan')
ax.set_xlabel('X Coordinate (meters)')
ax.set_ylabel('Y Coordinate (meters)')

# 컬러바 추가
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax)
cbar.set_label('Temperature (°C)')

# 그래프를 PNG 파일로 저장
output_file_path = 'block_heatmap1.png'
plt.savefig(output_file_path)

# 그래프 표시
#plt.show()
