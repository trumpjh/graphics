import json

# 3rd_grade_complete.json 읽기
with open('3rd_grade_complete.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"전체 문제 개수: {len(questions)}\n")

# 처음 5개 문제의 구조 확인
print("처음 5개 문제의 구조:")
for i in range(min(5, len(questions))):
    q = questions[i]
    print(f"\n문제 {i+1}:")
    print(f"  - correct 타입: {type(q.get('correct'))}")
    print(f"  - correct 값: {q.get('correct')}")
    print(f"  - 문제: {q['question'][:60]}")

# 모든 correct 값들의 통계
correct_values = {}
for q in questions:
    val = str(q.get('correct'))
    correct_values[val] = correct_values.get(val, 0) + 1

print("\n\ncorrect 값의 분포:")
for val, count in sorted(correct_values.items(), key=lambda x: -x[1])[:10]:
    print(f"  {val}: {count}개")

# correct가 리스트가 아닌 경우, 혹시 다른 필드가 있는지 확인
print("\n\n첫 번째 문제의 모든 필드:")
print(json.dumps(questions[0], ensure_ascii=False, indent=2))
