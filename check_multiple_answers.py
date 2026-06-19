import json

# 3rd_grade_complete.json 읽기
with open('3rd_grade_complete.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 정답이 2개 이상인 문제 찾기
multiple_answers = []

for i, q in enumerate(questions):
    # correct 필드가 리스트인 경우
    if isinstance(q.get('correct'), list) and len(q['correct']) > 1:
        multiple_answers.append({
            'index': i,
            'question': q['question'][:80],
            'correct': q['correct'],
            'options': q['options'],
            'count': len(q['correct'])
        })

print(f"정답이 2개 이상인 문제 개수: {len(multiple_answers)}\n")

# 정답이 정확히 2개인 문제 세기
exactly_two = [x for x in multiple_answers if x['count'] == 2]
print(f"정답이 정확히 2개인 문제: {len(exactly_two)}")

# 처음 10개 표시
for item in multiple_answers[:10]:
    print(f"\n문제 {item['index'] + 1}: {item['question']}")
    print(f"정답 개수: {item['count']}, 정답 인덱스: {item['correct']}")
    for idx in item['correct']:
        if idx < len(item['options']):
            print(f"  ✓ {item['options'][idx]}")
