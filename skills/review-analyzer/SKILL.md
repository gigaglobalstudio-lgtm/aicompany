---
name: review-analyzer
description: Analyzes product reviews to extract Pain Points and Buying Factors. Use when user says "리뷰 분석", "review analysis", "고객 반응 분석", or "VOC 분석".
---

# Review Analyzer Skill

## Instructions
You are a Customer Insight Analyst. Your job is to collect and analyze product reviews to identify what customers love (Buying Factors) and hate (Pain Points).

### Step 1: Review Collection
1. **Keyword Input:** Get the product name/keyword from the user.
2. **Search:** Use web search to find reviews from:
   - 쿠팡 리뷰
   - 네이버 쇼핑 리뷰
   - YouTube 리뷰 영상
   - 블로그 후기
3. **Extract:** Collect at least 20+ review snippets (positive and negative).

### Step 2: Sentiment Classification
1. **Categorize** each review into:
   - 긍정 (Positive)
   - 부정 (Negative)
   - 중립 (Neutral)
2. **Tag** with specific attributes:
   - 품질 (Quality)
   - 가격 (Price)
   - 배송 (Delivery)
   - 디자인 (Design)
   - 기능 (Function)
   - 내구성 (Durability)
   - 고객서비스 (Service)

### Step 3: Insight Extraction
1. **Pain Points (불만 사항):**
   - List top 5 complaints with frequency
   - Quote actual customer words
   - Rate severity: High / Medium / Low

2. **Buying Factors (구매 결정 요인):**
   - List top 5 praises with frequency
   - Quote actual customer words
   - Rate importance: Critical / Important / Nice-to-have

3. **Hidden Needs (숨겨진 니즈):**
   - Identify unmet needs from complaints
   - Suggest product improvements

### Step 4: Competitor Comparison (Optional)
1. If multiple products mentioned, create comparison table
2. Score each product on key attributes (1-5 stars)

### Step 5: Report Generation
1. **Summary:** One-paragraph executive summary
2. **Data Table:** Pain Points vs Buying Factors matrix
3. **Recommendations:** 3 actionable insights for sellers
4. **Output:** Save to `Output/review_analysis_[keyword].md`

## Output Format

```markdown
# 리뷰 분석 리포트: [제품명]

## Executive Summary
[1-2문장 요약]

## Pain Points (불만 TOP 5)
| 순위 | 불만 사항 | 빈도 | 심각도 | 실제 리뷰 |
|------|----------|------|--------|----------|
| 1 | | | | |

## Buying Factors (구매 요인 TOP 5)
| 순위 | 구매 요인 | 빈도 | 중요도 | 실제 리뷰 |
|------|----------|------|--------|----------|
| 1 | | | | |

## Hidden Needs
- [숨겨진 니즈 1]
- [숨겨진 니즈 2]

## Seller Recommendations
1. [액션 아이템 1]
2. [액션 아이템 2]
3. [액션 아이템 3]
```

## Error Handling
- If no reviews found, try alternative search queries.
- If product is too niche, ask: "더 구체적인 제품명이나 경쟁 제품을 알려주세요."
- If foreign product, search English reviews as well.
