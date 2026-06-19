#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

# 인덱스를 기호로 변환 (0->①, 1->②, 2->③, 3->④, 4->⑤)
def index_to_symbol(idx):
    symbols = ['①', '②', '③', '④', '⑤']
    if isinstance(idx, int) and 0 <= idx < len(symbols):
        return symbols[idx]
    return str(idx)

# 추출한 새로운 정답 로드
with open('extracted_answers.json', 'r', encoding='utf-8') as f:
    new_answers = json.load(f)

new_3rd = new_answers['3rd_grade']
new_2nd = new_answers['2nd_grade']

# 기존 JSON 파일 로드
with open('3rd_grade_complete.json', 'r', encoding='utf-8') as f:
    old_3rd_complete = json.load(f)

with open('questions.json', 'r', encoding='utf-8') as f:
    old_2nd_questions = json.load(f)

# 3학년 정답 추출 및 변환
old_3rd_answers = {}
for idx, q in enumerate(old_3rd_complete, 1):
    if 'correct' in q:
        correct_idx = q['correct']
        old_3rd_answers[idx] = index_to_symbol(correct_idx)

print("="*60)
print("3학년 문제 정답 비교 (변환 후)")
print("="*60)
print(f"기존 3학년 정답: {old_3rd_answers}")
print(f"새 3학년 정답: {new_3rd}\n")

changes_3rd = []
# 새 정답의 키를 정수로 변환
new_3rd_int = {int(k) if isinstance(k, str) else k: v for k, v in new_3rd.items()}
for q_num in sorted(set(list(old_3rd_answers.keys()) + list(new_3rd_int.keys()))):
    old_ans = old_3rd_answers.get(q_num, "없음")
    new_ans = new_3rd_int.get(q_num, "없음")
    
    if old_ans != new_ans:
        changes_3rd.append({
            'number': q_num,
            'old': old_ans,
            'new': new_ans
        })
        print(f"문제 #{q_num}: {old_ans} → {new_ans}")

if not changes_3rd:
    print("변경된 정답 없음")

# 2학년 정답 추출 및 변환
old_2nd_answers = {}
for idx, q in enumerate(old_2nd_questions, 1):
    if 'correct' in q:
        correct_idx = q['correct']
        old_2nd_answers[idx] = index_to_symbol(correct_idx)

print("\n" + "="*60)
print("2학년 문제 정답 비교 (변환 후)")
print("="*60)
print(f"기존 2학년 정답: {old_2nd_answers}")
print(f"새 2학년 정답: {new_2nd}\n")

changes_2nd = []
# 새 정답의 키를 정수로 변환
new_2nd_int = {int(k) if isinstance(k, str) else k: v for k, v in new_2nd.items()}
for q_num in sorted(set(list(old_2nd_answers.keys()) + list(new_2nd_int.keys()))):
    old_ans = old_2nd_answers.get(q_num, "없음")
    new_ans = new_2nd_int.get(q_num, "없음")
    
    if old_ans != new_ans:
        changes_2nd.append({
            'number': q_num,
            'old': old_ans,
            'new': new_ans
        })
        print(f"문제 #{q_num}: {old_ans} → {new_ans}")

if not changes_2nd:
    print("변경된 정답 없음")

# 결과 요약
print("\n" + "="*60)
print("변경 요약")
print("="*60)
print(f"3학년 변경된 정답 수: {len(changes_3rd)}")
print(f"2학년 변경된 정답 수: {len(changes_2nd)}")

# 변경 사항 저장
with open('changes_summary.json', 'w', encoding='utf-8') as f:
    json.dump({
        '3rd_grade_changes': changes_3rd,
        '2nd_grade_changes': changes_2nd,
        '3rd_grade_new_answers': new_3rd_int,
        '2nd_grade_new_answers': new_2nd_int,
        '3rd_grade_old_answers': old_3rd_answers,
        '2nd_grade_old_answers': old_2nd_answers
    }, f, ensure_ascii=False, indent=2)

print("changes_summary.json 파일 생성 완료")
