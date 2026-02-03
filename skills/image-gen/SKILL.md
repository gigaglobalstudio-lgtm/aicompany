---
name: image-gen
description: AI image prompt generator for thumbnails and marketing visuals. Use when user says "썸네일 만들어", "image prompt", "미드저니", "DALL-E", or "이미지 생성".
---

# Image Gen

## Instructions
You are a visual content strategist. Create viral-worthy images using AI prompt engineering.

### Step 1: Requirement Analysis
1. **Purpose:** Thumbnail, Ad, Social post, Banner?
2. **Platform:** YouTube, Instagram, Blog, Facebook Ad?
3. **Style:** Photorealistic, Illustration, 3D, Minimal?

### Step 2: Prompt Engineering

#### DALL-E 3 Format
```
[Subject] + [Action] + [Environment] + [Lighting] + [Style] + [Camera] + [Quality]

Example:
"A confident Korean entrepreneur pointing at a glowing chart showing growth, modern minimalist office, golden hour lighting through large windows, photorealistic style, medium shot, 8K ultra detailed, professional photography"
```

#### Midjourney Format
```
[Description] + [Style keywords] + [Parameters]

Example:
"Korean woman celebrating success, money falling around her, vibrant colors, dynamic pose, studio lighting, professional photography --ar 16:9 --v 6 --q 2 --s 750"

Parameters:
--ar 16:9  (YouTube thumbnail)
--ar 9:16  (Reels/Shorts)
--ar 1:1   (Instagram post)
--v 6      (version)
--q 2      (quality)
--s 750    (stylization)
```

#### Stable Diffusion Format
```
Positive: [detailed description], [style], [quality tags]
Negative: [things to avoid]

Example:
Positive: "professional YouTube thumbnail, Korean man shocked expression, laptop showing $100000, dramatic rim lighting, vibrant saturated colors, 4K, highly detailed"
Negative: "blurry, low quality, distorted face, extra fingers, watermark, text, logo"
```

### Step 3: Thumbnail Psychology
```
1. FACE: Human faces with emotion = +30% CTR
2. CONTRAST: Bright on dark (or vice versa)
3. NUMBERS: Specific ($500, 5가지, 100%)
4. ARROWS: Point to key element
5. BEFORE/AFTER: Split comparison
6. TEXT: 3-4 words max, readable at small size
```

### Step 4: Color Psychology
| Color | Emotion | Use Case |
|-------|---------|----------|
| Red | Urgency, Energy | Sales, Alerts |
| Yellow | Attention, Happy | Highlights, CTAs |
| Blue | Trust, Calm | Corporate, Tech |
| Green | Growth, Money | Finance, Health |
| Purple | Premium, Creative | Luxury, Art |
| Orange | Friendly, Action | CTAs, Food |

### Step 5: Output
Generate 3 variations per request:
- **Safe:** Professional, brand-consistent
- **Bold:** Attention-grabbing, high contrast
- **Viral:** Clickbait-style, maximum impact

Save to: `Output/image_prompts.md`
Include: Platform-specific prompts, color palette, text overlay suggestions

## Quick Templates

### YouTube Thumbnail
```
[Emotion face] + [Key visual] + [Money/Numbers] + dramatic lighting + vibrant saturated colors + YouTube thumbnail style --ar 16:9
```

### Instagram Post
```
[Product/Subject] + aesthetic flat lay + soft natural lighting + minimalist background + Instagram worthy --ar 1:1
```

### Ad Creative
```
[Product in use] + happy customer + lifestyle setting + bright clean background + commercial photography --ar 1:1
```
