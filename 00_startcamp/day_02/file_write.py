lunches = {
    '양자강': '02-888-9999',
    '김밥카페': '02-578-9654',
    '순남시래기': '02-634-9871'
}

with open('lunch.csv', 'w', encoding='utf-8') as f:
    f.write('식당이름, 전화번호\n')
    for name, phone in lunches.items():
        f.write(f'{name},{phone}\n')

#for name, phone in lunches.items():
   #print(name,phone)
