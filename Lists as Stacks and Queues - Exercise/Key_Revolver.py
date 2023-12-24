from collections import deque

bullet_price = int(input())
gun_barrel = int(input())

bullets = deque([int(b) for b in input().split()])
locks = deque([int(l) for l in input().split()])

reward = int(input())

bullets_in = gun_barrel
bullets_shot = 0

while bullets and locks:
    bullet = bullets.pop()
    lock = locks.popleft()

    if bullet <= lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(lock)

    bullets_in -= 1
    bullets_shot += 1

    if bullets_in == 0 and bullets:
        bullets_in = gun_barrel if len(bullets) >= gun_barrel else len(bullets)
        print("Reloading!")

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    earned_money = abs((bullet_price * bullets_shot) - reward)
    print(f"{len(bullets)} bullets left. Earned ${earned_money}")
