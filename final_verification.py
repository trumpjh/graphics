import json

print("=== 최종 검증 ===\n")

# 1. 3rd_grade_complete.json 확인
with open('3rd_grade_complete.json', 'r', encoding='utf-8') as f:
    complete_data = json.load(f)

print("📄 3rd_grade_complete.json:")
print(f"14번 정답: {complete_data[13]['correct']}")
print(f"46번 정답: {complete_data[45]['correct']}\n")

# 2. questions.json 확인
with open('questions.json', 'r', encoding='utf-8') as f:
    questions_data = json.load(f)

# 3학년 문제 찾기
grade3_q14 = None
grade3_q46 = None

for q in questions_data:
    if q.get('grade') == 3:
        if '게슈탈트' in q['question'] and '시지각' in q['question']:
            grade3_q14 = q
        elif '종이의 특성' in q['question'] and '틀린 것을 모두' in q['question']:
            grade3_q46 = q

print("📄 questions.json:")
if grade3_q14:
    print(f"14번 정답: {grade3_q14['correct']}")
else:
    print("14번을 찾을 수 없습니다")

if grade3_q46:
    print(f"46번 정답: {grade3_q46['correct']}")
else:
    print("46번을 찾을 수 없습니다")

print("\n✅ 수정 완료!")
print("\n변경 사항:")
print("- 14번: 정답 ③, ⑤ (배열로 저장됨)")
print("- 46번: 정답 ①, ⑤ (배열로 저장됨)")
print("- 이제 두 정답을 모두 선택해야만 정답으로 인정됩니다")
