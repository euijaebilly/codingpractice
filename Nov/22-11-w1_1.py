"""
IP 주소 훼손하기
유효한 (IPv4) IP address가 주어질 때, 이 IP 주소의 훼손된 버전을 반환하세요.

훼손된 IP 주소는 모든 마침표 "."이 "[.]"으로 교체된 거예요.
"""
def replacer(ip_address):
    result =''
    for chr in ip_address:
        if chr == '.':
            result += '[.]'
            continue
        result+=chr
    return result


if __name__ == '__main__':
    origin = '111.111.111.111'
    print(replacer(origin))
    origin = origin.replace('.', '[.]')
    print(origin)