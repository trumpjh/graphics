#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from docx import Document

# 3학년 문서 읽기
doc = Document('(3학년) 광고콘텐츠 재작.docx')

all_text = []
for para in doc.paragraphs:
    text = para.text.strip()
    if text:
        all_text.append(text)

print("=== 전체 텍스트 개수 ===")
print(f"전체 단락: {len(all_text)}\n")

print("=== 정답 섹션 (뒤에서부터 200줄) ===\n")

# 뒤에서부터 200줄 출력
start_idx = max(0, len(all_text) - 200)
for i in range(start_idx, len(all_text)):
    line = all_text[i]
    print(f"[{i-start_idx}] {line}")

print("\n\n=== '정답' 또는 '답:' 포함 줄 찾기 ===\n")
for i, line in enumerate(all_text):
    if '정답' in line or '답:' in line or '답(' in line:
        print(f"[{i}] {line}")
