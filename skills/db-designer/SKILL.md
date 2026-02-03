---
name: db-designer
description: Database schema designer with ERD. Use when user says "DB 설계", "database schema", "테이블 설계", "ERD", or "데이터 모델링".
---

# DB Designer

## Instructions
You are a database architect. Design normalized, scalable database schemas.

### Step 1: Requirements Analysis
1. **Entities:** What objects need to be stored?
2. **Relationships:** How are they connected?
3. **Cardinality:** 1:1, 1:N, N:M
4. **Constraints:** Required fields, unique, foreign keys

### Step 2: Schema Design Principles

#### Normalization Rules
```
1NF: Atomic values, no repeating groups
2NF: No partial dependencies
3NF: No transitive dependencies
BCNF: Every determinant is a candidate key
```

#### Naming Conventions
```
Tables: plural, snake_case (users, order_items)
Columns: singular, snake_case (user_id, created_at)
Primary Key: id or {table}_id
Foreign Key: {referenced_table}_id
Timestamps: created_at, updated_at, deleted_at
```

### Step 3: ERD Generation (ASCII)
```
┌─────────────┐       ┌─────────────┐
│   users     │       │   orders    │
├─────────────┤       ├─────────────┤
│ id (PK)     │──┐    │ id (PK)     │
│ email       │  │    │ user_id (FK)│──┐
│ name        │  └───>│ total       │  │
│ created_at  │       │ status      │  │
└─────────────┘       │ created_at  │  │
                      └─────────────┘  │
                            │          │
                            ▼          │
                      ┌─────────────┐  │
                      │ order_items │  │
                      ├─────────────┤  │
                      │ id (PK)     │  │
                      │ order_id(FK)│──┘
                      │ product_id  │
                      │ quantity    │
                      │ price       │
                      └─────────────┘
```

### Step 4: SQL Generation

#### PostgreSQL
```sql
-- Users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Orders table
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    total DECIMAL(10,2) NOT NULL,
    status VARCHAR(20) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_status ON orders(status);
```

#### SQLAlchemy (Python ORM)
```python
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    orders = relationship("Order", back_populates="user")

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    total = Column(Numeric(10, 2))

    user = relationship("User", back_populates="orders")
```

### Step 5: Output
```
database/
├── schema.sql          # Raw SQL
├── migrations/         # Version controlled changes
├── models.py           # ORM models
├── erd.md              # ASCII ERD diagram
└── data_dictionary.md  # Column descriptions
```

## Quick Commands
| Command | Action |
|---------|--------|
| "이커머스 DB 설계해" | E-commerce schema |
| "ERD 그려줘" | ASCII ERD diagram |
| "마이그레이션 만들어" | Migration file |
| "인덱스 추천해줘" | Index optimization |

## Databases Supported
- PostgreSQL
- MySQL
- SQLite
- MongoDB (document design)
