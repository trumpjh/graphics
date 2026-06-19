import json

# questions.json 파일 읽기
try:
    with open('questions.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 3학년 문제만 필터링하여 인덱스 찾기
    grade3_questions = [q for q in data if q.get('grade') == 3]
    print(f"3학년 문제 개수: {len(grade3_questions)}")
    
    # 3학년 문제에서 14번과 46번 찾기
    for i, q in enumerate(grade3_questions):
        if '게슈탈트' in q['question'] and '시지각' in q['question']:
            print(f"찾음 - 14번: 원래 위치 {i}")
            q['correct'] = [2, 4]  # ③, ⑤
        elif '종이의 특성' in q['question'] and '틀린 것을 모두' in q['question']:
            print(f"찾음 - 46번: 원래 위치 {i}")
            q['correct'] = [0, 4]  # ①, ⑤
    
    # 파일 저장
    with open('questions.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("\nquestions.json 저장 완료!")
    
except FileNotFoundError:
    print("questions.json 파일을 찾을 수 없습니다.")
except Exception as e:
    print(f"오류: {e}")
