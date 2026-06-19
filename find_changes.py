#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

# 인덱스를 기호로 변환
def index_to_symbol(idx):
    symbols = ['①', '②', '③', '④', '⑤']
    if isinstance(idx, int) and 0 <= idx < len(symbols):
        return symbols[idx]
    elif isinstance(idx, list):
        return ','.join(symbols[i] for i in idx if 0 <= i < len(symbols))
    return str(idx)

# 새 정답 로드
with open('all_extracted_answers.json', 'r', encoding='utf-8') as f:
    new_answers = json.load(f)

# 문자열 키를 정수로 변환
new_3rd = {int(k): v for k, v in new_answers['3rd_grade'].items()}
new_2nd = {int(k): v for k, v in new_answers['2nd_grade'].items()}

# 기존 JSON 로드
with open('3rd_grade_complete.json', 'r', encoding='utf-8') as f:
    old_3rd_complete = json.load(f)

with open('questions.json', 'r', encoding='utf-8') as f:
    old_2nd_questions = json.load(f)

# 3학년 기존 정답 추출 및 변환
old_3rd_answers = {}
for idx, q in enumerate(old_3rd_complete, 1):
    if 'correct' in q:
        correct_idx = q['correct']
        old_3rd_answers[idx] = index_to_symbol(correct_idx)

# 2학년 기존 정답 추출 및 변환
old_2nd_answers = {}
for idx, q in enumerate(old_2nd_questions, 1):
    if 'correct' in q:
        correct_idx = q['correct']
        old_2nd_answers[idx] = index_to_symbol(correct_idx)

# 변경 사항 찾기
print("="*60)
print("3학년 정답 변경 사항")
print("="*60)

changes_3rd = {}
for q_num in range(1, 61):
    old = old_3rd_answers.get(q_num)
    new = new_3rd.get(q_num)
    
    if old is not None and old != new:
        changes_3rd[q_num] = {
            'old': old,
            'new': new
        }
        print(f"문제 #{q_num}: {old} → {new}")

if not changes_3rd:
    print("변경된 정답 없음")
else:
    print(f"\n총 {len(changes_3rd)}개 변경")

print("\n" + "="*60)
print("2학년 정답 변경 사항")
print("="*60)

changes_2nd = {}
for q_num in range(1, 61):
    old = old_2nd_answers.get(q_num)
    new = new_2nd.get(q_num)
    
    if old is not None and old != new:
        changes_2nd[q_num] = {
            'old': old,
            'new': new
        }
        print(f"문제 #{q_num}: {old} → {new}")

if not changes_2nd:
    print("변경된 정답 없음")
else:
    print(f"\n총 {len(changes_2nd)}개 변경")

# 변경 사항 저장
with open('final_changes.json', 'w', encoding='utf-8') as f:
    json.dump({
        '3rd_grade_changes': changes_3rd,
        '2nd_grade_changes': changes_2nd,
        '3rd_grade_new_answers': new_3rd,
        '2nd_grade_new_answers': new_2nd
    }, f, ensure_ascii=False, indent=2)

print("\nfinal_changes.json 파일 생성 완료")
