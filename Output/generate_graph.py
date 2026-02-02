import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import os

# 한글 폰트 설정 (Windows)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 월별 매출 데이터
months = ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월']
revenue = [150, 200, 350, 450, 500, 600, 550, 500, 700, 850, 1000, 950]
cumulative = np.cumsum(revenue)

# 그래프 생성 (2개 서브플롯)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
fig.suptitle('AI 1인 기업 1년차 매출 계획', fontsize=16, fontweight='bold')

# 1. 월별 매출 막대 그래프
colors = ['#3498db' if r < 500 else '#e74c3c' if r >= 800 else '#2ecc71' for r in revenue]
bars = ax1.bar(months, revenue, color=colors, edgecolor='white', linewidth=1.5)
ax1.set_ylabel('매출 (만원)', fontsize=12)
ax1.set_title('월별 매출', fontsize=14, pad=10)
ax1.set_ylim(0, 1200)

# 막대 위에 값 표시
for bar, val in zip(bars, revenue):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 20,
             f'{val}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# 평균선 추가
avg = np.mean(revenue)
ax1.axhline(y=avg, color='#e67e22', linestyle='--', linewidth=2, label=f'월 평균: {avg:.0f}만원')
ax1.legend(loc='upper left', fontsize=10)

# 그리드
ax1.grid(axis='y', alpha=0.3)
ax1.set_axisbelow(True)

# 2. 누적 매출 라인 그래프
ax2.fill_between(months, cumulative, alpha=0.3, color='#9b59b6')
ax2.plot(months, cumulative, color='#9b59b6', linewidth=3, marker='o', markersize=8)
ax2.set_ylabel('누적 매출 (만원)', fontsize=12)
ax2.set_xlabel('월', fontsize=12)
ax2.set_title('누적 매출', fontsize=14, pad=10)

# 누적 값 표시
for i, (m, c) in enumerate(zip(months, cumulative)):
    if i % 2 == 0 or i == 11:  # 짝수 월 + 마지막 월만 표시
        ax2.annotate(f'{c:,}', (m, c), textcoords="offset points",
                    xytext=(0, 10), ha='center', fontsize=9, fontweight='bold')

# 목표선
ax2.axhline(y=6800, color='#e74c3c', linestyle='--', linewidth=2, label='연간 목표: 6,800만원')
ax2.legend(loc='upper left', fontsize=10)
ax2.grid(alpha=0.3)
ax2.set_axisbelow(True)

# 레이아웃 조정
plt.tight_layout()

# 저장
output_path = os.path.join(os.path.dirname(__file__), 'graph.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

print(f"=" * 50)
print(f"  그래프 생성 완료!")
print(f"=" * 50)
print(f"  저장 위치: {output_path}")
print(f"  연간 총 매출: {sum(revenue):,}만원")
print(f"  월 평균 매출: {avg:.0f}만원")
print(f"=" * 50)
