# 파일명 및 함수명을 변경하지 마시오.
def summary(word):
    """
    아래에 코드를 작성하시오.
    word는 알파벳으로 구성되어 있습니다.
    요약된 문자열을 반환합니다.
    """
    # 리스트로 바꾼다
    letters = []
    letters.extend(word)

    # 문자와 갯수를 담을 딕셔너리 생성
    raw = {}

    # 문자열 리스트를 돌면서 하나만 있는 문자는 딕셔너리에 key와 value로 넣고 문자는 리스트에서 지운다
    for letter in letters:
        raw[letter] = 0
        if letters.count(letter) == 1:
            raw[letter] = 1
            letters.remove(letter)

    # 겹치는 문자가 없는 문자열은 리스트가 비어있을테니 valueerror 처리해서 pass
    # 겹치는 문자열만 남은 리스트들은 letter가 뒤의 letter와 다를 때 딕셔너리의 value를 하나씩 올린다
    # 앞에 중복되는 문자가 있는 경우에는 딕셔너리 value를 1로 다시 바꾼다. 뒤의 문자와 같을 때 마다 value를 하나씩 더한다.
    try:
        for letter in letters:
            raw[letter] = 0
            if letter in word[:word.rfind(letter)-1]:
                raw[letter] = 1
                if letter != letters[letters.index(letter)+1]:
                    raw[letter] = raw.get(letter) + 1
    except ValueError:
        pass

    # 딕셔너리의 key와 value를 각각 list로 뽑는다
    # 숫자인 value를 key list의 홀수 인덱스에 삽입한다
    # key list를 join 메서드로 문자열로 바꾸어 반환한다.

    return raw

# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(summary('aabbaacc'))
    print(summary('ffgggeeeef'))
    print(summary('abcdefg'))
