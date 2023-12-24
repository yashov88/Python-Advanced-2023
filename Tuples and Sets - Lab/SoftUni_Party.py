n = int(input())

reservations = set()

for _ in range(n):
    reservation_num = input()
    reservations.add(reservation_num)

guest_reservation = input()

while guest_reservation != "END":
    if guest_reservation in reservations:
        reservations.remove(guest_reservation)
    guest_reservation = input()


print(len(reservations))
for num in sorted(reservations):
    print(num)
