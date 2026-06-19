#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from docx import Document

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

# 3학년 데이터 매핑 (기존 order별로)
old_3rd_answers = {}
for idx, q in enumerate(old_3rd_complete, 1):
    # 옛날 형식에서 correct 값 추출
    if 'correct' in q:
        # correct는 0부터 시작하는 인덱스이므로 option 번호로 변환
        # 아니면 단순히 저장된 형태 그대로 사용
        correct = q['correct']
        if isinstance(correct, int):
            # 0 -> ①, 1 -> ②, etc.
            # 하지만 문제마다 다를 수 있으니, 일단 저장된 값 그대로 사용
            old_3rd_answers[idx] = correct

print("="*60)
print("3학년 문제 정답 비교")
print("="*60)

changes_3rd = []
for q_num in sorted(new_3rd.keys()):
    old_ans = old_3rd_answers.get(q_num)
    new_ans = new_3rd[q_num]
    
    if old_ans is not None and str(old_ans) != str(new_ans):
        changes_3rd.append({
            'number': q_num,
            'old': old_ans,
            'new': new_ans
        })
        print(f"문제 #{q_num}: {old_ans} → {new_ans}")

if not changes_3rd:
    print("변경된 정답 없음")

# 2학년 데이터 비교
old_2nd_answers = {}
for idx, q in enumerate(old_2nd_questions, 1):
    if 'correct' in q:
        old_2nd_answers[idx] = q['correct']

print("\n" + "="*60)
print("2학년 문제 정답 비교")
print("="*60)

changes_2nd = []
for q_num in sorted(new_2nd.keys()):
    old_ans = old_2nd_answers.get(q_num)
    new_ans = new_2nd[q_num]
    
    if old_ans is not None and str(old_ans) != str(new_ans):
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
        '3rd_grade_new_answers': dict(new_3rd),
        '2nd_grade_new_answers': dict(new_2nd)
    }, f, ensure_ascii=False, indent=2)

print("changes_summary.json 파일 생성 완료")
