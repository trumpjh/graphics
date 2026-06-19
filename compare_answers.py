#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

# ① = 0, ② = 1, ③ = 2, ④ = 3, ⑤ = 4

def convert_answer(answer_str):
    """정답 문자열을 인덱스로 변환"""
    if ',' in answer_str:
        # 복수 정답
        answers = answer_str.split(',')
        return sorted([ord(a.strip()) - ord('①') for a in answers])
    else:
        # 단일 정답
        return ord(answer_str.strip()) - ord('①')

# 3학년 정답표 (docx)
answers_3yr_docx = {
    1: '⑤', 16: '③', 31: '④', 46: '①,⑤',
    2: '④', 17: '④', 32: '②', 47: '⑤',
    3: '①', 18: '②', 33: '①', 48: '⑤',
    4: '④', 19: '④', 34: '⑤', 49: '②',
    5: '④', 20: '④', 35: '④', 50: '①',
    6: '②', 21: '③', 36: '④', 51: '④',
    7: '③', 22: '④', 37: '②', 52: '②',
    8: '②', 23: '②', 38: '①', 53: '①',
    9: '③', 24: '③', 39: '④', 54: '②',
    10: '②', 25: '③', 40: '①', 55: '⑤',
    11: '①', 26: '④', 41: '②', 56: '⑤',
    12: '⑤', 27: '①', 42: '③', 57: '①',
    13: '④', 28: '①', 43: '②', 58: '①',
    14: '③,⑤', 29: '①', 44: '③', 59: '①',
    15: '④', 30: '③', 45: '①', 60: '②',
}

# 2학년 정답표 (docx)
answers_2yr_docx = {
    1: '⑤', 16: '①', 31: '②', 46: '②',
    2: '①', 17: '④', 32: '②', 47: '④',
    3: '②', 18: '②', 33: '③', 48: '④',
    4: '③', 19: '③', 34: '②', 49: '②',
    5: '④', 20: '①', 35: '②', 50: '①',
    6: '②', 21: '②', 36: '①', 51: '②',
    7: '①', 22: '③', 37: '②', 52: '③',
    8: '①', 23: '①', 38: '②', 53: '④',
    9: '④', 24: '②', 39: '②', 54: '③',
    10: '②', 25: '③', 40: '①', 55: '④',
    11: '③', 26: '①', 41: '①', 56: '①',
    12: '①', 27: '②', 42: '①', 57: '②',
    13: '③', 28: '⑤', 43: '③', 58: '②',
    14: '②', 29: '③', 44: '②', 59: '②',
    15: '②', 30: '①', 45: '①', 60: '②',
}

# JSON 파일 로드
with open('3rd_grade_complete.json', 'r', encoding='utf-8') as f:
    json_3yr = json.load(f)

with open('questions.json', 'r', encoding='utf-8') as f:
    all_questions = json.load(f)
    
json_2yr = [q for q in all_questions if q.get('grade') == 2]

print("="*70)
print("3학년 정답 비교 (docx vs JSON)")
print("="*70)

# 3학년 비교
mismatches_3yr = []
for q_num, docx_answer in answers_3yr_docx.items():
    json_obj = json_3yr[q_num - 1]  # 0-indexed
    json_correct = json_obj['correct']
    docx_correct = convert_answer(docx_answer)
    
    # 정규화
    if isinstance(json_correct, list):
        json_correct = sorted(json_correct)
    if isinstance(docx_correct, list):
        docx_correct = sorted(docx_correct)
    
    match = json_correct == docx_correct
    
    if not match:
        mismatches_3yr.append({
            'num': q_num,
            'docx': docx_answer,
            'json': json_correct,
            'question': json_obj['question'][:50]
        })
    
    symbol = "✓" if match else "✗"
    print(f"{symbol} {q_num:2d}. docx: {docx_answer:5s} | json: {json_correct}")

if mismatches_3yr:
    print(f"\n⚠️ 3학년 불일치 {len(mismatches_3yr)}개:")
    for m in mismatches_3yr:
        print(f"  {m['num']}번: docx={m['docx']}, json={m['json']} - {m['question']}")
else:
    print("\n✅ 3학년 모든 정답이 일치합니다!")

print("\n" + "="*70)
print("2학년 정답 비교 (docx vs JSON)")
print("="*70)

# 2학년 비교
mismatches_2yr = []
for q_num, docx_answer in answers_2yr_docx.items():
    if q_num - 1 < len(json_2yr):
        json_obj = json_2yr[q_num - 1]  # 0-indexed
        json_correct = json_obj['correct']
        docx_correct = convert_answer(docx_answer)
        
        # 정규화
        if isinstance(json_correct, list):
            json_correct = sorted(json_correct)
        if isinstance(docx_correct, list):
            docx_correct = sorted(docx_correct)
        
        match = json_correct == docx_correct
        
        if not match:
            mismatches_2yr.append({
                'num': q_num,
                'docx': docx_answer,
                'json': json_correct,
                'question': json_obj['question'][:50]
            })
        
        symbol = "✓" if match else "✗"
        print(f"{symbol} {q_num:2d}. docx: {docx_answer:5s} | json: {json_correct}")

if mismatches_2yr:
    print(f"\n⚠️ 2학년 불일치 {len(mismatches_2yr)}개:")
    for m in mismatches_2yr:
        print(f"  {m['num']}번: docx={m['docx']}, json={m['json']} - {m['question']}")
else:
    print("\n✅ 2학년 모든 정답이 일치합니다!")
