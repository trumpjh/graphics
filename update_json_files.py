#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

# 기호를 인덱스로 변환
def symbol_to_index(symbol):
    """기호를 인덱스로 변환 (①->0, ②->1 등)"""
    symbol_map = {'①': 0, '②': 1, '③': 2, '④': 3, '⑤': 4}
    if symbol in symbol_map:
        return symbol_map[symbol]
    return None

def handle_multiple_answers(answer_str):
    """③,⑤ 형태의 복수 답을 리스트로 변환"""
    parts = answer_str.split(',')
    result = []
    for part in parts:
        part = part.strip()
        idx = symbol_to_index(part)
        if idx is not None:
            result.append(idx)
    return result

# 3학년 JSON 수정
print("="*60)
print("3학년 JSON 파일 수정")
print("="*60)

with open('3rd_grade_complete.json', 'r', encoding='utf-8') as f:
    data_3rd = json.load(f)

# 55번 문제 수정 (인덱스는 54번)
if len(data_3rd) > 54:
    old_correct = data_3rd[54]['correct']
    new_correct = handle_multiple_answers('③,⑤')
    data_3rd[54]['correct'] = new_correct
    print(f"문제 #55 수정: {old_correct} → {new_correct}")
    print(f"문제 내용: {data_3rd[54]['question'][:50]}...")

with open('3rd_grade_complete.json', 'w', encoding='utf-8') as f:
    json.dump(data_3rd, f, ensure_ascii=False, indent=2)

print("3rd_grade_complete.json 저장 완료")

# 2학년 JSON 수정
print("\n" + "="*60)
print("2학년 JSON 파일 수정")
print("="*60)

with open('questions.json', 'r', encoding='utf-8') as f:
    data_2nd = json.load(f)

# 41번 문제 수정 (인덱스는 40번)
if len(data_2nd) > 40:
    old_correct = data_2nd[40]['correct']
    new_correct = symbol_to_index('④')
    data_2nd[40]['correct'] = new_correct
    print(f"문제 #41 수정: {old_correct} → {new_correct}")
    print(f"문제 내용: {data_2nd[40]['question'][:50]}...")

with open('questions.json', 'w', encoding='utf-8') as f:
    json.dump(data_2nd, f, ensure_ascii=False, indent=2)

print("questions.json 저장 완료")

print("\n" + "="*60)
print("JSON 파일 수정 완료!")
print("="*60)
