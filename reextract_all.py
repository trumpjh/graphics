#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from docx import Document
import json
import re

# 3학년 문서 읽기
doc = Document('(3학년) 광고콘텐츠 재작.docx')

all_text = [p.text.strip() for p in doc.paragraphs if p.text.strip()]

# 문제 추출 (개선된 알고리즘)
questions = []
i = 0

while i < len(all_text):
    text = all_text[i]
    
    # 문제 번호 찾기 (예: "1.", "1번", "1)")
    q_match = re.match(r'^(\d+)[.)번]*\s*(.+)', text)
    
    if q_match:
        q_num = int(q_match.group(1))
        q_text_part = q_match.group(2).strip()
        
        # 선택지 모으기
        options = []
        
        # 현재 문장에 선택지가 있으면 추출
        option_matches = re.findall(r'[①②③④⑤]\s*(.+?)(?=[①②③④⑤]|$)', text)
        
        if option_matches:
            # 같은 줄에 선택지가 있음
            for opt in option_matches:
                options.append(opt.strip())
        else:
            # 다음 줄에서 선택지 찾기
            next_idx = i + 1
            while next_idx < len(all_text) and len(options) < 5:
                next_text = all_text[next_idx]
                
                # 선택지 패턴 찾기
                opt_matches = re.findall(r'[①②③④⑤]\s*(.+?)(?=[①②③④⑤]|$)', next_text)
                
                if opt_matches:
                    for opt in opt_matches:
                        clean_opt = opt.strip()
                        # 다음 문제 번호가 섞여있으면 제거
                        clean_opt = re.sub(r'\d+[.)]*\s*$', '', clean_opt).strip()
                        if clean_opt and len(options) < 5:
                            options.append(clean_opt)
                    
                    # 5개 다 모았으면 이동
                    if len(options) >= 5:
                        i = next_idx
                        break
                elif next_text and next_text[0].isdigit() and '.' in next_text:
                    # 다음 문제 시작
                    break
                
                next_idx += 1
        
        # 35번, 36번은 이미지 문제
        if q_num in [35, 36]:
            q_text_part = f"{q_text_part} [이미지: {q_num}번.png]"
        
        # 5개 선택지 있으면 추가
        if len(options) >= 5:
            questions.append({
                "grade": 3,
                "question": q_text_part,
                "options": options[:5],
                "correct": -1
            })
    
    i += 1

print(f"추출된 질문: {len(questions)}개\n")

# 처음 5개 확인
for i in range(min(5, len(questions))):
    q = questions[i]
    print(f"{i+1}. {q['question'][:70]}...")
    for j, opt in enumerate(q['options']):
        print(f"   {chr(9312+j)} {opt[:50]}...")

# 저장
with open('3rd_grade_all_questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"\n3rd_grade_all_questions.json에 {len(questions)}개 문제 저장")
