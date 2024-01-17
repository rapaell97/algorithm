number_of_book = 100
name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

def create_user(name,age,address):
    user_info = {'name': name, 'age': age, 'address': address}
    print(f'{name}님 환영합니다!')
    return user_info

def decrease_book(rental_num):
    global number_of_book
    number_of_book -= rental_num
    return number_of_book

many_user = list(map(create_user,name,age,address))

info_a = list(map(lambda x : {'name':x['name'],'age':x['age']}, many_user))
def rental_book(info):
    rentbook_num = info['age']//10
    decrease_book(rentbook_num)
    print('남은 책의 수 :', number_of_book)
    print(f'{info["name"]}님이 {rentbook_num}권의 책을 대여하였습니다.')

# info_a=dict(map(,kkk['name'],kkk['age']))
list(map(rental_book,info_a))