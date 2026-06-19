#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

print("="*60)
print("변경 사항 검증")
print("="*60)

# 3학년 #55 확인
print("\n【3학년 #55 문제】")
with open('3rd_grade_complete.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    if len(data) > 54:
        q55 = data[54]
        print(f"문제: {q55['question'][:80]}...")
        print(f"선택지: {q55['options']}")
        print(f"정답: {q55['correct']}")
        
        # 기호로 표시
        symbols = ['①', '②', '③', '④', '⑤']
        if isinstance(q55['correct'], list):
            ans_symbols = ','.join(symbols[i] for i in q55['correct'] if 0 <= i < len(symbols))
        else:
            ans_symbols = symbols[q55['correct']] if 0 <= q55['correct'] < len(symbols) else str(q55['correct'])
        print(f"정답 (기호): {ans_symbols}")

# 2학년 #41 확인
print("\n" + "="*60)
print("【2학년 #41 문제】")
with open('questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    if len(data) > 40:
        q41 = data[40]
        print(f"문제: {q41['question'][:80]}...")
        print(f"선택지: {q41['options']}")
        print(f"정답: {q41['correct']}")
        
        symbols = ['①', '②', '③', '④', '⑤']
        ans_symbol = symbols[q41['correct']] if 0 <= q41['correct'] < len(symbols) else str(q41['correct'])
        print(f"정답 (기호): {ans_symbol}")

# docx 파일의 정답과 비교
print("\n" + "="*60)
print("【docx 파일과 비교】")
with open('all_extracted_answers.json', 'r', encoding='utf-8') as f:
    docx_answers = json.load(f)
    
    print("\n3학년 #55 (docx): ③,⑤")
    print(f"3학년 #55 (JSON): {ans_symbols}")
    print(f"일치: {'✓' if ans_symbols == '③,⑤' else '✗'}")
    
    print("\n2학년 #41 (docx): ④")
    print(f"2학년 #41 (JSON): {ans_symbol}")
    print(f"일치: {'✓' if ans_symbol == '④' else '✗'}")

print("\n" + "="*60)
print("검증 완료!")
print("="*60)
