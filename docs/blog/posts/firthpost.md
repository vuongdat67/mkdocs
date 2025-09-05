---
date:
    created: 2025-01-09
    updated: 2025-02-09
readtime: 5
categories:
    - AI
tags:
    - AI
---

# E-commerce Platform - AI Coding Workflow

## Dự án: Full-stack E-commerce Platform

**Tech Stack**: React (Frontend), Node.js/Express (Backend), MongoDB (Database), Redis (Cache)
<!-- more -->
-----

## Phase 1: Project Setup & Architecture

### Prompt 1.1: Project Architecture

```
CONTEXT: Building a scalable e-commerce platform with microservices architecture
TECH STACK: React, Node.js, Express, MongoDB, Redis, Docker
REQUIREMENTS:
- User authentication & authorization
- Product catalog management
- Shopping cart & checkout
- Order management
- Payment integration
- Admin dashboard

Create a complete project structure with:
1. Folder organization for frontend/backend
2. Database schema design
3. API endpoints planning
4. Security considerations
5. Scalability architecture

Include package.json for both frontend/backend with all necessary dependencies.
```

### Prompt 1.2: Database Design

```
CONTEXT: E-commerce platform database design
REQUIREMENTS:
- Users (customers, admins)
- Products (categories, variants, inventory)
- Orders (items, status, payment)
- Reviews & ratings
- Shopping cart persistence

Design MongoDB schemas with:
1. Collections structure
2. Relationships between collections
3. Indexing strategy for performance
4. Data validation rules
5. Sample data for testing

Provide Mongoose schemas with proper validation and middleware.
```

-----

## Phase 2: Backend Development

### Prompt 2.1: Authentication System

```
CONTEXT: E-commerce backend - User authentication
CURRENT STATE: Basic Express server setup with MongoDB connection
GOAL: Implement secure JWT-based authentication

REQUIREMENTS:
- User registration/login
- Password hashing (bcrypt)
- JWT token generation/validation
- Role-based access control (customer/admin)
- Password reset functionality
- Email verification

CONSTRAINTS:
- Use industry security best practices
- Implement rate limiting
- Secure cookie handling
- Input validation & sanitization

Provide complete auth middleware, controllers, and routes.
```

### Prompt 2.2: Product Management API

```
CONTEXT: E-commerce backend - Product management
CURRENT STATE: 
[Attach current auth system files]
GOAL: Build comprehensive product CRUD API with advanced features

REQUIREMENTS:
- Product CRUD operations
- Category management
- Image upload handling
- Search & filtering
- Pagination
- Inventory tracking

FEATURES:
- Full-text search
- Price filtering
- Category filtering
- Sorting options
- Bulk operations (admin only)

Provide controllers, routes, and middleware with proper error handling.
```

### Prompt 2.3: Shopping Cart & Checkout

```
CONTEXT: E-commerce backend - Shopping cart and checkout system
CURRENT STATE: 
- Auth system implemented
- Product API completed
- [Attach relevant files]

GOAL: Implement persistent shopping cart and secure checkout process

REQUIREMENTS:
- Add/remove/update cart items
- Cart persistence (Redis + MongoDB backup)
- Price calculations
- Inventory validation
- Checkout process
- Order creation

BUSINESS LOGIC:
- Stock validation before checkout
- Price consistency checks
- Cart expiration handling
- Guest cart to user cart migration

Include Redis integration and proper error handling for edge cases.
```

-----

## Phase 3: Frontend Development

### Prompt 3.1: React App Structure

```
CONTEXT: E-commerce frontend - React application setup
BACKEND: REST API with auth, products, cart endpoints available
GOAL: Create scalable React app with modern patterns

REQUIREMENTS:
- Redux Toolkit for state management
- React Router for navigation
- Axios for API calls
- Material-UI/Tailwind for styling
- Form validation (Formik/React Hook Form)

STRUCTURE:
- Components architecture (atomic design)
- Custom hooks for API calls
- Error boundary implementation
- Loading states management
- Responsive design

Create folder structure and core setup files with TypeScript configuration.
```

### Prompt 3.2: Product Catalog Frontend

```
CONTEXT: E-commerce frontend - Product catalog pages
CURRENT STATE: [Attach React app structure and API integration setup]
BACKEND API: Product endpoints with search, filter, pagination

GOAL: Build complete product browsing experience

COMPONENTS NEEDED:
- ProductList with pagination
- ProductCard component
- ProductDetail page
- SearchBar with filters
- CategoryNavigation
- ProductImages gallery

FEATURES:
- Infinite scroll or pagination
- Advanced filtering UI
- Search with debouncing
- Product image zoom
- Related products
- Reviews display

Include responsive design and proper state management with Redux.
```

### Prompt 3.3: Shopping Cart & Checkout UI

```
CONTEXT: E-commerce frontend - Shopping cart and checkout
CURRENT STATE: [Attach product components and Redux store setup]
BACKEND: Cart API and checkout endpoints ready

GOAL: Complete shopping cart and checkout flow

COMPONENTS:
- Cart sidebar/page
- CartItem component
- Checkout multi-step form
- PaymentForm component
- OrderSummary component
- OrderConfirmation page

FEATURES:
- Real-time cart updates
- Quantity adjustment
- Remove items with confirmation
- Form validation
- Payment integration UI
- Order tracking

Implement with proper UX patterns and error handling.
```

-----

## Phase 4: Advanced Features

### Prompt 4.1: Admin Dashboard

```
CONTEXT: E-commerce admin dashboard
CURRENT STATE: [Attach all previous components and API]
GOAL: Complete admin panel for platform management

REQUIREMENTS:
- Dashboard with analytics
- Product management interface
- Order management system
- User management
- Inventory tracking
- Sales reports

COMPONENTS:
- DataTable with CRUD operations
- Charts and analytics
- Bulk actions interface
- Export functionality
- Role management

Use admin-specific routing and enhanced security checks.
```

### Prompt 4.2: Performance Optimization

```
CONTEXT: E-commerce platform performance optimization
CURRENT STATE: [Complete application built]
GOAL: Optimize for production performance

AREAS TO OPTIMIZE:
- Database queries and indexing
- API response caching
- Frontend bundle optimization
- Image optimization
- Lazy loading implementation
- CDN integration

REQUIREMENTS:
- Implement Redis caching strategy
- Add database query optimization
- Frontend code splitting
- Image lazy loading
- API response compression
- Performance monitoring setup

Provide specific optimization code and configuration.
```

-----

## Phase 5: Testing & Deployment

### Prompt 5.1: Testing Implementation

```
CONTEXT: E-commerce platform testing
CURRENT STATE: [Complete application]
GOAL: Comprehensive testing coverage

TESTING TYPES:
- Unit tests (Jest)
- Integration tests (Supertest)
- Frontend tests (React Testing Library)
- E2E tests (Cypress)

COVERAGE AREAS:
- API endpoints testing
- Database operations
- Authentication flows
- Component functionality
- User workflows

Create test files with good coverage and realistic test scenarios.
```

### Prompt 5.2: Production Deployment

```
CONTEXT: E-commerce platform deployment
CURRENT STATE: [Complete tested application]
GOAL: Production-ready deployment setup

REQUIREMENTS:
- Docker containerization
- CI/CD pipeline (GitHub Actions)
- Environment configuration
- Security hardening
- Monitoring setup
- Backup strategies

INFRASTRUCTURE:
- Database replication
- Load balancing
- SSL configuration
- Error tracking (Sentry)
- Performance monitoring

Provide Docker files, deployment scripts, and CI/CD configuration.
```

-----

## Prompt Tổng Hợp (Alternative Approach)

```
CONTEXT: Full-stack E-commerce Platform Development
TECH STACK: React, Node.js, Express, MongoDB, Redis

I need to build a complete e-commerce platform. Please provide a comprehensive development plan and implementation.

PROJECT REQUIREMENTS:
- User authentication (JWT-based)
- Product catalog with search/filter
- Shopping cart functionality
- Secure checkout process
- Order management
- Admin dashboard
- Payment integration
- Responsive design

TECHNICAL SPECIFICATIONS:
- RESTful API design
- Database optimization
- Security best practices
- Performance optimization
- Scalable architecture
- Error handling
- Testing coverage

DELIVERABLES NEEDED:
1. Complete project structure
2. Database schemas and models
3. Backend API with all endpoints
4. Frontend React components
5. State management setup
6. Authentication system
7. Admin panel
8. Testing suite
9. Deployment configuration

Please provide:
- Detailed file structure
- Complete code implementation
- Best practices integration
- Security considerations
- Performance optimizations
- Documentation

Start with the overall architecture and then dive into each component with full implementation details.
```

-----

## Tips for Effective AI Prompting in Coding:

### DO:

- ✅ Provide specific context and requirements
- ✅ Include current code/file structure
- ✅ Specify constraints and best practices
- ✅ Ask for complete, working examples
- ✅ Request error handling and edge cases
- ✅ Include testing considerations

### DON’T:

- ❌ Ask vague questions like “build me a website”
- ❌ Forget to mention tech stack requirements
- ❌ Skip security and performance considerations
- ❌ Ask for code without proper structure
- ❌ Ignore error handling in requirements

### Advanced Techniques:

1. **Chain prompts** for complex features
1. **Reference previous outputs** to maintain consistency
1. **Ask for alternatives** when stuck
1. **Request explanations** for learning
1. **Iterate and refine** based on results