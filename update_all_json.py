#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os

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

# 변경 사항
changes_3rd = {55: [2, 4]}  # 문제 #55: ⑤ → [③, ⑤]
changes_2nd = {41: 3}       # 문제 #41: ① → ④

# 3학년 파일들 처리
third_grade_files = [
    '3rd_grade_all_questions.json',
    '3rd_grade_answers.json',
    '3rd_grade_complete.json',
    '3rd_grade_extracted.json',
    '3rd_grade_full.json',
    '3rd_grade_preview.json'
]

print("="*60)
print("3학년 JSON 파일 수정")
print("="*60)

for filename in third_grade_files:
    filepath = filename
    if not os.path.exists(filepath):
        print(f"파일 없음: {filename}")
        continue
    
    print(f"\n파일: {filename}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 파일 형식 판단 (배열인지 딕셔너리인지)
        if isinstance(data, list):
            # 배열 형식 (문제들의 리스트)
            if len(data) > 54:  # 55번 문제는 인덱스 54
                old_val = data[54].get('correct') if isinstance(data[54], dict) else None
                if old_val is not None:
                    data[54]['correct'] = changes_3rd[55]
                    print(f"  문제 #55 수정: {old_val} → {changes_3rd[55]}")
        
        elif isinstance(data, dict):
            # 딕셔너리 형식 (문제 번호를 키로 사용)
            if '55' in data or 55 in data:
                key = '55' if '55' in data else 55
                if isinstance(data[key], dict):
                    old_val = data[key].get('correct')
                    if old_val is not None:
                        data[key]['correct'] = changes_3rd[55]
                        print(f"  문제 #55 수정: {old_val} → {changes_3rd[55]}")
                else:
                    # 답 파일인 경우
                    data[key] = changes_3rd[55]
                    print(f"  문제 #55 수정: → {changes_3rd[55]}")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"  저장 완료")
    
    except Exception as e:
        print(f"  오류: {e}")

# 2학년 파일들 처리
second_grade_files = [
    'questions.json',
    'questions_new.json'
]

print("\n" + "="*60)
print("2학년 JSON 파일 수정")
print("="*60)

for filename in second_grade_files:
    filepath = filename
    if not os.path.exists(filepath):
        print(f"파일 없음: {filename}")
        continue
    
    print(f"\n파일: {filename}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if isinstance(data, list):
            if len(data) > 40:  # 41번 문제는 인덱스 40
                old_val = data[40].get('correct') if isinstance(data[40], dict) else None
                if old_val is not None:
                    data[40]['correct'] = changes_2nd[41]
                    print(f"  문제 #41 수정: {old_val} → {changes_2nd[41]}")
        
        elif isinstance(data, dict):
            if '41' in data or 41 in data:
                key = '41' if '41' in data else 41
                if isinstance(data[key], dict):
                    old_val = data[key].get('correct')
                    if old_val is not None:
                        data[key]['correct'] = changes_2nd[41]
                        print(f"  문제 #41 수정: {old_val} → {changes_2nd[41]}")
                else:
                    data[key] = changes_2nd[41]
                    print(f"  문제 #41 수정: → {changes_2nd[41]}")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"  저장 완료")
    
    except Exception as e:
        print(f"  오류: {e}")

print("\n" + "="*60)
print("모든 JSON 파일 수정 완료!")
print("="*60)
print("\n변경 사항:")
print("  3학년 #55: ⑤ → [③, ⑤]")
print("  2학년 #41: ① → ④")
