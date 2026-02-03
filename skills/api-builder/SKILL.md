---
name: api-builder
description: REST/GraphQL API endpoint generator. Use when user says "API 만들어", "endpoint 생성", "REST API", "GraphQL", or "백엔드 개발".
---

# API Builder

## Instructions
You are a backend architect. Design and generate production-ready API endpoints.

### Step 1: Requirements Gathering
1. **API Type:** REST or GraphQL
2. **Resource:** What entity? (users, products, orders)
3. **Operations:** CRUD, custom actions
4. **Authentication:** JWT, OAuth, API Key

### Step 2: REST API Design

#### Endpoint Conventions
```
GET    /api/v1/users          # List all
GET    /api/v1/users/:id      # Get one
POST   /api/v1/users          # Create
PUT    /api/v1/users/:id      # Update (full)
PATCH  /api/v1/users/:id      # Update (partial)
DELETE /api/v1/users/:id      # Delete
```

#### Response Format
```json
{
  "success": true,
  "data": { ... },
  "meta": {
    "page": 1,
    "limit": 20,
    "total": 100
  },
  "error": null
}
```

#### Error Format
```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid email format",
    "details": [
      {"field": "email", "message": "Must be valid email"}
    ]
  }
}
```

### Step 3: Code Generation

#### FastAPI (Python)
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    email: str
    name: str

class UserResponse(BaseModel):
    id: int
    email: str
    name: str

@app.post("/api/v1/users", response_model=UserResponse)
async def create_user(user: UserCreate):
    # Implementation
    pass

@app.get("/api/v1/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    # Implementation
    pass
```

#### Express (Node.js)
```javascript
const express = require('express');
const router = express.Router();

router.post('/api/v1/users', async (req, res) => {
  try {
    const user = await User.create(req.body);
    res.json({ success: true, data: user });
  } catch (error) {
    res.status(400).json({ success: false, error: error.message });
  }
});

module.exports = router;
```

### Step 4: Documentation (OpenAPI)
```yaml
openapi: 3.0.0
info:
  title: User API
  version: 1.0.0
paths:
  /api/v1/users:
    post:
      summary: Create user
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserCreate'
      responses:
        '201':
          description: Created
```

### Step 5: Output Files
```
api/
├── routes/
│   └── users.py
├── models/
│   └── user.py
├── schemas/
│   └── user.py
├── services/
│   └── user_service.py
└── docs/
    └── openapi.yaml
```

## Quick Commands
| Command | Action |
|---------|--------|
| "User API 만들어" | Full CRUD for users |
| "인증 API 추가해" | Auth endpoints |
| "GraphQL 스키마 만들어" | GraphQL schema |
| "API 문서 생성해" | OpenAPI spec |

## Frameworks Supported
- Python: FastAPI, Django REST, Flask
- Node.js: Express, NestJS
- GraphQL: Strawberry, Apollo
