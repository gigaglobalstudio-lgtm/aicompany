---
name: doc-generator
description: Technical documentation generator. Use when user says "문서화", "documentation", "README 작성", "API docs", or "기술 문서".
---

# Doc Generator

## Instructions
You are a technical writer. Create clear, comprehensive documentation.

### Step 1: Documentation Types
1. **README.md** - Project overview
2. **API Documentation** - Endpoint reference
3. **Architecture Docs** - System design
4. **User Guide** - How to use
5. **Contributing Guide** - How to contribute

### Step 2: README Template

```markdown
# Project Name

Brief description of the project.

## Features

- Feature 1
- Feature 2
- Feature 3

## Tech Stack

- Python 3.11+
- FastAPI
- PostgreSQL
- Redis

## Quick Start

### Prerequisites

- Python 3.11+
- Docker (optional)

### Installation

\`\`\`bash
# Clone the repository
git clone https://github.com/user/project.git
cd project

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp .env.example .env

# Run the application
python main.py
\`\`\`

### Docker

\`\`\`bash
docker-compose up -d
\`\`\`

## Usage

\`\`\`python
from project import Client

client = Client(api_key="your-key")
result = client.do_something()
\`\`\`

## API Reference

See [API Documentation](docs/api.md)

## Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| DATABASE_URL | Database connection | sqlite:///db.sqlite |
| API_KEY | API authentication | None |

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing`)
5. Open Pull Request

## License

MIT License - see [LICENSE](LICENSE)
```

### Step 3: API Documentation

```markdown
# API Documentation

## Base URL

\`\`\`
https://api.example.com/v1
\`\`\`

## Authentication

All endpoints require Bearer token:

\`\`\`
Authorization: Bearer <token>
\`\`\`

## Endpoints

### Users

#### Create User

\`\`\`
POST /users
\`\`\`

**Request Body:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| email | string | Yes | User email |
| name | string | Yes | User name |
| password | string | Yes | Min 8 chars |

**Example:**

\`\`\`json
{
  "email": "user@example.com",
  "name": "John Doe",
  "password": "securepass123"
}
\`\`\`

**Response:**

\`\`\`json
{
  "success": true,
  "data": {
    "id": 1,
    "email": "user@example.com",
    "name": "John Doe",
    "created_at": "2024-01-15T10:30:00Z"
  }
}
\`\`\`

**Errors:**

| Code | Message |
|------|---------|
| 400 | Invalid email format |
| 409 | Email already exists |
```

### Step 4: Architecture Documentation

```markdown
# System Architecture

## Overview

\`\`\`
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Client    │────>│   API GW    │────>│  Services   │
│  (Web/App)  │     │  (Nginx)    │     │  (FastAPI)  │
└─────────────┘     └─────────────┘     └─────────────┘
                                              │
                    ┌─────────────────────────┼─────────────────────────┐
                    │                         │                         │
                    ▼                         ▼                         ▼
             ┌─────────────┐          ┌─────────────┐          ┌─────────────┐
             │  PostgreSQL │          │    Redis    │          │     S3      │
             │    (DB)     │          │   (Cache)   │          │  (Storage)  │
             └─────────────┘          └─────────────┘          └─────────────┘
\`\`\`

## Components

### API Gateway
- Load balancing
- SSL termination
- Rate limiting

### Application Services
- User Service
- Order Service
- Payment Service

### Data Layer
- PostgreSQL: Primary database
- Redis: Caching, sessions
- S3: File storage

## Data Flow

1. Client sends request to API Gateway
2. Gateway routes to appropriate service
3. Service processes request
4. Response returned to client
```

### Step 5: Docstring Standards

#### Python (Google Style)
```python
def calculate_total(items: list[dict], discount: float = 0) -> float:
    """Calculate total price with optional discount.

    Args:
        items: List of items with 'price' and 'quantity' keys.
        discount: Discount percentage (0-100). Defaults to 0.

    Returns:
        Total price after discount.

    Raises:
        ValueError: If discount is not between 0 and 100.

    Example:
        >>> items = [{"price": 10, "quantity": 2}]
        >>> calculate_total(items, discount=10)
        18.0
    """
    pass
```

#### JavaScript (JSDoc)
```javascript
/**
 * Calculate total price with optional discount.
 * @param {Array<{price: number, quantity: number}>} items - List of items
 * @param {number} [discount=0] - Discount percentage (0-100)
 * @returns {number} Total price after discount
 * @throws {Error} If discount is not between 0 and 100
 * @example
 * const items = [{price: 10, quantity: 2}];
 * calculateTotal(items, 10); // Returns 18
 */
function calculateTotal(items, discount = 0) {
  // ...
}
```

## Quick Commands
| Command | Action |
|---------|--------|
| "README 만들어" | Generate README.md |
| "API 문서 작성해" | API documentation |
| "아키텍처 문서 만들어" | System design docs |
| "함수 주석 추가해" | Add docstrings |

## Output
- `README.md`
- `docs/api.md`
- `docs/architecture.md`
- `CONTRIBUTING.md`
- `CHANGELOG.md`
