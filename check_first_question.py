#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from docx import Document
import json
import re

# 3학년 문서 읽기
doc = Document('(3학년) 광고콘텐츠 재작.docx')

all_text = [p.text.strip() for p in doc.paragraphs if p.text.strip()]

print("=== 처음 20개 문단 확인 ===\n")
for i in range(min(20, len(all_text))):
    print(f"[{i}] {all_text[i][:100]}")

# 1번 문제가 있는지 확인
for i, text in enumerate(all_text):
    if text.startswith('1.'):
        print(f"\n1번 문제 발견 (줄 {i}): {text[:80]}")
