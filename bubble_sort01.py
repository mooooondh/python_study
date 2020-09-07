# bubble_sort01.py

# 버블정렬(bubble sort)
# 주어진 데이터를 한번 다 사용하면 1 epoch라고 부름
# 1epoch가 끝난 후 제일 큰 값은 무조건 마지막 인덱스에 위치
# 같은 값인 인덱스인 경우 A, B 값 교환이 일어나지 않는다.

# list_val : 정렬할 요소값(n개)이 들어간 리스트 변수
# a : 비교할 인덱스 A. 초깃값 = 0
# b : 비교할 인덱스 B. 초깃값 = 1
# count : (1epoch 당) 인덱스 A, B 값 교환이 일어난 수


list_val = [10, 1, 1, 50]
a = 0
b = 1
count = 0

# 탈출 조건 : 첫 인덱스부터 마지막 인덱스까지 비교했을 때 인덱스 간 값 교환이 일어나지 않았다.
#                즉, 마지막 인덱스까지 비교할때까지 인덱스간 교환이 하나도 일어나지 않을 경우에 탈출
# 한 epoch를 돌 때는 b가 4가 되기 전이기 때문에 while 루프를 돌게 되고,
# 한 epoch를 다 돌고 난 시점에서는 정렬이 완료되지 않았기 때문에 교환이 일어나 count가 0이 아니므로,
# 초기화가 돼 while문을 또 돌게 되는 조건을 만족한다.
# 그러다가 한 epoch를 모두 돌았는데 count가 0이 되게 되면 두번째 if문이 수행되지 않고 넘어가게 되므로
# while문 조건에 만족하지 않게 돼 탈출한다.


while (count != 0 or b != len(list_val)):

    if (list_val[a] > list_val[b]):  # 인덱스 A가 인덱스 B보다 크면 ==> 인덱스 A와 B 값 교환 ==> 교환 수 1 증가
        list_val[a], list_val[b] = list_val[b], list_val[a]
        count += 1
        pass  # if

    a += 1  # 다음 인덱스 비교를 위해 A, B 인덱스를 1 증가시킴
    b += 1

    # 전체 값 비교 중 교환이 1번이라도 일어났다면 인덱스 변수 A, B와 count 변수 초기화
    if (b == len(list_val) and count != 0):
        count = 0
        a = 0
        b = 1
        pass  # if

    # (0번째 인덱스) ~ (마지막 인덱스) 간 버블 정렬 재수행

    pass  # while loop

print('Bubble 정렬 결과 : ', list_val)