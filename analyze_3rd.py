#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from docx import Document

# 3학년 문서 읽기
doc = Document('(3학년) 광고콘텐츠 재작.docx')

print("=== 3학년 광고콘텐츠 재작.docx 구조 분석 ===\n")

# 처음 30개 문단 출력
for i, para in enumerate(doc.paragraphs[:50]):
    text = para.text.strip()
    if text:
        print(f"[{i}] {text[:100]}")
        if i > 50:
            break
