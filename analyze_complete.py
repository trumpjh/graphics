import json

# 파일 읽기
with open('3rd_grade_complete.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('전체 문제:', len(data))

# 각 문제를 자세히 확인
print("\n모든 문제와 정답:")
for i, q in enumerate(data):
    question_short = q['question'][:50]
    correct = q.get('correct')
    print(f"{i+1:2d}. correct={correct:2d} | {question_short}")
