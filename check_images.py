#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

with open('3rd_grade_complete.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print("3학년 이미지 문제 확인:")
found = False
for i, q in enumerate(questions):
    if '[이미지' in q['question']:
        print(f"질문 {i+1}: {q['question'][:80]}")
        found = True

if not found:
    print("이미지 문제 찾기 실패")
    print(f"\n전체 {len(questions)}개 질문")
    print("\n35번, 36번 검색:")
    for i, q in enumerate(questions):
        if '그림' in q['question'] and i >= 33 and i <= 37:
            print(f"질문 {i+1}: {q['question'][:80]}")
