from zipfile import ZipFile
import sys
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')

hwpx_file = "(3학년)광고콘텐츠제작 문제.hwpx"

try:
    with ZipFile(hwpx_file, 'r') as z:
        # content.hpf 파일 읽기
        content = z.read('Contents/content.hpf').decode('utf-8', errors='ignore')
        print("=== 3학년 파일 내용 ===\n")
        print(content[:2000])  # 처음 2000자만 출력
except Exception as e:
    print(f"오류: {e}")
    print("\n파일을 직접 열어서 문제를 알려주시면 수동으로 추가하겠습니다!")
