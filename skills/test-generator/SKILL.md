---
name: test-generator
description: Automated test case generator. Use when user says "테스트 코드", "unit test", "테스트 작성", "pytest", or "jest test".
---

# Test Generator

## Instructions
You are a QA engineer. Generate comprehensive test suites with high coverage.

### Step 1: Test Strategy
1. **Test Type:**
   - Unit Tests (individual functions)
   - Integration Tests (components together)
   - E2E Tests (full user flows)

2. **Coverage Goals:**
   - Happy path (normal flow)
   - Edge cases (boundaries)
   - Error cases (failures)

### Step 2: Test Structure

#### AAA Pattern
```python
def test_example():
    # Arrange - Setup test data
    user = User(name="Test")

    # Act - Execute the code
    result = user.get_greeting()

    # Assert - Verify the result
    assert result == "Hello, Test!"
```

#### Given-When-Then (BDD)
```python
def test_user_login():
    # Given a registered user
    user = create_user(email="test@test.com")

    # When they login with correct password
    response = login(email="test@test.com", password="correct")

    # Then they should receive a token
    assert response.status_code == 200
    assert "token" in response.json()
```

### Step 3: Python (pytest)

#### Basic Tests
```python
import pytest
from app.services import UserService

class TestUserService:

    @pytest.fixture
    def user_service(self):
        return UserService()

    def test_create_user_success(self, user_service):
        """Test successful user creation."""
        user = user_service.create(
            email="test@example.com",
            name="Test User"
        )
        assert user.id is not None
        assert user.email == "test@example.com"

    def test_create_user_duplicate_email(self, user_service):
        """Test duplicate email raises error."""
        user_service.create(email="test@example.com", name="User 1")

        with pytest.raises(ValueError, match="Email already exists"):
            user_service.create(email="test@example.com", name="User 2")

    @pytest.mark.parametrize("email,expected", [
        ("valid@email.com", True),
        ("invalid", False),
        ("", False),
        (None, False),
    ])
    def test_email_validation(self, user_service, email, expected):
        """Test email validation with various inputs."""
        result = user_service.validate_email(email)
        assert result == expected
```

#### Async Tests
```python
import pytest

@pytest.mark.asyncio
async def test_async_fetch():
    result = await fetch_data()
    assert result is not None
```

#### Mocking
```python
from unittest.mock import Mock, patch

def test_external_api_call():
    with patch('app.services.external_api') as mock_api:
        mock_api.get_data.return_value = {"status": "ok"}

        result = process_data()

        assert result["status"] == "ok"
        mock_api.get_data.assert_called_once()
```

### Step 4: JavaScript (Jest)

```javascript
describe('UserService', () => {
  let userService;

  beforeEach(() => {
    userService = new UserService();
  });

  describe('createUser', () => {
    it('should create user with valid data', async () => {
      const user = await userService.create({
        email: 'test@example.com',
        name: 'Test User'
      });

      expect(user.id).toBeDefined();
      expect(user.email).toBe('test@example.com');
    });

    it('should throw error for duplicate email', async () => {
      await userService.create({ email: 'test@example.com', name: 'User 1' });

      await expect(
        userService.create({ email: 'test@example.com', name: 'User 2' })
      ).rejects.toThrow('Email already exists');
    });
  });

  describe.each([
    ['valid@email.com', true],
    ['invalid', false],
    ['', false],
  ])('validateEmail(%s)', (email, expected) => {
    it(`should return ${expected}`, () => {
      expect(userService.validateEmail(email)).toBe(expected);
    });
  });
});
```

### Step 5: Test Report
```
============ Test Results ============
Total:    45
Passed:   42
Failed:   2
Skipped:  1
Coverage: 87%

Failed Tests:
- test_user_service.py::test_edge_case
- test_api.py::test_timeout

Coverage Report:
- services/user.py: 92%
- services/order.py: 85%
- utils/helpers.py: 78%
======================================
```

## Quick Commands
| Command | Action |
|---------|--------|
| "이 함수 테스트 만들어" | Unit tests for function |
| "API 테스트 작성해" | Integration tests |
| "커버리지 높여줘" | Add missing test cases |
| "모킹 처리해줘" | Add mock objects |

## Output
- `tests/test_{module}.py`
- `tests/conftest.py` (fixtures)
- Coverage report
