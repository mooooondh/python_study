# quick_sort01.py

data = [25, 28, 4, 95, 5, 23, -5, 12, 12, 30, 82, 34, 55, 19, 10, 13, 6]


def quicksort(data, left, right):
    pivot = left
    while 1:
        if data[left] > data[pivot]:  # 큰값 > 기준키

            while (data[right] >= data[pivot]):
                right -= 1
                if left > right:
                    break
                pass  # ene

            if left > right:
                break

            data[left], data[right] = data[right], data[left]

        else:
            left = left + 1

            if left > right:
                break

    data[pivot], data[right] = data[right], data[pivot]

    return right
    pass


data_left = 0
data_right = len(data) - 1
data_pivot = 0
epoch_counter = 0  # 몇번의 epoch를 실행했는지 count

check = []  # 정렬할 리스트의 시작, 끝 index를 동적으로 저장, 삭제할 리스트

print("data: ", data)
print("=" * 30)

check.append(data_left)  # check리스트에 초기 data 처음과 끝 index 삽입
check.append(data_right)

while (len(check) != 0):  # check 리스트에 값이 없을 때 까지 반복
    data_right = check.pop()  # 정렬할 리스트의 마지막 index pop
    data_left = check.pop()  # 정렬할 리스트의 첫번째 index pop
    data_pivot = quicksort(data, data_left, data_right)  # 1epoch 수행 후 pivot 저장

    epoch_counter += 1  # 몇번의 epoch가 실행됐는지 count
    print("%s epoch: " % (epoch_counter))
    print(data)
    print("=" * 30)

    # epoch 수행 후 더 정렬할 index가 있는지 확인
    # index가 남아있다면 check리스트에 시작 및 끝 index 삽입
    if (data_pivot - 1 > data_left):  # pivot기준 왼쪽으로 더 정렬할 데이터가 있는지 확인
        check.append(data_left)
        check.append(data_pivot - 1)
        pass  # end of if

    if (data_pivot + 1 < data_right):  # pivot기준 오른쪽으로 더 정렬할 데이터가 있는지 확인
        check.append(data_pivot + 1)
        check.append(data_right)
        pass  # end of elif
    pass  # end of while