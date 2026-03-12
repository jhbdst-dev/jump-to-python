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

"""
while True는 항상 참이기 때문에 
이 코드는 무한 루프 형태의 제어 루프입니다.

loop_count += 1 은 루프가 한 번 돌 때마다
제어 루프가 몇 번 실행되었는지 기록하는 역할을 합니다.

이 값은 나중에 로그 출력이나 디버깅에 사용됩니다.
"""
while True:
    loop_count += 1

    """
    2) 오차 계산

    현재 위치에서 목표 위치까지 이동해야 하는 방향과 거리의 정보를 구하는 것입니다.
    """
    # 2) 오차 계산 (목표 - 현재)
    error_x = target_x - current_x
    error_y = target_y - current_y

    """
    3) 거리 계산

    오차(error_x, error_y)는 목표 위치와 현재 위치 사이의 차이를 나타낸다.

    하지만 오차 값만으로는 목표까지 얼마나 멀리 떨어져 있는지 알기 어렵기 때문에
    두 점 사이의 직선 거리를 계산한다.

    좌표 평면에서 두 점 사이의 거리는 *피타고라스 정리* 를 이용해 구할 수 있다.

    distance = √(error_x² + error_y²)

    먼저 error_x와 error_y를 제곱하여 더한 뒤,
    루트를 적용해 실제 거리(distance)를 구한다.

    distance는 현재 위치에서 목표 위치까지의 직선 거리이다.

    제곱: 두 축의 차이를 이용해 거리 계산을 하기 위한 과정
    루트: 제곱된 값을 다시 실제 거리 크기로 되돌리는 과정
    """
    # 3) 거리 계산
    distance = (error_x**2 + error_y**2) ** 0.5

    """
    4) 도착 판정

    목표까지의 거리가 일정 기준(tolerance)보다 작아지면
    도착으로 판단하고 현재 상태를 출력한 뒤 제어 루프를 종료한다.
    """
    # 4) 도착 판정
    # .2f 는 소수점 둘째 자리까지 출력하라는 형식
    if distance < tolerance:
        print(f"[DONE] loop_count={loop_count}, pos=({current_x:.2f},{current_y:.2f}), distance={distance:.3f}")
        break
    """
    5) 비율 계산

    만든 목적 :
    멀리 있을 때는 빠르게 움직이고,
    목표를 지나치지 않기 위해서,
    목표에 가까워질수록 천천히 움직이게 만들기 위함입니다.
    """
    # 5) 비율 계산 (0~1 사이로 속도 조절 느낌)
    # distance가 클 때는 1에 가깝게, 작을 때는 0에 가깝게

    # distance → 0 이면 ratio → 0
    # distance → 무한대이면 ratio → 1
    # 항상 0~1 사이로 유지됨 (안전)
    
    ratio = distance / (distance + 1)   

    """
    6) 한 스탭 이동량 결정

    이동 속도는 ratio * max_speed로 계산합니다.
    하지만 목표보다 더 많이 움직이면
    딱 목표까지만 이동합니다.

    속도 제어 + 목표 보호
    """
    # 6) "한 스텝 이동량" 결정 (속도 개념)
    # ratio * max_speed 를 기본으로, 남은 거리가 더 작으면 distance만큼만
    step_move = ratio * max_speed

    # 목표를 지나치지 않도로 하기 위한 코드
    if step_move > distance:
        step_move = distance

    """
    7) 방향 정규화

    목표 방향을 유지하면서, 이번 스텝에서 이동해야 할 x축과 y축 이동량을 계산하는 과정입니다.
    """
    # 7) 방향 정규화 (각 축으로 얼마나 움직일지)
    # error_x,error_y를 distance로 나누면 단위 방향벡터가 된다
    move_x = (error_x / distance) * step_move
    move_y = (error_y / distance) * step_move

    """
    8) 위치 업데이트

    current_x = current_x + move_x
    current_y = current_y + move_y
    현재 위치에 이번 스텝에서 이동한 만큼을 더해 새로운 위치를 갱신하는 것입니다.
    """
    # 8) 위치 업데이트
    current_x += move_x
    current_y += move_y

    """
    9) 주기 제어

    %는 나눗셈의 나머지를 구하는 연산자

    "loop_count를 10으로 나눴을 때
    나머지가 0인가?"
    라는 뜻입니다.

    나머지가 0이라는 것은 10으로 딱 나누어 떨어진다는 뜻입니다.

    10 % 10 = 0 일 때만 print가 실행됩니다.
    """
    # 9) 주기 제어: 10스텝마다 로그
    if loop_count % 10 == 0:
        print(f"[LOG] loop_count={loop_count}, pos=({current_x:.2f},{current_y:.2f}), distance={distance:.3f}, ratio={ratio:.2f}")