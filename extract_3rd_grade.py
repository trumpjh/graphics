#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from docx import Document
import json
import re

# 3학년 문서 읽기
doc = Document('(3학년) 광고콘텐츠 재작.docx')

# 문제 추출
questions = []

for para in doc.paragraphs:
    text = para.text.strip()
    
    if not text:
        continue
    
    # 문제 번호 찾기 (예: "1. 다음 중...")
    q_match = re.match(r'^(\d+)\.\s*(.+)', text)
    
    if q_match:
        q_num = int(q_match.group(1))
        full_text = text
        
        # 선택지와 질문 분리
        # 패턴: "번호. 질문 ① 선택1 ② 선택2 ③ 선택3 ④ 선택4 ⑤ 선택5"
        
        # 먼저 원형 숫자로 분리
        parts = re.split(r'[①②③④⑤]\s*', full_text)
        
        if len(parts) > 1:
            # 첫 부분은 번호와 질문
            question_part = parts[0]
            question_part = re.sub(r'^\d+\.\s*', '', question_part).strip()
            
            # 35번, 36번은 이미지 처리
            if q_num in [35, 36]:
                question_part = f"{question_part} [이미지: {q_num}번.png]"
            
            # 나머지는 선택지
            options = [opt.strip() for opt in parts[1:6]]  # 최대 5개
            
            # 선택지 끝에서 다음 문제 번호 제거
            options = [re.sub(r'\s*\d+\.\s*$', '', opt).strip() for opt in options]
            
            if question_part and len(options) == 5:
                questions.append({
                    "grade": 3,
                    "question": question_part,
                    "options": options,
                    "correct": -1
                })

print(f"\n추출된 문제 수: {len(questions)}")
print("\n처음 5개 문제:")
for i, q in enumerate(questions[:5]):
    print(f"\n문제 {i+1}:")
    print(f"  질문: {q['question'][:80]}...")
    print(f"  선택지: {len(q['options'])}개")
    for j, opt in enumerate(q['options'][:5]):
        print(f"    {chr(9312+j)}. {opt[:50]}...")

# 미리보기 저장
with open('3rd_grade_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(questions[:10], f, ensure_ascii=False, indent=2)

print(f"\n처음 10개 미리보기를 3rd_grade_extracted.json에 저장")

# 전체 저장
with open('3rd_grade_full.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"전체 {len(questions)}개 문제를 3rd_grade_full.json에 저장")

# 첫 번째 문제도 수동 추가 (1번 문제)
print("\n1번 문제 추가 확인:")
if len(questions) > 0:
    print(f"첫 번째 질문: {questions[0]['question'][:60]}")
    print(f"첫 번째 정답이 필요한지 확인")
