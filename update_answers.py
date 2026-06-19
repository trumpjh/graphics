import json

# 파일 읽기
with open('3rd_grade_complete.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 14번 문제 (index 13) 확인
print(f"14번 문제: {data[13]['question'][:60]}")
print(f"현재 정답: {data[13]['correct']}")
print(f"선택지: {data[13]['options']}\n")

# 46번 문제 (index 45) 확인
print(f"46번 문제: {data[45]['question'][:60]}")
print(f"현재 정답: {data[45]['correct']}")
print(f"선택지: {data[45]['options']}")

# 수정
# 14번: ③, ⑤ → [2, 4]
# 46번: ①, ⑤ → [0, 4]
data[13]['correct'] = [2, 4]
data[45]['correct'] = [0, 4]

print("\n\n=== 수정 후 ===")
print(f"14번 정답: {data[13]['correct']}")
print(f"46번 정답: {data[45]['correct']}")

# 파일 저장
with open('3rd_grade_complete.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\n저장 완료!")
