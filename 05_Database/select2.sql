--SQLite
-- SELECT DISTINCT age FROM users;

-- SELECT * FROM users WHERE age=30;
-- SELECT first_name FROM users WHERE age >= 30;

--users 에서 age 30이상, 성이 김씨인 사람의 성과 나이만 가져온다면?
-- SELECT last_name, age FROM users WHERE age >= 30 and last_name='김';

-- -- COUNT
-- SELECT COUNT(*) FROM users;

-- AVE, SUM, MIN, MAX
-- 30살 이상인 사람들의 평균나이
-- SELECT AVG(age) FROM users WHERE age >= 30;

-- users에서 잔액이 가장 높은 사람과 잔액
-- SELECT first_name, MAX(balance) FROM users;

-- users에서 30살 이상인 사람의 평균 계좌 잔액
-- SELECT AVG(balance) FROM users WHERE age>=30;

-- WILD CARDS
-- users에서 20대인 사람?
-- SELECT * FROM users WHERE age LIKE '2_'

-- 폰번호에 02가 있는 사람
-- SELECT phone FROM users WHERE phone LIKE '02-%'

-- 이름이 준으로 끝나는 사람
-- SELECT first_name FROM users WHERE first_name LIKE '%준'

-- 번호에 5114가 있는 사람
-- SELECT phone FROM users WHERE phone LIKE '%5114%'

-- ORDER (정렬 기준을 우선순위 순으로 써야한다)
-- SELECT age FROM users ORDER BY age DESC LIMIT 10;
-- SELECT age, last_name FROM users ORDER BY last_name, age LIMIT 10;
-- SELECT age, balance FROM users ORDER BY age, balance LIMIT 10;
SELECT first_name, last_name, balance FROM users ORDER BY balance DESC LIMIT 10;

