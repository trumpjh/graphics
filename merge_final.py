#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

# 현재 questions.json 로드 (2학년)
with open('questions.json', 'r', encoding='utf-8') as f:
    grade2_questions = json.load(f)

# 3학년 완성 JSON 로드
with open('3rd_grade_complete.json', 'r', encoding='utf-8') as f:
    grade3_questions = json.load(f)

print(f"2학년: {len(grade2_questions)}개")
print(f"3학년: {len(grade3_questions)}개")

# 병합
all_questions = grade2_questions + grade3_questions

print(f"총합: {len(all_questions)}개")

# 저장
with open('questions.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print("\nquestions.json에 병합 완료!")

# 확인
print("\n병합 확인:")
grade2_count = len([q for q in all_questions if q['grade'] == 2])
grade3_count = len([q for q in all_questions if q['grade'] == 3])
print(f"2학년: {grade2_count}개")
print(f"3학년: {grade3_count}개")

# 35번, 36번 이미지 문제 확인
print("\n3학년 이미지 문제 확인:")
for q in all_questions:
    if q['grade'] == 3 and ('이미지' in q['question'] or '그림' in q['question']):
        print(f"  {q['question'][:80]}")
