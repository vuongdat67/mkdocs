# Testing FastAPI Ormar Alembic Apps

Comprehensive guide to testing FastAPI applications with Ormar ORM and Alembic migrations.

## Setup Test Environment

### 1. Test Database Configuration

```python
# conftest.py
import pytest
import asyncio
from sqlalchemy import create_engine
from ormar import ModelMeta

DATABASE_URL = "sqlite:///./test.db"

@pytest.fixture(scope="session")
def event_loop():
    """Create event loop for async tests."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="function")
async def database():
    """Create fresh database for each test."""
    engine = create_engine(DATABASE_URL)
    metadata.create_all(engine)
    
    yield
    
    metadata.drop_all(engine)
    engine.dispose()
```

### 2. Test Client Setup

```python
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client(database):
    """Create test client."""
    with TestClient(app) as client:
        yield client
```

## Testing Models

### Simple Model Test

```python
# tests/test_models.py
import pytest
from app.models import User

@pytest.mark.asyncio
async def test_create_user(database):
    """Test user creation."""
    user = await User.objects.create(
        email="test@example.com",
        username="testuser"
    )
    
    assert user.id is not None
    assert user.email == "test@example.com"
    assert user.username == "testuser"

@pytest.mark.asyncio
async def test_user_unique_email(database):
    """Test email uniqueness constraint."""
    await User.objects.create(
        email="test@example.com",
        username="user1"
    )
    
    with pytest.raises(Exception):
        await User.objects.create(
            email="test@example.com",
            username="user2"
        )
```

## Testing Endpoints

### Basic CRUD Tests

```python
# tests/test_api.py
def test_create_user_endpoint(client):
    """Test POST /users endpoint."""
    response = client.post(
        "/users",
        json={
            "email": "test@example.com",
            "username": "testuser"
        }
    )
    
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_get_user(client):
    """Test GET /users/{id} endpoint."""
    # Create user
    create_response = client.post(
        "/users",
        json={"email": "test@example.com", "username": "test"}
    )
    user_id = create_response.json()["id"]
    
    # Get user
    response = client.get(f"/users/{user_id}")
    
    assert response.status_code == 200
    assert response.json()["id"] == user_id

def test_update_user(client):
    """Test PUT /users/{id} endpoint."""
    # Create user
    create_response = client.post(
        "/users",
        json={"email": "test@example.com", "username": "test"}
    )
    user_id = create_response.json()["id"]
    
    # Update user
    response = client.put(
        f"/users/{user_id}",
        json={"username": "updated"}
    )
    
    assert response.status_code == 200
    assert response.json()["username"] == "updated"

def test_delete_user(client):
    """Test DELETE /users/{id} endpoint."""
    # Create user
    create_response = client.post(
        "/users",
        json={"email": "test@example.com", "username": "test"}
    )
    user_id = create_response.json()["id"]
    
    # Delete user
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 204
    
    # Verify deletion
    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 404
```

## Testing with Alembic Migrations

### Migration Test Setup

```python
# tests/test_migrations.py
import pytest
from alembic.config import Config
from alembic import command

@pytest.fixture
def alembic_config():
    """Create Alembic configuration."""
    config = Config("alembic.ini")
    config.set_main_option("sqlalchemy.url", DATABASE_URL)
    return config

def test_migrations_run_successfully(alembic_config):
    """Test that migrations run without errors."""
    command.upgrade(alembic_config, "head")
    command.downgrade(alembic_config, "base")
```

## Testing with Factories

Using `factory_boy` for test data generation:

```python
# tests/factories.py
import factory
from app.models import User

class UserFactory(factory.Factory):
    class Meta:
        model = User
    
    email = factory.Sequence(lambda n: f"user{n}@example.com")
    username = factory.Sequence(lambda n: f"user{n}")
    is_active = True

# Usage in tests
@pytest.mark.asyncio
async def test_with_factory(database):
    """Test using factory."""
    user_data = UserFactory.build()
    user = await User.objects.create(**user_data.__dict__)
    
    assert user.email == user_data.email
```

## Async Tests Tips

!!! tip "Pytest Asyncio"
    Always mark async tests with `@pytest.mark.asyncio`

```python
@pytest.mark.asyncio
async def test_async_operation():
    """Example async test."""
    result = await some_async_function()
    assert result is not None
```

## Coverage Report

```bash
# Install coverage
pip install pytest-cov

# Run tests with coverage
pytest --cov=app --cov-report=html

# View coverage
open htmlcov/index.html
```

## Complete Example: pytest.ini

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
asyncio_mode = auto
addopts = 
    -v
    --strict-markers
    --cov=app
    --cov-report=term-missing
    --cov-report=html
```

## Best Practices

1. ✅ **Isolate tests** - Each test should be independent
2. ✅ **Use fixtures** - Reuse common setup code
3. ✅ **Test edge cases** - Not just happy paths
4. ✅ **Mock external services** - Don't make real API calls
5. ✅ **Use factories** - Generate test data easily
6. ✅ **Check coverage** - Aim for >80% coverage

## Common Pitfalls

!!! warning "Database State"
    Always clean up database state between tests!

!!! warning "Async/Await"
    Don't forget `await` in async tests!

```python
# ❌ Wrong
async def test_create():
    user = User.objects.create(email="test@test.com")  # Missing await!

# ✅ Correct
async def test_create():
    user = await User.objects.create(email="test@test.com")
```

Happy testing! 🧪✨
