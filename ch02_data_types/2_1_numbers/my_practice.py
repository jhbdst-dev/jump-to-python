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

"""
로봇의 현재 위치(current)와 목표 위치(target)를 초기값으로 설정합니다.

또한 한 번의 루프에서 이동할 수 있는 최대 거리(max_speed)와
목표에 충분히 가까워졌다고 판단하는 기준 거리(tolerance)를 정의합니다.

이 코드는 while 반복문으로 제어 루프를 실행하므로,
루프가 몇 번 반복되는지 확인하기 위해 loop_count 변수도 함께 초기화합니다.
"""

while True:
    loop_count += 1

    # 2) 오차 계산 (목표 - 현재)
    error_x = target_x - current_x
    error_y = target_y - current_y

    # 3) 거리 계산
    distance = (error_x**2 + error_y**2) ** 0.5

    # 4) 도착 판정
    # .2f 는 소수점 둘째 자리까지 출력하라는 형식
    if distance < tolerance:
        print(f"[DONE] loop_count={loop_count}, pos=({current_x:.2f},{current_y:.2f}), distance={distance:.3f}")
        break

    # 5) 비율 계산 (0~1 사이로 속도 조절 느낌)
    # distance가 클 때는 1에 가깝게, 작을 때는 0에 가깝게

    # distance → 0 이면 ratio → 0
    # distance → 무한대이면 ratio → 1
    # 항상 0~1 사이로 유지됨 (안전)
    
    ratio = distance / (distance + 1)   

    # 6) "한 스텝 이동량" 결정 (속도 개념)
    # ratio * max_speed 를 기본으로, 남은 거리가 더 작으면 distance만큼만
    step_move = ratio * max_speed
    if step_move > distance:
        step_move = distance

    # 7) 방향 정규화 (각 축으로 얼마나 움직일지)
    # error_x,error_y를 distance로 나누면 단위 방향벡터가 된다
    move_x = (error_x / distance) * step_move
    move_y = (error_y / distance) * step_move

    # 8) 위치 업데이트
    current_x += move_x
    current_y += move_y

    # 9) 주기 제어: 10스텝마다 로그
    if loop_count% 10 == 0:
        print(f"[LOG] loop_count={loop_count}, pos=({current_x:.2f},{current_y:.2f}), dist={distance:.3f}, ratio={ratio:.2f}")