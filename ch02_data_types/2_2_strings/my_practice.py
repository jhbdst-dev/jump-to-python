"""
이 연습 코드는 로봇이 현재 위치에서 목표 위치까지 이동하고,
목표에 충분히 가까워지면 멈추는 단순한 이동 제어 구조를 구현한 것입니다.
"""

# 1) 초기값 설정
current_x, current_y = 0.0, 0.0          # 현재 위치
target_x, target_y = 10.0, 10.0          # 목표 위치

max_speed = 1.0          # 한 스텝에서 이동할 최대 거리(속도 느낌)
tolerance = 0.1          # 목표에 이 정도로 가까우면 "도착"

loop_count = 0           # 제어 루프 반복 횟수

# 목표 지점으로 이동
print("───────────────────────── START ──────────────────────────")
print(f"[START] 🤖 start_pos = ({current_x},{current_y}) → 🎯 target = ({target_x},{target_y})\n")

while True:
    loop_count += 1

    # 2) 오차 계산 (목표 - 현재)
    error_x = target_x - current_x
    error_y = target_y - current_y

    # 3) 거리 계산
    distance = (error_x**2 + error_y**2) ** 0.5

    # 4) 도착 판정
    if distance < tolerance:
        print("───────────────────────── DONE ──────────────────────────")
        print(f"[DONE] 🚩 loop_count = {loop_count}, pos = ({current_x:.2f},{current_y:.2f}), distance = {distance:.3f}\n")
        break
    
    # 5) 비율 계산 (0~1 사이로 속도 조절 느낌)
    ratio = distance / (distance + 1)   

    # 6) "한 스텝 이동량" 결정 (속도 개념)
    step_move = ratio * max_speed

    if step_move > distance:
        step_move = distance

    # 7) 방향 정규화 (각 축으로 얼마나 움직일지)
    move_x = (error_x / distance) * step_move
    move_y = (error_y / distance) * step_move

    # 8) 위치 업데이트
    current_x += move_x
    current_y += move_y

    # 9) 주기 제어: 5스텝마다 로그
    if loop_count % 5 == 0:
        print("───────────────────────── MOVING ─────────────────────────")
        print(f"[MOVING] 🟢 ➡️   ➡️   ➡️   ➡️   ➡️   ➡️   ➡️   ➡️   ➡️   ➡️   ➡️\n")
        print(f"loop_count = {loop_count}\npos = ({current_x:.2f}, {current_y:.2f})\ndistance = {distance:.3f}\nratio = {ratio:.2f}\n")